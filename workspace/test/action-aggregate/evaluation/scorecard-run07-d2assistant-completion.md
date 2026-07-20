# Evaluation scorecard — D2-ASSISTANT COMPLETION run (run-07) vs `output-example/`

*Blind clean-room run after (a) the **fundamentals completion** naming the D2 Assistant a
Human-Position-First position, re-synced into the benchmark's constitution snapshot, and (b) the
**calibrated** distinctness guard. Generator: fresh sub-agent, forbidden `output-example/`,
`evaluation/`, `work/`, `benchmark_verification/`. Judge (Layer B): Claude. Baselines: run-05
(over-elaborated ≈89), run-06 (over-merged ≈85) in `../work/`.*

Date: 2026-07-19   Engine: fresh blind sub-agent   Judge: Claude (Layer B)
Structural (Layer A): **PASS** (exit 0) · **8 roles · 62 actions** · all 7 checks green

## Headline — best result yet, and it validates two changes at once

**First run with full role coverage: 8/8, clean 1:1 alignment** (R-00…R-07 all match by id *and*
name — including **R-07 D2 Assistant**, derived from `completions.md C-2026-07-19-1`). Its three example
actions — conduct/answer (A-059), route (A-060), present (A-062) — are now **homed**; the orphaned-work
gap is closed **by construction** (a named position → conformance requires it). Work-conservation
reported **nothing orphaned**. And the **calibrated distinctness guard worked**: it merged genuine
mechanics (reserve-authority, node-report+submission) while **preserving fundamentals-made distinctions**
— monitor-cost (A-017) vs monitor-health (A-018), routine vs user-facing health (A-047/A-048) — so no
over-merge (run-06's failure) and no over-elaboration (run-05's, 62 vs 67).

## Gates

| Gate | Result |
|---|---|
| Conformance (gating) | **CLEAR** — all named positions present, incl. the completion-named D2 Assistant |
| Completeness + **work-conservation** | **CLEAR** — no orphaned actions; every position kept |
| Distinctness (calibrated) | **CLEAR** — mechanics merged, fundamentals-made distinctions preserved |
| G1 / G2 / G3 | integrity clear; traceability clear (completions cited in-namespace); **G3 now CLEAR — every example role present** |

## Scores (Layer B estimate)

| Dimension | run-07 | Weight | Weighted | vs run-05 |
|---|---|---|---|---|
| **Role match** | **8/8**, clean 1:1, 0 extras | 25 | **25.0** | ↑ from 21.9 (full coverage) |
| Action coverage | Σmatch ≈ 50/63 = 0.79 | 35 | 27.7 | ~ (0.83; R-01 lower, R-07 now covered) |
| Traceability | in-namespace (+ completions) | 15 | 15.0 | = |
| Integrity | 4/4 | 10 | 10.0 | = |
| Substance | clean; calibrated granularity | 15 | 14.5 | ↑ (no over-elaboration) |
| **COMPOSITE** | | 100 | **≈ 92** | ↑ from 89 |

## Composite & role progression

| | r-02 | r-03 | r-04 | r-05 | r-06 | **r-07** |
|---|---|---|---|---|---|---|
| roles | 7/8 | 7/8 | 7/8 | 7/8 | 7/8 | **8/8** |
| actions | 50 | 44 | 47 | 67 | 48 | 62 |
| composite | 86 | 84 | 85 | 89 | 85 | **92** |

## What this run teaches

1. **Fix-at-source worked.** The D2-Assistant gap was un-closeable in the module (it would have to
   *guess* the role); completing the **fundamentals** to name the position closed it by construction —
   full role coverage, orphaned work homed. This is the clearest vindication of "fix the constraint at
   its layer" in the whole sequence.
2. **The calibrated guard is now validated.** Previously unmeasured, run-07 shows it hits the sweet spot:
   mechanics merged, distinct concerns preserved (monitor cost vs health), 62 clean actions — neither
   run-05's 67 (over) nor run-06's 48 (under).
3. **Remaining residual is the genuinely-hard tail** (~category 3): revise-setup-later,
   tune-resolution-depth, discuss-concern, operator notifications, deploy/wrapper-health — the items with
   thin in-package Source or open-tail derivation. This is exactly what the **lifecycle + intention
   derivation lens** (proposed, not yet written up) targets.

## Bottom line

Completing the fundamentals (D2 Assistant as a named position) + the calibrated guard produced the
**best run yet — composite ≈ 92, first full 8/8 role coverage, work conserved, clean granularity**. The
remaining gap is the hard-to-derive tail, whose fix is the lifecycle/intention lens. Baselines: run-05
`../work/run05-completeness-harness/`, run-06 `../work/run06-distinctness/`.
