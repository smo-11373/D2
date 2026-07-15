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

## Actions

*Grouped by role. Each action keeps a stable `A-` id (referenced by `action-capability-map.md` and `designer-queries.md`). Baseline-derived unless the Source says otherwise; Designer-stated actions are tagged with a date. Actions marked **position-derived** are elaborated from the role's job function under Human Position First (Phase 5), at Designer direction (2026-07-12), to cover the role's work — especially the D0 Operator.*

*Retired: **A-003** (Request investigation) — merged into **A-008** on 2026-07-12; id not reused.*

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-010 | Complete / clarify / expand D2's living working sets (glossary, query catalog, philosophy) | Phase 5 §Item 2 | Low-hurdle Designer-originated completion |
| A-011 | Revise D2's persistent working sets through the explicit D2 design process | Phase 3–5 | Working sets change only via explicit revision |

### R-01 — D1 Designer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-012 | Confirm the Designer–D2 Operating Contract (relationship terms) | Phase 3 §Item 1 | Accept defaults or adjust; the contract is one item within the full setup package (A-016) |
| A-013 | Provide the initial design input (Predecessor D1 package + intended change) | Phase 3 §Item 2 | Any useful initial form; need not be complete |
| A-014 | Review the initial design understanding & direction | Phase 3 §Item 3 | A Review Stop |
| A-015 | Select a design posture (Standard / High Harness / Lean) | Phase 6 Item 1 §2 | One choice → many detailed settings |
| A-016 | Review / revise the Selected Setup Configuration Package | Phase 6 Item 1 §4 | Progressive disclosure; accept, compare, or revise |
| A-017 | Revise setup material later (governed) | Phase 6 Item 1 §8 | With impact analysis; history preserved |
| A-001 | Accept the proposed D1 Design Operating Framework | Phase 4 §Item 1 | Low-cost default response |
| A-002 | Modify selected parts of the framework | Phase 4 §Item 1 | |
| A-004 | Discuss a material concern | Phase 4 §Item 1 | Designer-initiated (→ C-20) |
| A-005 | Review a Design Node (e.g. approve / "continue") | Phase 4 §Item 2 | An event, distinct from revision authority |
| A-006 | Reserve or assign revision authority over a design object | Phase 4 §Item 2 | A continuing governance property |
| A-007 | Inquiry / inspection (explain, report, trace, show, compare design or process state) | Phase 4 §Item 3 | |
| A-008 | Investigation / concern (request D2 critically examine a matter or suspected problem and recommend action) | Phase 4 §Item 1, §Item 3 | Absorbs former A-003 (request investigation) |
| A-009 | Designer directive (impose, revise, reserve, suspend, or exercise authority) | Phase 4 §Item 3 | e.g. stop a branch, reserve approval |
| A-018 | Answer a Clarification Request | Phase 3/4; Phase 6 Item 2 §11 | Distinct from a Review Stop |
| A-019 | Tune resolution depth / intervention posture | Phase 2 §2.6 | Adjusts investigation depth vs attention cost |
| A-020 | Request / review an optional D2 audit after completion | Phase 3 §Item 5 | "Did D2 design D1 well?" |
| A-052 | Monitor design progress (advancement, changes since last review, revision counts) | Phase 4 §Item 3 | Active/standing monitoring subject; abstracted from the Item 3 query set |
| A-053 | Monitor resource & cost spend (time and cost, cumulative & per node) | Phase 4 §Item 3 | Active/standing monitoring subject |
| A-054 | Monitor design-process health & anomalies (abnormal behavior, rejection loops, high-impact open issues) | Phase 4 §Item 3 | Active/standing; investigation escalates via A-008 |
| A-055 | Evaluate D2 and decide whether to adopt it for this design (adopt / decline / defer) | Phase 1; Phase 2 | Entry-point decision; the choice is the Designer's, D2 supports it by orientation |
| A-056 | Review and adjust the roles table (the cast of roles for this project) | Phase 5 §Item 3; Phase 6 setup | Accept defaults or tailor; intrinsic roles fixed, default (product-side) roles changeable |
| A-057 | Review and confirm the D1 foundational documents (the D1 Constitution) | Phase 3 §Item 3; Phase 4 §Item 1 | A key, strongly-encouraged Review Stop; the Constitution is Designer-governed (C-17) |
| A-058 | Evaluate a proposed change before formalizing it (impact dry-run — probe up & down, get a report) | Designer 2026-07-15 | Separate command from the official proposal (RU-06); precedes upward proposal A-027 |

