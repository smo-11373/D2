# Role–Action Catalog

*Living. Roles / positions and the actions each performs — the top of the Phase 6 hierarchy (Role → Action → Capability). Intentionally open and expandable. See `README.md` for ID conventions.*

## Roles

*Positions are conceptual responsibility boundaries (Phase 5). "Relationship" = how the role relates to the D2 / D1 / D0 products. The **D1 Designer (R-01) is D2's primary and only user**; the **D2 Designer (R-00) builds D2** and is not a D2 user. See glossary: `d2-designer`, `d1-designer`, `designer`.*

| ID | Role | Relationship | Description | Source |
|------|------|--------------|-------------|--------|
| R-00 | D2 Designer | builds D2 | Builds the D2 product (currently the human developing D2). Not a user of D2; holds Designer-originated completion authority over D2's living sets. | Phase 5 (ref) |
| R-01 | D1 Designer | uses D2 → builds D1 | Primary & only user of D2. Uses D2's tools (setup defaults, design tree, design node modules) to build a D1 product (which wraps D0). This is Phase 1's "Designer" — the primary user of D2. | Phase 1 §2; Phase 5 §Item 3 |
| R-02 | Design Node Builder | internal to D2 | Builds a Design Node (a bounded design responsibility) under the D1 Designer's direction; a worker with a relatively narrow relevant skill set. Occupied by a D2 agent. | Phase 5 §Item 3 |
| R-03 | D1 Programmer | implements code | Changes product code according to implementation specifications (produces the D0 code inside the D1 product). | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | maintains D1 | Technical admin of the delivered D1 product: maintains and upgrades it and changes governed tuning parameters, without changing product code. | Phase 5 §Item 3 |
| R-05 | D0 Operator | operates D0 | Runs D0; routine operation and user-level monitoring; normally low understanding of technical norms. (Phase 6 Item 1's "D0 user.") | Phase 5 §Item 3 |
| R-06 | D0 Technical Manager | supports D0 | Front-line technical support for a D0 deployment; installs and technically maintains it. | Phase 5 §Item 3 |

**Candidate roles (referenced but not yet confirmed):**

- **D1 system operator** — monitors the delivered D1 system. Not among Phase 5's positions; the D2 Designer noted it may likely be omitted.

> **Resolved — role layering (corrected).** R-00 **D2 Designer** builds D2; R-01 **D1 Designer** is D2's primary & only user and builds the D1 product (= Phase 1's "Designer"). Design Node Builder / D1 Programmer are internal to D2. See `../decisions/open-questions.md` and glossary.

## Actions

*All seeded actions are performed by R-01 (the D1 Designer) — Phase 4's "Designer" is the primary user of D2 — from the frozen Phase 4 baseline.*

| ID | Action | Role(s) | Source | Notes |
|-------|--------|---------|--------|-------|
| A-001 | Accept the proposed D1 Design Operating Framework | R-01 | Phase 4 §Item 1 | Low-cost default response |
| A-002 | Modify selected parts of the framework | R-01 | Phase 4 §Item 1 | |
| A-003 | Request investigation | R-01 | Phase 4 §Item 1 | Possible overlap with A-008 — see `../decisions/open-questions.md` |
| A-004 | Discuss a material concern | R-01 | Phase 4 §Item 1 | |
| A-005 | Review a Design Node (e.g. approve / "continue") | R-01 | Phase 4 §Item 2 | An event, distinct from revision authority |
| A-006 | Reserve or assign revision authority over a design object | R-01 | Phase 4 §Item 2 | A continuing governance property |
| A-007 | Inquiry / inspection (explain, report, trace, show, compare design or process state) | R-01 | Phase 4 §Item 3 | |
| A-008 | Investigation / concern (critically examine a suspected problem; recommend action) | R-01 | Phase 4 §Item 3 | |
| A-009 | Designer directive (impose, revise, reserve, suspend, or exercise authority) | R-01 | Phase 4 §Item 3 | e.g. stop a branch, reserve approval |
