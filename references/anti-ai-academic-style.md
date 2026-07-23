# Academic Anti-AI-Style Gate

This gate removes formulaic AI-assisted prose while preserving the correct voice of an AAAI paper: precise, evidence-bound, technical, and usually written in first-person plural. It must not turn a paper into a blog post, and it must not help with disclosure evasion.

## Operating Principle

The fix for AI-smell is not "sound casual." The fix is:

1. Make each sentence carry a claim, mechanism, result, or transition.
2. Tie every empirical or novelty claim to a number, figure, table, citation, or scoped condition.
3. Use direct syntax when direct syntax is accurate.
4. Vary rhythm enough that the paper reads written, not generated.
5. Preserve terms, equations, citations, labels, and calibrated hedges.

## High-Priority Tells In AAAI Drafts

Fix these before word-level polishing:

| Tell | Why it hurts | Rewrite target |
|---|---|---|
| Negative parallelism: `not X but Y`, `not only X but also Y`, repeated `rather than` | Makes the paper sound defensive and generated | State the positive contribution, then add one scoped boundary if needed |
| Formulaic openings: `In recent years`, `With the rapid development of`, `Despite recent advances` | Wastes the first sentence and delays the claim | Open with the failure mode, technical gap, or empirical anomaly |
| Connector stacking: repeated `Furthermore`, `Moreover`, `Additionally`, `Notably`, `Importantly` | Creates filing-cabinet prose | Let paragraph order carry logic; use plain `but`, `so`, `therefore`, or no connector |
| Inflated academic adjectives: `novel`, `robust`, `comprehensive`, `significant`, `powerful`, `promising` | Replaces evidence with assertion | Name the mechanism, dataset count, baseline, metric, or condition |
| Clause-stacked sentences | Hides the main verb and weakens review memory | Split at the claim boundary; one sentence earns one job |
| Synonym cycling for the same object | Makes terminology unstable | Repeat the canonical term once it is defined |
| Generic contribution bullets | Reviewer cannot remember what changed | Each bullet contains method object + evidence preview + nearest contrast |
| Summary closers | Ends by repeating rather than advancing | Close with what the result licenses next, or stop after the scoped finding |

## Academic Exceptions

Do not over-correct these:

- Evidence-tied hedges such as `suggests`, `is consistent with`, `we hypothesize`, and `may indicate` are correct when uncertainty is real.
- Passive voice is acceptable when the actor is irrelevant, especially in methods.
- `we` is normal in AAAI papers.
- Technical uses of `robust`, `state-of-the-art`, `significant`, and `comprehensive` are acceptable when backed by a metric, statistical test, benchmark, or well-defined coverage set.
- Dense equations, definitions, and theorem statements may require uniform structure.
- Repetition of a defined method name is better than cycling through synonyms.

## Four-Pass Rewrite

Pass 1: claim skeleton.

- Extract one sentence per paragraph: what does this paragraph add?
- If two paragraphs add the same thing, merge or cut one.
- If a paragraph only says the topic is important, replace it with a specific failure, cost, or result.

Pass 2: evidence binding.

- For every strong verb, ask: what evidence licenses this verb?
- Replace `demonstrates` with `shows` or `suggests` when the evidence is empirical, narrow, or preliminary.
- Replace `significantly improves` with the exact metric and test, or with `improves` if no significance test is supplied.

Pass 3: rhythm and syntax.

- Avoid three consecutive sentences with nearly identical length or structure.
- Use short sentences sparingly for reviewer memory, not for drama.
- Prefer `X is Y` over `X serves as Y` when the simple form is accurate.
- Split sentences over about 35-40 words unless the sentence is a formal definition or theorem.

Pass 4: final AI-smell scan.

- Remove `delve`, `underscore`, `pivotal`, `seamless`, `holistic`, `leverage` as filler, `utilize`, `plays an important role`, and `it is worth noting`.
- Remove em-dash driven reversals in prose drafts; LaTeX ranges such as `3--5` are fine.
- Remove headings that announce generic structure without a claim.
- Keep only one deliberate antithesis per major section.

## Rewrite Patterns

Pattern: formulaic opening to gap-first opening.

```text
Before: In recent years, LLM agents have attracted increasing attention.
After: LLM agents still fail at a basic commitment problem: deciding when an intermediate result is reliable enough to act on.
```

Pattern: generic contribution to evidence-bound claim.

```text
Before: We conduct extensive experiments showing the robustness of our method.
After: Across three task suites and five seeds, the method reduces premature commits by 18-27% relative to the strongest agent baseline.
```

Pattern: AI-sounding contrast to positive scope.

```text
Before: We do not propose a general theory of agent commitment, but rather a practical evaluation protocol.
After: We define a practical evaluation protocol for agent commitment decisions under fixed task traces.
```

Pattern: clause stack to reviewer-memory sentence.

```text
Before: The proposed method, which combines calibration with trajectory-level auditing while preserving task-specific constraints, provides a robust way to analyze agent behavior.
After: The method audits commitment decisions at the trajectory level. It keeps task constraints fixed, so changes in score reflect the commitment policy rather than a changed task.
```

## Output For This Gate

Return:

| Issue | Severity | Example | Fix |
|---|---|---|---|
| Negative parallelism | high/medium/low | quoted span | positive-scope rewrite |
| Formulaic opening | high/medium/low | quoted span | gap-first rewrite |
| Evidence-free adjective | high/medium/low | quoted span | metric/mechanism rewrite |
| Uniform rhythm | high/medium/low | location | sentence split/merge plan |

Then provide the rewritten passage and a short note confirming that numbers, citations, equations, and labels were preserved.
