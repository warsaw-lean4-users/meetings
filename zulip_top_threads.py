#!/usr/bin/env python3
"""Rank Zulip public-channel topics by human messages + human reactions.

Human accounts are users explicitly marked is_bot=false by Zulip. Reactions
count even on bot messages, but only on messages posted in the chosen period.
Full message snapshots are cached by UTC month under ~/.cache/zulip-top-threads
(or XDG_CACHE_HOME). Cached reactions reflect when each message was fetched.
Lookback months include the current UTC calendar month, through the run time.

Setup:
    python3 -m venv .venv
    . .venv/bin/activate
    python3 -m pip install requests
Run: python3 zulip_top_threads.py
Refresh cached reactions/edits: python3 zulip_top_threads.py --refresh-cache
"""
import argparse
import configparser
import calendar
import hashlib
import json
import os
import sys
import tempfile
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

try:
    import requests
except ImportError:
    sys.exit(
        "The requests package is missing. Set up and activate a virtual environment:\n\n"
        "    python3 -m venv .venv\n"
        "    . .venv/bin/activate\n"
        "    python3 -m pip install requests\n\n"
        "Then run: python3 zulip_top_threads.py"
    )


def ask_int(label, default):
    while True:
        value = input(f"{label} [{default}]: ").strip()
        if not value:
            return default
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Enter a positive integer.")


def subtract_months(dt, months):
    year, month = divmod(dt.year * 12 + (dt.month - 1) - months, 12)
    return dt.replace(year=year, month=month + 1,
                      day=min(dt.day, calendar.monthrange(year, month + 1)[1]))


def credentials(site):
    config_path = Path(os.environ.get("ZULIPRC", "~/.zuliprc")).expanduser()
    email = os.environ.get("ZULIP_EMAIL")
    key = os.environ.get("ZULIP_API_KEY")
    if email and key:
        return email, key, site

    if not config_path.is_file():
        print("\nNo Zulip credentials found. Click this link (or copy it into your browser):")
        print(f"\n{site}/#settings/account-and-privacy\n")
        print("Go to Personal settings → Account & privacy → Manage your API key,")
        print("then download the zuliprc file.")
        print("Save it in your home directory as ~/.zuliprc.")
        print("The download is named zuliprc by default: add the leading dot to make it .zuliprc.")
        print("If it was saved in ~/Downloads, run: mv ~/Downloads/zuliprc ~/.zuliprc")
        entered = input("Path to downloaded .zuliprc [~/.zuliprc]: ").strip()
        config_path = Path(entered or "~/.zuliprc").expanduser()

    if not config_path.is_file():
        sys.exit("Credential file not found. Check the configured credential file location.")
    if os.name == "posix" and (config_path.stat().st_mode & 0o077):
        print("Warning: credential file is readable by others; restrict its permissions to mode 600.")
    config = configparser.ConfigParser()
    config.read(config_path)
    if not config.has_section("api"):
        sys.exit("Invalid .zuliprc: missing [api] section")
    email = config.get("api", "email")
    key = config.get("api", "key")
    configured_site = config.get("api", "site", fallback=site).rstrip("/")
    if configured_site != site:
        print(f"Using site in .zuliprc: {configured_site}")
    return email, key, configured_site


def get_api(session, site, endpoint, params=None):
    for attempt in range(5):
        try:
            response = session.get(site + "/api/v1/" + endpoint, params=params, timeout=60)
        except requests.RequestException:
            if attempt == 4:
                raise RuntimeError("Could not connect to the Zulip API after repeated attempts.") from None
            time.sleep(2 ** attempt)
            continue
        if response.status_code == 429 or response.status_code >= 500:
            if attempt < 4:
                time.sleep(min(float(response.headers.get("Retry-After", 2 ** attempt)), 30))
                continue
        if not response.ok:
            raise RuntimeError(f"Zulip API request failed (HTTP {response.status_code}).")
        data = response.json()
        if data.get("result") != "success":
            raise RuntimeError("Zulip API returned an unsuccessful result.")
        return data
    raise RuntimeError("Too many retries")


