# AAAI Paper Architect

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A Codex skill for planning, rewriting, tightening, and restructuring AAAI papers and revision packages.

`aaai-paper-architect` is built for the layer between technical content and acceptance-facing presentation:

- claim-first paper architecture;
- evidence-calibrated contribution framing;
- section-level rhetorical control;
- de-defensifying academic prose;
- reducing templated AAAI writing patterns;
- rebalancing main paper versus supplement during revision;
- tightening title, abstract, TL;DR, and OpenReview-facing metadata;
- reusing valid frozen artifacts instead of rerunning work by default.

## What It Does

The skill helps Codex:

- turn a paper idea into an identity sentence, contribution set, and page-budgeted outline;
- rewrite abstracts, introductions, methods, experiments, related work, and conclusions;
- map claims to evidence before polishing prose;
- reduce mirrored contribution structures, repeated binary framing, and generic AI-style transitions;
- keep reviewer-critical results in the main paper when page budget permits;
- calibrate scope so controls and robustness checks are not overstated;
- audit local `.tex`, `.txt`, and `.md` paper directories with the bundled style script.

## Best Use Cases

Use it when you have one of these situations:

- an AAAI paper idea that needs a defensible narrative spine;
- a draft whose writing is too defensive, too templated, or too uniform;
- a revision package whose supplement is carrying too much of the acceptance decision;
- abstract, TL;DR, keyword, or OpenReview text that has become dense or over-claimed;
- a local submission folder with frozen artifacts that should be reused unless truly invalidated.

## Install

Codex reads personal skills from `$CODEX_HOME/skills` when `CODEX_HOME` is configured, otherwise from `~/.codex/skills`. Clone this repository into that directory. The GitHub repository is named `AAAI-Writer`, but the destination folder should be `aaai-paper-architect` so it matches the skill name.

PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
git clone https://github.com/cxcx52/AAAI-Writer.git "$HOME\.codex\skills\aaai-paper-architect"
```

macOS or Linux:

```bash
mkdir -p "$HOME/.codex/skills"
git clone https://github.com/cxcx52/AAAI-Writer.git "$HOME/.codex/skills/aaai-paper-architect"
```

Open a new Codex task after installation so the skill catalog refreshes.

## Invoke

Example prompt:

```text
Use $aaai-paper-architect to rebuild my AAAI paper or revision package into a clearer claim-first manuscript.
```

For a useful first pass, provide the main `.tex` entry point, current build folder or PDF, supplementary source if present, reviewer comments if present, and the current page-budget constraint.

See [中文使用说明](docs/usage_zh.md) and the [copyable example request](examples/example_input.md).

## Expected Output

Depending on the task, the skill returns:

- an identity sentence and narrative spine;
- contribution claims plus claim-evidence mapping;
- section-level rewrite plans or rewritten text;
- main-paper versus supplement moves for revision packages;
- title, abstract, keyword, TL;DR, or OpenReview edits when needed;
- residual evidence, scope, and reviewer-risk notes.

## Repository Contents

- `SKILL.md`: core workflow and boundaries
- `agents/openai.yaml`: UI metadata and default invocation prompt
- `references/paper-architecture.md`: whole-paper planning and page budget
- `references/claim-calibration.md`: contribution and claim-strength control
- `references/defensive-style-gate.md`: defensive-style rewrite guidance
- `references/anti-ai-academic-style.md`: anti-template and anti-AI-smell guidance
- `references/section-playbook.md`: section-specific drafting patterns
- `references/source-basis.md`: provenance for the skill synthesis
- `scripts/audit_aaai_style.py`: local rewrite-queue audit script
- `docs/usage_zh.md`: concise Chinese usage guide
- `examples/example_input.md`: realistic request template
- `CHANGELOG.md`: public release history
- `LICENSE`: MIT license

## Scope

This skill rewrites arguments, prose, section structure, and revision packaging. It does not invent evidence, citations, or results, and it does not rerun frozen experiments unless a requested change makes the existing artifact set invalid.
