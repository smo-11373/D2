# Design-tree dry run — the ACTION AGGREGATE as hub

*A **materialized** dry run centered on the **action aggregate node**. The aggregate sits at the
**top**; its **production branch** hangs below (the pieces that merge into its table); its
**successor branch** (capabilities → architecture → …) comes off it and is **delayed**. Data is
**copied in** from the authoritative sources in `../../design/`. Non-authoritative snapshot — a test
of the framework in `../../design-tree-tool/`.*

## The shape (folders mirror the tree)

```
action-aggregate/            ← TOP · hub · key data = the merged role-action aggregate table (A-)
├── passive-action/          [production] the D1 Designer's passive [P] pieces
└── active-action/           [production] the D1 Designer's active [A] pieces
                                 …merge up → action-aggregate/role-action-table.md

successor-branch/            [DELAYED] capability → architecture → …  (driven by the aggregate, RU-11)
context/                     [inputs]  role table + method + rules (read-only, RU-08)
```

- **Production branch** (below) *produces* the aggregate — free internal shape, aggregate at the
  boundary (`RU-10`); the aggregate's author owns it (`RU-09`).
- **Successor branch** (off the hub) *consumes* the aggregate — the action aggregate **drives** the
  capability design (`RU-11`). Delayed here; the focus is the aggregate.
- **Context** holds the read-only inputs (the role table, method, rules); to change the role table
  the aggregate would **propose up** to the Role node.

## What was copied in (snapshot)

| File | Copied from |
|---|---|
| `action-aggregate/role-action-table.md` | `design/catalogs/role-action.md` → Actions table |
| `context/role-table.md` | `design/catalogs/role-action.md` → Roles table |
| `context/method.md` | functional doc §1 (Methodology) |
| `context/rules.md` | `design/catalogs/rules.md` (RU-01…RU-11) |
| `successor-branch/capability/capabilities-table.md` | `design/catalogs/capabilities.md` |
| `successor-branch/capability/action-capability-map.md` | `design/catalogs/action-capability-map.md` |

## Reading order

Start at `action-aggregate/node.md` (the hub). Each `node.md` states **owns/authors · contract
received · contract to children · justification**.
