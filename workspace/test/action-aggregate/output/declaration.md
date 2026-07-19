# Declaration — the Action-Aggregate node

*Product 3 of the Action-Aggregate node (contract §1.3). The node's manifest / plan / downstream
interface: its identity, what it will deliver, and the interface it offers the capability branch.
Step 1 (activation) material — submitted with the algorithm before the node spawns children.*

## Identity

- **Node:** Action-Aggregate (a.k.a. the action-integration node).
- **Parent:** Fundamentals (the D2 Designer's frozen constitution + method + rules).
- **Place in the design tree:** child of **Roles**, on the spine **Roles → Role-Action →
  Functionality (capabilities) → Architecture** — mirroring the Phase 6 governing hierarchy
  *Role → Action → Capability → Architecture → Implementation* (`design-tree.md`).
- **Owned data (authorship = ownership, `RU-09`):** the **role-action aggregate table** — the `A-*`
  actions each role performs. This node **authors** it; the parent reads it by read + request, never
  edits it. (The `R-*` role table is authored by the Roles node and inherited read-only.)

## What it will deliver (the contracted deliverable, §1)

An output package of three products, across a two-step submission (§6):

1. **`role-action-catalog.md`** — the role-action aggregate table with substantial descriptions:
   actions merged, grouped by role, stable IDs, each row Source-cited, each action and each role
   substantially described. Target = the common, anticipable open-list set. *(Step 2 — result.)*
2. **`algorithm.md`** — the derivation procedure (seek roles → per-role actions → aggregate →
   self-check), written for reproduction. *(Step 1 — activation.)*
3. **`declaration.md`** — this manifest / plan / downstream interface. *(Step 1 — activation.)*

## Inputs consumed (read-only, `RU-08`)

Constitution Phases 1–5 · method §1 · rules `RU-01…RU-11` · glossary · framework
(`design-tree`, `design-node-algorithm`, `conformance`). Citations resolve inside the package
namespace (`sources.md`).

## Method commitments (how the deliverable is bound)

- **Conformance is gating** (`conformance.md`): the table contradicts no governing statement of the
  fundamentals — checked first, before any dependent child is spawned. On conflict: revise-to-conform
  or propose-up-and-halt (`RU-04`/`RU-05`), never emit-and-flag.
- **Completeness is active**: the should-exist set is derived from the fundamentals and each piece
  checked present — gating for named/listed pieces (the Phase 5 Item 3 position enumeration, the
  passive/active journey, the depth-frame facets, the position-oriented control lists), with the
  **harness-richness** emphasis surfacing each position's test/monitor/detect/make-visible facets.
- **Decompose freely, aggregate always** (`RU-10`): internally the node may split by category
  (passive-action / active-action sub-nodes, per-role action children) but returns the single
  aggregate `A-` table at its boundary.

## Downstream interface (offered to the capability branch, `RU-11`)

- **Consumer:** the **Functionality / Capability node** (dependency child).
- **Contract offered:** the completed aggregate `A-` table is the **read-only driver** of the
  capability design. Its obligation to the consumer — *coverage is the contract*: **every action maps
  to ≥1 capability** (autonomous capabilities excepted); the action↔capability map records the
  linkage and a coverage check verifies nothing is missed.
- **Stability guarantee:** IDs are stable and contiguous (`A-003` retired — permanently skipped), so
  the capability map's references remain valid across re-derivations.
- **Change protocol:** the capability branch reaches this table by **read + request-down** (`RU-09`);
  this node reaches ancestor-owned data (e.g. the role table) by **propose-up-and-halt**
  (`RU-04`/`RU-05`).
- **Adjacency (`RU-07`):** the node communicates only with its immediate parent (Roles / Fundamentals
  chain) and its children; read-only input links (`RU-08`) are context, not channels.

## Confirmation flagged (contract §1.3)

"Declaration" is taken as the node's **manifest + plan + downstream interface** (first-cut meaning per
contract §1.3). Flagged for the parent to confirm at activation; no conformance conflict identified,
so the node proceeds under this reading pending confirmation (not a propose-up-and-halt).

## Submission plan (§6 — structure defined, not exercised here)

- **Step 1 — activation:** submit `algorithm.md` + `declaration.md` for the parent's approval
  (`RU-02`). Only on acceptance does the node spawn Roles → per-role action children.
- **Step 2 — result:** submit `role-action-catalog.md` with substantial descriptions; on acceptance
  it is final and drives the capability cascade (`RU-11`).
