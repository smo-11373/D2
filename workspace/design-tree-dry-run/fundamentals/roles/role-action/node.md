# Node: Role-Action (the Action node)

- **Authors / owns:** `role-action-table.md` — the **aggregate role-action table `A-`**
  (`A-001…A-058`, A-003 retired). **This node is the author** (`RU-09`); the parent (Roles) may
  **read** it but is not the author. To change a row, Roles **requests down** and this node makes the
  change; to change the *role* table, this node **proposes up** (`RU-04`, `RU-09`).
- **Contract received (from Roles, `RU-10`):** deliver the role-action table **as an aggregate**;
  the **role table** is supplied read-only (`RU-08`).
- **Decomposition (`RU-10`) — free internally, aggregate at the boundary:**
  - `passive-action/` — the D1 Designer's **passive [P]** action pieces.
  - `active-action/` — the D1 Designer's **active [A]** action pieces.
  - The two are **merged** into `role-action-table.md`, the contracted aggregate.
- **Justification (`RU-02`):** each row's `Source` column (baseline-derived / position-derived /
  Designer-dated).
- **Finding (dry run).** The passive/active split cleanly covers **R-01 (the D1 Designer)**. The
  aggregate *also* holds **R-00 meta** (`A-010/011`) and the **downstream/agent roles** R-02–R-06
  (`A-021…A-051`), which are neither Designer-passive nor Designer-active. A full decomposition would
  give those their own sub-nodes (e.g. an *agent-actions* node, a *downstream-role-actions* node);
  here they sit directly in the aggregate. Logged as the next decomposition question.
