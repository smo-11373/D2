# Node: Actions-by-Role (production branch — step 2)

*For **each role** (from `../roles/`), figure out that role's actions. The pieces **merge up** into
the action aggregate. Depends on `roles/`.*

- **Contract received (from the action aggregate):** produce every role's actions, for merge into the
  aggregate `A-` table. The **role table** is supplied read-only (`RU-08`).
- **One piece per role** (full text in `../role-action-table.md`):
  - **R-00 D2 Designer** — `A-010, A-011` (meta)
  - **R-01 D1 Designer** — 24 actions → detailed in `d1-designer/` (split **passive / active**)
  - **R-02 Design Node Builder** — `A-021–A-027`
  - **R-03 D1 Programmer** — `A-028, A-040, A-041`
  - **R-04 D1 Technical Manager** — `A-029–A-033, A-042, A-043`
  - **R-05 D0 Operator** — `A-034–A-036, A-044–A-048`
  - **R-06 D0 Technical Manager** — `A-037–A-039, A-049–A-051`
  - **R-07 D2 Assistant** — *no actions* (a contact-point role)
- **Contract to child (`d1-designer/`):** produce the D1 Designer's action set (passive + active).
- **Justification (`RU-02`):** each row's `Source`. The union of the per-role pieces **is** the
  aggregate — the coverage the parent's contract demands.
