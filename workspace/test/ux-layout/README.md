# Test — the Experience (UX) node

*Home test directory for the **Experience node** — the **dependency-child of the Action-Aggregate node**
in the design tree: **Role → Action → Experience → Capability → Architecture**. Given the accepted
**action aggregate**, it lays out **how each action is experienced** by its position (the interaction
patterns, attention-budgeted) — the surface the D2 Assistant delivers and that then *demands* the
capabilities. Non-authoritative sandbox. **Self-contained** — fundamentals + module are copied in, plus
the inherited action aggregate.*

## The pieces

| Piece | What it holds | Status |
|---|---|---|
| `environment/` | the **fundamentals + module** (constitution, method, rules, glossary, sources, completions, `framework/`) **plus** `action-aggregate/` — the **inherited, accepted action aggregate** (parent-owned, read-only) the Experience node consumes. | populated |
| `input/` | the **contract** for the Experience node (instantiated from the standard contract template). | populated |
| `output/` | the node's **produced UX layout** (a blind run). | **empty** |
| `evaluation/` | the scorer — `rubric.md` + `scoring-method.md` (coverage + proximity-to-poles). | populated |
| `benchmark_verification/` | the **exemplar-anchored benchmark**: `positive/` (ceiling) + `negative/` (floor) UX pair. | populated (v0) |

**No `output-example/`.** UX has no derivable answer key, so the benchmark is **exemplar-anchored** — the
positive pole *is* the reference (see `benchmark_verification/README.md`).

## How it will run (later)

1. A blind agent reads `input/contract.md` + `environment/` (incl. the inherited action aggregate) and runs
   the design-node **module's method** to produce a **UX layout** into `output/`.
2. `evaluation/` scores it: **coverage** (every action → an experience pattern) + **quality** (proximity to
   `positive/`, distance from `negative/`), per `rubric.md`.
3. **Iterate**: improve the module toward the current bar; **raise the bar** (enrich `positive/`) as we learn
   — each a versioned step.

## Scope

Deliberately isolates the **Experience node's derivation** (accepted aggregate → UX layout) first, on an
**exemplar-anchored** benchmark. The **spawning / contract-template / two-step submission machinery**
(Action → Experience cascade) is **defined but not yet exercised** — see `scope.md`.
