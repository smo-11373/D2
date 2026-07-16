## Roles

*Positions are conceptual responsibility boundaries (Phase 5). "Relationship" = how the role relates to the D2 / D1 / D0 products. The **D1 Designer (R-01) is D2's primary and only user**; the **D2 Designer (R-00) builds D2** and is not a D2 user. See glossary: `d2-designer`, `d1-designer`, `designer`.*

| ID | Role | Relationship | Description | Source |
|------|------|--------------|-------------|--------|
| R-00 | D2 Designer | builds D2 | Builds the D2 product (currently the human developing D2). Not a user of D2; holds Designer-originated completion authority over D2's living sets. | Phase 5 (ref) |
| R-01 | D1 Designer | uses D2 → builds D1 | Primary & only user of D2. Uses D2's tools (setup defaults, design tree, design node modules) to build a D1 product (which wraps D0). This is Phase 1's "Designer" — the primary user of D2. | Phase 1 §2; Phase 5 §Item 3 |
| R-02 | Design Node Builder | internal to D2 | Builds a Design Node (a bounded design responsibility) under the D1 Designer's direction; a worker with a relatively narrow relevant skill set. Occupied by a D2 agent. | Phase 5 §Item 3 |
| R-03 | D1 Programmer | implements code | Changes product code according to implementation specifications (produces the D0 code inside the D1 product). | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | operates the D1 wrapper | Technical admin / IT manager of the delivered D1 product. Runs the D1 wrapper — deploys and upgrades D0 (running the smoke-test suite, keeping upgrade records), monitors D0 health, and changes governed tuning parameters — without changing product code. May deploy D0 into production while retaining D1. | Phase 5 §Item 3 |
| R-05 | D0 Operator | operates D0 | **D1's primary beneficiary** — D1 is built for the D0 Operator's convenience first and foremost. Runs the deployed D0 in production; routine operation and user-level monitoring; normally low understanding of technical norms. (Phase 6 Item 1's "D0 user.") | Phase 5 §Item 3; Designer 2026-07-12 |
| R-06 | D0 Technical Manager | supports D0 | Front-line technical support for a D0 deployment; installs and technically maintains it. | Phase 5 §Item 3 |
| R-07 | D2 Assistant | fronts D2 for the Designer | Non-human, LLM-based position: the **D1 Designer's single point of contact** with the entire D2 system (the unified D2 interaction point). Conducts the design on his behalf and answers his queries; he never addresses a Design Node, governing authority, or service directly. Intrinsic to the D2 ecosystem — not a Designer-configurable default. | Phase 4 §Item 3; Designer 2026-07-13 |

*D1 wraps D0: D0 is the core distributable; the thin D1 wrapper adds monitoring, upgrade smoke-tests, and upgrade records ("half a level above D0"). See glossary: `d0`, `d1`, `half-level`.*

*__Primary-user principle__ (self-similar): each layer's product exists primarily for its primary user — D2 for the D1 Designer (Phase 1); D1/D0 for the **D0 Operator** (Designer 2026-07-12). The D0 Operator's job functions are therefore covered thoroughly below.*

*Roles can **derive rules** ("position existence creates design consequences," Phase 5). E.g. **R-04 D1 Technical Manager** derives **RU-01** (no hard-coded numbers) — see `rules.md`.*

**Candidate roles (referenced but not yet confirmed):**

- **D1 system operator** — monitors D0 health from the D1 wrapper (~half a level above D0). Not among Phase 5's positions; likely folded into the D1 Technical Manager (R-04) or omitted.

> **Resolved — role layering (corrected).** R-00 **D2 Designer** builds D2; R-01 **D1 Designer** is D2's primary & only user and builds the D1 product (= Phase 1's "Designer"). Design Node Builder / D1 Programmer are internal to D2. See `../decisions/open-questions.md` and glossary.

