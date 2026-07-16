# design-tree-tool — a work-in-progress D2 **design tool** (conceptually D3-level)

*Sits **next to** the D2 design package (`../design/`), deliberately **outside** the D2 quad,
because it is a different layer. Work in progress; a **side issue updated all along**, not a phase.*

## What this is

The **design-tree / design-node framework** — the apparatus we are **using to conduct the D2
design**. We adopted it as a **concept and an experiment**: structure D2's own design as a tree of
self-contained nodes, and *learn the tree's real shape as we go*.

Crucially, this framework is **above** the D2 design. It is the tool that *produces* D2, the way D2
is the tool that produces D1 — so conceptually it is **provided by "D3"**, even though no D3 exists.
For that reason it must **not be mixed with the D2 design content** in `../design/` (the functional
document, the Role–Action / Capability catalogs — *what D2 is*). This folder holds *how we are
designing D2*, which is a separate thing.

We do **not** yet know the framework's full shape. That is expected: we put it down as we move
through the D2 design and refine it continuously. It is **not an independent phase** and nothing
here is frozen.

**Reusability.** The point is not D2 alone — a framework that works here is meant to **migrate into
the D1 design template** D2 provides. What proves out becomes a default D2 hands to D1.

## Contents

- `design-tree.md` — the first-cut D2 design tree (dependency-shaped) + node governance (contracts,
  proposals, stopping points, adjacency, input links) with worked examples.
- `registry.md` — the **table of tables**: author/owner and read/write authority for each catalog
  table (the design-tree ownership discipline applied to D2's own catalogs).

## Relation to the D2 catalog (the thorny bit, flagged)

The framework's **formal entries** — rules `RU-02…RU-08`, glossary `design-node` /
`submission-package`, and design-process capabilities (`C-16`, `C-17`, `C-41`) — currently still
live in `../design/catalogs/`, where the relational model keeps their **stable IDs** and coverage
checks. Fully disentangling the D3-level tool from the D2 design record is exactly the kind of
question we are **leaving open and updating as we go**. For now: the *documents* live here; the
*IDs* stay in the catalog, cross-referenced.
