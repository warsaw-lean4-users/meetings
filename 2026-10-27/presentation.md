---
title:
- "Meetings of Lean 4 users in Warsaw: intro"
author:
- Paweł Balawender
date:
- Tuesday, 27th of October, 2026
# pandoc -t beamer presentation.md -o presentation.pdf --bibliography references.bib --citeproc  -M link-citations=true -V colortheme:crane -V theme:CambridgeUS --csl apa.csl
---


# A. Intro + organisation

## A. Intro + organisation

- **A. Intro + organisation**
- **B. Summer–October:** events + Lean Zulip trends
- **C. October–November:** events, deadlines + opportunities
- **D. AI4Math:** results, discussion + funding
- **E. Software verification:** tools + cybersecurity funding

Many directions to develop yourself in Lean; today: **AI4Math** and **software verification**.

## A. Warsaw Lean 4 users

- **GitHub:** [warsaw-lean4-users](https://github.com/warsaw-lean4-users).
- **Meetings:** Tuesdays, monthly; next: **24 November, 15 December 2026**.
- **Communication:** Lean Zulip — Warsaw location topic.
- **NOT a UW koło naukowe.** Possible future discussion: registration needs **5 students + an academic supervisor with a PhD**.

# B. Summer–October

## B. Selected events since June 2026

\footnotesize
:::: {.columns align=top}
::: {.column width="48%"}
### June–July

- **30 June:** [UNSOUND 2026](https://2026.ecoop.org/home/unsound-2026) — Brussels.
- **6–11 July:** [ICML 2026](https://icml.cc/Conferences/2026) — Seoul; [Lean + machine learning tutorial](https://leanmachinelearning.org/icml-tutorial/) on **6 July**.
- **11 July:** ICML's dedicated [AI4Math workshop](https://ai4math2026.github.io/).
- **13–29 July:** [FLoC 2026](https://www.floc26.org/) — Lisbon; includes summer schools.
- **20–23 July:** [LICS 2026](https://lics.siglog.org/lics26/) — at FLoC.
- **25 July:** [Lean Workshop 2026](https://leanprover-community.github.io/floc-2026-lean-workshop/) — at FLoC.
- **26–29 July:** **[CAV 2026](https://conferences.i-cav.org/2026/)** and **[ITP 2026](https://itp-conference-2026.github.io/)** — both part of FLoC.
:::
::: {.column width="48%"}
### August–October

- **24–29 August:** [ICFP 2026 + affiliated events](https://icfp26.sigplan.org/) — Indianapolis.
- **7–11 September:** [Proof Society 2026](https://proofsociety26.sciencesconf.org/) — school and workshop, Aussois.
- **15–18 September:** **[FMCAD 2026](https://fmcad.org/FMCAD26/program/)** — Graz; Verus tutorial and program-verification track.
- **21–25 September:** [CICM 2026](https://cicm-conference.org/2026/cicm.php) — Ljubljana.
- **4–9 October:** [SPLASH 2026](https://2026.splashcon.org/) — Oakland.
- **24–29 October:** [EMNLP 2026](https://2026.emnlp.org/) — Budapest; **underway at this meeting**.
:::
::::

\scriptsize
**Major venues:** ITP — interactive theorem proving; CAV/FMCAD — formal verification. [Full calendar](https://ruplet.com/ai4math-calendar).
\normalsize

## B. Summer / September–October

- [Physlib: Yukawa sector of the Standard Model](https://leanprover.zulipchat.com/#narrow/channel/479953-Physlib/topic/Project%3A%20Formalising%20the%20Yukawa%20sector%20of%20the%20Standard%20Model/near/630990313) — started **14 July**.
- [Counterexample to the Lean Conjecture — soundness bug](https://leanprover.zulipchat.com/#narrow/channel/270676-lean4/topic/Counterexample%20to%20the%20Lean%20Conjecture%20%28Soundness%20Bug%29/near/620332700).

## B. Zulip — you WILL become visible quickly

**Only 1,671 users active in the last 15 days** — out of 17,953 total users.

\begin{center}
\includegraphics[width=0.94\textwidth,height=0.49\textheight,keepaspectratio]{assets/zulip-total-users-all-time.pdf}
\end{center}

\scriptsize
[Lean Zulip statistics](https://leanprover.zulipchat.com/stats) · 26 October 2026 · “Active users” → “Total users”, all time; rendered from chart data.
\normalsize

# C. October–November

## C. October–November: events + calendar

### My AI4Math calendar

**[ruplet.com/ai4math-calendar](https://ruplet.com/ai4math-calendar)** — conferences, workshops, deadlines, student opportunities.

- **ONGOING, 26–30 Oct: [Bristol Lean week](https://bristol-lean.github.io/blue/events/)** — **Patrick Massot**; Lean mini-course **27–29 Oct**, teaching seminar **30 Oct**. Registration closed.
- **ONGOING, 24–29 Oct: [EMNLP 2026](https://2026.emnlp.org/)** — Budapest.
- **24 Nov:** next Warsaw Lean 4 users meeting.

## C. ELLIS closes 31 OCTOBER

### ELLIS PhD applications CLOSE 31 OCTOBER

**31 October 2026, 23:59 AoE — FIRM DEADLINE.**

[ELLIS PhD programme — 2027 intake](https://ellis.eu/news/ellis-phd-program-call-for-applications-2026) · [Apply](https://apply.ellis.eu).

- [Mathlib reviewer bootcamp 2027](https://leanprover.zulipchat.com/#narrow/channel/579629-Event-announcements/topic/Mathlib.20reviewer.20bootcamp.202027/with/628706744) — deadline **31 October**.

## C. Student opportunities — November deadlines

\small
**EACL / NAACL mentorship:** feedback on a student paper's writing, structure and presentation before submission; NLP / computational linguistics. Optional; acceptance not guaranteed.

- **6 Nov (AoE): [EACL ’27 Student Research Workshop](https://2027.eacl.org/calls/srw/)** — submit a **draft** for mentorship; feedback **5 Dec**; final paper **15 Dec**.
- **11 Nov (AoE): [POPL ’27 student volunteers](https://popl27.sigplan.org/track/POPL-2027-student-volunteers)** — registration + meals; travel / lodging excluded. [Zulip call](https://leanprover.zulipchat.com/#narrow/channel/579629-Event-announcements/topic/POPL27.3A.20Call.20for.20Student.20Volunteers/with/630961882).
- **16 Nov (AoE): [NAACL ’27 Student Research Workshop](https://2027.naacl.org/calls/srw/)** — request a mentor; **complete draft not required**; final paper **11 Jan 2027**.
- **30 Nov–4 Dec (ET): [AAAI ’27 scholar / volunteer applications](https://aaai.org/conference/aaai/aaai-27/student-scholar-volunteer-program/)** — opens **30 Nov**, closes **4 Dec**; AAAI membership required.

\scriptsize
[AI4Math calendar](https://ruplet.com/ai4math-calendar) · deadlines checked 26 October 2026.
\normalsize

## C. Community announcements + recurring meetings

- **Recurring meetings:** CSLib, The Meta Café.
- **[Lean events page](https://leanprover-community.github.io/events)** — conferences, workshops, schools, tutorials.
- **Zulip channels:** [job postings](https://leanprover.zulipchat.com/#narrow/channel/284757-job-postings) · [Calls for papers](https://leanprover.zulipchat.com/#narrow/channel/579636-Calls-for-papers) · [Event announcements](https://leanprover.zulipchat.com/#narrow/channel/579629-Event-announcements).

# D. AI4Math

## D. AI4Math: autoformalization in 2026

\small
- **February: [Gauss / Math, Inc.](https://www.math.inc/sphere-packing)** — sphere packing. [Maintainers](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/): proof completed; refactoring / integration remain.
- **[Aristotle / Harmonic](https://www.harmonic.fun/aristotle/)** — [UW spring projects](https://ai.math.uw.edu/projects/spring-2026/): textbook formalization; mathlib contributions are a goal.
- **[AxiomProver](https://deancureton.com/projects/axiom-formalization/)** — October releases: [Bondal–Thomsen](https://github.com/AxiomMath/BondalThomsen), [Dedekind zeta](https://github.com/AxiomMath/DedekindZetaZeroFree). **[AXLE](https://axiommath.ai/research/releasing-axle/)** — Lean checking service, released **5 March**.
\normalsize

## D. AI4Math: OpenAI results + discussion

\small
:::: {.columns align=top}
::: {.column width="48%"}
### Navier–Stokes

- **8 September:** [announcement](https://openai.com/index/navier-stokes-solution/) · [paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) · [Lean dump](https://github.com/openai/NavierStokesAndEuler).
- [Independent build / Comparator check](https://leanprover.zulipchat.com/#narrow/channel/113488-general/topic/Independent.20verification.20of.20OpenAI.20NavierStokesAndEuler/near/622689813).
- **6 October:** [*Navier–Stokes lost in translation*, arXiv:2610.08144](https://arxiv.org/abs/2610.08144) — paper / Lean mismatch; $m+4$ vs. $m+5$ derivatives. No claim that the written proof is incorrect.
- [Mathematicians' discussion](https://leanprover.zulipchat.com/#narrow/channel/113488-general/topic/Lean.20in.20the.20wild.3A.20Navier-Stokes.20proved/near/629885972).
:::
::: {.column width="48%"}
### October results dump

- **6 October:** [announcement](https://openai.com/index/sharing-ai-progress-in-mathematics/) · [dump](https://github.com/openai/math).
- [Manuscripts](https://github.com/openai/math/blob/main/CONTENTS.md) · [Lean catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml) · [reasoning summaries](https://github.com/openai/math/tree/main/reasoning_traces). Partial formalization coverage.
- [David Michael Roberts](https://leanprover.zulipchat.com/#narrow/channel/583339-AI-authored-projects/topic/OpenAI.20releases.20solutions.20to.20hundreds.20of.20problems/near/630613075): check headline statements / definitions.
- [Johan Commelin](https://leanprover.zulipchat.com/#narrow/channel/583339-AI-authored-projects/topic/OpenAI.20releases.20solutions.20to.20hundreds.20of.20problems/near/630339312): Comparator configurations allowing redefined definitions.
:::
::::
\normalsize

## D. AI4Math: Anthropic + community responses

\small
- **4 September: [Anthropic — FLT formalization](https://www.anthropic.com/research/formalizing-fermats-last-theorem)** · [Lean repository](https://github.com/anthropics/fermats-last-theorem).
- **Kevin Buzzard:** compiled / checked with Comparator; **his FLT project continues** — mathlib contributions + a human-readable modern proof. [Original explanation](https://xenaproject.wordpress.com/2026/09/04/flt-anthropic-has-beaten-me-to-it/) · [Zulip comment](https://leanprover.zulipchat.com/#narrow/channel/416277-FLT/topic/Anthropic.20formalization/near/621822462).
- **[Jeremy Avigad](https://leanprover.zulipchat.com/#narrow/channel/583339-AI-authored-projects/topic/OpenAI.20releases.20solutions.20to.20hundreds.20of.20problems/near/630512233):** “we bring deep, thoughtful judgment about what makes for good mathematics.”
- **[Sébastien Gouëzel](https://leanprover.zulipchat.com/#narrow/channel/583339-AI-authored-projects/topic/OpenAI.20releases.20solutions.20to.20hundreds.20of.20problems/near/630613587):** “exciting and interesting and novel (and very badly written!)”.
\normalsize

## D. AI4Math funding — a Polish grant recipient

- **Bartosz Naskręcki (UAM / PW): AI for Math Fund 2026 grant recipient** — **Renaissance Philanthropy / XTX Markets**. [Award list](https://www.renaissancephilanthropy.org/ai-for-math-fund-2026-projects).
- **[Agentic Approach to Computer Algebra Systems](https://www.renaissancephilanthropy.org/agentic-approach-to-computer-algebra-systems):** LLM → CAS (Magma / SageMath / PARI/GP) → independent cross-check → **Lean certificate**.
- **6 October:** [funding round announced — $17.1M, 22 awards](https://www.renaissancephilanthropy.org/insights/renaissance-philanthropy-and-xtx-markets-announce-further-171-million-to-accelerate-mathematical-progress).
- **[Simons — targeted grants to Math+AI institutes, 2027](https://www.simonsfoundation.org/funding/targeted-grants-to-mathai-institutes-2027/).**

# E. Software verification

## E. Software verification: Verus + Velvet

\small
- **[Signal Shot](https://www.beneficialaifoundation.org/signal-shot)** — ongoing verification of the **Signal protocol + Rust implementation in Lean**. **Leo de Moura + Max Tegmark:** steering co-chairs; Signal / BAIF / Lean FRO. [Leo's overview](https://leodemoura.github.io/blog/2026-4-20-signal-shot-the-platform-is-ready/).
- [VeriContest](https://hiprel-group.github.io/VeriContest/) — LeetCode verification in **Verus**.
- **[Verifying the Rust Standard Library](https://model-checking.github.io/verify-rust-std/)**; Runtime Verification; RustConf.
- **[FMCAD 2026](https://fmcad.org/FMCAD26/program/):** **15 September**, Travis Hance — **Verifying Rust code with Verus**. **16–18 September:** Program Verification and Synthesis track.
- **[CAV 2026](https://conferences.i-cav.org/2026/) — part of FLoC:** **[Velvet](https://velvetprover.dev/)** — imperative-program verification in **Lean 4**. [CAV tool paper](https://verse-lab.org/papers/velvet-cav26.pdf); insertion-sort demo.
\normalsize

## E. Dafny — an interactive proof mode?

- **[Interactive proof mode for Dafny](https://profs.info.uaic.ro/stefan.ciobaca/aipmda.html)** — construct proofs interactively; complement automated verification.
- **Ciobâcă, Leino, Mercaș, Timon:** design + **prototype**, presented at **[Dafny ’26](https://popl26.sigplan.org/details/dafny-2026-papers/10/The-Design-of-an-Interactive-Proof-Mode-for-Dafny)** and **[WPTE / FLoC, 19 July](https://program.floc26.org/2026-07-19)**. [Paper](https://arxiv.org/abs/2512.20486).

## E. Cryptography / blockchain

\small
:::: {.columns align=top}
::: {.column width="48%"}
### Cryptography — Warsaw demo

**Dziembowski, Fabiański, Micciancio, Stefański:**

- [*Computationally-Sound Symbolic Cryptography in Lean*](https://eprint.iacr.org/2025/1700), CSF 2026. [Code](https://github.com/ravst/SymbolicCryptographyLean).
- [*Game Hopping in Lean*](https://arxiv.org/abs/2608.06261), August 2026 — **HOPSCOTCH**. [Demo / code](https://github.com/ravst/Hopscotch).
:::
::: {.column width="48%"}
### Blockchain — industry

- [ArkLib](https://lean-lang.org/use-cases/arklib/) — SNARKs.
- [Nethermind](https://www.nethermind.io/formal-verification) — EVM/Yul, ZK circuits, verification tooling.
:::
::::
\normalsize

## E. EU funding: formal verification + security

\small
**[ECCC / Horizon Europe — HORIZON-CL3-2026-02-CS-ECCC](https://cybersecurity-centre.europa.eu/funding-opportunities/calls-proposals/cybersecurity-horizon-cl3-2026-02-cs-eccc_en)**

- **01 · €20M:** software / hardware security; **formal verification + AI-driven security testing**.
- **02 · €21.2M:** **SecureAI** — security, privacy and robustness of AI systems.
- **03 · €15M:** high-assurance cryptographic implementations; **formal verification tools**, post-quantum migration.

**Deadline: 15 September 2026 — CLOSED.**

\scriptsize
[CPPC — cybersecurity calls](https://www.gov.pl/web/cppc/nabory-2026-z-obszaru-cyberbezpieczenstwo) · [FIRST TEAM FENG, 2/2026 — 20 Nov](https://www.fnp.org.pl/component/fnp_programs/program/first-team-feng/nabor-2-2026).
\normalsize

<!-- removed

Public material removed from the slides; retained here for future editing.
Keep future removals of conferences, people and projects in this comment.
Keep an item either in the slides or here, never in both.
Private contact / outreach information must not be retained here.

Funding — European / Polish calls
SME CALLS https://eudis.europa.eu/eudis-tracks/sme-calls_en
FENG call: https://funduszeeuropejskie.gov.pl/aktualnosci/technologie-obronne-w-feng-kryteria-konkursowe-i-terminy-pierwszych-naborow/

AI safety — understanding / checking AI-generated proofs.
Dual-use AI: AI that programs well? Lean: hard to write proofs; easy to check them.

Learning resources
Natural Number Game: basic introduction to writing proofs in Lean.
Mathematics in Lean: tutorial on mathematics in Lean and Mathlib.
Theorem Proving in Lean: tutorial on Lean's type theory.
Functional Programming in Lean: tutorial on programming in Lean.
https://lean-lang.org/community/

People / teaching / local groups
FORM centre: https://www.linkedin.com/company/form-centre/home/
Software Foundations in Lean.
Cambridge Lean User Group:
https://leanprover.zulipchat.com/#narrow/channel/224796-Geographic-locality/topic/Cambridge.2C.20UK/near/631701362

Reading / next talks
Fabrizio Montesi's blog: https://www.fabriziomontesi.com/
Software Verification in Lean 2026, Paris (April 2026), videos:
https://www.youtube.com/playlist?list=PLtlBXrgM1AlOg-jxchcgkLfTdwZWm-oN3
Swarat Chaudhuri, June 2026 / Science: https://arxiv.org/abs/2605.22763

Other Lean projects
Hex: verified computer algebra.
Aeneas: Rust code verified in Lean.

Funding — mathematical AI
Coefficient Giving.

-->
