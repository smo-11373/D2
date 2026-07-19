# Design note — the evaluation harness (scratch)

*Intermediate working notes. The polished harness lives in `../evaluation/`.*

## What the harness must do

Score a generated `output/` against `output-example/` and decide **"substantially the same"** —
per `input/contract.md` §3 acceptance: **same roles**, **substantially the same actions** modulo
naming / granularity / open-list, plus **traceability** (every row Source-cited) and **integrity**
(stable/unique IDs, grouped by role, deduplicated).

Key tension: the primary product (`role-action-catalog.md`) is an **open list** and IDs/naming are
free to vary. So matching is **semantic**, not string-equality. But several acceptance checks are
**mechanical** (Source present? IDs unique? roles grouped?). ⇒ **two layers.**

## Two-layer design

**Layer A — structural / deterministic (code).** Parse both catalogs; verify the mechanical
acceptance criteria; emit a structural report. Runnable now; run it against `output-example/` itself
as a self-test (the reference must pass its own structural checks — Verification Before Realization,
Phase 2 §P4). This layer also produces a **lexical pre-alignment** (token-overlap candidate matches)
to seed Layer B — it proposes, it does not judge.

**Layer B — semantic judgment (LLM/human, rubric-driven).** Finalize the alignment example↔output
(matched / partial / merged / split / missing / extra), judged by role + action *meaning*, not text.
Score coverage and substance. Deterministic code cannot judge "substantially the same"; the rubric
pins *how* the judgment is made so two judges converge.

## Scoring dimensions & weights (first cut)

| Dim | What | Layer | Weight |
|---|---|---|---|
| Role match | every example role present (semantically); no unjustified extra roles | A proposes / B confirms | 25 |
| Action coverage | fraction of example actions with a semantic match in output (open-list ⇒ this is the core "substantial" number) | B | 35 |
| Traceability | every output row cites a Source that exists in the frozen inputs | A | 15 |
| Integrity | IDs unique & well-formed, grouped by role, deduped, no retired-ID reuse | A | 10 |
| Substance | each role & action carries a substantial description (not just an ID) | A screens length / B judges quality | 15 |

Overall = weighted sum, 0–100. **Threshold: ≥ 85 ⇒ "substantially the same."** Extras in the output
are **open-list-allowed** — not penalized under coverage; only *spurious/untraceable* extras cost
(they fail traceability). Missing example roles are near-fatal (roles are the *pinned* part).

## Matching procedure (the alignment)

1. **Role align.** Match by ID if reused, else by name/meaning. Every example role must map to ≥1
   output role. Report unmatched-example (gap) and unmatched-output (extra → must be justified).
2. **Action align (within matched roles).** Many-to-many: an example action may **split** into
   several output actions or several example actions may **merge** into one — both count as covered
   if the semantic content is present. Classify each example action: `matched` / `partial` /
   `missing`. Classify each output action: `aligned` / `extra-justified` / `spurious`.
3. **Coverage** = matched(full=1, partial=0.5) / total example actions.

## Files to produce in `evaluation/`

- `README.md` — overview + how to run + status (replaces the EMPTY stub).
- `scoring-method.md` — the spec above, formalized (dimensions, weights, procedure, thresholds,
  scorecard format).
- `structural_check.py` — Layer A: parser + structural checks + lexical pre-alignment; stdlib only.
- `semantic-judgment.md` — Layer B: the judge rubric + alignment worksheet + scorecard template.

## Self-test plan

Run `structural_check.py` on `output-example/role-action-catalog.md`:
- expect: 8 roles (R-00…R-07), ~60 actions, all Source-cited, IDs unique, A-003 absent (retired).
- this validates the parser and gives a **baseline** the generated output is scored against.
