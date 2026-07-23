# Claim Calibration

## Claim Ladder

Use the strongest verb justified by the evidence.

| Verb | Evidence required | Example use |
|---|---|---|
| `suggests` | Directional trend or incomplete evidence | Exploratory analysis, ablation without full controls |
| `shows` | Direct empirical result with clear setup | Main tables, paired comparisons, controlled benchmark |
| `demonstrates` | Multiple consistent results across settings | Main claim backed by baselines and sensitivity |
| `establishes` | Formal result or exhaustive controlled evidence | Theorem, proof, exact enumeration, certified property |
| `proves` | Formal proof only | Theorem statements |

Avoid `novel`, `significant`, `state-of-the-art`, `comprehensive`, `robust`, and `substantial` unless a concrete number or formal statement immediately follows.

## Contribution Bullets

Each contribution should be a claim with evidence, not a process.

Weak:

```text
We propose a new benchmark and conduct extensive experiments.
```

Better:

```text
Benchmark. NAME isolates <failure mode> by holding <control> fixed across <N> settings.
Evidence. On <dataset/setup>, <metric> changes from <A> to <B>, showing <interpretation>.
```

Use 3-4 bullets:

1. Formulation or benchmark contribution.
2. Method or analysis contribution.
3. Empirical finding with headline number.
4. Resource/reproducibility contribution, if real.

## Claim-Evidence Table

Maintain this table before drafting:

| Claim | Evidence | Status | Allowed wording |
|---|---|---|---|
| <claim> | <figure/table/theorem/experiment> | have/planned/missing | suggests/shows/demonstrates/establishes |

Rules:

- If evidence is missing, do not draft the claim as a result.
- If evidence is descriptive, use descriptive verbs.
- If the result is controlled but not deployed, state the controlled setting once and keep the rest positive.
- If a limitation applies to many claims, centralize it in a limitations paragraph instead of repeating `not a claim that...` in every section.

## Positive Scope Control

Replace defensive boundary sentences with positive scope sentences.

Weak:

```text
This is not a claim that calibration rankings generally reverse.
```

Better:

```text
The result characterizes reversals within the frozen finite protocol family.
```

Weak:

```text
The learned policy is diagnostic rather than a proposed architecture.
```

Better:

```text
We use the learned policy as a diagnostic probe of which state features support commitment decisions.
```

Keep the boundary only when it blocks a likely reviewer misunderstanding. Even then, write the positive claim first.

## Reviewer Memory Test

After drafting, answer:

1. What one sentence should a reviewer remember?
2. Which figure/table proves it?
3. Which prior assumption does it change?
4. Which limitation is real but not central?
5. Which claim would be rejected if a reviewer demanded one more experiment?
