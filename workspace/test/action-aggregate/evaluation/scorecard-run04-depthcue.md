# Evaluation scorecard — DEPTH-CUE run (run-04) vs `output-example/`

*Blind clean-room run of the module **after adding the position-derived depth frame** (conformance
already in). Generator: a fresh sub-agent given only `environment/` + `input/`, forbidden
`output-example/`, `evaluation/`, `work/`, `benchmark_verification/`. Judge (Layer B): Claude.
Baseline: run-03 (`../work/run03-conformant/`, conformant but pre-depth-cue).*

Date: 2026-07-19   Engine: fresh blind sub-agent   Judge: Claude (Layer B)
Structural (Layer A): **PASS** (exit 0) · **7 roles · 47 actions** · all 7 checks green

## Headline

**The depth cue did its job on its target.** The four operational roles it governs (R-03–R-06) rose
sharply — the run walked the frame's facets (operate / monitor / configure / view / handle-errors /
escalate, + diagnose→fix→recover→record for maintenance) and surfaced the position-derived tail run-03
left implicit. **But the composite only nudged (84 → ~85)**, because *this* run elaborated the **D1
Designer** less (it merged the three monitoring actions into one and dropped a few) — open-list variance
on a role the frame **deliberately does not touch** (scope guard). Conformance holds; role structure is
identical to run-03 (7 roles, D2 Assistant absent — a modelling role, not a named-enumeration miss).

## Gates

| Gate | Result |
|---|---|
| **Conformance (gating)** | **CLEAR** — all six Phase-5 named positions present; no fold |
| G1 integrity | clear (7 checks green; `A-003` skipped) |
| G2 traceability | clear (all rows sourced) — *minor nit:* two rows cite `framework design-node-algorithm` as a Source; the frame is the *method*, not a content Source, but each also carries a Phase-5 Source |
| G3 (literal) | fail only on R-07 D2 Assistant (modelling role — same as run-03) |

## Per-role action coverage — run-03 → run-04

| Role | run-03 Σ/n | run-04 Σ/n | Δ | note |
|---|---|---|---|---|
| R-00 D2 Designer | 2.5/3 | 2.5/3 | — | not in frame scope |
| R-01 D1 Designer | **21/24** | **15.5/24** | **−5.5** | *not in frame scope*; open-list variance — merged monitor×3→1, dropped a few |
| R-02 Design Node Builder | 6/8 | 6.5/8 | +0.5 | not in frame scope |
| **R-03 D1 Programmer** | 1/3 | **2/3** | **+1** | frame: added fix-defects, escalate |
| **R-04 D1 Technical Manager** | 3.5/7 | **5/7** | **+1.5** | frame: added rollback/recover, records |
| **R-05 D0 Operator** | 3/8 | **5/8** | **+2** | frame: added handle-errors, escalate |
| **R-06 D0 Technical Manager** | 3/7 | **6/7** | **+3** | frame: added monitor, diagnose, recover, escalate |
| R-07 D2 Assistant | 0.5/3 | 0.5/3 | — | role absent |
| **Σ total** | **40.5/63 = 0.64** | **43/63 = 0.68** | **+2.5** | |
| **operational (R-03–R-06)** | **10.5** | **18** | **+7.5** | **the cue's target — clear lift** |

## Scores (Layer B estimate)

| Dimension | run-04 | Weight | Weighted | vs run-03 |
|---|---|---|---|---|
| Role match | 7/8, clean 1:1 | 25 | 21.9 | = |
| Action coverage | 0.68 | 35 | **23.9** | ↑ from 22.5 |
| Traceability | in-namespace | 15 | 15.0 | = |
| Integrity | 4/4 | 10 | 10.0 | = |
| Substance | strong | 15 | 14.5 | = |
| **COMPOSITE** | | 100 | **≈ 85** | ↑ ~1 from 84 |

## What this run teaches

1. **The depth cue works — measured on its target.** Operational-role Σmatch rose **10.5 → 18** (+7.5),
   exactly the roles the frame governs, with the added actions traced to the frame's facets. The lever
   does what it was designed to do.
2. **The composite is a noisy estimator of a single change.** It moved only +1 (84 → 85) because the
   **D1 Designer** — *outside* the frame's scope — happened to be elaborated less this run (21 → 15.5).
   The frame neither helped nor hurt it; it is open-list run-to-run variance. A single clean-room run's
   composite cannot cleanly resolve a ~2-point change against that background noise.
3. **Methodological implication.** To attribute a module change's effect, read the **targeted
   dimension** (here, operational coverage — unambiguous) and/or **average several runs**, rather than
   one composite. The composite bounces 86 → 84 → 85 largely on D1-Designer depth variance
   (24 → 22 → 21 → 15.5 across example/run-02/03/04), not on the changes under test.
4. **A residual worth noting.** Even the "scaffolded" D1 Designer varies run-to-run — the method §1
   journey gives it structure but not a fixed depth. If we want to stabilize *its* coverage too, that is
   a candidate future depth-scaffold refinement for the passive/active journey (separate from this
   operational frame).

## Bottom line

The position-derived depth frame **lifts the open-list tail it targets** (operational coverage
+7.5 Σmatch) while preserving conformance and role structure. The composite gain is modest and
noise-masked; the honest signal is in the targeted dimension. Baseline run-03: `../work/run03-conformant/`.
