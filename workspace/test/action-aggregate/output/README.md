# output — the node's produced package (clean-room run, run-06: + distinctness guard)

The Action Aggregate node's **untainted** output after **five** module changes — conformance, depth
frame, completeness, harness bias, and the **distinctness / de-dup-by-responsibility guard**. Derived by
a fresh blind agent given only `../environment/` + `../input/`, blind to `../output-example/`,
`../work/`, `../evaluation/`, `../benchmark_verification/`.

- `role-action-catalog.md` — 7 roles (`R-00…R-06`), 48 actions (`A-001…A-049`, `A-003` skipped).
- `algorithm.md`, `declaration.md` — Step-1 products.

**Scored:** `../evaluation/scorecard-run06-distinctness-guard.md` → conformance clear, composite **≈ 85**.
**Mixed result:** the guard **fixed the over-elaboration it targeted** (Design Node Builder 14 → 8,
total 67 → 48, no mechanics-as-actions) but, as written, **over-corrected** — it merged genuinely-distinct
responsibilities (D1 Designer's monitor cost/health×3 → 1), dropping recall **0.83 → 0.68** and composite
**89 → 85**. The guard has since been **calibrated** in the module (merge mechanics/rule-restatements
only; preserve distinctions the fundamentals themselves make, e.g. monitor cost vs health). **This
run-06 output measured the *pre-calibration* guard**; the calibrated guard is not yet re-measured
(deferred to a proper re-run, ideally under a multi-run harness).

*Baselines: run-05 (over-elaborated, ≈89) `../work/run05-completeness-harness/`; run-04 `../work/run04-depthcue/`;
run-03 `../work/run03-conformant/`. Validity controls in `../benchmark_verification/`.*
