# The D2 Design Tree — first cut

*Provisional. D2's own design, laid out on the **design-tree framework it prescribes** (dogfooding).
See `working-notes.md` for the spawning mechanism (`RU-03`) and node definition (glossary
`design-node`); `../decisions/` for open questions.*

## Principle — edges are design dependency, not action order

The tree records **design dependency**: an edge `A → B` means **B's design depends on A's**. It is
**not** the Designer's action order. Two steps adjacent in the Designer's journey can be
*independent* in design (e.g. *deciding to use D2* and *setup*), and a chain that reads as one
topic can be a real dependency (Roles → Role-Action → …). This supersedes the earlier
journey-cluster grouping: the **functional document's sections are a reading order; the design tree
is dependency-shaped.**

## The tree (first cut)

```
Fundamentals
├── Decision to use D2                     (independent of Setup)
└── Setup
    └── Roles  (role table)
        └── Role-Action  (role-action table)          depends on Roles
            └── Functionality  (capabilities)          depends on Role-Action   (optional)
                └── Architecture                        depends on Functionality (Phase 7)
```

The spine **Roles → Role-Action → Functionality → Architecture** mirrors the Phase 6 governing
hierarchy: *Role → Action → Capability → Architecture → Implementation.*

## Nodes and their own data (first cut)

| Node | Own data (owns & enforces) | Depends on |
|---|---|---|
| **Fundamentals** | D2 constitution (Phases 1–5) + Phase 6 method (§1) + rules `RU-01…03` | — (root) |
| **Decision to use D2** | `A-055`; `C-37` (orientation summary) | Fundamentals |
| **Setup** | posture + setup package: `A-015/A-016/A-017/A-019`; `C-01/C-02/C-03/C-05/C-22` | Fundamentals |
| **Roles** | the roles table `R-*`; `A-056`; `C-38` | Setup |
| **Role-Action** | the role-action table — the actions `A-*` each role performs | Roles |
| **Functionality** | the capabilities `C-*` + the Action↔Capability map | Role-Action |
| **Architecture** | Phase 7 architecture | Functionality |

## To resolve next (the "own data" question)

1. **Table nodes vs functional nodes overlap.** `A-055` (Decision) and `A-015` (Setup) also live in
   the **Role-Action table** the Role-Action node owns. Decide the ownership model: does the
   Role-Action node own the *whole* `A-` table (and Decision/Setup only *reference* their rows), or
   is the table's content *distributed* to the functional nodes that use it?
2. **"Functionality" node** may be **omitted / folded** into Role-Action or Architecture.
3. **Roles under Setup?** The role table was part of setup in functional-doc §3; here Roles is a
   *child* of Setup. Confirm.
4. **Shared capabilities** (`C-13/C-14/C-15/C-20…`) sit in the Functionality layer; ownership
   within it still TBD.
