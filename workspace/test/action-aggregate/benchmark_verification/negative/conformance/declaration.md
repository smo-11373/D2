# Declaration — the Action Aggregate node's manifest

*The node's manifest / plan / downstream interface, submitted at **Step 1 (activation)** with the
algorithm (`input/contract.md` §1.3, §6). First-cut meaning of "declaration": the node's identity,
what it will deliver, and the interface it offers the capability branch.*

## 1. Identity

- **Node:** the **Action Aggregate node** (a.k.a. the action-integration node) — a `design-node`
  agent, self-contained, holding its own data and authority below the human Designer's.
- **Contract fulfilled:** `input/contract.md`, issued by its parent **Fundamentals / the D2
  Designer**.
- **Governance:** the design-tree rules **`RU-01…RU-11`**. It **authors and owns** the role–action
  (`A-`) table (`RU-09`); it inherits the roles table as read-only contract context and would
  **propose up** to change it (`RU-04`), never rewrite it.
- **Position in the tree:** child of **Roles**, parent of the **Functionality/Capability** node it
  will later drive (`framework/design-tree.md`; `RU-11`).

## 2. What it will deliver (the output package — three products)

1. **`role-action-catalog.md`** — the role–action aggregate table with substantial descriptions:
   actions merged, grouped by role, stable IDs, every row Source-cited, each action and each role
   substantially described. *(Step 2 — the result.)*
2. **`algorithm.md`** — the reproducible derivation procedure (seek roles → per-role actions →
   aggregate → coverage self-check). *(Step 1 — activation.)*
3. **`declaration.md`** — this manifest. *(Step 1 — activation.)*

## 3. Roles in scope (seven)

| ID | Role | Relationship | Tag |
|---|---|---|---|
| R-00 | D2 Designer | D2 builder (human) | Intrinsic |
| R-01 | D1 Designer | Primary user of D2 (human) | Intrinsic |
| R-02 | D2 Assistant | D2's unified interaction agent | Intrinsic |
| R-03 | D1 Programmer | D1 product position (implements code) | Default |
| R-04 | D1 Technical Manager | D1 product position (non-code maintenance) | Default |
| R-05 | D0 Operator | D0 product position (routine operation) | Default |
| R-06 | D0 Technical Manager | D0 product position (deployment maintenance) | Default |

Derived from **Phase 5 §Item 3** + the layer model (D2 → D1 → D0), with the D2 Designer
(Phase 5 §Item 2 / glossary `d2-designer`) and D2 Assistant (Phase 2 §Principle 3 + Phase 4 §Item 3)
added. Phase 5's **Design Node Builder** is represented by the D2 Assistant's node-building actions,
not as a separate role (flagged).

## 4. Action scope

- **ID scheme:** `A-<digits>`, allocated sequentially from **A-001**, **skipping the retired
  `A-003`**. Roles use `R-00…R-06`.
- **Planned figures:** **~50 actions across the 7 roles**, range **A-001…A-051** (A-003 skipped).
- **The D1 Designer (R-01)** carries the largest set — ~21 actions — each **sub-split
  `[P]` passive / `[A]` active** per the method's discipline; planned split **~11 [P] / ~10 [A]**.
- **Downstream product roles (R-03…R-06)** carry actions elaborated from each position's Phase 5
  §Item 3 job function, tagged **`position-derived`**.
- **R-00 / R-02** carry the builder's and D2's own standing obligations.

## 5. What it commits to (acceptance, `input/contract.md` §3)

- **Coverage** — every action a competent re-derivation from the frozen inputs would surface is
  present (open-list target: the common, anticipable set).
- **Traceability** — every role and action row cites a `Source` **only** from the `sources.md`
  namespace (Phases 1–5 §Items, `method §1`, `RU-01…11`, `glossary <slug>`, framework docs); no
  `Phase 6` or bare `Designer <date>` citation.
- **Integrity** — stable, unique IDs; grouped by role; deduplicated; `A-003` retired; the table
  shaped so the action↔capability map resolves.
- **Substance** — each role and each action carries a real descriptive phrase (what it *is*).

## 6. Downstream interface offered to the Capability node (`RU-11`)

The completed **aggregate `A-` table** is the node's boundary output and the **read-only driver**
for the successor **Capability node**, whose contract will be to **design the capabilities (`C-`)
that support every action** in the aggregate. **Coverage is the contract:** every action must map to
≥1 capability (autonomous capabilities excepted); the action↔capability map records it and a
coverage check verifies nothing is missed. Communication with the Capability node is **adjacency
only** (`RU-07`); the aggregate is handed down as curated read-context (`RU-08`).

## 7. Two-step submission plan (`input/contract.md` §6 — defined, not exercised here)

- **Step 1 — activation.** Submit **algorithm.md** + **declaration.md** to the parent
  (Fundamentals) for approval (`RU-02`). Only on acceptance is the node **activated** and may spawn
  its Roles and per-role action children and do the work.
- **Step 2 — result.** After the work, submit **role-action-catalog.md** — the table with
  substantial descriptions of each action and each role — for acceptance. On acceptance the
  deliverable is final, and the node then calls out its successor branch **capability →
  architecture → implementation** as a cascade (`RU-11`).

An open upward proposal would be a **stopping point** (`RU-05`): the node halts rather than advance
on unapproved change.
