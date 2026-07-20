# Evaluation scorecard — DISTINCTNESS-GUARD run (run-06) vs `output-example/`

*Blind clean-room run after adding the **distinctness / de-dup-by-responsibility guard** (Quality over
Expediency) on top of conformance + depth-cue + completeness + harness bias. Generator: fresh sub-agent,
forbidden `output-example/`, `evaluation/`, `work/`, `benchmark_verification/`. Judge (Layer B): Claude.
Baseline: run-05 (over-elaborated, ≈89) in `../work/run05-completeness-harness/`.*

Date: 2026-07-19   Engine: fresh blind sub-agent   Judge: Claude (Layer B)
Structural (Layer A): **PASS** (exit 0) · **7 roles · 48 actions** · all 7 checks green

## Headline — the guard did its job, then over-corrected

**Win (its target):** the over-elaboration is gone. The Design Node Builder dropped **14 → 8** (matching
the example), total actions **67 → 48**, and the governance **mechanics-as-actions** (adjacency,
decompose, work-within-contract, coverage) were folded into the actions they govern. Substance/quality
up; no spurious rows.

**But it over-corrected on recall.** The run read "de-dup by responsibility" too broadly and **merged
genuinely-distinct responsibilities** the fundamentals separate — collapsing the D1 Designer's
**monitor-progress / monitor-cost / monitor-health** (3 in the example, Phase 4 Item 3) into one row, and
**review-node / reserve-authority / rule-on-proposals** into one. Recall fell **0.83 → 0.68** and the
composite **89 → 85** — back to run-04's level.

## Composite & recall progression

| | run-03 | run-04 | run-05 | run-06 |
|---|---|---|---|---|
| actions | 44 | 47 | **67** | 48 |
| Builder R-02 rows | 6 | 6.5 | **14** (over) | **8** (clean) |
| Σmatch recall | 0.64 | 0.68 | **0.83** | 0.68 |
| composite | 84 | 85 | **89** | 85 |

## Per-role coverage (Σmatch / n), run-05 → run-06

| Role | run-05 | run-06 | note |
|---|---|---|---|
| R-00 D2 Designer | 3 | 2.5 | — |
| **R-01 D1 Designer** | 20 | **14** | **over-merged** monitor×3→1 and review/authority×3→1 |
| R-02 Design Node Builder | 8 (+6 extras) | **8 (clean)** | ✓ guard removed the mechanics — its intended effect |
| R-03 D1 Programmer | 3 | 3 | clean |
| R-04 D1 Technical Manager | 5 | 5 | — |
| R-05 D0 Operator | 5.5 | 4.5 | merged monitor+view |
| R-06 D0 Technical Manager | 7 | 6.5 | — |
| R-07 D2 Assistant | 0.5 | 0.5 | absent (correctly not manufactured) |
| **Σ** | **52 (0.83)** | **43 (0.68)** | |

## Diagnosis — the guard is under-specified, not wrong

The guard correctly removed **mechanical steps and rule-restatements** (the Builder's `RU-07`/`RU-10`
rows — real over-elaboration). But "**merge candidates that express the same underlying responsibility**"
is ambiguous: *monitoring cost* and *monitoring health* share the verb "monitor" yet are **distinct
concerns the fundamentals separate** (Phase 4 Item 3; the example gives them distinct IDs). The run read
the shared verb as one responsibility and merged. The pendulum swung from over-elaboration (run-05, 67)
to over-merging (run-06, 48); the target (63) sits between.

**The fix — calibrate, don't remove.** Anchor distinctness in the **fundamentals' own granularity**:
*merge only mechanical steps and rule-restatements; **preserve any distinction the fundamentals
themselves make** (distinct data, distinct concern, distinct Source).* "Monitor cost" ≠ "monitor health"
because Phase 4 Item 3 treats them as distinct; "communicate via adjacency (RU-07)" is a rule the node
operates under, not a distinct action. That keeps run-05's recall **and** run-06's cleanliness.

## Confound (the standing noise finding, again)

The D1-Designer count has now been 21 → 15.5 → 20 → 14 across runs — large run-to-run variance that
**confounds single-run attribution**. The Builder fix (14 → 8) is unambiguous; the D1-Designer recall
drop is part guard-over-merge, part variance. This is the clearest case yet for the **multi-run harness**
(average N blind runs per module version) before trusting a composite delta.

## Bottom line

The distinctness guard **fixed the over-elaboration it targeted** (Builder 14 → 8, no mechanics) but,
as written, **over-merged distinct responsibilities**, costing recall (0.83 → 0.68) and composite
(89 → 85). It needs **calibration** — merge mechanics/rule-restatements only, preserve
fundamentals-made distinctions — not removal. Baseline: `../work/run05-completeness-harness/`.

## Calibration applied (post-run)

The guard was calibrated in the module (source + benchmark snapshot, `design-node-algorithm.md` step 4;
`contract.md` §3): *merge only mechanical steps and rule-restatements; **preserve any distinction the
fundamentals themselves make** (distinct data, concern, or Source — e.g. monitor cost vs health, Phase 4
Item 3); de-dup at the fundamentals' own granularity.* **run-06 above measured the pre-calibration
guard**; the calibrated guard is **not yet re-measured** — deferred to a proper re-run (ideally under the
multi-run harness, given the D1-Designer variance that confounds single-run attribution).
