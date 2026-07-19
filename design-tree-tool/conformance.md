# Conformance — a module acceptance requirement (layer-relative)

*Provisional, part of the **module** (the design tree + design node module — §"Naming" below). Stated
once here and meant to read the **same at every layer**: it is the D3-provided module that designs D2,
the same module D2 hands to D1. Where this doc says "the layer above," read the concrete governing
layer for the instantiation — the D2 fundamentals for the D2 module, the D1 constitution for the D1
module.*

## Naming (anchor)

- **module** — the **design tree + design node module** together; "just module" when unambiguous. It
  is a D2 (conceptually D3-level) **design element**: a **method** that emits deliverables, an
  **enforcer**, an **acceptance** step, and **submission**. The D1 module is the *same* module, minor
  modifications only where a layer forces them.
- **run outputs** — `algorithm.md`, `declaration.md`, the role table, the role-action table, … are
  **products of running the module**, not the module. They are never edited by hand to satisfy this
  requirement; the module is changed and re-run.

## The requirement

**Every node's deliverable must conform to the governing layer it inherits.** *Conform* means it
**contradicts no governing statement** of that layer — no principle, no named enumeration, no method
discipline, no rule. This is a **first-class, gating acceptance criterion**: a non-conformant
deliverable is unacceptable regardless of how well it scores on coverage, traceability, integrity, or
substance.

Layer-relative, one formulation, both instantiations:

- **D2 module** → the deliverable conforms to the **D2 fundamentals** (the notional D3 product).
- **D1 module** → the deliverable conforms to the **D1 constitution**.

No per-layer edit; authored once in the module, correct at each layer. (A conformance requirement
written D2-specifically would itself violate the "same as the D1 module" principle — another sign the
layer-relative form is the right one.)

## Conformance is not traceability

The two are distinct, and the distinction is the whole point:

| | asks | answers |
|---|---|---|
| **Traceability** (provenance) | does every element cite a `Source` in the inherited layer? | "it came from somewhere legal" |
| **Conformance** (agreement) | does the deliverable — element by element and as a whole — contradict any governing statement of the inherited layer? | "it violates nothing above it" |

Provenance is **necessary but not sufficient**. A traceable element can still be non-conformant.
Worked instance (the action-aggregate benchmark): a result that folded a **named Phase-5 Item-3
position** into another role **passed traceability 57/57** — every row cited a Source — and was still
**non-conformant**, because it contradicted the constitution's named-position enumeration and
Top-to-Bottom's bar against premature collapse. Under a traceability-only acceptance test it was
accepted; under conformance it is rejected.

## Where it lives in the module

Conformance is not a mechanism bolted onto one deliverable; it is a property enforced across the
module's components and along the tree:

- **Acceptance** — conformance is the **first and gating** criterion, a peer of (arguably above)
  coverage / traceability / integrity / substance. Fail conformance → reject, full stop.
- **Enforcer** — checks the deliverable for conformance against the inherited governing layer
  (semantic check by the node's standard-enforcer, re-reading the layer above — not a citation count).
- **Submission** — the submission package's **justification carries an explicit conformance argument**
  ("here is why my deliverable violates nothing above it"). The parent, acting in the **enforcer /
  acceptance** position, independently runs the conformance gate before accepting (`RU-02`). So
  conformance is enforced **twice**: node self-check before submission (`RU-06`), parent-check at
  acceptance (`RU-02`).
- **Design tree** — the requirement **propagates by contract**: a parent's contract carries "conform
  to the layer above" **down** to each child, along with the read-only governing layer it must conform
  to (`RU-04`, `RU-08`). An unresolved conformance conflict propagates **up** as a proposal (see next).

## Behavior — conform, or halt

On a conformance conflict there are exactly two legal moves:

1. **Revise to conform** — bring the deliverable into agreement with the governing layer, and re-check.
2. **Propose up and halt** — if the node believes the conflict stems from a *defect in the governing
   layer itself*, it raises an **upward proposal** (`RU-04`) and **stops** (`RU-05`): it may not spawn
   children or advance until the owning node / Designer rules.

**"Flag and continue" is not a legal state.** A node may not emit a deliverable it knows deviates from
the layer above while noting the deviation for later. Silent deviation dressed as a flagged judgment
call is precisely the failure the benchmark exposed; it is closed by construction here.

## Check placement (strategic — Harness First)

*Where* conformance is tested is an optimization; *that* it must hold is the invariant. Following
Harness First (make deviation visible before the design space expands downward), stage the **same**
gate at each natural boundary rather than only at the end:

- after each **owned deliverable** is produced (e.g. a node's table) and **before** it spawns
  dependent children — so a non-conformant deliverable is caught before it contaminates everything
  derived from it;
- at **submission** (node self-check) and again at the **parent** (enforcer acceptance).

These are placements of one requirement, not separate requirements.

## What this is not

Not a role mechanism, not an enumeration trick, not a change to the method's derivation, and not an
edit to any run output. The named-position example is one *consequence* of the general requirement,
not a special case of it. Fix the requirement in the module; re-run the module; let the fixed
evaluation benchmark re-score the new outputs.

## Formalization (flagged)

This requirement most naturally becomes a **formal rule** in `../design/catalogs/rules.md` (a new
`RU-*`: "a node's deliverable must conform to its governing layer; conform or propose-up-and-halt"),
so contracts can cite it by ID the way they cite `RU-04/05/08/10`. Per this folder's README the
*document* lives here; the *ID* would be minted in the catalog. Deferred to a catalog pass.
