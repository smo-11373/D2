# Declaration — the Action-Aggregate node

*Product 3 of the node's output package (contract §1.3): the node's **manifest / plan / downstream
interface** — its identity, what it will deliver, and the interface it offers the capability branch.
First-cut meaning of "declaration" per contract §1.3, submitted (with the algorithm) at **Step 1
activation**, before children are spawned.*

## 1. Identity (manifest)

- **Node:** Action-Aggregate (a.k.a. the action integration node).
- **Place in the tree:** child of **Fundamentals**; parent of the **Functionality / Capability** node.
  Spine: `Fundamentals → … → Roles → Role-Action → Functionality → Architecture` (design-tree.md).
- **Owns / authors:** the **role-action aggregate `A-` table** (`role-action-catalog.md`). Ownership =
  authorship (`RU-09`) — the node authors and owns this table; the parent may **read** the package but
  is not its author.
- **Reads (read-only, via contract):** the **role table `R-*`** handed down from the **Roles** node
  (`RU-04`/`RU-08`), plus the inherited fundamentals — constitution Phases 1–5, method §1, rules
  `RU-01…11`, glossary, framework. Communication is adjacency-only (`RU-07`).

## 2. Deliverable (plan)

An **output package of three products**, delivered across a **two-step submission** (contract §6;
`RU-02`):

- **Step 1 — activation** (before spawning children): submit the **algorithm** (`algorithm.md`) and
  this **declaration** (`declaration.md`) to Fundamentals for approval. Only on acceptance is the node
  activated and may spawn its children.
- **Step 2 — result** (after the work): submit the **role-action aggregate table with substantial
  descriptions** (`role-action-catalog.md`) — a substantial description of each action and of each
  role — with the node's justification and conformance argument.

**Delivered content:** 7 roles (`R-00…R-06`) and 47 actions (`A-001…A-048`, `A-003` retired/skipped),
grouped by role, every row Source-cited within the namespace.

## 3. Internal decomposition (discretionary — `RU-10`)

The contract fixes the **aggregate** as the obligation and leaves internal shape to the node. Planned
decomposition, merged back into the single `A-` table at the boundary:

```
Role-Action (authors the aggregate A- table)
├── Roles seek            → derive R-00…R-06 from Phase 5 Item 3 + layer model
├── passive-action node   → D1 Designer [P]: entry · operating-contract · input · setup ·
│                            understanding · foundational-docs · operating-framework · node-review …
├── active-action node    → D1 Designer [A]: inspect · monitor · investigate · direct · initiate · audit
└── per-role action nodes → R-00, R-02 (meta, no depth frame); R-03…R-06 (position-derived depth frame)
```

Passive-action spawning is implemented first; active-action spawning is the harder, deferred case
(`RU-03`). All pieces are merged; only the aggregate is the contracted boundary output (`RU-10`).

## 4. Downstream interface (to the capability branch)

- **The aggregate drives the capability design (`RU-11`).** The completed `A-` table is the read-only
  **input and driver** for the **Capability node**, whose contract is to design the capabilities
  (`C-`) that **support every action** in the aggregate. **Coverage is the contract:** every action
  maps to ≥1 capability (autonomous capabilities excepted); the action↔capability map records it and a
  coverage check verifies "nothing is missed."
- **Access is read + request, not edit.** Downstream and parent nodes **read** the whole package but
  do not edit it; a change to the `A-` table routes **through its author** — parent **requests down**,
  a descendant **proposes up** and halts (`RU-09`/`RU-04`/`RU-05`).
- **Successor cascade (out of scope here):** capability → architecture → implementation (`RU-11`).

## 5. Conformance argument (gating self-check — passed)

The deliverable **conforms** — it contradicts no governing statement of the fundamentals:

- **Named enumeration preserved.** Every position of the **Phase 5 Item 3** enumeration is present as
  a role, none collapsed, dropped, or re-cast; the D2 Designer is added from the glossary layer anchor,
  not substituted for one.
- **Method discipline honoured.** The D1 Designer's actions are sub-split **passive / active**
  (method §1); the **D0-user throughline** is carried (`A-020`); the list is treated as **open**
  (common, anticipable set, not exhaustive).
- **Depth-frame guards held.** The position-derived depth frame was applied only to the operational
  cast (R-03…R-06) as a completeness prompt — genuinely-implied facets only, **no invented rows** — and
  **not** to the D1 Designer (scaffolded by the journey) or the internal/meta roles (R-00, R-02).
- **Rules not contradicted.** Ownership/authorship (`RU-09`), aggregate-at-the-boundary (`RU-10`),
  coverage-drives-capability (`RU-11`), propose-up/stop (`RU-04`/`RU-05`), and governed-parameter
  derivation (`RU-01`) are all respected.
- **Traceability.** Every row cites an in-namespace `Source` (`sources.md`); traceability is treated
  as necessary but not sufficient — conformance was checked first and independently.

No conformance conflict was found; therefore **no propose-up-and-halt** is raised and the node
proceeds to emit the deliverable. (Had a conflict been found, this section would instead record a
revise-to-conform or a propose-up-and-halt per `conformance.md` — never emit-and-flag.)

## 6. To confirm with the parent (open, first-cut)

- The **first-cut meaning of "declaration"** (identity + plan + downstream interface) — confirm scope
  (contract §1.3 flags this as "to confirm").
- The **intrinsic/default** tagging of Design Node Builder (tagged intrinsic as part of D2's design
  mechanism) — confirm against the Roles node's owned role table (`RU-04`; the Roles node authors that
  distinction).
