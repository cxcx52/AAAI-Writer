# Example Input

The request below is concrete enough for a package-level AAAI rewrite:

```text
Use $aaai-paper-architect on the AAAI project at <paper-folder>.

Inputs:
- main source: <paper-folder>/main.tex
- current build: <paper-folder>/build
- supplement: <paper-folder>/supplementary.tex
- reviewer notes: <paper-folder>/revision_notes.md

Goals:
- rebuild the identity sentence and contribution logic;
- make the main paper self-contained for the acceptance decision when page budget permits;
- reduce defensive and templated phrasing;
- calibrate claims to the exact controls and evidence already in the project;
- tighten abstract, keywords, and TL;DR if they are overloaded;
- reuse frozen figures, tables, and experiment artifacts unless a source change invalidates them.

Deliver:
1. revised source text or patch-ready rewrite recommendations;
2. a claim-evidence map;
3. main-paper versus supplement moves if needed;
4. synchronized metadata text;
5. residual risks that still need author judgment.
```

For a narrower task, remove unrelated inputs and ask for one output surface only.
