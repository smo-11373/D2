# positive — the ceiling control (cheat run)

A **maximum-information** run: the engine was given sight of `../../output-example/` and reproduced it.
Because it copies the target, the shared harness (`../../evaluation/`) must score it **~100 with all
gates clear** — including the conformance gate, since a copy of the 8-role example carries every
Phase-5 named position.

- `role-action-catalog.md`, `algorithm.md`, `declaration.md` — the cheat output (formerly `run-01`).
- `scorecard.md` — its scorecard.

**Measured:** Layer A **PASS**, 8 roles, 63 actions, **100%** provisional coverage vs the example.

**What passing proves:** the harness has **no false-negative at the ceiling** (a truly-matching output
scores high), the **target is achievable and self-consistent** (its format/IDs/structure are
producible), and the harness **runs end-to-end**. It does **not** prove the target is correct — that is
a separate target-vs-fundamentals check (see `../README.md`).

*Not a real measurement.* This engine cheated by design; it is a calibration standard, kept out of
`../../output/`.
