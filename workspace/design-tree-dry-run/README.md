# Design-tree dry run — the ACTION AGGREGATE as hub

*A **materialized** dry run centered on the **action aggregate node**. It sits at the **top**; its
**production branch** hangs below and formulates its key data (the role-action aggregate table); its
**successor branch** (capabilities → architecture → …) comes off it and is **delayed**. Data is
**copied in** from `../../design/`. Non-authoritative snapshot — a test of the framework in
`../../design-tree-tool/`.*

## The shape (folders mirror the tree)

```
action-aggregate/                 ← TOP · hub · key data = the role-action aggregate table (A-)
├── roles/                        [production step 1] seek out the roles → role table (R-)
└── actions-by-role/              [production step 2] for each role, its actions (depends on roles)
    └── d1-designer/              the D1 Designer's actions → { passive.md, active.md }
                                     …all per-role pieces merge up → role-action-table.md

successor-branch/                 [DELAYED] capability → architecture → …  (driven by the complete aggregate, RU-11)
context/                          [inputs]  the fundamentals: method + rules (read-only, RU-08)
```

## The production order (the correction this run bakes in)

1. **Seek out the roles** first (`roles/`).
2. **Then, for each role, its actions** (`actions-by-role/`) — depends on step 1.
   The **passive / active** split is a *sub-split under the D1 Designer only*, **not** the top cut.
3. The action aggregate **merges** all per-role actions into `role-action-table.md`.
4. Only when the aggregate is **fully formulated** may the **successor branch** consume it — "formulate
   all the user actions, then pass that data downstream."

## What was copied in (snapshot)

| File | Copied from |
|---|---|
| `action-aggregate/role-action-table.md` | `design/catalogs/role-action.md` → Actions table |
| `action-aggregate/roles/role-table.md` | `design/catalogs/role-action.md` → Roles table |
| `context/method.md` | functional doc §1 (Methodology) |
| `context/rules.md` | `design/catalogs/rules.md` (RU-01…RU-11) |
| `successor-branch/capability/*` | `design/catalogs/capabilities.md`, `action-capability-map.md` |

## Reading order

Start at `action-aggregate/node.md` (the hub), then descend the production branch: `roles/` →
`actions-by-role/` → `d1-designer/`.
