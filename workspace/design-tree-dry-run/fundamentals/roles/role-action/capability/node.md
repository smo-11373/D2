# Node: Capability (driven by the action aggregate)

- **Authors / owns:**
  - `capabilities-table.md` — the **capability catalog `C-`** (`C-01…C-41`), the D2 support for the
    actions.
  - `action-capability-map.md` — the **Action ↔ Capability join** (coverage of `A-` by `C-`).
- **Contract received (from the action aggregate node, Role-Action):** *"design the capabilities
  that **support every action** in the aggregate `A-` table."* The **aggregate action table** is
  supplied read-only (`RU-08`) and **drives** this design (`RU-11`).
- **Coverage is the contract (`RU-11`).** Every action must map to ≥1 capability (autonomous
  capabilities excepted); the join records it and a coverage check verifies **nothing is missed**.
  - *Snapshot:* 56 actions, 41 capabilities; every action supported; the only capabilities with no
    action are the expected **autonomous** ones (`C-04/07/08/18/19`).
- **Contract to children:** none in this run — a fuller decomposition would split by capability layer
  (**D2** / **D1-product** / **D0-product**) into sub-nodes, each aggregating up.
- **Justification (`RU-02`):** each capability's `Source`; the coverage check is the node's proof it
  met its contract.
- **Finding (dry run).** This node is a **dependency successor** of the action aggregate (it
  *consumes* the aggregate), whereas `passive-action` / `active-action` are the aggregate's
  **internal decomposition** (they *produce* it). Both are "children" of Role-Action but of two
  different kinds — worth distinguishing in the framework (internal-decomposition edge vs
  dependency edge).
