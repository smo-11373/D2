# design / catalogs — living working sets

The project-wide **living catalogs**: continuously edited and authoritative (not scratch — that
lives in the top-level `workspace/`). Carried across phases; Phase 7 keeps using them.

## Files

- `registry.md` — **the table of tables**: author/owner and read/write authority for each catalog table
- `role-action.md` — Roles (`R-`) and the Actions (`A-`) each performs
- `capabilities.md` — Capabilities (`C-`), tagged by layer (D2 / D1-product / D0-product)
- `action-capability-map.md` — the Action ↔ Capability join table
- `designer-queries.md` — Designer query examples (`Q-`)
- `rules.md` — design rules (`RU-`), each derived from a role or principle
- `glossary.md` — D2 / D1 / D0 term definitions

## Relational conventions

These catalogs form a small relational model expressed in Markdown. Designer-oriented text is
deliberately preferred over a machine format (Phase 5 — Top-to-Bottom: don't swap an editable text
format for JSON merely because it's easier to implement).

- **Stable numeric IDs = primary keys.** Every entity has an ID that never changes and is never
  reused or renumbered. Wording may change freely; the ID holds the identity.

  | Entity | Prefix | Example |
  |---|---|---|
  | Role | `R-` | `R-01` |
  | Action | `A-` | `A-001` |
  | Capability | `C-` | `C-01` |
  | Query | `Q-` | `Q-001` |
  | Rule | `RU-` | `RU-01` |
  | Glossary term | term-slug | `design-node` |

  Glossary is the one exception: a definition is referenced by its term, so the slug is its key.

- **Foreign keys = reference by ID**, with the human name shown alongside for readability —
  e.g. `A-014 (Show me the Design Tree)`.
- **Join tables are explicit.** `action-capability-map.md` is the Action ↔ Capability relation.
  Keep references normalized: a Query points at Action(s); capability linkage flows through the
  map — don't duplicate a capability FK onto the query.
- **Format by shape:** Markdown *tables* for narrow relations (roles, actions, the map, queries);
  *one record per entity* (heading + field bullets) for rich entities (capabilities, glossary).
- **Provenance:** tag entries carried from the frozen baseline with a `Source` (e.g.
  `Phase 4 §Item 3`), preserving the Phase 1 §4.6 provenance distinction inside a living table.
- **Integrity** is not auto-enforced in text. When it matters, add a validator in `workspace/`
  that checks every foreign key resolves — Verification Before Realization, without changing the
  source format.
