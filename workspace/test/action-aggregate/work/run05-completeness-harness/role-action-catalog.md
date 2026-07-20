# Role–Action Aggregate Catalog

*Product 1 of the Action-Aggregate node (contract §1.1). The actions each recognized role performs,
merged, grouped by role, stable IDs, each row Source-cited, each row substantially described. Target
= the common, anticipable (open-list) set. Derived from the frozen inputs (constitution Phases 1–5 +
method §1 + rules `RU-*` + glossary + framework); nothing invented.*

*Notes-column tags: **[P]** passive / **[A]** active (D1 Designer split, method §1); depth-frame facet
`operate · monitor · configure · view · handle-errors · escalate` (+ `diagnose→fix→recover→record` for
maintenance) for operational roles; **[H]** = harness facet (Harness First, Phase 5 Item 1 — test /
monitor / detect-hidden-errors / make-failures-visible). `A-003` retired — skipped.*

## Roles

| ID | Role | Relationship | Description | Source |
|---|---|---|---|---|
| R-00 | D2 Designer | Intrinsic · meta / D2-builder | Builds and maintains the **D2** product (the design system: setup defaults, design tree, design-node modules, tools). Not a user of D2; holds Designer-originated completion/clarification authority over D2's own living working sets. Fixed to the ecosystem. | glossary `d2-designer`; Phase 5 §Item 3; method §1 |
| R-01 | D1 Designer | Intrinsic · D1 layer (primary user) | The **primary and only user of D2**. Directs the evolution of a Predecessor D1 into a materially revised successor D1; supplies incremental intent, retains effective design authority, and holds scarce attention D2 must conserve. Phase 1's "Designer." | glossary `d1-designer`; Phase 1 §2; Phase 5 §Item 3 |
| R-02 | Design Node Builder | Intrinsic · D2 design mechanism | The conceptual position (a self-contained agent) that **builds a Design Node** under a governing contract: investigates, designs, checks/tests, submits, enforces its data's rules, and may spawn children. Works largely within its bounded sandbox. | Phase 5 §Item 3; Phase 4 §Item 2; glossary `design-node` |
| R-03 | D1 Programmer | Default · D1 layer (implementation) | Changes **product code according to implementation specifications**. Ideally implements a completed design without reconstructing the earlier design process. Present by default where the change requires code. | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | Default · D1 layer (product maintenance) | **Maintains and upgrades the technical product package within the established design, without changing product code** — governed product parameters, packaging, release. Default position D2 provides; the Designer may reconfigure. | Phase 5 §Item 3; RU-01; glossary `d1` |
| R-05 | D0 Operator | Default · D0 layer (operation) | **Performs routine operation and routine user-level monitoring** of a running D0 product, within approved operating choices. Default cast member for the distributable product. | Phase 5 §Item 3; glossary `d0`; glossary `user` |
| R-06 | D0 Technical Manager | Default · D0 layer (deployment) | **Installs and technically maintains a particular D0 deployment**; provides front-line support for it. Default cast member the Designer may reconfigure per project. | Phase 5 §Item 3; glossary `d0`; glossary `d1` |

*Intrinsic/default tag (glossary `role`): the two human authorities (D2 Designer, D1 Designer) and
D2's own design mechanism (Design Node Builder) are **intrinsic** — structurally fixed to the
ecosystem; the D1/D0 cast (Programmer, D1/D0 Technical Managers, D0 Operator) are **defaults** D2
provides in the project's role table and the D1 Designer may change/merge/omit/map-to-agents (Phase 5
Item 3 — "one agent to one position, one agent to several positions"). IDs fixed by the inputs: R-00,
R-01 (glossary `d2-designer`/`d1-designer`), R-04 (RU-01), R-05, R-06 (glossary `d0`); R-02, R-03
placed in design→implementation layer order.*

## Actions

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-001 | Build and maintain the D2 product — setup defaults, design tree, design-node modules, and other tools the D1 Designer uses to build D1. | glossary `d2`, `d2-designer` | Core function |
| A-002 | Perform Designer-originated completion / clarification / expansion of D2's intentionally-open living sets (glossary, query catalog, Phase 5 itself). | Phase 5 §Item 2 | Lower-hurdle amendment |
| A-004 | Author and derive D2's governing rules from the principles ("derived, not invented"; able to explain the quality concern each protects). | rules.md preamble; Phase 5 §Item 4 | — |
| A-005 | Hold and exercise approval authority over material revision of Designer-governed D2 design. | Phase 5 §Item 2; Phase 4 §Item 2 | Designer-governed node |
| A-006 | Audit whether D2 designed D1 well — review process cost / time / Designer Attention Cost and adopt candidate D2 improvements (never silent). | Phase 3 §Item 5 | [H] process audit |

