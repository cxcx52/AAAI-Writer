---
name: aaai-paper-architect
description: Build, rewrite, tighten, and audit AAAI papers with claim-first architecture, evidence-calibrated contribution framing, section-level rhetorical moves, anti-defensive style control, academic anti-AI-smell editing, and revision-package restructuring. Use when the user wants to write an AAAI paper, create an AAAI outline, draft or rewrite abstract/introduction/method/experiments/related work/conclusion, reduce AI-smell, remove defensive not-but/rather-than prose, calibrate claim strength, map experiments to claims, rebalance main paper versus supplement, tighten abstract/TL;DR/OpenReview metadata, or turn Codex workflow materials, PDFs, LaTeX, figures, tables, literature notes, and frozen submission folders into an AAAI-ready manuscript or revision package.
---

# AAAI Paper Architect

Use this skill for AAAI writing and rewriting. It is a synthesis layer over local AAAI/Nature writing skills, external paper-writing/reviewer workflows, and the user's observed draft failure mode: evidence-safe prose that becomes too defensive.

## Core Stance

- Write from the paper's positive contribution first, then place limits only where they prevent overclaiming.
- Treat claims as contracts: every abstract, introduction, heading, and contribution claim needs an evidence pointer.
- Prefer concrete mechanisms, numbers, and named evaluation questions over generic adjectives.
- Avoid rhetorical antithesis as a default style. `not X but Y`, `rather than`, and `instead` are allowed only when the contrast is a factual contribution boundary.
- Build the paper twice: use Draft 0 to find the story, then rewrite the final introduction and abstract after the evidence map is stable.
- For revision packages, rebuild the story from the real decision point, not from the inherited section order or prior contribution symmetry.
- Keep reviewer-critical material in the main paper whenever the page budget permits; treat the supplement as audit trail and reproducibility support, not as a shadow main paper.
- Reuse frozen artifacts, existing figures, and current upload packages unless a textual or structural change actually invalidates them.

## Workflow

1. Classify the paper type.
   Use algorithm/theory, method/model, benchmark/resource, application-driven, or systems/agent evaluation.
2. Build the paper contract.
   Produce one identity sentence, 3-4 contribution claims, a claim-evidence table, and a 7-page AAAI budget.
3. Design the narrative spine.
   Use the sequence: stakes -> structural gap -> key abstraction -> design intuition -> evidence preview -> contributions.
4. Draft by topic sentences first.
   Write the topic sentence sequence for a section before full paragraphs. If the topic sentences do not form an argument, do not expand them.
5. Audit revision-package necessity when revising an existing paper.
   For each definition, mechanism, result, and diagnostic, decide whether a reviewer needs it to accept or reject the paper without opening the supplement.
6. Redistribute content when the package is top-heavy or over-supplemented.
   Pull indispensable material into the main paper. Push only derivations, exhaustive sensitivity tables, provenance detail, and replay material into the supplement.
7. Calibrate claim strength.
   Match verbs to evidence: `suggests`, `shows`, `demonstrates`, `establishes`, or `proves`.
8. Tighten metadata surfaces when submission text exists.
   Rewrite title, abstract, keywords, TL;DR, and OpenReview text to reduce numeric clutter, mirrored contribution phrasing, and over-strong interpretation.
9. Run the defensive-style gate.
   Use the script when files are available. Rewrite excess negation into positive contribution statements.
10. Run the academic anti-AI-style gate.
   Remove template openers, connector stacking, generic praise, synonym cycling, and uniform rhythm without casualizing the paper or weakening evidence-bound claims.
11. Run a reviewer-risk pass.
   For scoring or simulated reviews, route to `aaai-review-simulator`; for writing revisions, stay in this skill.
12. Preserve artifact efficiency.
   Reuse existing sources, figures, and upload archives when valid. Avoid recomputation unless a content change requires it.

## Reference Routing

- Read [references/paper-architecture.md](references/paper-architecture.md) for whole-paper planning, page budget, and narrative spine.
- Read [references/claim-calibration.md](references/claim-calibration.md) for claim strength, contribution bullets, and evidence mapping.
- Read [references/defensive-style-gate.md](references/defensive-style-gate.md) when revising AI-smell, `not-but`, `rather than`, hedging, or defensive scope prose.
- Read [references/anti-ai-academic-style.md](references/anti-ai-academic-style.md) when the user asks to reduce AI-smell, humanize academic prose, de-template writing, or preserve author voice.
- Read [references/section-playbook.md](references/section-playbook.md) when drafting or rewriting a specific section.
- Read [references/source-basis.md](references/source-basis.md) when you need provenance for the synthesis or want to inspect what this skill learned from.

## Script

When the user provides `.tex`, `.txt`, or `.md` files or a paper directory, run:

```bash
python scripts/audit_aaai_style.py <path>
```

Use the output as a rewrite queue. Fix high-density defensive constructions first, then generic adjectives, then throat-clearing and AI-smell.

## Output Contracts

For a new paper plan, return:

- `Identity sentence`
- `Paper type`
- `Narrative spine`
- `Contribution claims`
- `Claim-evidence map`
- `Section/page plan`
- `Figure/table plan`
- `Immediate missing evidence`

For a rewrite, return:

- `Diagnosis`
- `Rewritten text`
- `Claim/evidence changes`
- `Defensive-style fixes`
- `Residual risks`

For a revision package, return:

- `Revision diagnosis`
- `Narrative spine`
- `Main-paper moves`
- `Supplement moves`
- `Metadata edits`
- `Artifact reuse plan`
- `Residual risks`

For a section draft, return:

- `Topic-sentence sequence`
- `Draft`
- `Section self-check`
- `Claims that still need evidence`

## Boundaries

- Do not invent experiments, citations, numbers, baselines, or award-paper patterns.
- Do not make the prose more aggressive than the evidence supports.
- Do not hide real limitations; move them to a controlled limitation sentence or limitations section.
- Do not use simulated review score as a writing objective. Use review output only to identify revision targets.
- Do not optimize prose for evading AI detectors. Treat AI-smell reduction as scholarly editing: clarity, specificity, rhythm, and evidence discipline.
- Do not preserve mirrored contribution structure or binary framing when the evidence is asymmetric.
- Do not describe a control as ruling out an explanation beyond the scope actually tested.
- Do not rerun frozen pipelines or regenerate upload packages unless a text or artifact change requires it.
