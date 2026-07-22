# Artifact Governance

## Use this file when

- the project already has frozen results, manifests, or upload archives;
- the prose is being revised without rerunning experiments;
- reviewer risk is driven by overclaiming, denominator ambiguity, or stale package records rather than by missing experiments.

## Keep these four ledgers separate

1. Result fact sheet
   Store artifact facts only: exact numbers, intervals, denominators, source files, and conditions.
   Do not write paper prose here.
2. Claim boundary list
   Split into `SUPPORTED`, `NOT CLAIMED`, and, when useful, `FORBIDDEN CLAIMS`.
   Use it to stop the draft from drifting into universal or externally validated language.
3. Reviewer risk matrix
   Record each plausible reviewer objection, severity, evidence, mitigation, and residual risk.
   This helps distinguish "must rewrite now" from "true limitation that should stay explicit."
4. Package audit record
   Track runtime wording, hash manifests, upload-folder contents, local checklist status, and any stale statements inherited from older submission passes.

## What these ledgers prevent

- abstract or conclusion language that outruns the actual artifact facts;
- denominator claims that silently harden from exploratory to definitive;
- old audit notes that contradict the final package;
- package regeneration done only because the team lost track of which archive is still valid.

## Practical rewrite rule

When revising a sentence:

1. verify the number or condition in the fact sheet;
2. verify the wording against the claim-boundary list;
3. check whether the sentence addresses a known reviewer risk;
4. if the sentence affects packaging or runtime description, update the package audit record too.

## Common patterns worth preserving

- Keep exploratory external checks explicitly exploratory instead of upgrading them into validation.
- Report both the mitigation and the residual risk when a reviewer objection cannot be eliminated.
- Treat runtime totals carefully when stage timers and end-to-end wall time use different measurement scopes.
- Update hash lists and upload manifests after text-only fixes if the package bytes changed.

## Output to produce when useful

- `result_fact_sheet.md`
- `claims_boundary.txt`
- `forbidden_claims.md`
- `reviewer_risk_matrix.csv`
- `package_validation.md` or equivalent final audit note