### R-01 — D1 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-007 | Decide whether to use D2 for the intended D1 upgrade (the entry-point decision). | method §1; Phase 1 §3 | [P] entry |
| A-008 | Review and confirm the Designer–D2 operating contract — how D2 will seek intervention and how he will observe/intervene; normally accept the provided defaults. | Phase 3 §Item 1 | [P] |
| A-009 | Establish the initial design input — supply the Predecessor D1 package and the (incremental, loosely-structured) expression of intended change. | Phase 3 §Item 2; Phase 1 §4 | [P] |
| A-010 | Establish/confirm the roles table (the cast, each intrinsic or a changeable default) and the run's default design posture, in one setup step. | method §1; Phase 3 §Item 1–2 | [P] setup |
| A-011 | Review the consolidated initial design understanding and proposed direction at the default Review Stop (review now, or continue). | Phase 3 §Item 3 | [P] Review Stop |
| A-012 | Acknowledge D2's notification that setup is complete and D1 design mode is entered. | Phase 3 §Item 4 | [P] |
| A-013 | Review and confirm the proposed D1 Design Operating Framework (skeleton, inherited/derived rules, control points) — accept, modify, or discuss. | Phase 4 §Item 1 | [P] |
| A-014 | Confirm the D1 foundational documents / D1 Constitution at the strongly-encouraged key Review Stop. | method §1; Phase 4 §Item 2 | [P] high node |
| A-015 | Answer D2's consolidated Clarification Requests — supply the material design judgment D2 cannot resolve by further investigation. | Phase 3 phase-wide rule; Phase 4 §Item 2 | [P] |
| A-016 | Review Design Node reports at Review Stops, with attention scaled to node height (higher nodes get more). | Phase 4 §Item 2 | [P] |
| A-017 | Set each node's revision authority — D2-governed vs Designer-governed — by level/class default, attending mainly to recommended exceptions. | Phase 4 §Item 2 | [P] |
| A-018 | Approve or reject a node's submission package and its justification (submission ≠ acceptance). | RU-02; Phase 4 §Item 2 | [P] |
| A-019 | Rule on upward revision proposals routed to him for Designer-governed nodes (preventing silent revision, not upward feedback). | Phase 4 §Item 2; RU-04; RU-05 | [P] |
| A-020 | Inspect / inquire into the emerging D0 design and ongoing D1 process through the unified interaction point — ask, show, trace, drill down, compare — in natural language. | Phase 4 §Item 3; Phase 2 §Principle 3 | [A] |
| A-021 | Monitor D1 design progress — elapsed time and cost consumed, overall and per node. | Phase 4 §Item 3 | [A] |
| A-022 | Monitor D1 design-process health and detect abnormal process behavior (design health report; "are any parts behaving abnormally?"). | Phase 4 §Item 3; Phase 2 §3.1 | [A][H] |
| A-023 | Investigate a suspected design or process problem — move from high-level observation to deeper investigation before deciding whether/how to intervene. | Phase 2 §3.4; Phase 4 §Item 3 | [A][H] |
| A-024 | Issue Designer directives — impose or revise a rule, reserve approval authority over an object, suspend or stop a branch. | Phase 4 §Item 3 | [A] authority |
| A-025 | Redirect the design — lay down a high-level governing principle, invariant, or tradeoff that governs many lower decisions. | Phase 1 §2.5; Phase 4 §Item 3; method §1 | [A] |
| A-026 | Hold D0-user optimization in view as a standing consideration and direct the D1 design toward D0-user priorities / skill level. | method §1 (D0-user throughline); Phase 5 §Item 3 | [A] standing |
| A-027 | Evaluate a proposed change before formally proposing it — a separate dry-run that commits nothing, probing up and down. | RU-06 | [A] |
| A-028 | Request an optional D2-level audit of the completed design process (checking how well D2 served him — cost, time, attention). | Phase 3 §Item 5; method §1 | [A][H] |

### R-02 — Design Node Builder

| ID | Action | Source | Notes |
|---|---|---|---|
| A-029 | Receive the governing node contract and work within its bounded sandbox (responsibility, inputs, constraints, permitted actions, expected outputs). | Phase 4 §Item 2; Phase 5 §Item 5; RU-04; RU-08 | Strong boundary, local autonomy |
| A-030 | Investigate autonomously — study the Predecessor D1, provided inputs, and reference material; resolve material uncertainty before escalating. | Phase 4 §Item 2; Phase 2 §2.1 | [H] investigate |
| A-031 | Develop candidate design(s) through the node's internal design and governance process. | Phase 4 §Item 2 | — |
| A-032 | Produce the proposed Node Design Specification (or equivalent node result). | Phase 4 §Item 2 | Deliverable |
| A-033 | Check, test, and verify the node's design internally against its harness before advancing (verification before realization). | Phase 4 §Item 2; Phase 2 §Principle 4; Phase 5 §Item 1 | [H] |
| A-034 | Enforce the rules its own data specifies (a node holds its data, has authority over it, and enforces its rules). | glossary `design-node`; Phase 4 §Item 2 | — |
| A-035 | Accumulate high-leverage questions and raise a consolidated Clarification Request when material Designer judgment is needed. | Phase 4 §Item 2; Phase 2 §Principle 1 | [P]-facing |
| A-036 | Author the node's justification and submit the submission package upward for the parent's acceptance. | RU-02; glossary `submission-package` | — |
| A-037 | Propose a spawning strategy and spawn child nodes, driven by the relevant Designer's potential actions (passive first, active deferred). | Phase 4 §Item 2; RU-03; RU-10 | — |
| A-038 | Decompose the work internally to any depth and merge the child pieces into the single contracted aggregate at its boundary. | RU-10 | Aggregate always |
| A-039 | Run the acceptance self-check on its own deliverable — conformance (gating) then completeness — before spawning dependents. | conformance.md; design-node-algorithm §4 | [H] self-check |
| A-040 | Propose changes to inherited (ancestor-owned) data upward and stop until resolved (an open upward proposal is a stopping point; no drift). | RU-04; RU-05 | — |
| A-041 | Communicate only with its immediate parent or child (adjacency); reach farther nodes by relaying level by level. | RU-07 | — |
| A-042 | Revise the node and re-submit in response to a parent's request-down (the author makes the change). | RU-09; Phase 4 §Item 2 | — |

