# Design-tree dry run — materialized sandbox (up to the role-action table)

*A **materialized** dry run of the D2 design tree: the nodes are folders, nested parent → child, and
each node holds a `node.md` card (its contract, ownership, justification) plus its **authored data**,
**copied in** from the authoritative sources. Non-authoritative by nature (workspace) — a snapshot to
**test the framework** in `../../design-tree-tool/`. Authoritative data lives in `../../design/`.*

## The tree (folders mirror the tree)

```
fundamentals/                         constitution (Phases 1–5) + method + rules
└── roles/                            authors the role table (R-)
    └── role-action/                  authors the aggregate role-action table (A-)
        ├── passive-action/           the D1 Designer's passive [P] action pieces
        └── active-action/            the D1 Designer's active [A] action pieces
```

Edges are **design dependency** (not action order). Resolved per `RU-09` (author owns its table) and
`RU-10` (contract demands the aggregate; child decomposes freely).

## What was copied in (snapshot)

| File | Copied from |
|---|---|
| `fundamentals/method.md` | functional doc §1 (Methodology) |
| `fundamentals/rules.md` | `design/catalogs/rules.md` (RU-01…RU-10) |
| `fundamentals/roles/role-table.md` | `design/catalogs/role-action.md` → Roles table |
| `fundamentals/roles/role-action/role-action-table.md` | `design/catalogs/role-action.md` → Actions table |

The `passive-action` / `active-action` cards list which `A-` rows each owns (the *pieces*); the
Action node holds the *merged aggregate*. Constitution (Phases 1–5) is referenced in `../../ref/`,
not copied.

## Reading order

Start at `fundamentals/node.md`, then descend. Each `node.md` states: **owns/authors**, **contract
received**, **contract to children**, **justification**, and **children**.
