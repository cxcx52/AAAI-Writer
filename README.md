# AAAI Revision Detemplater

A Codex skill for rebuilding AAAI revision packages into cleaner, more defensible submissions.

This skill is aimed at a specific failure mode that shows up in real paper revisions:

- the story becomes over-templated;
- contributions are forced into artificial symmetry;
- critical content gets pushed into the supplement;
- abstracts and TL;DR fields become numerically dense;
- conclusions sound stronger than the actual control or robustness evidence;
- authors rerun packages unnecessarily instead of reusing valid frozen artifacts.

`aaai-revision-detemplater` fixes that layer.

## What it does

The skill helps Codex:

- rebuild the paper's narrative spine from the real review question;
- reduce template feel in titles, contributions, section names, and experiment framing;
- decide what must stay in the main paper versus what belongs in supplementary material;
- tighten title, abstract, keywords, TL;DR, and OpenReview registration text;
- soften over-strong claims so they match the actual evidence scope;
- prefer package reuse over unnecessary recomputation.

## Why this is different

Most paper-writing prompts optimize for fluent prose.

This skill optimizes for revision quality under AAAI constraints:

- reviewer-facing clarity;
- evidence-calibrated claims;
- main-paper-first content allocation;
- lower "AI smell" from mirrored structure and repetitive rhetorical framing.

## Best use cases

Use it when you already have:

- a working AAAI `.tex` submission;
- figures, tables, and experiment artifacts;
- a supplementary document or upload package;
- reviewer comments or internal critique;
- a draft that feels technically solid but rhetorically too uniform.

## Install

Clone or copy this repository into your local Codex skills directory so the folder name matches the skill name:

```powershell
git clone https://github.com/cxcx52/AAAI-Writer.git "$HOME\\.codex\\skills\\aaai-revision-detemplater"
```

If you already cloned it elsewhere, make sure the usable skill folder is named:

```text
aaai-revision-detemplater
```

## Invoke

Example prompt:

```text
Use $aaai-revision-detemplater to rebuild this AAAI paper and supplement into a reviewer-facing revision package without rerunning experiments.
```

## Repository contents

- `SKILL.md`: core workflow and operating boundaries
- `agents/openai.yaml`: UI metadata and default invocation prompt
- `references/narrative-rebuild.md`: how to reconstruct the story
- `references/main-vs-supplement.md`: main-paper versus supplement allocation
- `references/metadata-surfaces.md`: abstract, TL;DR, title, and keywords
- `references/evidence-calibration.md`: how to avoid overclaiming

## Current limitation

The repository name is currently `AAAI-Writer`, while the actual skill name is `aaai-revision-detemplater`.

For discoverability and installation ergonomics, renaming the repository to `aaai-revision-detemplater` would be cleaner.