### R-03 — D1 Programmer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-043 | Read and consult the implementation specification and design intent, implementing without reconstructing the earlier design process. | Phase 5 §Item 3 (design-to-programming handoff) | view/consult |
| A-044 | Implement product code according to the implementation specification (realize the understood design into working D0). | Phase 5 §Item 3; Phase 2 §5.3 | operate/perform |
| A-045 | Test and verify the implementation against the specification's harness to confirm it satisfies the constrained behavior. | Phase 2 §Principle 4; Phase 5 §Item 1 | monitor · [H] |
| A-046 | Diagnose and fix implementation defects surfaced by tests (make failures visible, then correct). | Phase 5 §Item 1; Phase 2 §Principle 4 | handle-errors · [H] |
| A-047 | Raise an upward proposal / clarification when the specification is insufficient or reveals a design defect (lower nodes may challenge higher design). | Phase 4 §Item 2; Phase 2 §2 | escalate |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-048 | Diagnose whether a required change is governable at the product-parameter level within the established design (perform at the lowest position with the authority). | Phase 5 §Item 3 (position hierarchy) | diagnose |
| A-049 | Upgrade the D0 product package within the established design without changing product code. | Phase 5 §Item 3 | operate/perform |
| A-050 | Adjust governed product parameters — product/provider defaults, retry policy within accepted ranges, feature-policy choices, resource profiles, release/packaging parameters. | Phase 5 §Item 3; RU-01 | configure |
| A-051 | Run the required validation / regression harness (the D1 wrapper's upgrade smoke-test suite) after a change — "no code change does not mean no harness." | Phase 5 §Item 3; RU-01; glossary `d1` | monitor/verify · [H] |
| A-052 | Update release state, repackage, and distribute the upgraded product. | Phase 5 §Item 3 | apply-fix |
| A-053 | Maintain upgrade records for the package. | glossary `d1` | record |
| A-054 | Recover / roll back from a failed upgrade (restore prior release state when the regression harness fails). | Phase 5 §Item 3; RU-01 | recover · [H] |
| A-055 | Escalate to the D1 Programmer / Designer when a required change needs code change or substantive redesign (beyond the established design). | Phase 5 §Item 3 (position hierarchy) | escalate |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|---|---|---|---|
| A-056 | Perform routine operation of the running D0 product within approved operating choices. | Phase 5 §Item 3 | operate/perform |
| A-057 | Perform routine user-level monitoring of D0 health and status. | Phase 5 §Item 3; glossary `user` | monitor · [H] |
| A-058 | Set approved operating choices — daily spending limits, routine scheduling, collection scope. | Phase 5 §Item 3 | configure |
| A-059 | View the D0 health report as represented at the operator's level ("what will the D0 health report look like to the user?"). | Phase 4 §Item 3; Phase 5 §Item 3 | view · [H] |
| A-060 | Handle routine operational errors within the approved operating choices. | Phase 5 §Item 3 | handle-errors · [H] |
| A-061 | Escalate a fault beyond routine operation to the D0 Technical Manager (front-line support). | Phase 5 §Item 3; glossary `d0` | escalate |

### R-06 — D0 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-062 | Install and deploy a particular D0 deployment into production (an IT manager may deploy just D0, retaining D1 to manage it). | Phase 5 §Item 3; glossary `d1` | operate/perform |
| A-063 | Configure the deployment — deployment paths, storage endpoints, service configuration, resource limits, credential integration, deployment health settings. | Phase 5 §Item 3 | configure |
| A-064 | Monitor deployment health per the deployment-health settings, including D0-crash detection. | Phase 5 §Item 3; glossary `d1` | monitor · [H] |
| A-065 | View the specific deployment's health/status surface (the same event represented for this position). | Phase 5 §Item 3; Phase 4 §Item 3 | view · [H] |
| A-066 | Technically maintain the deployment — diagnose and resolve deployment faults as front-line support. | Phase 5 §Item 3; glossary `d0` | diagnose/fix · [H] |
| A-067 | Recover the deployment from a failure (e.g. crash recovery flagged by crash detection). | glossary `d1`; Phase 5 §Item 3 | recover · [H] |
| A-068 | Escalate a fault requiring product-level change or upgrade to the D1 Technical Manager (position hierarchy). | Phase 5 §Item 3 | escalate |
