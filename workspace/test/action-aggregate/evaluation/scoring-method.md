# Scoring method — the evaluation harness

*How `evaluation/` decides whether a generated `../output/` is **substantially the same** as the
target `../output-example/`. This is the spec; `structural_check.py` implements Layer A and
`semantic-judgment.md` drives Layer B.*

## What we are scoring, and against what

- **Scored object:** the node's Step-2 result — `output/role-action-catalog.md` (the role-action
  table with substantial descriptions). The Step-1 products (`algorithm.md`, `declaration.md`) are
  scored separately and lightly (shape/intent only — see §6).
- **Target:** `output-example/role-action-catalog.md` — a **comparison example, not an answer key**.
- **Bar:** `input/contract.md` §3 — **same roles**, **substantially the same actions** modulo
  naming / granularity / open-list, with **traceability** and **integrity**.

Because the deliverable is an **open list** with free IDs and naming, success is *substantial match*,
not identity. That single fact forces the harness into **two layers**.

## Two layers

**Layer A — structural / deterministic** (`structural_check.py`, runnable now).
Parses the catalog and checks the mechanical criteria: IDs well-formed & unique, actions grouped
under known roles, no retired-ID reuse, every row Source-cited, descriptions not thin. Also emits a
**lexical pre-alignment** (token-overlap candidate matches) to seed Layer B. Layer A *proposes and
screens*; it never judges "substantially the same." A Layer-A `FAIL` is acceptance-blocking on its
own — a table with duplicate IDs or missing Sources fails integrity/traceability regardless of
semantics.

**Layer B — semantic judgment** (`semantic-judgment.md`, LLM/human, rubric-driven).
Finalizes the alignment example↔output by *meaning* (matched / partial / merged / split / missing /
extra), and judges description substance. This is where "substantially the same" is actually decided.
Deterministic code cannot do it (paraphrase and re-granularization defeat string matching — proven
by the negative-test fixture, where a paraphrased action scored 0.13 lexically yet is a true match).
The rubric pins *how* the judgment is made so two independent judges converge.

## Dimensions & weights

| # | Dimension | Question | Layer | Weight |
|---|---|---|---|---|
| 1 | **Role match** | Is every example role present (semantically)? No unjustified extra roles? | A proposes → B confirms | 25 |
| 2 | **Action coverage** | What fraction of example actions have a semantic match in the output? | B | 35 |
| 3 | **Traceability** | Does every output row cite a Source that exists in the frozen inputs? | A (+ B spot-check) | 15 |
| 4 | **Integrity** | IDs unique & well-formed, grouped by role, deduped, no retired-ID reuse? | A | 10 |
| 5 | **Substance** | Does every role & action carry a *substantial* description (not just an ID)? | A screens → B judges | 15 |

**Overall = weighted sum, 0–100.**

## Gates (before the weighted score means anything)

Some failures are disqualifying regardless of the number:

- **G1 — Integrity gate.** Layer A `FAIL` on `action_ids_unique_wellformed`, `no_retired_id_reuse`,
  or `actions_grouped_by_role` ⇒ **not acceptable**; fix and re-run before scoring.
- **G2 — Traceability gate.** Any output row missing a Source ⇒ **not acceptable** (the Source *is*
  the derivation trace; §3 makes it binding).
- **G3 — Role gate.** Any **example role missing** from the output ⇒ capped at "partial"; roles are
  the *pinned* part of the contract (§5), so a missing role is a structural miss, not open-list slack.

A run that clears G1–G3 is then scored on the five dimensions.

## How each dimension is scored

**1. Role match (25).**
`role_score = matched_example_roles / total_example_roles − 0.5 · unjustified_extra_roles/total`.
Extra roles are only penalized when the judge marks them *unjustified* (not traceable to Phase 5 +
the layer model). Example set = R-00…R-07 (8 roles).

**2. Action coverage (35).** The core "substantial" number.
For each example action the judge assigns: `matched` = 1.0, `partial` (right idea, weaker/narrower, or
only one side of a split) = 0.5, `missing` = 0.
`coverage = Σ(match_value) / total_example_actions`. Example set ≈ 63 actions.
**Open-list rule:** output actions with **no** example counterpart are **not** counted against
coverage *if* the judge marks them `extra-justified` (traceable, plausible). Only `spurious`
(untraceable/invented) extras cost — via the traceability dimension, not coverage.

**3. Traceability (15).** `traceability = sourced_rows / total_rows`, from Layer A (0/1 per row).
Layer B spot-checks that cited Sources actually support the row (a citation to a real but irrelevant
phase is a Layer-B deduction, sampled).

**4. Integrity (10).** Fraction of Layer-A integrity checks passing
(`ids_unique_wellformed`, `no_retired_id_reuse`, `actions_grouped_by_role`, `no_obvious_text_dupes`).
Note the hard ones are already gates (G1); this dimension rewards the softer integrity signals.

**5. Substance (15).** Two parts, averaged: (a) Layer-A screen — fraction of rows above the thin
threshold; (b) Layer-B quality — sampled judgment that descriptions say *what the action/role is*,
not merely restate the name. `substance = 0.5·screen + 0.5·quality`.

## Verdict

`overall = 0.25·role + 0.35·coverage + 0.15·traceability + 0.10·integrity + 0.15·substance`, ×100.

| Overall | Gates | Verdict |
|---|---|---|
| ≥ 85 | all clear | **Substantially the same** — accept |
| 70–84 | all clear | **Close** — accept with noted gaps; list missing/partial actions |
| < 70, or any gate failed | — | **Not substantially the same** — return with the gap list |

The threshold is deliberately not 100: naming, granularity, which position-derived actions get
elaborated, and the open-list tail are *expected* variation (§5). The report must always accompany
the number with the **gap list** (missing + partial example actions) and the **extras list**
(output actions to classify) — the number without the lists is not a usable result.

## Reproducibility of the evaluation itself

Layer A is deterministic — same input, same report. Layer B is LLM/human judgment; the rubric,
the fixed alignment categories, and the worked scorecard template (`semantic-judgment.md`) are what
make two judges converge — the same discipline the contract asks of the node (§5), applied to the
scorer. Provenance: every deduction in a scorecard cites the row(s) and the rule it applies.
