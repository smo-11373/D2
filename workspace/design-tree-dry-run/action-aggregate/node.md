# Node: Action Aggregate (top of this dry run — the hub)

*The focus. Its **key data** is the **role-action aggregate table** (`role-action-table.md`), which it
**cannot pass downstream until it is fully formulated** — every user action, for every role. Two
branches meet here: the **production branch** (below) formulates the aggregate; the **successor
branch** (off the hub) consumes it — delayed.*

- **Authors / owns:** `role-action-table.md` — the **aggregate role-action table `A-`**, merged from
  the production branch (`RU-09`).
- **Production branch — below, in order (this is a dependency pipeline):**
  1. `roles/` — **seek out the roles** first → the role table (`R-`).
  2. `actions-by-role/` — then, **for each role, figure out its actions** (depends on `roles/`).
     The D1 Designer's actions further split into **passive / active** (a sub-split, not the top cut).
  3. **Aggregate** — this node **merges** all per-role actions into `role-action-table.md`.
- **Successor branch — off the hub, DELAYED:** `../successor-branch/` (capability → architecture, …),
  driven by the aggregate (`RU-11`). **Gated:** it may not begin until the aggregate is *complete* —
  "formulate all the user actions, then pass that data downstream."
- **Inputs (read-only, `RU-08`), in `../context/`:** the governing **method + rules**.
- **Justification (`RU-02`):** each row's `Source`; the aggregate is complete and consistent.