def topic_stats():
    return {"messages": 0, "reactions": 0, "participants": set(), "id": 0}


def cache_directory(site, email):
    root = Path(os.environ.get("XDG_CACHE_HOME", "~/.cache")).expanduser()
    identity = hashlib.sha256(f"{site}\n{email}".encode()).hexdigest()
    return root / "zulip-top-threads" / identity


def read_month_cache(path, month):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if (data["version"] != 1 or data["month"] != month
                or not isinstance(data["complete"], bool)
                or not isinstance(data["older_anchor"], int)
                or not isinstance(data["messages"], list)):
            raise ValueError("invalid cache metadata")
        for msg in data["messages"]:
            if (not isinstance(msg["id"], int)
                    or datetime.fromtimestamp(msg["timestamp"], timezone.utc).strftime("%Y-%m") != month):
                raise ValueError("invalid cached message")
        return data
    except FileNotFoundError:
        return None
    except (ValueError, KeyError, TypeError, OverflowError):
        print(f"Ignoring invalid cache for {month}; it will be fetched again.", file=sys.stderr)
        return None


def write_month_cache(path, data):
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    # Replace only after a full month fetch/update succeeds; interrupted writes
    # cannot destroy a previously usable snapshot.
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=path.name + ".", delete=False) as output:
            temporary = Path(output.name)
            json.dump(data, output, ensure_ascii=False)
            output.flush()
            os.fsync(output.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def cached_messages(session, site, cache_dir, cutoff, now, refresh=False):
    """Yield full monthly snapshots, before any date/human/ranking filters.

    Closed months are reused. Open snapshots fetch newer IDs, including a final
    catch-up after month rollover. Refresh rebuilds the requested months from scratch.
    """
    start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    anchor = "newest"
    while True:
        end = subtract_months(start, -1)
        month = start.strftime("%Y-%m")
        path = cache_dir / f"{month}.json"
        cached = None if refresh else read_month_cache(path, month)
        if cached is not None and cached["complete"]:
            print(f"Cache {month}: reused {len(cached['messages']):,} messages", file=sys.stderr)
        else:
            by_id = {msg["id"]: msg for msg in cached["messages"]} if cached else {}
            # An existing snapshot covers the beginning of its month, so only
            # newer IDs are needed. A missing month is fetched backwards.
            forward = cached is not None
            cursor = max(by_id, default=max(cached["older_anchor"] - 1, 0)) if forward else anchor
            older_anchor = cached["older_anchor"] if cached else 0
            fetched = 0
            while forward or cursor != 0:
                data = get_api(session, site, "messages", {
                    "anchor": cursor,
                    "num_before": 0 if forward else 1000,
                    "num_after": 1000 if forward else 0,
                    "include_anchor": "true" if cursor == "newest" else "false",
                    "apply_markdown": "false",
                    "narrow": '[{"operator":"channels","operand":"public"}]',
                })
                page = data["messages"]
                if not page:
                    break
                for msg in page:
                    if start.timestamp() <= msg["timestamp"] < end.timestamp():
                        by_id[msg["id"]] = msg  # Preserve every field, including bot activity.
                fetched += len(page)
                print(f"Cache {month}: fetched {fetched:,} messages", file=sys.stderr)
                if forward:
                    next_cursor = max(msg["id"] for msg in page)
                    finished = data.get("found_newest") or any(msg["timestamp"] >= end.timestamp() for msg in page)
                else:
                    next_cursor = min(msg["id"] for msg in page)
                    older = [msg["id"] for msg in page if msg["timestamp"] < start.timestamp()]
                    finished = data.get("found_oldest") or bool(older)
                    if older:
                        # Include the first message older than this month on the next fetch.
                        older_anchor = max(older) + 1
                    elif data.get("found_oldest"):
                        older_anchor = 0
                if finished:
                    break
                if (isinstance(cursor, int)
                        and (next_cursor <= cursor if forward else next_cursor >= cursor)):
                    raise RuntimeError("Message pagination stopped advancing; cache update aborted")
                cursor = next_cursor
            cached = {"version": 1, "month": month, "complete": end <= now,
                      "updated_at": datetime.now(timezone.utc).isoformat(),
                      "older_anchor": older_anchor,
                      "messages": sorted(by_id.values(), key=lambda msg: msg["id"])}
            write_month_cache(path, cached)
        yield from cached["messages"]
        anchor = cached["older_anchor"]
        if start.timestamp() <= cutoff:
            break
        start = subtract_months(start, 1)


def rank_topics(topics):
    # Use the same deterministic tie-breaks for the actual and hypothetical rankings.
    return sorted(topics.items(), key=lambda kv: (
        -(kv[1]["messages"] + kv[1]["reactions"]),
        -len(kv[1]["participants"]), -kv[1]["messages"], kv[0],
    ))


def report_unknown_activity(topics, unknown_topics, unknown_accounts, top_k):
    messages = sum(row["messages"] for row in unknown_accounts.values())
    reactions = sum(row["reactions"] for row in unknown_accounts.values())
    print(f"\nUnknown bot status: {len(unknown_accounts)} encountered accounts; "
          f"{messages} messages; {reactions} reactions; {len(unknown_topics)} topics.")
    print("These messages and reactions are excluded from the human ranking.")
    if not unknown_accounts:
        print("Ranking impact: none; no unknown activity was encountered.")
        return

    combined = {key: {**row, "participants": set(row["participants"])}
                for key, row in topics.items()}
    for key, unknown in unknown_topics.items():
        row = combined.setdefault(key, topic_stats())
        row["messages"] += unknown["messages"]
        row["reactions"] += unknown["reactions"]
        row["participants"].update(unknown["participants"])
    actual = [key for key, _ in rank_topics(topics)[:top_k]]
    hypothetical = [key for key, _ in rank_topics(combined)[:top_k]]
    entered = set(hypothetical) - set(actual)
    left = set(actual) - set(hypothetical)
    changed_scores = sum(key in unknown_topics for key in actual)
    print(f"If ALL unknown activity were human: scores would increase in {len(unknown_topics)} topics "
          f"({changed_scores} in the current top {top_k}).")
    print(f"    Top {top_k} membership changes: {'yes' if entered or left else 'no'} "
          f"({len(entered)} enter, {len(left)} leave).")
    print(f"    Ordered top {top_k} list changes: {'yes' if actual != hypothetical else 'no'}.")
    print("This comparison assumes all unknown accounts are human; their actual status remains unknown.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--refresh-cache", action="store_true",
                        help="re-download the requested months to refresh reactions, edits and deletions")
    args = parser.parse_args()
    site = (input("Zulip server [https://leanprover.zulipchat.com]: ").strip()
            or "https://leanprover.zulipchat.com").rstrip("/")
    if not site.startswith("https://"):
        sys.exit("For security, provide an https:// Zulip server URL")
    months = ask_int("How many calendar months, including the current month?", 3)
    top_k = ask_int("Show top how many topics?", 20)
    email, key, site = credentials(site)
    session = requests.Session()
    session.auth = (email, key)
    session.headers.update({"User-Agent": "zulip-top-threads/1.0"})

    users = get_api(session, site, "users")
    human_ids = {user["user_id"] for user in users["members"]
                 if user.get("is_bot") is False}
    print(f"Counting activity from {len(human_ids)} known human accounts.", file=sys.stderr)

    now = datetime.now(timezone.utc)
    first_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    minimum_date = subtract_months(first_month, months - 1)
    cutoff = minimum_date.timestamp()
    timespan = (f"{minimum_date.isoformat(sep=' ')} through {now.isoformat(sep=' ')} "
                f"(UTC, inclusive; {months} calendar months including the current month)")
    topics = defaultdict(topic_stats)
    unknown_topics = defaultdict(topic_stats)
    unknown_accounts = defaultdict(lambda: {"messages": 0, "reactions": 0})
    total = 0
    classified_ids = {user["user_id"] for user in users["members"]
                      if isinstance(user.get("is_bot"), bool)}
    cache_dir = cache_directory(site, email)
    print(f"\nReading public channel messages: {timespan} ...", file=sys.stderr)
    for msg in cached_messages(session, site, cache_dir, cutoff, now, args.refresh_cache):
        if not cutoff <= msg["timestamp"] <= now.timestamp():
            continue
        if msg.get("type") not in ("stream", "channel"):
            continue
        stream_id = msg.get("stream_id")
        if stream_id is None:
            continue
        sender_id = msg["sender_id"]
        reaction_ids = [reaction["user_id"] for reaction in (msg.get("reactions") or [])]
        topic = msg.get("subject", "")
        channel = msg.get("display_recipient", str(stream_id))
        topic_key = (stream_id, topic, channel)
        unknown_message = sender_id not in classified_ids
        unknown_reactions = [user_id for user_id in reaction_ids if user_id not in classified_ids]
        if unknown_message or unknown_reactions:
            row = unknown_topics[topic_key]
            row["messages"] += int(unknown_message)
            row["reactions"] += len(unknown_reactions)
            row["participants"].update(unknown_reactions)
            if unknown_message:
                row["participants"].add(sender_id)
                unknown_accounts[sender_id]["messages"] += 1
            for user_id in unknown_reactions:
                unknown_accounts[user_id]["reactions"] += 1
        human_message = sender_id in human_ids
        human_reactions = [user_id for user_id in reaction_ids if user_id in human_ids]
        if not human_message and not human_reactions:
            continue
        row = topics[topic_key]
        row["messages"] += int(human_message)
        row["reactions"] += len(human_reactions)
        row["participants"].update(human_reactions)
        if human_message:
            row["participants"].add(sender_id)
        row["id"] = max(row["id"], msg["id"])
        total += int(human_message)
    print(f"Processed {total:,} in-range human messages", file=sys.stderr)
    ranking = rank_topics(topics)
    print(f"\nGenerated: {datetime.now(timezone.utc).isoformat(sep=' ')} (UTC)")
    print(f"Timespan checked: {timespan}")
    print(f"\nTop {min(top_k, len(ranking))} topics of {len(ranking)}; score = human messages + human reactions\n")
    for pos, ((stream_id, topic, channel), row) in enumerate(ranking[:top_k], 1):
        score = row["messages"] + row["reactions"]
        # Stable channel-ID and topic-based URL with an anchor to a recent message.
        link = (f"{site}/#narrow/channel/{stream_id}-"
                f"{quote(channel, safe='')}/topic/{quote(topic, safe='')}/near/{row['id']}")
        print(f"{pos:>2}. [{score:>5} human interactions] #{channel} > {topic or '(no topic)'}")
        print(f"    {row['messages']} human messages | {row['reactions']} human reactions | "
              f"{len(row['participants'])} human participants (authors or reactors)")
        print(f"    {link}")
    report_unknown_activity(topics, unknown_topics, unknown_accounts, top_k)
    print("\nNote: reactions are from the cached snapshots of messages posted during the chosen period;")
    print("the API does not indicate when each reaction was added. Only accessible public history is counted.")
    print("Use --refresh-cache to update cached reactions, edits and deletions.")
    print("Human reactions count even on bot messages. Bot-authored activity and unknown accounts are excluded.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        sys.exit("\nCancelled")
    except RuntimeError as exc:
        sys.exit(f"Error: {exc}")
    except (OSError, configparser.Error):
        sys.exit("Error: could not read or write local configuration/cache files. Check their format and permissions.")
    except (requests.RequestException, ValueError):
        sys.exit("Error: could not read a valid response from the Zulip API.")
