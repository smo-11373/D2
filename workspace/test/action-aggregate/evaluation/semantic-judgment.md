# Layer B — semantic judgment (the rubric)

*How a judge (LLM or human) turns Layer A's lexical pre-alignment into the final "substantially the
same" verdict. Weights, gates, and formulas live in `scoring-method.md`; this file is the
**procedure** and the **templates** that make two judges converge.*

## Inputs the judge receives

1. `structural_check.py --compare output/…-catalog.md output-example/role-action-catalog.md` output
   — the structural report (must be `PASS`, gates G1–G2 clear) + the lexical pre-alignment worksheet.
2. Both catalogs, and read access to `../environment/` (the frozen inputs) for traceability
   spot-checks.

## Why a judge is needed (not more code)

Lexical matching proposes; it cannot decide. In the negative-test fixture, the example action
*"Provide the initial design input (Predecessor D1 package + intended change)"* was paraphrased to
*"Give the starting design materials — the prior D1 build plus the change the Designer wants"* and
scored **0.13** lexically — a true match the code called `MISSING?`. Re-granularization (one example
action split into two output actions, or two merged into one) breaks string matching the same way.
The judge resolves these by **meaning**.

## Procedure

### Step 1 — confirm role alignment
For each example role, accept Layer A's match or correct it by meaning (name may differ; role is the
same responsibility boundary). Mark each: `matched` / `missing` (example role absent from output) /
`extra` (output role with no example — then judge `extra-justified` vs `unjustified` against Phase 5
Item 3 + the D2→D1→D0 layer model). **Any `missing` trips gate G3.**

### Step 2 — finalize action alignment (per matched role)
Walk each example action. Starting from the proposed match, assign one category:

| Category | Meaning | Coverage value |
|---|---|---|
| `matched` | same action, whatever the wording/ID | 1.0 |
| `partial` | right idea but narrower/weaker, **or** only one half of a split is present | 0.5 |
| `merged` | several example actions collapsed into one output action that covers them | 1.0 to each covered example action |
| `split` | one example action realized as several output actions | 1.0 (count the example action once) |
| `missing` | no output action carries this meaning | 0.0 |

Then walk **output actions with no example counterpart** (the worksheet's "unmatched" list) and mark
each `extra-justified` (traceable to the inputs, plausible member of the open list) or `spurious`
(untraceable/invented — e.g. the fixture's *"Reboot the universe nightly"*). `extra-justified` costs
nothing (open-list); `spurious` is a traceability deduction.

Granularity differences (`merged`/`split`) are **expected variation, not error** — do not penalize
them; only penalize *lost meaning*.

### Step 3 — traceability spot-check
Layer A already verified a Source string exists on every row. Sample ~10 rows (bias toward
position-derived and any the judge doubts) and confirm the cited Source **actually supports** the
row. A citation to a real but irrelevant phase is a deduction.

### Step 4 — substance judgment
Sample ~10 roles/actions. Confirm the description says *what the thing is / does*, not merely a
longer restatement of the name. Score `quality` ∈ [0,1] as the sampled fraction that are substantial.

### Step 5 — score & write the scorecard
Apply the formulas in `scoring-method.md`. Fill the template below. Always attach the **gap list** and
**extras list**; the number alone is not a result.

## Alignment worksheet (fill from the pre-alignment)

```
| example_action | role | category | output_action(s) | note (why) |
|----------------|------|----------|------------------|------------|
| A-013          | R-01 | matched  | A-0xx            | paraphrase; same meaning |
| ...            |      |          |                  |            |
```

Extras:
```
| output_action | role | class            | note |
|---------------|------|------------------|------|
| A-0xx         | R-04 | spurious         | untraceable; no Source support |
```

## Scorecard template

```
# Evaluation scorecard — <output path> vs output-example
Date: <YYYY-MM-DD>   Judge: <id>   Structural: PASS/FAIL (Layer A)

Gates:  G1 integrity [ ]   G2 traceability [ ]   G3 roles-complete [ ]

Dimension        Raw                         Weight  Weighted
Role match       <m>/8 roles, <x> extras      25     <..>
Action coverage  Σmatch <v> / 63 = <c>        35     <..>
Traceability     <s>/<n> rows sourced         15     <..>
Integrity        <k>/4 checks                 10     <..>
Substance        0.5·screen + 0.5·quality     15     <..>
-----------------------------------------------------------
OVERALL                                       100    <NN>/100

Verdict: Substantially the same / Close / Not substantially the same

Gap list (missing + partial example actions):
  - A-0xx (R-0y) missing — <why it should have surfaced>
  ...
Extras list (output actions to classify):
  - A-0xx (R-0y) spurious — <why>
  ...
Notes:
  - <granularity differences observed, judgment calls, provenance of deductions>
```

## Convergence discipline

- Judge by **meaning**, never by ID or wording.
- `merged`/`split`/renamed ⇒ not penalties. Only **lost meaning** and **spurious/untraceable**
  content cost.
- Every deduction cites the row(s) and the rule (from `scoring-method.md`) it applies.
- When uncertain between `matched` and `partial`, default to `partial` and record the doubt — same
  "make the residual visible" discipline the contract asks of the node (§5).
