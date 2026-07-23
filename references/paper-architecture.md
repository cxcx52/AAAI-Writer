# Paper Architecture

## Planning Contract

Before drafting polished prose, produce these artifacts:

| Artifact | Purpose |
|---|---|
| Identity sentence | One sentence answering: what does the paper show? |
| Paper type | Algorithm/theory, method/model, benchmark/resource, application-driven, or systems/agent evaluation |
| Key abstraction | A 2-4 word name for the contribution readers should remember |
| Claim-evidence map | Every major claim linked to a figure, table, theorem, experiment, or planned result |
| Page budget | AAAI main text discipline, usually 7 pages excluding references |
| Figure/table plan | Each visual answers one reader question |

## Narrative Spine

Use this order for the introduction and the whole paper:

1. Stakes: name the task, affected users, or scientific question.
2. Structural gap: explain which assumption in current approaches fails.
3. Key abstraction: name the concept that organizes the paper.
4. Design intuition: explain how the method or benchmark follows from the abstraction.
5. Evidence preview: give the headline result only after it is real.
6. Contributions: list claims, not activities.

Bad spine:

```text
Prior work does X. Prior work does not do Y. We do Y.
```

Better spine:

```text
Evaluation requires Y because X collapses under condition Z. The paper introduces NAME to measure/control Z directly. Experiments show when Z changes the conclusion.
```

## Draft Order

Use Draft 0 before the evidence is final:

1. Draft 0 introduction as a framing scaffold.
2. Evaluation plan with claim-to-experiment mapping.
3. Method/problem formulation.
4. Related work as positioning, not bibliography.
5. Final introduction rewritten from scratch.
6. Abstract last.

## AAAI Page Budget

| Section | Target |
|---|---:|
| Introduction | 1.0-1.4 pages |
| Related Work | 0.5-0.9 pages |
| Problem/Formulation | 0.5-1.0 pages |
| Method/Analysis | 1.5-2.3 pages |
| Experiments | 2.0-2.8 pages |
| Conclusion/Limitations | 0.2-0.5 pages |

If a section exceeds budget, compress by removing tutorial background, moving details to appendix, and promoting dense number lists to figures or tables.

## Figure/Table Plan

Every AAAI paper needs a first-page memory object when possible:

- Concept or pipeline figure for method/model papers.
- Benchmark construction and protocol figure for benchmark/resource papers.
- Decision geometry or theorem intuition figure for theory/algorithm papers.
- Main result table plus one diagnostic figure for empirical papers.

Each figure must answer one question:

```text
Figure: <name>
Question answered: <what reviewer learns>
Claim supported: <introduction/contribution claim>
Minimal caption takeaway: <one sentence>
```

## Integration Checks

- Abstract sentence 1 maps to introduction paragraph 1.
- Every contribution bullet maps to one method/design element and one evidence item.
- Section headings carry conclusions where possible.
- The first sentence of each section tells a coherent story when read in sequence.
- Related work states categories and assumptions, not one-paper summaries.
