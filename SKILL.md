---
name: aaai-revision-detemplater
description: Restructure AAAI revision packages around a clearer argument while reducing template feel, redistributing essential content from supplement to main paper, tightening abstract/TL;DR/OpenReview metadata, and reusing existing experiment artifacts without unnecessary reruns. Use when Codex needs to revise AAAI `.tex` projects, submission folders, appendices, or upload packages after reviews or internal critique.
---

# AAAI Revision Detemplater

Use this skill when a draft already has technical content and experiments, but the package still reads as over-symmetrized, over-templated, or too dependent on the supplement.

## Core stance

- Rebuild the story from the paper's real decision point, not from the existing section order.
- Move any result needed for reviewer judgment into the main paper whenever page budget permits.
- Treat the supplement as audit trail, derivation support, and reproducibility record, not as a shadow main paper.
- Prefer reuse of frozen artifacts, existing figures, and current zip packages unless the user explicitly asks to rerun experiments.
- Replace broad conclusion language with scope-true statements tied to the exact control, stress test, or family evaluated.

## Workflow

1. Classify the revision target.
   Distinguish whether the main problem is narrative duplication, page-budget misallocation, metadata overload, over-strong interpretation, or package hygiene.
2. Rebuild the narrative spine.
   Write one identity sentence, one central question, and one evidence sequence before touching headings.
3. Audit main-paper necessity.
   For each definition, mechanism, result, and diagnostic, decide whether a reviewer needs it to accept or reject the paper without opening the supplement.
4. Redistribute content.
   Pull indispensable material into the main paper. Push only derivations, exhaustive sensitivity tables, provenance detail, and replay material into the supplement.
5. De-template the rhetoric.
   Reduce one-to-one mirrored contributions, repetitive binary framing, and conclusion-shaped section titles. Allow asymmetric contribution granularity when the evidence is asymmetric.
6. Separate facts from claims.
   Maintain a result fact sheet, a claim-boundary list, and a reviewer-risk matrix so the prose can be rewritten without drifting beyond the artifact facts.
7. Tighten metadata surfaces.
   Rewrite title, abstract, keywords, TL;DR, and OpenReview registration text so they expose the contribution with lower numeric clutter and less editorialized interpretation.
8. Preserve package efficiency.
   Reuse existing sources, figures, and upload archives when valid. Avoid recomputation unless a change truly invalidates prior artifacts.
9. Run the package audit.
   Before finalizing, check that local audit notes, runtime wording, hash manifests, upload-folder contents, read-only PDFs, and portal-preview expectations all reflect the current text rather than an older packaging pass.

## Reference routing

- Read [references/narrative-rebuild.md](references/narrative-rebuild.md) when the paper's story is trapped inside its current wording or section structure.
- Read [references/main-vs-supplement.md](references/main-vs-supplement.md) when deciding what must remain in the main paper under AAAI page limits.
- Read [references/artifact-governance.md](references/artifact-governance.md) when you need to keep narrative claims, artifact facts, reviewer risks, and final package records aligned.
- Read [references/upload-audit.md](references/upload-audit.md) when source ZIPs, PDF previews, checksum tables, or submission-portal rendering need to be checked before upload.
- Read [references/metadata-surfaces.md](references/metadata-surfaces.md) when editing the abstract, TL;DR, title, keywords, or OpenReview fields.
- Read [references/evidence-calibration.md](references/evidence-calibration.md) when a sentence sounds stronger than the actual control or robustness evidence.

## Output contracts

For a package-level rewrite, return:

- `Revision diagnosis`
- `Narrative spine`
- `Main-paper moves`
- `Supplement moves`
- `Metadata edits`
- `Artifact reuse plan`
- `Residual risks`

For a section or metadata rewrite, return:

- `Problem`
- `Rewritten text`
- `Why this wording is safer`
- `What evidence still limits the claim`

## Boundaries

- Do not invent new experiments, statistics, citations, figures, or theoretical claims.
- Do not move critical definitions or headline evidence out of the main paper merely to make the supplement look fuller.
- Do not preserve symmetry for its own sake when asymmetry matches the evidence better.
- Do not describe a control as ruling out an explanation beyond the scope actually tested.
- Do not rerun frozen pipelines or regenerate upload packages unless a text or artifact change requires it.
