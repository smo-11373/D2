## Actions

*Grouped by role. Each action keeps a stable `A-` id (referenced by `action-capability-map.md` and `designer-queries.md`). Baseline-derived unless the Source says otherwise; Designer-stated actions are tagged with a date. Actions marked **position-derived** are elaborated from the role's job function under Human Position First (Phase 5), at Designer direction (2026-07-12), to cover the role's work — especially the D0 Operator.*

*Retired: **A-003** (Request investigation) — merged into **A-008** on 2026-07-12; id not reused.*

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-010 | Complete / clarify / expand D2's living working sets (glossary, query catalog, philosophy) | Phase 5 §Item 2 | Low-hurdle Designer-originated completion |
| A-011 | Revise D2's persistent working sets through the explicit D2 design process | Phase 3–5 | Working sets change only via explicit revision |
| A-061 | Review and adopt / reject D2 improvements proposed by the optional post-run D2 audit | Phase 3 §Item 5 | Governs D2's revision (Designer-originated completion authority); cf. A-020 (R-01 requests the audit) |

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
| A-060 | Establish the node's verification harness and derive design evidence *before* committing the design (observation / monitoring / health-visibility, representative inputs, expected outputs, evaluation cases) | Phase 2 §P4 (Verification Before Realization); Phase 5 §Item 1 (Harness First) | "Monitoring before usage"; distinct from passive study A-021 |

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
| A-059 | Monitor / observe D0 deployment health and status (standing, proactive) | Phase 5 §Item 3 | The operational-monitoring counterpart to A-038's health *settings*; distinct from reactive diagnosis A-049 |

### R-07 — D2 Assistant

*The non-human interaction point. Its actions deliver D2's support to the D1 Designer — they map to the D2 capabilities that serve R-01. (Whether these belong as R-07 role-actions or stay purely capability-level is a modelling call — flagged.)*

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-062 | Conduct the design on the Designer's behalf and answer his queries through the single interaction point | Phase 2 §P3; Phase 4 §Item 3 | The D2 Assistant's core function |
| A-063 | Interpret and route the Designer's input (direction, clarification, investigation, monitoring, intervention) to the right D2 function; preserve interaction context | Phase 2 §4.1–4.3 | D2 owns the routing burden |
| A-064 | Present Designer-oriented output — completion reports, Review Stops, Clarification Requests, human-readable summaries — with drill-down on request | Phase 1 §2.4; Phase 2 §3.2, §3.4; Phase 3 phase-wide rule | The reporting side of every item |
