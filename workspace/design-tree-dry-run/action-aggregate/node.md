# Node: Action Aggregate (top of this dry run)

*The focus of this run and the **hub**. Its **key data** is the **merged role-action aggregate
table** (`role-action-table.md`), assembled from the nodes on its **production branch** below. From
this same node a **successor branch** (capabilities → architecture → …) begins — **delayed** for now.*

- **Authors / owns:** `role-action-table.md` — the **aggregate role-action table `A-`**
  (`A-001…A-058`), **merged from the production branch**. The author owns it (`RU-09`).
- **Inputs (read-only, `RU-08`), in `../context/`:** the **role table** (the roles the actions serve)
  and the governing **method + rules** (`RU-01…RU-11`).
- **Production branch — below, produces the aggregate (`RU-10`):**
  - `passive-action/` — the D1 Designer's **passive [P]** pieces.
  - `active-action/` — the D1 Designer's **active [A]** pieces.
  - *(A fuller run adds by-role pieces — R-00 meta, R-02–R-06 downstream — merged up too.)*
  - The pieces **merge** into `role-action-table.md`. Producing the aggregate is the **only** hard
    requirement (`RU-10`); the internal shape is free.
- **Successor branch — off this node, DELAYED:** `../successor-branch/` holds the **capability**
  design (driven by the aggregate, `RU-11`); **architecture** follows it. Delayed on purpose — the
  focus is the aggregate itself.
- **Justification (`RU-02`):** each row's `Source`; the merge is complete and consistent.

**Two branch kinds meet here.** *Production* children (passive/active) hang **below** and *produce*
the aggregate; the *successor* branch (capability → architecture) comes **off** the node and
*consumes* it. Same hub, two directions.
