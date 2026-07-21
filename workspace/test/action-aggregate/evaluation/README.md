# evaluation — the scoring harness

Compares a generated `../output/` against the target `../output-example/` and decides whether the
re-derived role-action table is **substantially the same** — per `../input/contract.md` §3
(same roles; substantially the same actions modulo naming / granularity / open-list; traceability;
integrity).

**Status:** harness built and validated; used for one real clean-room measurement.

- **Harness validity** is checked in `../benchmark_verification/` — a **positive** control (cheat run →
  must score ~100) and **negative** controls (a structural floor and a conformance floor → must fail).
  That directory validates *this* harness; keep it green whenever the harness or the target changes.
- **The real measurement** of the conformant module is **`scorecard-run03-conformant.md`** (output
  `../output/`): conformance gate clear (the fold is closed), composite ≈ 84. Its pre-conformance
  (run-02) and contaminated (run-01) predecessors are now the negative/positive controls in
  `../benchmark_verification/`.

## Design in one line

The deliverable is an **open list** with free IDs and naming, so "substantially the same" is a
**semantic** judgment, not string-equality — which splits the harness into two layers: mechanical
checks in code, meaning-based judgment by rubric.

| Layer | File | Does | Runnable |
|---|---|---|---|
| **A — structural** | `structural_check.py` | parse; check IDs / grouping / Sources / substance screen; emit a lexical pre-alignment | **yes, now** |
| **B — semantic** | `semantic-judgment.md` | finalize alignment by meaning; judge coverage & substance; write the scorecard | LLM/human |
| spec | `scoring-method.md` | dimensions, weights, gates, thresholds, verdict | — |

## How to run

```bash
# Layer A — structural check on one catalog
python evaluation/structural_check.py output/role-action-catalog.md

# Layer A — structural check + lexical pre-alignment vs the target
python evaluation/structural_check.py output/role-action-catalog.md \
    --compare output-example/role-action-catalog.md

# machine-readable
python evaluation/structural_check.py output/role-action-catalog.md \
    --compare output-example/role-action-catalog.md --json
```

Then a judge runs Layer B (`semantic-judgment.md`) over Layer A's output and the two catalogs, and
fills the **scorecard template**. Exit code: `0` if Layer A passes, `1` if it fails (CI-friendly).

## Verdict scale

`overall = 0.25·role + 0.35·coverage + 0.15·traceability + 0.10·integrity + 0.15·substance` (×100),
behind gates G1–G3 (integrity / traceability / roles-complete). **≥ 85 = substantially the same.**
The number always ships with a **gap list** and **extras list** — see `scoring-method.md` §Verdict.
**Recall-first (bias to more):** the example is a **floor**, not a bullseye — justified extras are a
richness signal, never a penalty; across N runs the headline is **union recall** (`multi-run-method.md`).

## Self-test (Verification Before Realization)

The runnable layer is validated against the reference itself:

- `structural_check.py output-example/role-action-catalog.md` → **PASS**, 8 roles, 63 actions, all
  checks green (the reference passes its own structural checks — the baseline).
- self-compare (example vs example) → **100%** provisional coverage, all roles matched, no extras.
- a deliberately-broken fixture (`../benchmark_verification/negative/structural/degraded-fixture.md`) →
  **FAIL** with every injected fault surfaced (duplicate ID, retired-ID reuse, missing Source, thin
  text, missing role R-07, spurious extra). Confirms the harness *makes deviation visible* (Phase 5
  Item 1, Harness First). This self-test is now formalized as the pos/neg controls in
  `../benchmark_verification/`.

## What this harness does not do

- It does not generate `../output/` — that is the node/engine's job (the other empty piece).
- Layer A does not judge meaning — paraphrase and re-granularization are deferred to Layer B by
  design (a paraphrased action scored 0.13 lexically in the self-test yet is a true match).
- Scoring the Step-1 products (`algorithm.md`, `declaration.md`) is shape/intent-only and light; the
  primary scored object is the role-action catalog.
