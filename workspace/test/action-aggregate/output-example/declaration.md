# Output product 3 — the declaration (example)

*One of three output products. The node's **manifest**: what it is, what it delivers, its status, and
the interface it offers downstream. (First-cut meaning of "declaration" — to confirm.)*

## Node

- **Identity:** the **Action Aggregate** node (a.k.a. action integration node).
- **Governed by:** its contract (`../../input/contract.md`) and the rules `RU-01…RU-11`.

## Delivers

- **The role-action aggregate table** (`role-action-catalog.md`) — the actions each role performs,
  grouped by role, stable IDs, Source-cited.
- **Scale:** 8 roles (`R-00…R-07`); actions `A-001…A-058` (`A-003` retired). The D1 Designer's set
  splits 16 passive / 8 active.

## Status

- **Coverage:** every action Source-cited; the set is the common, anticipable one (open-list — not
  claimed exhaustive).
- **Integrity:** IDs stable and deduplicated.

## Interface offered downstream

- The **aggregate `A-` table** is the **driver/input** for the **capability** node (`RU-11`): its
  contract will be *"design capabilities covering every action in this aggregate."*
- On approval by the parent (Fundamentals), this declaration is what the **successor branch**
  (capability → architecture → implementation) consumes to begin.
