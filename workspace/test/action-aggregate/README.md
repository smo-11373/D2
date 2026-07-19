# Test — the Action Aggregate node

*Home test directory for the **action aggregate node**. It packages a runnable test of the
design-node algorithm: given the **environment** + **input** (contract), a (future) program produces
its own **output**; **evaluation** then compares that output against the **output example** and scores
how close it came. Non-authoritative snapshot (workspace). **Strictly self-contained** — every input
the node needs (fundamentals, framework, algorithm, contract) is copied in here; nothing outside the
package is required.*

## The pieces

| Piece | What it holds | Status |
|---|---|---|
| `environment/` | the **fundamentals + module** the node reads — constitution (Phases 1–5), method (§1), rules (`RU-*`), glossary, and `framework/` (the module: design tree + design node module, incl. `conformance.md`). | populated |
| `input/` | the **contract** for the action aggregate node | populated |
| `output/` | the node's **produced output** — the real, **blind clean-room** run of the conformant module (run-03) | populated |
| `evaluation/` | the **shared scoring harness** (`structural_check.py` + scoring/judgment specs) and the real scorecard | populated |
| `benchmark_verification/` | the **harness-validity tool**: a **positive** (cheat/ceiling) control and **negative** (structural + conformance floor) controls that prove the harness discriminates | populated |
| `output-example/` | an **example** of the target **three-product output** — table + algorithm + declaration; a comparison target, **not** an exact answer key | populated |

The output example sits at the **home level** (not inside `output/`) on purpose: `output/` is reserved
for what the program generates, so the two never get confused. Likewise the **benchmark-validity
controls** (cheat/degraded/fold) live in `benchmark_verification/`, never in `output/` — a contaminated
control must never be read as a real measurement.

## How it will run (later)

1. A program reads `input/contract.md` + `environment/` and runs the **design-node algorithm**
   (`environment/framework/design-node-algorithm.md`).
2. It writes its result — a re-derived role-action table — into `output/`.
3. `evaluation/` compares `output/` against `output-example/` and scores **"substantially the same"**
   (same roles; substantially the same actions, modulo naming / granularity / open-list).

Because the output is an **open list**, success is *substantial* match, not identity — the example is
a target, not a key.

## Scope

This test deliberately pins down only the **shape of the output** and the **shape of the input
contract (narrative)**; the contract form is **fluid**. Contract *generation*, *why this node is
first*, and whether the **algorithm / declarations** belong in the input are **left open** — see
`scope.md`.
