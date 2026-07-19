# design-tree-tool — the D2 **module** (design tree + design node module; work in progress, conceptually D3-level)

*Sits **next to** the D2 design package (`../design/`), deliberately **outside** the D2 quad,
because it is a different layer. Work in progress; a **side issue updated all along**, not a phase.*

## What this is

The **module** — the **design tree + design node module** (the apparatus we are **using to conduct
the D2 design**; earlier called "the design-tree / design-node framework"). *Just* **module** when
unambiguous. We adopted it as a **concept and an experiment**: structure D2's own design as a tree of
self-contained nodes, and *learn the tree's real shape as we go*.

**Naming.** The **module** is a D2 (conceptually D3-level) design element with four components — a
**method** (emits deliverables), an **enforcer**, an **acceptance** step, and **submission**. Its
**run outputs** — `algorithm.md`, `declaration.md`, the role table, the role-action table — are
*products of running the module*, **not** the module itself. The **D1 module** is the *same* module,
minor modifications only where a layer forces them.

Crucially, the module is **above** the D2 design. It is the tool that *produces* D2, the way D2
is the tool that produces D1 — so conceptually it is **provided by "D3"**, even though no D3 exists.
For that reason it must **not be mixed with the D2 design content** in `../design/` (the functional
document, the Role–Action / Capability catalogs — *what D2 is*). This folder holds *how we are
designing D2*, which is a separate thing.

We do **not** yet know the module's full shape. That is expected: we put it down as we move
through the D2 design and refine it continuously. It is **not an independent phase** and nothing
here is frozen.

**Reusability.** The point is not D2 alone — a module that works here is meant to **migrate into
the D1 design template** D2 provides. What proves out becomes a default D2 hands to D1. This is the
"same as the D1 module" principle: one module, instantiated per layer.

## Contents

- `design-node-algorithm.md` — the **module's method**: how a node emits its children's contracts
  (downward) and fulfils its own contract (upward), and the acceptance test that makes it terminate
  and reproduce.
- `design-tree.md` — the first-cut D2 design tree (dependency-shaped) + node governance (contracts,
  proposals, stopping points, adjacency, input links) with worked examples.
- `conformance.md` — the **conformance** acceptance requirement (layer-relative): a deliverable must
  contradict no governing statement of the layer above; conform or propose-up-and-halt.
- `registry.md` — the **table of tables**: author/owner and read/write authority for each catalog
  table (the ownership discipline applied to D2's own catalogs).
- `dry-run.md` — a worked dry-run of the module.

## Relation to the D2 catalog (the thorny bit, flagged)

The module's **formal entries** — rules `RU-02…RU-08`, glossary `design-node` /
`submission-package`, and design-process capabilities (`C-16`, `C-17`, `C-41`) — currently still
live in `../design/catalogs/`, where the relational model keeps their **stable IDs** and coverage
checks. Fully disentangling the D3-level tool from the D2 design record is exactly the kind of
question we are **leaving open and updating as we go**. For now: the *documents* live here; the
*IDs* stay in the catalog, cross-referenced.
