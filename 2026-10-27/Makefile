.PHONY: all
all: presentation.pdf

presentation.pdf: presentation.md references.bib apa.csl assets/zulip-total-users-all-time.pdf
	mkdir -p build/tmp
	TMPDIR="$(CURDIR)/build/tmp" pandoc -t beamer --slide-level=2 presentation.md -o presentation.pdf --bibliography references.bib --citeproc -M link-citations=true -V colortheme:crane -V theme:CambridgeUS --csl apa.csl
