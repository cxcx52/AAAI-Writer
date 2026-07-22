# Main vs Supplement

## Principle

AAAI reviewers are not obligated to read the supplement. Anything needed to judge novelty, technical correctness at a high level, empirical relevance, or robustness scope should stay in the main paper if page budget allows.

## Keep in the main paper

- the exact research question or audit object;
- the minimum formalism needed to understand what is being optimized, audited, or compared;
- the experimental questions that support the headline claim;
- the principal results, including the negative result when it bounds the paper's claim;
- the one or two diagnostics that prevent an obvious misreading of the main result;
- the practical interpretation or reporting recommendation if it is part of the contribution.

## Move to the supplement

- complete derivations and proofs after the main intuition is already clear;
- exhaustive sensitivity sweeps once the main trend is established in the paper;
- provenance manifests, file maps, and runtime logs;
- replayable endpoint constructions, exhaustive cut tuples, and larger supporting tables;
- secondary diagnostics that sharpen interpretation but are not necessary for acceptance.

## Anti-patterns

- A supplement that restates the abstract, definitions, and conclusion almost in parallel with the main paper.
- A main paper that refers to a headline mechanism or robustness result that only becomes understandable in the supplement.
- Moving core model lists, exact witness examples, or key distribution summaries out of the main paper when they directly explain the result.

## Compression rule

When a result must stay in the main paper, compress by reducing narrative scaffolding first, not by pushing the core evidence into the supplement.
