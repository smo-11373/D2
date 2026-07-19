# Conformance — a module acceptance requirement (layer-relative)

*Part of the **module** (the design tree + design node module). Sandbox snapshot. Stated once and
meant to read the **same at every layer**: for this node, "the layer above" is the **fundamentals**
it inherits (the constitution `constitution/`, the method `method.md`, the rules `rules.md`).*

## The requirement

**Every node's deliverable must conform to the governing layer it inherits.** *Conform* means it
**contradicts no governing statement** of that layer — no principle, no **named enumeration**, no
method discipline, no rule. This is a **first-class, gating acceptance criterion**: a non-conformant
deliverable is unacceptable regardless of how well it scores on coverage, traceability, integrity, or
substance.

Layer-relative: the same clause reads "conform to the fundamentals" for this (D2) instantiation and
"conform to the D1 constitution" for the D1 instantiation. One formulation, no per-layer edit.

## Conformance is not traceability

The two are distinct:

- **Traceability** (provenance) — does every element cite a `Source` in the inherited layer? "It came
  from somewhere legal."
- **Conformance** (agreement) — does the deliverable, element by element and as a whole, contradict
  any governing statement of the inherited layer? "It violates nothing above it."

Provenance is **necessary but not sufficient**. A traceable element can still be non-conformant — for
example, a deliverable that **collapses, drops, or re-casts an item the fundamentals name in an
explicit enumeration** may cite that enumeration as its Source and still contradict it. Traceability
alone would accept such a result; conformance rejects it.

## Behaviour — conform, or halt

On a conformance conflict there are exactly two legal moves:

1. **Revise to conform** — bring the deliverable into agreement with the governing layer.
2. **Propose up and halt** — if the node believes the conflict stems from a *defect in the governing
   layer itself*, raise an **upward proposal** (`RU-04`) and **stop** (`RU-05`) until the owner rules.

**"Flag and continue" is not a legal state.** A node may not emit a deliverable it knows deviates from
the layer above while merely noting the deviation. Silent deviation dressed as a flagged judgment call
is not permitted.

## Where it is checked (Harness First)

Conformance is checked **first and gating** in the acceptance self-check (see
`design-node-algorithm.md` step 4), and again by the parent at acceptance (`RU-02`). Stage it at each
internal boundary — after an owned deliverable is produced and **before** dependent children are
spawned — so a non-conformant deliverable is caught before it contaminates what is derived from it.
