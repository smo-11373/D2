# Scope & deliberately-open questions — this test

*What this test fixes now, and what it deliberately leaves open. The contract form is **fluid** — not
fixed at this point; expect it to change down the road.*

## In focus now (the substance we are pinning down)

- The **shape of the output** — what the deliverable looks like (`output-example/`).
- The **shape of the input contract, in narrative terms** (`input/contract.md`).

Everything below is deliberately deferred.

## Deliberately not addressed (open)

1. **How the contract is specified / generated.** Conceptually the contract **comes from the
   fundamentals** (the parent derives it — see `../../../design-tree-tool/design-node-algorithm.md`).
   We do **not** exercise that generation here. First we want to learn whether the **current shape**
   of the contract can produce the desired outcome at all; contract *generation* comes after.

2. **Why this node — and why first.** We isolate the **action aggregate** node on the assumption that
   **figuring out the user actions is the first thing to do, in any layer (D2 / D1 / D0), and
   especially D1** — before capabilities, architecture, implementation. That ordering is *assumed*
   here, not derived; the isolation reflects the assumption.

3. **The algorithm and the "declarations" — and whether they belong in the input.** The design-node
   **algorithm** and the node's **declarations** are **left open**: whether they should be part of
   `input/`, and in what form, is an **open question**. For now `input/` holds only the contract.

## Status of the contract form

**Fluid — not fixed.** The form of the contract is expected to change; nothing about it is frozen at
this point. This test exists to probe whether the *current* output-shape + contract-shape can drive
the desired result — not to lock the contract down.
