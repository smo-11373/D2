# Role–Action Catalog

*Living. Roles / positions and the actions each performs — the top of the Phase 6 hierarchy (Role → Action → Capability). Intentionally open and expandable. See `README.md` for ID conventions.*

## Roles

*Positions are conceptual responsibility boundaries (Phase 5). "Layer" = which of D2 / D1 / D0 the position primarily belongs to.*
*__Naming convention:__ a `Dn Designer` operates `Dn` to design `D(n-1)` — so the D2 Designer (R-01) designs D1; the D1 Designer (R-02) designs D0.*

| ID | Role | Layer | Description | Source |
|------|------|-------|-------------|--------|
| R-01 | D2 Designer | D2 | Primary user of D2; operates D2 to direct the evolution of an existing D1 system into an upgraded successor, and retains effective design authority over D1. Same entity Phase 5 calls "the D2 Designer." | Phase 1 §2 |
| R-02 | D1 Designer | D1 | Changes what the product (D0) is designed to be — operates D1 to design the D0 product. | Phase 5 §Item 3 |
| R-03 | Design Node Builder | D1 | Performs a bounded design responsibility (a Design Node); a worker with a relatively narrow relevant skill set operating within a clear governing contract and boundary. | Phase 5 §Item 3 |
| R-04 | D1 Programmer | D1 | Changes product code according to implementation specifications. | Phase 5 §Item 3 |
| R-05 | D1 Technical Manager | D1 | Maintains and upgrades the technical product package within the established design, without changing product code. | Phase 5 §Item 3 |
| R-06 | D0 Technical Manager | D0 | Installs and technically maintains a particular D0 deployment. | Phase 5 §Item 3 |
| R-07 | D0 Operator | D0 | Performs routine operation and routine user-level monitoring. | Phase 5 §Item 3 |

**Candidate roles (referenced but not yet confirmed):**

- **D0 User** — the end user of the D0 product. Referenced by Phase 6 Item 1 ("D0 user priorities," "user skill level") but not among Phase 5's enumerated positions; may or may not be distinct from the D0 Operator.
- **Internal conceptual positions** — D2-internal positions (the handoff lists this as a role category). Not yet enumerated; Phase 5 notes that agents may later occupy positions.

> **Resolved — "Designer" is now layer-qualified.** R-01 is the **D2 Designer** (Phase 1's "Designer" = Phase 5's "the D2 Designer"); R-02 the **D1 Designer** is a distinct lower-layer role. See glossary: `d2-designer`, `d1-designer`.

## Actions

*All seeded actions are performed by R-01 (the D2 Designer), from the frozen Phase 4 baseline.*

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
