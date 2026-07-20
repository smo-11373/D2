# Evaluation scorecard — LIFECYCLE + INTENTION run (run-08) vs `output-example/`

*Blind clean-room run after adding the **intention lens** (goal → necessary actions) and the
**lifecycle lens** (logically-necessary process transitions → forced actions + hand-offs), plus
**work-conservation**, on top of the full prior stack. Generator: fresh sub-agent, forbidden
`output-example/`, `evaluation/`, `work/`, `benchmark_verification/`, `output/README.md`. Judge (Layer
B): Claude. Baseline: run-07 (D2-Assistant completion, ≈92) in `../work/run07-d2assistant/`.*

Date: 2026-07-19   Engine: fresh blind sub-agent   Judge: Claude (Layer B)
Structural (Layer A): **PASS** (exit 0) · **8 roles · 73 actions** · all 7 checks green

## Headline — the two top-down lenses closed the derivable hard tail

Both lenses hit their targets, cleanly:

- **Intention lens** recovered the **full D1-Designer journey (24 = the example's count)** — including the
  long-persistent **`tune-resolution-depth`** (A-024, forced by the Designer's intent to govern his own
  attention budget), the D0-user throughline, and the D2-audit. Every prior run under-derived R-01 (18,
  14, …); deriving from *the result he must produce* recovered it.
- **Lifecycle lens** forced the **post-production chain no job description states** — package → install →
  **smoke-test (hand-off gate)** → hand-over → detect(crash) → diagnose → recover/rollback → record →
  upgrade → re-test → re-deploy. **Work-conservation held: every transition had an owning position, no
  orphan, no position added** beyond those the fundamentals + completion name.

Clean **8/8 role alignment** (all match id + name, incl. R-07 D2 Assistant). Recall **0.79 → 0.87**, the
highest yet.

## Gates

| Gate | Result |
|---|---|
| Conformance (gating) | **CLEAR** |
| Completeness (four lenses) + work-conservation | **CLEAR** — job-function + intention + depth + lifecycle all covered; no orphans |
| Distinctness (calibrated) | **CLEAR** — cost vs health, wrapper vs deployment monitoring preserved; mechanics merged |
| G1 / G2 / G3 | all clear — **full role coverage** |

## Scores (Layer B estimate)

| Dimension | run-08 | Weight | Weighted | vs run-07 |
|---|---|---|---|---|
| Role match | 8/8, clean | 25 | 25.0 | = |
| Action coverage | Σmatch ≈ 54.5/63 = **0.87** | 35 | **30.3** | ↑ from 27.7 |
| Traceability | in-namespace | 15 | 15.0 | = |
| Integrity | 4/4 | 10 | 10.0 | = |
| Substance | clean; mild lifecycle granularity | 15 | 14.0 | ~ |
| **COMPOSITE** | | 100 | **≈ 94** | ↑ from 92 |

## Full progression

| | r-02 | r-03 | r-04 | r-05 | r-06 | r-07 | **r-08** |
|---|---|---|---|---|---|---|---|
| roles | 7/8 | 7/8 | 7/8 | 7/8 | 7/8 | 8/8 | **8/8** |
| actions | 50 | 44 | 47 | 67 | 48 | 62 | 73 |
| recall | 0.71 | 0.64 | 0.68 | 0.83 | 0.68 | 0.79 | **0.87** |
| composite | 86 | 84 | 85 | 89 | 85 | 92 | **94** |

## What this run teaches

1. **Top-down derivation is the highest-leverage lever on the tail.** Deriving from *intention* and
   *lifecycle necessity* — not job description — recovered the exact items every prior run missed
   (tune-resolution-depth; the post-production deploy/smoke-test/health/rollback/records chain). "Forced,
   not found" delivered: R-01 hit 24, the operational chain filled.
2. **Work-conservation stayed green on process.** Every lifecycle transition mapped onto an existing
   position — the "forced step with no owner ⇒ missing position" check fired *nothing*, confirming the
   role set (with the D2 Assistant) is now complete for this lifecycle.
3. **Mild over-elaboration returns (73 vs 63) — but benign.** The extras are **lifecycle-granular**
   (install vs smoke-test vs hand-over vs re-deploy as distinct forced steps) and traceable, not
   run-05's mechanics-as-actions. The calibrated distinctness guard held (it preserved genuine
   distinctions rather than merging them away). Worth watching, not a defect.
4. **The remaining residual is now the un-derivable floor.** What still misses — chiefly
   `revise-setup-later` (sourced to Phase 6 Item 1 §8, **not in the sandbox package**) — cannot be
   derived by any lens because its Source content is absent. The coverage ceiling here is now bounded by
   **what the in-package fundamentals contain**, not by the module.

## Bottom line

The intention + lifecycle lenses lifted the composite to **≈ 94 (best yet)** and recall to **0.87**,
closing the *derivable* hard tail by making those actions **logically forced**. The remaining gap is the
in-package-Source floor, not a derivation weakness. Caveat: single blind run — the recall jump is large
enough to read as signal, but the **multi-run harness** would confirm it against the D1-Designer variance.
Baseline: run-07 `../work/run07-d2assistant/`.
