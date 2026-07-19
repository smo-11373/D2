# negative — the floor controls (must be rejected)

Outputs whose correct score is **low / fail**. If the harness ever scores one of these acceptably, it
has lost its discrimination and must be fixed before any real number is trusted. Two kinds, because the
harness must reject on **two** axes:

## structural/ — broken structure → Layer A FAIL

`degraded-fixture.md` injects mechanical faults (duplicate ID, retired-ID reuse, missing Source, thin
text, missing role, spurious extra). The runnable Layer A must **FAIL (exit 1)** with the faults
surfaced.

**Measured:** Layer A **FAIL** — `action_ids`, `retired-id-reuse`, `traceability`, `substance` trip.
✔ the harness makes structural deviation visible (Phase 5 Item 1).

## conformance/ — clean structure, non-conformant content → must be rejected

`role-action-catalog.md` is the **run-02 fold**: structurally clean, fully traceable, but it **collapses
a named Phase-5 position** (Design Node Builder) into another role. A traceability-only check accepts it;
conformance must reject it.

**Measured — and this is the instructive part:** Layer A **PASSes** (exit 0, 7 roles, 50 actions). Its
role-alignment **silently aliases** the reused id — example `R-02` (Design Node Builder) *and* `R-07`
(D2 Assistant) both map onto the fold's single output `R-02`, so Layer A reports **no missing role**.
The fold is caught only by **Layer B** (the semantic judge) and the module's **conformance gate**.

This negative therefore documents **where discrimination lives**: structural rejection is mechanical
(Layer A); conformance rejection is **semantic (Layer B)**. That is a recorded property of the harness,
not a defect to re-engineer — improving the evaluation is not the goal here.

- `scorecard.md` — the detailed Layer-B analysis of the fold (why it is non-conformant).

*Neither of these is a real measurement.* They are calibration standards, kept out of `../../output/`.
