# Example input

The following request is intentionally concrete enough for a package-level revision:

```text
Use $aaai-revision-detemplater on the AAAI submission at <paper-folder>.

Inputs:
- main source: <paper-folder>/main.tex
- supplement: <paper-folder>/supplementary.tex
- current build: <paper-folder>/build
- upload package: <paper-folder>/submission
- reviewer notes: <paper-folder>/revision_notes.md

Constraints:
- keep the technical-content portion within the current AAAI page budget;
- make the main paper self-contained for the acceptance decision;
- reduce mirrored contribution and section structures;
- calibrate claims to the exact controls and stress tests;
- keep the OpenReview TL;DR within 250 characters;
- reuse frozen results, figures, and code/data archives unless a source change invalidates them.

Deliver:
1. revised source files and, when a local toolchain is available, verified compiled PDFs;
2. a main-versus-supplement move log;
3. synchronized abstract, keywords, and OpenReview text;
4. a package reuse/replace manifest;
5. a final upload audit with unresolved risks.
```

For a narrower task, remove unrelated inputs and ask for one output surface only. For example: “Revise only the abstract and TL;DR; do not change the paper source.”
