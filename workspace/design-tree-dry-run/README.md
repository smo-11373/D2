# Design-tree dry run — materialized sandbox (up to the role-action table)

*A **materialized** dry run of the D2 design tree: the nodes are folders, nested parent → child, and
each node holds a `node.md` card (its contract, ownership, justification) plus its **authored data**,
**copied in** from the authoritative sources. Non-authoritative by nature (workspace) — a snapshot to
**test the framework** in `../../design-tree-tool/`. Authoritative data lives in `../../design/`.*

## The tree (folders mirror the tree)

```
fundamentals/                         constitution (Phases 1–5) + method + rules
└── roles/                            authors the role table (R-)
    └── role-action/                  the ACTION AGGREGATE — authors the aggregate A- table
        ├── passive-action/           [internal] the D1 Designer's passive [P] action pieces
        ├── active-action/            [internal] the D1 Designer's active [A] action pieces
        └── capability/               [dependency] driven by the aggregate — authors C- + the map
```

Edges are **design dependency** (not action order). `RU-09` (author owns its table), `RU-10`
(contract demands the aggregate; child decomposes freely), `RU-11` (the action aggregate **drives**
the capability design; coverage is the contract). Two child kinds appear under the action aggregate:
**internal-decomposition** (passive/active — *produce* the aggregate) and **dependency**
(capability — *consumes* it).

## What was copied in (snapshot)

| File | Copied from |
|---|---|
| `fundamentals/method.md` | functional doc §1 (Methodology) |
| `fundamentals/rules.md` | `design/catalogs/rules.md` (RU-01…RU-10) |
| `fundamentals/roles/role-table.md` | `design/catalogs/role-action.md` → Roles table |
| `fundamentals/roles/role-action/role-action-table.md` | `design/catalogs/role-action.md` → Actions table |
| `fundamentals/roles/role-action/capability/capabilities-table.md` | `design/catalogs/capabilities.md` |
| `fundamentals/roles/role-action/capability/action-capability-map.md` | `design/catalogs/action-capability-map.md` |

The `passive-action` / `active-action` cards list which `A-` rows each owns (the *pieces*); the
Action node holds the *merged aggregate*. Constitution (Phases 1–5) is referenced in `../../ref/`,
not copied.

## Reading order

Start at `fundamentals/node.md`, then descend. Each `node.md` states: **owns/authors**, **contract
received**, **contract to children**, **justification**, and **children**.
