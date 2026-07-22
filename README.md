# AAAI Revision Detemplater

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

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

Codex reads personal skills from `$CODEX_HOME/skills` when `CODEX_HOME` is configured, otherwise from `~/.codex/skills`. Clone this repository into that directory. The GitHub repository is named `AAAI-Writer`, but the destination folder must be `aaai-revision-detemplater` so it matches the skill name.

The commands below use the default `~/.codex/skills` location.

PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
git clone https://github.com/cxcx52/AAAI-Writer.git "$HOME\.codex\skills\aaai-revision-detemplater"
```

macOS or Linux:

```bash
mkdir -p "$HOME/.codex/skills"
git clone https://github.com/cxcx52/AAAI-Writer.git "$HOME/.codex/skills/aaai-revision-detemplater"
```

Open a new Codex task after installation so the skill catalog is refreshed.

## Invoke

Example prompt:

```text
Use $aaai-revision-detemplater to rebuild this AAAI paper and supplement while reusing valid experiment artifacts.
```

For a useful first pass, provide the main `.tex` entry point, supplementary source, current PDF or build folder, reviewer comments if available, and any existing upload ZIPs. State the page budget and whether experiment artifacts are frozen.

See [中文使用说明](docs/usage_zh.md) and the [copyable example request](examples/example_input.md).

## Expected output

A package-level run returns:

- a revision diagnosis and one-sentence narrative spine;
- specific main-paper and supplement moves;
- title, abstract, keyword, TL;DR, and OpenReview edits when present;
- an artifact-reuse plan that identifies what can remain frozen;
- residual claim, page-budget, and upload-package risks.

## Repository contents

- `SKILL.md`: core workflow and operating boundaries
- `agents/openai.yaml`: UI metadata and default invocation prompt
- `references/narrative-rebuild.md`: how to reconstruct the story
- `references/main-vs-supplement.md`: main-paper versus supplement allocation
- `references/artifact-governance.md`: fact sheets, claim boundaries, and package records
- `references/upload-audit.md`: source ZIP, PDF preview, checksum, and portal checks
- `references/metadata-surfaces.md`: abstract, TL;DR, title, and keywords
- `references/evidence-calibration.md`: how to avoid overclaiming
- `docs/usage_zh.md`: concise Chinese usage guide
- `examples/example_input.md`: realistic request template
- `CHANGELOG.md`: public release history
- `LICENSE`: MIT license

## Scope

This skill revises arguments, prose, source layout, metadata, and submission packaging. It does not invent evidence, guarantee acceptance, or rerun frozen experiments unless a requested change invalidates the existing artifacts.
