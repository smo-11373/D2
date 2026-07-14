# Catalog Registry — the table of tables

*Living. Bookkeeping **over the catalog tables themselves**: who authors/owns each table, and who
may read and write it. This applies the **design-tree governance discipline to D2's own design**
early — while it is cheap to shape — so the working apparatus can be refined here and later
**migrated into the D1 design template** D2 provides. See `README.md` for the catalogs' relational
conventions.*

## Why this exists

- **Dogfooding.** The same authorship/authority discipline D2 will ask of a D1 design should
  govern D2's own catalogs first. What works here becomes a default D2 hands to D1.
- **Provenance at the table level** (Phase 1 §4.6): every table has a recorded author/owner, so it
  is always clear who governs its meaning.
- **Read/write clarity:** authority follows meaning — the owner of a table governs its content;
  others read freely and *propose* changes.

## The tables

| Table | Holds | Author / Owner | Read | Write |
|---|---|---|---|---|
| `registry.md` (this file) | the table of tables | D2 Designer (R-00) | open | Owner |
| `role-action.md` | Roles `R-`, Actions `A-` | D2 Designer (R-00) | open | Owner; others propose |
| `capabilities.md` | Capabilities `C-` | D2 Designer (R-00) | open | Owner; others propose |
| `action-capability-map.md` | Action ↔ Capability join | D2 Designer (R-00) | open | Owner; others propose |
| `designer-queries.md` | Queries `Q-` | D2 Designer (R-00) | open | Owner; others propose |
| `rules.md` | Rules `RU-` | D2 Designer (R-00) | open | Owner; others propose |
| `glossary.md` | Terms | D2 Designer (R-00) | open | Owner; others propose |

*Current drafting is done by the **D2-design assistant** (the LLM building D2) under Designer
direction; the **D2 Designer (R-00)** holds Designer-originated completion authority over these
living sets (Phase 5, Item 2), and is therefore recorded as owner. As the D2 design tree grows,
authorship may resolve to specific design nodes/agents — the mechanism below is meant to carry
that.*

## Governance rules (ad hoc, evolving)

1. **One owner per table.** Every catalog table is registered here with exactly one author/owner
   before it is used.
2. **Authority follows meaning.** The owner holds write authority over the table's content; anyone
   else *proposes* changes, which the owner accepts, adjusts, or rejects.
3. **Read is open by default.** Any design participant may read any table unless it is explicitly
   marked restricted here.
4. **Cross-table references are read-only.** A table may reference another's IDs (foreign keys) but
   must not rewrite them; the referenced table's owner governs those IDs.
5. **Provenance is preserved.** Authorship and material changes are recorded, never silently
   rewritten (Phase 1 §4.6).
6. **The registry governs itself.** New tables, owner changes, or access changes are recorded here
   first; the registry's own owner is the D2 Designer.

*These rules are ad hoc and evolving. As the tool design develops, new rules and refinements are
added here; settled ones may graduate into `rules.md` as `RU-` entries.*
