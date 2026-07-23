# Source Basis

This skill synthesizes local and external sources. It should not claim that any pattern is official AAAI policy unless the source is an AAAI page or author kit.

## Local User Drafts

Two supplied PDFs were sampled with `pypdf`:

| Draft | Pages | Extracted words | Defensive-style observations |
|---|---:|---:|---|
| `dmcb_aaai27_major_revision/openreview_submission_packet/00_READY_TO_UPLOAD/main.pdf` | 8 | 4534 | `rather than` appeared 6 times; `not...but` appeared once; `not claim` style appeared twice |
| `when-should-an-agent-commit-to-2/paper_s01_aaai27/build/main.pdf` | 8 | 4087 | `rather than` appeared 6 times; scope-boundary language clustered around related work, estimand, and limitations |

Interpretation: the drafts are evidence-conscious, but the local style problem is excess boundary framing. The fix is not to remove limitations; it is to state the positive scoped contribution first and centralize limitations.

## Local Installed Skills

- `aaai-writing`: useful for AAAI section taxonomy, page budget, sentence craft, red flags, and review-simulator routing.
- `aaai-review-simulator`: useful for strict scoring and reviewer-risk synthesis, but it should not write prose by itself.
- `nature-writing` / `nature-polishing`: useful for router design, static/dynamic split, section-specific loading, and claim/evidence discipline.
- `nature-reviewer`: useful for separating reviewer assessment from author response.

## External Skill Repositories

- `Master-cai/Research-Paper-Writing-Skills`: paper-writing workflow with paragraph flow, section references, claim-evidence alignment, and reviewer-friendly presentation.
- `FanBroWell/AI-paper-reviewer`: pre-submission audit layer for claim strength, citations, numbers, anonymity, reproducibility, and AI-smell.
- `SNL-UCSB/paper-writing-skill`: strong project-context workflow, topic-sentence-first drafting, compression, mechanical gates, and independent red-team pattern.
- `conorbronsdon/avoid-ai-writing`: useful AI-ism catalog, especially negative parallelism, connector stacking, generic vocabulary, and rewrite/detect separation.
- `AIScientists-Dev/academic-humanizer`: useful academic-specific guardrail: preserve citations, numbers, calibrated hedging, and scholarly register while removing AI tells.
- `blader/humanizer`: useful catalog of Wikipedia-style AI-writing signs, especially formulaic significance, vague attribution, copula avoidance, and rule-of-three overuse.
- `d-wwei/great-writer`: useful four-pass polish model: oral/readability test, density and rhythm, AI trace removal, and anti-style checking.

## AAAI Award Pages

The AAAI-24 and AAAI-25 paper award pages list outstanding papers and describe the award standard as combining technical contribution and exposition. Use these award lists as calibration targets for narrative clarity, not as proof that copying their sentence patterns guarantees acceptance.

Examples used as high-level calibration anchors:

- AAAI-25: `Every Bit Helps`, `Efficient Rectification of Neuro-Symbolic Reasoning Inconsistencies by Abductive Reflection`, `Revelations`.
- AAAI-24: `GxVAEs`, `Reliable Conflictive Multi-view Learning`, `Proportional Aggregation of Preferences for Sequential Decision Making`, `DISCount`.

## Practical Synthesis

The new skill keeps:

- claim-first architecture,
- topic-sentence-first drafting,
- introduction written twice,
- evidence-calibrated verbs,
- figure/table plan as part of the story,
- mechanical audit with grep output,
- anti-defensive rewrite rules.
- academic anti-AI-smell editing that improves specificity and rhythm without casualizing the manuscript.

The new skill rejects:

- piling many broad writing guides into context,
- turning a review prompt into a writing prompt,
- rhetorical `not-but` contrast as a default style,
- over-conservative prose that hides the main contribution,
- unsupported hype words as a cure for defensive writing.
- detector-evasion framing. AI-smell reduction is treated as scholarly revision, not as a way to bypass AI-use policies.
