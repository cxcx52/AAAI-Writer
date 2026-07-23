# Defensive Style Gate

This gate targets the user's observed failure mode: safe, scope-aware prose that overuses contrast and limitation language until the paper reads defensive.

## Mechanical Triggers

Run `scripts/audit_aaai_style.py` on available source files. Inspect every hit for:

- `not X but Y`
- `not only X but Y`
- `rather than`
- `instead`
- `not a claim`
- `does not claim`
- `not to defend`
- `not a general`
- `only conditional`
- repeated `however`, `while`, `though`, `although`
- generic adjectives and AI-smell phrases
- formulaic academic openers such as `In recent years`, `With the rapid development of`, and `Despite recent advances`
- connector stacking such as repeated `Furthermore`, `Moreover`, `Additionally`, `Notably`, and `Importantly`
- synonym cycling for the same method, task, or dataset

## Density Rule

For an 8-page AAAI paper:

- 0-3 factual contrast sentences: normal.
- 4-7: inspect density and cluster locations.
- 8 or more: rewrite the paper's stance unless most are in related work or limitations.

The two user-provided PDFs both had about six `rather than` hits in 8 pages. That is not automatically wrong, but it is high enough to require a pass.

## Keep, Move, Rewrite

Use this decision table:

| Case | Action |
|---|---|
| The contrast distinguishes the paper from a close prior work | Keep, but make it specific and cite the prior work |
| The contrast prevents overclaiming | Move to a single scope paragraph or limitations section |
| The contrast is rhetorical polish | Rewrite as a positive claim |
| The contrast repeats an already stated boundary | Delete |
| The contrast appears in abstract or contribution bullets | Rewrite unless indispensable |

## Rewrite Patterns

Pattern 1: Positive scope first.

```text
Before: Our work studies X rather than Y.
After: Our work studies X under <condition>. Y remains outside this evaluation.
```

Pattern 2: Mechanism instead of negation.

```text
Before: This is not a new general framework for calibration.
After: The audit fixes a finite protocol family and optimizes paired bin choices inside that family.
```

Pattern 3: Replace apology with evidence.

```text
Before: The result is descriptive rather than causal.
After: The analysis reports descriptive associations over frozen trajectories.
```

Pattern 4: One limitation, not three.

```text
Before: This is not deployed, not causal, and not a population estimate.
After: The experiment is a controlled benchmark study; deployment, causal, and population claims require separate evidence.
```

Pattern 5: Prior-work distinction without hostility.

```text
Before: Prior methods do not address X.
After: Prior methods optimize <A>; NAME evaluates <B>, where <technical difference> changes the decision.
```

## Anti-AI-Smell Rules

- Remove `In this paper, we...` unless the sentence immediately states the contribution.
- Replace `extensive experiments demonstrate` with the actual datasets, baselines, and headline number.
- Avoid three consecutive sentences with the same subject.
- Avoid repeated connector stacking: `However`, `Furthermore`, `Moreover`, `Additionally`.
- Replace `plays an important role` and `is challenging` with the mechanism or cost.
- Keep mean sentence length near 20-25 words; split sentences over 40 words.
- Keep academic precision. Do not replace correct technical hedging with casual certainty.
- Repeat defined technical terms instead of rotating synonyms to sound varied.
- Treat `not X but Y` and `not only X but also Y` as a scarce rhetorical resource: one deliberate use can work, repeated use reads generated.

## Output For Style Audits

Return:

| Pattern | Count | Risk | Fix strategy |
|---|---:|---|---|
| Defensive contrast | <n> | low/medium/high | keep/move/rewrite |
| Generic adjectives | <n> | low/medium/high | replace/delete |
| AI-smell phrases | <n> | low/medium/high | rewrite |

Then provide concrete rewrites for the highest-risk sentences.
