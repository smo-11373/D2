# Declaration — the Action-Aggregate node

*Deliverable 3 of the Action-Aggregate node (contract §1, delivered at Step 1 — activation). The
node's **manifest / plan / downstream interface**: its identity, what it delivers, and the interface
it offers the capability branch. First-cut meaning of "declaration," per contract §1 (to confirm).*

## 1. Identity (manifest)

- **Node:** Action-Aggregate (a.k.a. the action integration node), the **Role-Action** node on the
  D2 design tree.
- **Position in the tree:** child of **Roles**, itself under **Setup → Fundamentals**; parent of the
  dependency successor **Functionality (Capability)**. Spine: *Roles → Role-Action → Functionality →
  Architecture* (mirrors the Phase 6 governing hierarchy Role → Action → Capability → Architecture →
  Implementation). *(Source: `design-tree`.)*
- **Owned data (authors & enforces):** the **role-action aggregate table** — the actions `A-*` each
  role performs. The node **authors** this table; other nodes (including the parent) may **read** it
  but are not its author (`RU-09`).
- **Read-only inputs (from the contract):** the constitution (Phases 1–5), the method (§1), the rules
  (`RU-*`), glossary/framework, and — carried down in the contract — the **role table `R-*`** owned by
  the Roles node (`RU-04`, `RU-08`). The Source namespace is `sources.md`.
- **Authority:** a self-contained design agent with authority over its own table, below the human
  Designer's (glossary `design-node`). It may decompose internally and spawn children (`RU-03`,
  `RU-10`) but must return the contracted aggregate.

## 2. What it delivers (plan)

An **output package of three products** across a **two-step submission** (contract §1, §6):

- **Step 1 — activation:** this **declaration** + the **algorithm** (`algorithm.md`), submitted to the
  parent (Fundamentals) for approval (`RU-02`). Only on acceptance is the node activated and may spawn
  children.
- **Step 2 — result:** the **role-action aggregate table with substantial descriptions**
  (`role-action-catalog.md`) — a substantial description of each role and each action, grouped by role,
  stable-ID'd, every row Source-cited.

**Internal decomposition (discretionary, `RU-10`):** the node may dissect its work by category —
a **passive-action** sub-node (entry · operating contract · setup · foundational docs · operating
framework · node review · being-asked) and an **active-action** sub-node (inspect · monitor progress ·
monitor spend · investigate · redirect · lay down a rule · audit), each possibly with its own
children — and **merge** them into the single aggregate `A-` table. Spawning is driven by the
Designer's potential actions (`RU-03`); passive-action spawning is implemented first, active deferred.
The boundary obligation is the aggregate, not the internal shape.

## 3. Contents delivered (this run)

- **7 roles** `R-00…R-06` (D2 Designer, D1 Designer, Design Node Builder, D1 Programmer,
  D1 Technical Manager, D0 Operator, D0 Technical Manager).
- **44 actions** `A-001…A-045` (`A-003` retired/skipped), grouped by role; the D1 Designer's set
  sub-split passive `[P]` (12) / active `[A]` (9).
- Every role and action carries a substantial description and a namespace-resolved `Source`.

## 4. Downstream interface (offered to the capability branch)

Per **`RU-11`**, the completed aggregate `A-` table is the **read-only input and driver** for the
**Functionality (Capability)** node:

- **Contract offered downstream:** *design the capabilities `C-*` that support every action in the
  aggregate.* **Coverage is the contract** — every action maps to ≥1 capability (autonomous
  capabilities excepted); the **action↔capability map** records it and a coverage check verifies
  "nothing is missed."
- **Stable IDs as the join key:** the `A-*` IDs are the durable handles the action↔capability map
  resolves against; `A-003` is permanently retired and must not be reissued.
- **Change protocol:** the Capability node **reads** this table; to change it, it **proposes up** and
  the Action-Aggregate node (the author) makes the change and re-submits (`RU-09`). To change the
  ancestor **role table**, this node proposes up to the Roles node and **halts** until resolved
  (`RU-04`/`RU-05`). Communication is **adjacency-only** (`RU-07`).
- **Boundary exposure:** the interface exposes the `A-*` IDs, action names, per-action descriptions,
  role grouping, and `[P]`/`[A]` class — enough for capability derivation and coverage checking —
  while hiding the node's internal passive/active decomposition (`RU-08`, Phase 5 §Item 5).

## 5. Conformance argument (gating self-check result — contract §3)

Conformance was run **first and gating** (`conformance.md`; algorithm §4). The deliverable
contradicts no governing statement of the fundamentals:

- **Named enumeration preserved.** All six positions named in **Phase 5 §Item 3** appear as distinct
  roles (`R-01`–`R-06`); **none dropped, collapsed, or re-cast** — the named-enumeration conformance
  requirement. The layer model adds `R-00` D2 Designer.
- **Designer distinction preserved.** `R-00` D2 Designer and `R-01` D1 Designer are kept **separate**;
  folding them would contradict glossary `designer`/`d2-designer`/`d1-designer`. The internal-agent
  **Design Node Builder** is kept as a **full role** (not folded into "the design process") because
  Phase 5 §Item 3 names it in the enumeration.
- **Method discipline honoured.** The D1 Designer's actions carry the **passive/active** split and the
  **D0-user optimization** throughline (`A-024`); the list is treated as **open** (method §1).
- **Traceability within namespace.** Every row cites a `Source` resolving inside `sources.md`; no
  `Phase 6 Item N` or `Designer <date>` citation is used.

**No conformance conflict was found**, so **no propose-up-and-halt** was raised and the node did not
emit-and-flag. Had a conflict arisen, the node would have **revised to conform**, or — if the conflict
were a genuine defect in the fundamentals — raised an upward proposal (`RU-04`) and **halted**
(`RU-05`) here rather than emitting a deviating table.

## 6. Successor cascade (out of scope for this test)

After acceptance, the node calls out its successor branch — **capability → architecture →
implementation** — a cascade (`RU-11`). This test **defines** the two-step submission and the
downstream interface but does **not exercise** submission, approval, or the cascade.
