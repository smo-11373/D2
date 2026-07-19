# Evaluation scorecard — COMPLETENESS + HARNESS run (run-05) vs `output-example/`

*Blind clean-room run after adding **completeness** (acceptance) and the **harness-richness bias**
(method), on top of conformance + depth-cue. Generator: fresh sub-agent, forbidden `output-example/`,
`evaluation/`, `work/`, `benchmark_verification/`. Judge (Layer B): Claude. Baselines: run-03
(conformant), run-04 (depth-cue) in `../work/`.*

Date: 2026-07-19   Engine: fresh blind sub-agent   Judge: Claude (Layer B)
Structural (Layer A): **PASS** (exit 0) · **7 roles · 67 actions** · all 7 checks green

## Headline

**Both changes worked, strongly and measurably.** Recall jumped — Σmatch **0.68 → 0.83** — the largest
move yet and big enough to show clearly through the run-to-run noise. **Completeness** recovered the
full D1-Designer journey (run-04's 15.5 → 20) and forced the per-position control lists and maintenance
diagnose→fix→recover→record cycles into concrete actions. The **harness-richness bias** surfaced the
testing / monitoring / health-visibility / recovery actions across every role ([H]-tagged): Programmer
**tests** (A-045), the Builder's verify/self-check (A-033/A-039), D1-TM **regression harness + recover**
(A-051/A-054), D0 **health-monitoring + crash-detection + recovery** (A-057/A-064/A-067). Conformance
held; clean 1:1 role alignment.

**The flip side — mild over-generation.** 67 actions > the example's 63. The guard held against
*spurious* rows (all 67 are traceable), but not fully against *over-granular* ones: the Design Node
Builder inflated 8 → 14, several of them governance **mechanics-as-actions** (adjacency A-041, decompose
A-038, revise-on-request A-042, receive-contract A-029). "Biased to completeness" can over-elaborate;
the guard likely needs a "**distinct actions, not mechanical steps**" clause.

## Gates

| Gate | Result |
|---|---|
| Conformance (gating) | **CLEAR** — all six named positions present; no fold |
| **Completeness (new)** | **strong** — specified pieces recovered (journey, control lists, maintenance cycles); see caveat on over-elaboration |
| G1 integrity | clear (7 checks green; `A-003` skipped) |
| G2 traceability | clear (all 67 rows sourced in-namespace) |
| G3 (literal) | fail only on R-07 D2 Assistant — and note: completeness **correctly declined to manufacture it** (not a named enumeration, no fundamentals-grounded action set); this is disciplined, not a miss |

## Per-role coverage progression (Σmatch / n)

| Role | run-03 | run-04 | run-05 | n |
|---|---|---|---|---|
| R-00 D2 Designer | 2.5 | 2.5 | **3** | 3 |
| R-01 D1 Designer | 21 | 15.5 | **20** | 24 |
| R-02 Design Node Builder | 6 | 6.5 | **8** | 8 |
| R-03 D1 Programmer | 1 | 2 | **3** | 3 |
| R-04 D1 Technical Manager | 3.5 | 5 | **5** | 7 |
| R-05 D0 Operator | 3 | 5 | **5.5** | 8 |
| R-06 D0 Technical Manager | 3 | 6 | **7** | 7 |
| R-07 D2 Assistant | 0.5 | 0.5 | 0.5 | 3 |
| **Σ total** | **40.5** | **43** | **52** | 63 |
| **fraction** | 0.64 | 0.68 | **0.83** | |

## Scores (Layer B estimate)

| Dimension | run-05 | Weight | Weighted | vs run-04 |
|---|---|---|---|---|
| Role match | 7/8, clean 1:1 | 25 | 21.9 | = |
| Action coverage | 0.83 | 35 | **29.0** | ↑ from 23.9 |
| Traceability | in-namespace | 15 | 15.0 | = |
| Integrity | 4/4 | 10 | 10.0 | = |
| Substance | strong; slight over-granularity | 15 | 14.0 | ~ |
| **COMPOSITE** | | 100 | **≈ 89** | ↑ from 85 |

## What this run teaches

1. **Completeness + harness bias are the highest-leverage levers so far** — +0.15 recall in one step,
   clearly above noise (unlike the depth-cue's +1 composite). The two changes target the dimension that
   was actually holding the score down, and they hit it.
2. **Completeness showed disciplined judgment.** It recovered every *fundamentals-specified* piece it
   could derive, yet **declined to manufacture the D2 Assistant** (no named enumeration, no grounded
   action set). That is exactly the intended behavior: complete against the fundamentals, not against
   the example. The persistent D2-Assistant gap is confirmed as a **modelling/roles question**, not a
   completeness failure.
3. **Over-elaboration is the new failure mode to watch.** Biasing to completeness/harness trades a
   coverage gain for some over-granularity (Builder mechanics-as-actions). Net positive here, but the
   guard should gain an explicit "distinct actions, not mechanical steps" / de-duplicate-by-responsibility
   clause. This is the Quality-over-Expediency counter-pressure asserting itself.
4. **Two persistent D1-Designer misses remain** — revise-setup-later, tune-resolution-depth — sourced to
   Phase 6 Item 1 / Phase 2 material that is thin in-package; likely genuinely hard to derive here.

## Bottom line

Completeness (don't omit) + harness-richness (Harness First for the product) lifted recall from 0.68 to
**0.83** and the composite to **≈ 89** — the best yet — while conformance and role structure held. The
cost is mild over-elaboration (67 vs 63 actions), a Quality-over-Expediency guard to tighten next.
Baselines: run-03 `../work/run03-conformant/`, run-04 `../work/run04-depthcue/`.
