# Evaluation scorecard — CONFORMANT run (run-03) vs `output-example/`

*The clean-room run of the **conformant module** (conformance re-synced into `environment/framework/`
and `input/contract.md` §3). Generator: a fresh blind sub-agent given only `environment/` + `input/`,
forbidden `output-example/`, `evaluation/`, `work/`. Judge (Layer B): Claude. Compare against run-02 — now the
conformance floor, `../benchmark_verification/negative/conformance/scorecard.md`.*

Date: 2026-07-18   Engine: fresh blind sub-agent   Judge: Claude (Layer B)
Structural (Layer A): **PASS** (exit 0) · **7 roles · 44 actions** · all 7 checks green

## Headline

The conformance requirement did exactly what it was designed to do: the run's self-check produced a
**refusal to fold**, and **Design Node Builder is preserved as a full role** (8 actions). **All six
Phase-5 Item-3 named positions are present** (R-01–R-06), so the run **conforms** — the specific
non-conformance run-02 exposed (dropping a named position) is **closed**. Role alignment is now a
**clean 1:1** (no reused-id artifact). The one example role still absent is **D2 Assistant (R-07)** —
which is *not* in the Phase-5 named enumeration (it is a Phase-4 interaction-point role the example
itself flags as "a modelling call") — so its absence is **open-list / modelling variation, not a
conformance violation**.

## Gates

| Gate | Check | Result |
|---|---|---|
| **Conformance (new, gating)** | Deliverable contradicts no named enumeration / principle / rule | **CLEAR** — all six Phase-5 Item-3 named positions present; no fold |
| G1 | Integrity — IDs unique/well-formed, grouped, no retired-ID reuse (`A-003` skipped) | **clear** |
| G2 | Traceability — every row Source-cited, all within `sources.md` namespace | **clear** |
| G3 (literal) | Every *example* role present | **fail on R-07 D2 Assistant** — but a modelling role, not a named-enumeration position (see note) |

*Note — what run-03 shows about G3. The old G3 conflated two things: **named-enumeration positions**
(Phase-5 Item-3 — hard, conformance-gated) and **modelling roles** (D2 Assistant, Phase-4,
example-self-flagged — soft, open-list). Run-02 failed G3 on the hard kind (a conformance violation);
run-03 satisfies the hard kind and "fails" only the soft kind. Under the conformance model the run is
acceptable on roles; the D2-Assistant question is the open modelling call the example already flags.*

## Scores (Layer B estimate)

| Dimension | Raw | Weight | Weighted | vs run-02 |
|---|---|---|---|---|
| Role match | 7/8 example roles present by meaning; clean 1:1; 0 extra | 25 | **21.9** | = (but clean, no artifact) |
| Action coverage | Σmatch **≈40.5 / 63 = 0.64** (per-role below) | 35 | **22.5** | ↓ from 24.7 |
| Traceability | all rows sourced, in-namespace | 15 | **15.0** | = |
| Integrity | 4/4 | 10 | **10.0** | = |
| Substance | strong descriptions | 15 | **14.5** | ≈ |
| **COMPOSITE** | | 100 | **≈ 84** | ↓ ~2 from 86 |

**Verdict: Conformant — the fold is closed and the run conforms; composite ≈84 (flat vs 86).** The
composite did **not** rise, because the conformance change targeted **role conformance**, not the
**open-list action tail** — and run-03 happened to elaborate that tail *less* (44 actions vs run-02's
50) and lost D2-Assistant's 3 actions. That tail is the **separate, un-implemented lever** (the
position-derived depth cue); it is the main residual now.

### Action coverage, per role

| Role | Σmatch / n | Notes vs run-02 |
|---|---|---|
| R-00 D2 Designer | 2.5 / 3 | ≈ same |
| R-01 D1 Designer | 21 / 24 | strong; 12 `[P]` / 9 `[A]`; still missing revise-setup-later, tune-resolution-depth |
| R-02 Design Node Builder | **6 / 8** | **fixed** — full distinct role (was 4.5/8, collapsed). Missing: investigate-predecessor, harness-before-committing |
| R-03 D1 Programmer | 1 / 3 | thin (implement only); missing tests, fix-defects |
| R-04 D1 Technical Manager | 3.5 / 7 | missing deploy, monitor-health, rollback, review-records |
| R-05 D0 Operator | 3 / 8 | **thinner** than run-02 (4/8) — missing view-results, notifications, handle-errors, view-usage, support-request |
| R-06 D0 Technical Manager | 3 / 7 | missing diagnose, apply-fix, escalate, standing-monitoring |
| R-07 D2 Assistant | 0.5 / 3 | **role absent**; interaction-point function only partially present in R-01 A-018 / R-02 A-028 |

## What this run teaches

1. **Conformance works, precisely.** A blind run of the conformant module kept the named Phase-5
   position it previously folded — the self-check reported an explicit refusal to fold. The specific
   defect the benchmark measured is closed, and role alignment is now clean 1:1 (the reused-id artifact
   that needed a human correction in run-02 did not occur).
2. **The composite is flat, and that is honest.** Conformance fixed a *role* (gate) problem, not a
   *coverage* problem. The ~2-point dip is open-list-tail variation on dimensions conformance never
   targeted (thinner downstream actions; the dropped D2-Assistant actions). It is **not** a regression
   caused by conformance.
3. **The benchmark's role gate needs the same distinction the module now makes.** G3 "every example
   role present" should split into **named-enumeration roles** (conformance-gated, hard) and
   **modelling roles** (open, soft — e.g. D2 Assistant, which the example already self-flags). This is
   benchmark target-hygiene, not module work — and it connects to the earlier R-07 flag.
4. **Next lever is the depth cue.** To move coverage (and the composite) up, elaborate the
   position-derived downstream tail (operate/monitor/configure/view/handle-error/escalate/support) —
   the open-list lever we deliberately did not implement here.

Pre-conformance control (now the **conformance floor**): `../benchmark_verification/negative/conformance/`.
