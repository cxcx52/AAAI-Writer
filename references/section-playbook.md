# Section Playbook

## Abstract

Use 5 moves:

1. Problem or evaluation gap.
2. Why current approaches fail, with a concrete assumption or cost.
3. Method/benchmark/formulation name.
4. Main evidence with numbers.
5. Takeaway and scope.

Rules:

- Do not cite in the abstract.
- Introduce the method name by sentence 3 or 4.
- Include at least one concrete number if the paper has results.
- Avoid starting with `In recent years`.
- Avoid ending with `code will be released`; end on the strongest result or implication.

## Introduction

Use the 6-move structure:

1. Stakes.
2. Structural gap.
3. Key abstraction.
4. Design intuition.
5. Contributions.
6. Results preview.

Write Draft 0 early, then rewrite final Introduction after experiments are stable. The final version should promise exactly what the paper delivers.

## Related Work

Organize by conceptual category, not by author list.

For each category:

```text
<Category> optimizes or assumes <A>. This leaves <B> unresolved in our setting because <technical reason>.
```

Use specific prior-work names when available. Avoid claiming a whole area ignores the problem unless the literature search supports that.

## Method / Problem Formulation

Each subsection follows:

1. Why this piece is needed.
2. Definition or mechanism.
3. What design choice it enables.
4. How it links to an experiment or theorem.

Before every equation, tell the reader what the equation computes. After every equation, explain the intuition or role.

## Experiments

Design experiments as answers to claims:

| Experiment | Claim tested | Baselines | Metric | Expected reviewer question |
|---|---|---|---|---|

Each result paragraph should include:

- setup anchor,
- number or comparison,
- interpretation,
- takeaway sentence.

Avoid listing numbers in prose when a table can carry them.

## Conclusion / Limitations

Conclusion should be short:

1. Restate the main finding with different wording from the abstract.
2. State what the evidence establishes.
3. State one or two real limitations without re-litigating every scope boundary.

Do not introduce new citations, experiments, or claims.

## Section Self-Check

Use this after drafting any section:

- Topic sentence sequence forms an argument.
- Every claim has evidence or is marked as planned/missing.
- No paragraph exists only to apologize for scope.
- No repeated `rather than`/`not-but` construction.
- The strongest contribution appears before its limitation.
- The section has at least one specific noun or number per paragraph.