### R-02 — Design Node Builder

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-021 | Investigate relevant predecessor & reference material | Phase 6 Item 2 §4 | Enters via the Predecessor Reference Roadmap |
| A-022 | Develop, compare, and critique candidate design choices | Phase 6 Item 2 §5 | Bounded local autonomy under the harness |
| A-023 | Produce the Node Design Specification / design result | Phase 4 §Item 2; Phase 6 Item 2 §5 | |
| A-024 | Internally evaluate the result before submission | Phase 6 Item 2 §6 | "Submission is not the first evaluation" |
| A-025 | Submit the design result for acceptance | Phase 6 Item 2 §7 | Submission ≠ acceptance |
| A-026 | Propose a spawning strategy (descendant responsibilities) | Phase 4 §Item 2; Phase 6 Item 2 §14 | Spawning ≠ advancement |
| A-027 | Propose upward revision of governing design | Phase 4 §Item 2 | Routed by the affected node's revision authority |

### R-03 — D1 Programmer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-028 | Implement product (D0) code from the implementation specification | Phase 5 §Item 3 | Should not need to reconstruct the design |
| A-040 | Write and run implementation-level tests against the code | position-derived | |
| A-041 | Diagnose and fix implementation defects (code changes within the spec) | position-derived | |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-029 | Adjust a governed product parameter without changing code | Phase 5 §Item 3 | Derives **RU-01** (`rules.md`) |
| A-030 | Run the upgrade validation / regression (smoke-test) harness | Phase 5 §Item 3 | "No code change ≠ no harness"; D1-wrapper suite |
| A-031 | Update release state, repackage, and distribute the product | Phase 5 §Item 3 | |
| A-032 | Deploy D0 into production (optionally retaining D1) | Designer 2026-07-12 | Designer-stated, not baseline |
| A-033 | Monitor D0 health & performance via the D1 wrapper | Designer 2026-07-12 | ~half a level above D0 |
| A-042 | Roll back to a previous release on a failed upgrade | position-derived | Uses the D1-wrapper upgrade record |
| A-043 | Review upgrade records / release history | position-derived | D1-wrapper |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-034 | Perform routine operation — start, run, stop, schedule, pause/resume, or cancel D0 jobs | Phase 5 §Item 3 | Normally low technical understanding |
| A-035 | Perform routine user-level monitoring — observe whether D0 is working and healthy | Phase 5 §Item 3 | |
| A-036 | Set operator-level controls (spending limits, scheduling, collection scope, approved operating choices) | Phase 5 §Item 3 | Position-oriented configuration |
| A-044 | View D0 results, outputs, and reports | position-derived | The point of running D0 |
| A-045 | Acknowledge and respond to notifications, prompts, or routine approvals from D0 | position-derived | Simple, non-technical decisions |
| A-046 | Handle routine, non-technical error conditions (retry / restart within competence) | position-derived | Escalates beyond competence via A-048 |
| A-047 | View routine activity, usage, and cost-to-date (operator-level status) | Phase 5 §Item 3; Phase 6 Item 3 | Uses observation data |
| A-048 | Request front-line technical support / escalate a problem to the D0 Technical Manager (R-06) | position-derived | Low-technical operator's escape hatch |

### R-06 — D0 Technical Manager

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-037 | Install a D0 deployment | Phase 5 §Item 3 | |
| A-038 | Technically maintain a D0 deployment (deployment paths, storage endpoints, service config, resource limits, credentials, health settings) | Phase 5 §Item 3 | Position-oriented configuration |
| A-039 | Provide front-line technical support | Phase 5 §Item 3; Designer 2026-07-12 | Serves the D0 Operator (A-048) |
| A-049 | Diagnose a D0 deployment issue | position-derived | |
| A-050 | Apply a fix, patch, or configuration change to a deployment | position-derived | Within established design; no product redesign |
| A-051 | Escalate to the D1 Technical Manager (R-04) when a problem exceeds front-line support | position-derived | |
