# Role–Action Aggregate Table

*Derived, not invented, from the frozen inputs: constitution (Phases 1–5), the Designer-originated
completions, method §1, and the rules `RU-*`. Every row cites an in-namespace `Source` (see
`environment/sources.md`). Roles ordered by layer (D2 → D1 → D0); actions `A-001…` with `A-003`
retired (skipped). Grouped by role, merged, deduplicated at the fundamentals' own granularity.*

## Roles

| ID | Role | Relationship | Description | Source |
|---|---|---|---|---|
| R-00 | D2 Designer | intrinsic | The human who builds the **D2** product and holds Designer-originated completion/clarification authority over D2's living working sets. Not a user of D2. Its authority and attention are the top priority the whole ecosystem serves. | glossary `d2-designer`; Phase 1 §2; Phase 5 §Item 2 |
| R-01 | D1 Designer | intrinsic | The **primary and only user of D2** ("Designer" in the baseline). Uses D2's tools to direct the evolution of a Predecessor D1 into a materially revised successor D1 (which wraps D0). Retains effective design authority; his attention is a scarce primary resource. | glossary `d1-designer`; Phase 1 §2; Phase 5 §Item 3 |
| R-02 | Design Node Builder | intrinsic | The D2 position that builds the current Design Node — investigates, designs, checks, tests, submits, enforces, and revises within its governing contract, and proposes a spawning strategy. Treated as a bounded worker with a narrow relevant skill set. | Phase 5 §Item 3; Phase 4 §Item 2; glossary `design-node` |
| R-03 | D1 Programmer | default | Changes product code according to the implementation specifications the D1 Designer produces; realizes an understood design rather than discovering it through coding. | Phase 5 §Item 3; Phase 2 §Principle 5 |
| R-04 | D1 Technical Manager | default | Maintains and upgrades the technical product package within the established design **without changing product code** — adjusting governed parameters, running the required harness, and re-releasing. | Phase 5 §Item 3; RU-01; glossary `d1` |
| R-05 | D0 Operator | default | Performs routine operation and routine user-level monitoring of a deployed D0 product; front-line handler of routine operating conditions. | Phase 5 §Item 3; glossary `d0` |
| R-06 | D0 Technical Manager | default | Installs and technically maintains a particular D0 deployment; provides front-line support to the D0 Operator; owns deployment-level configuration and health. | Phase 5 §Item 3; glossary `d0`, `d1` |
| R-07 | D2 Assistant | intrinsic | The D1 Designer's single, unified point of contact with the entire D2 system — a Human-Position-First position occupied by a D2 agent. Conducts the design on the Designer's behalf, interprets/routes his input, preserves context, and presents his output. | completions.md C-2026-07-19-1; Phase 2 §Principle 3 |

## Actions

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-001 | Direct the material design of D2 and retain effective design authority over its evolution | Phase 1 §2.2 | Authority + attention are the top priority; approval of many machine decisions is not effective authority. |
| A-002 | Originate completion, clarification, and expansion of D2's intentionally-open living sets (glossary, query catalog, Phase 5) at a low hurdle | Phase 5 §Item 2 | Distinct from bottom-up revision; permitted when consistent with established design. Governs alongside the frozen baseline (see completions.md). |
| A-004 | Create, revise, supersede, or retire Designer rules for D2 (Designer-permission-gated) | Phase 4 §Item 2 | Designer rules require Designer permission for material creation/revision/supersession/retirement. |
| A-005 | Review and approve or reject upward revision proposals affecting Designer-governed D2 design | Phase 4 §Item 2 | Designer control prevents silent revision, not upward feedback; farther-up proposals face a higher hurdle (Phase 5 §Item 2). |

### R-01 — D1 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-006 | Decide whether to use D2 for the project (the entry point) | method §1 | [P] First decision; D2 backs it by orienting him with the concepts it needs. |
| A-007 | Review and confirm the Designer–D2 Operating Contract (intervention posture and defaults) | Phase 3 §Item 1 | [P] Compact, human-oriented; normal action is to accept the defaults. Covers both D2-initiated and Designer-initiated intervention. |
| A-008 | Establish the initial design input — the Predecessor D1 package and the intended incremental change | Phase 3 §Item 2 | [P] Change may be rough/loosely structured; full specification not required. |
| A-009 | Confirm the roles table and the run's design posture (the setup step) | method §1 | [P] Establishes the cast of roles (each intrinsic or a Designer-changeable default) and default design choices in one setup step. |
| A-010 | Review the consolidated initial design understanding and recommended direction at the Review Stop | Phase 3 §Item 3 | [P] A courtesy/control boundary, not an assertion of unresolved questions. |
| A-011 | Confirm the D1 foundational documents (the D1 Constitution) at the key Review Stop | method §1; Phase 4 §Item 1 | [P] Combines the setup skeleton, the predecessor V1, and the intended change; a Constitution node is a natural Review Stop. |
| A-012 | Review and confirm the D1 Design Operating Framework | Phase 4 §Item 1 | [P] One consolidated package: "here is how I propose to conduct this D1 design." Normal action stays low-cost. |
| A-013 | Set/confirm each node's revision-authority status (Designer-governed vs D2-governed) via framework defaults | Phase 4 §Item 2 | [P] Review (an event) is distinct from revision authority (a continuing property); framework supplies defaults by level/class. |
| A-014 | Review proposed Design Node results at Review Stops scaled to node significance | Phase 4 §Item 2 | [P] Designer attention should generally increase with node height. |
| A-015 | Respond to consolidated high-leverage Clarification Requests (supply material judgment D2 cannot resolve) | Phase 4 §Item 2; Phase 1 §2.5 | [P] Preferentially a high-level principle/invariant/tradeoff governing many lower decisions — being asked only when it is worth it. |
| A-016 | Inspect and progressively drill into the emerging D0 design, D1 process state, and the Design Tree (ask, show, trace, compare, view changes) | Phase 4 §Item 3 | [A] Natural-language requests via the unified interaction point; move from observation toward detail before deciding to intervene (Phase 2 §3.4). |
| A-017 | Monitor D1 design-process progress and time consumption | Phase 4 §Item 3 | [A] "How much time has D1 design consumed / which nodes consumed the most." Distinct from cost and health. |
| A-018 | Monitor D1 design-process cost / spend | Phase 4 §Item 3 | [A] "How much has the design process cost." Preserved distinct from time and health per the fundamentals' own queries. |
| A-019 | Monitor D1 design-process health and detect abnormal process behavior | Phase 4 §Item 3; Phase 2 §Principle 2 | [A] "Current D1 design health report / anything behaving abnormally / most-revised nodes." Harness-richness: make process health visible. |
| A-020 | Critically investigate a suspected design or process problem and obtain a recommendation | Phase 4 §Item 3; Phase 2 §Principle 3 | [A] Skeptical investigation of potential flaws/hidden assumptions/failure conditions; distinct from routine inquiry. |
| A-021 | Issue Designer directives — impose or reserve a rule, reserve approval authority, suspend or stop a branch | Phase 4 §Item 3 | [A] Authority actions recognized and applied promptly (e.g. "do not change Algorithm A without my approval"; "stop implementation branches"). |
| A-022 | Propose and drive a material design change (Designer-initiated), evaluated before it is officially proposed | RU-06; Phase 4 §Item 3 | [A] Usually after discussion; evaluation is a separate step that commits nothing (RU-06). Intervention normally initiates investigation, not direct mutation. |
| A-023 | Tune the resolution / intervention depth to manage his attention budget | Phase 2 §Principle 1 (2.6) | [A] The intention lens: manage attention cost → adjust the balance of investigate / infer / intervene / defer without removing D2's obligation to surface material uncertainty. |
| A-024 | Hold D0-user optimization as a standing design priority that shapes what D1 must do | method §1; Phase 5 §Item 3 | [A] The D0-user throughline cutting across passive and active involvement (Human Position First). |
| A-025 | Audit the D2 design process after a completed run (process cost, attention cost, improvement points) | Phase 3 §Item 5 | [A] Checking how well D2 served him; distinct from D1 review. May propose D2 improvements but must not silently modify D2 working sets. |

### R-02 — Design Node Builder

| ID | Action | Source | Notes |
|---|---|---|---|
| A-026 | Receive and work within the node's governing contract in a sandboxed local environment | Phase 4 §Item 2; RU-08 | Compiled governing contract with curated read-only input links to ancestors/siblings; strong boundary, local autonomy (Phase 5 §Item 5). |
| A-027 | Autonomously investigate the Predecessor D1, Designer material, and reference resources before escalating | Phase 2 §Principle 1; Phase 1 §4.5 | Investigate-before-escalating bias; dig deeper when it may materially resolve an uncertainty. |
| A-028 | Develop candidate designs and evaluate alternatives and consequences | Phase 4 §Item 2; Phase 1 §2.2 | Forms proposals, evaluates alternatives, resolves routine questions within its authority. |
| A-029 | Produce the proposed Node Design Specification (or equivalent node result) | Phase 4 §Item 2 | The contracted deliverable the node must return (RU-10). |
| A-030 | Establish the node's verification harness and test the design | Phase 5 §Item 1; Phase 2 §Principle 4 | Harness First / Verification Before Realization: constrain and make deviation visible before expanding the design space. Harness-richness bias applied to the Builder. |
| A-031 | Check the deliverable's conformance to the governing layer before spawning children | framework `conformance`; design-node-algorithm | Conformance is checked first and gating, staged at each internal boundary; distinct from citing a Source. |
| A-032 | Author the node's justification and submit the result upward for parent acceptance | RU-02 | Justification travels with the submission package; submission is not acceptance — the parent, as enforcer, approves or rejects. |
| A-033 | Accumulate and prepare consolidated high-leverage Clarification Requests when material Designer judgment is needed | Phase 4 §Item 2; Phase 1 §2.5 | Consolidate to concentrate Designer attention at high abstraction. |
| A-034 | Propose a spawning strategy and spawn child nodes driven by the relevant actions (passive-action spawning first) | RU-03; Phase 4 §Item 2 | Spawning is distinct from general design advancement; active-action spawning is deferred. |
| A-035 | Propose upward revision to governing design — evaluate first, then halt on an open proposal | RU-06; RU-04; RU-05 | Lower nodes may challenge higher design; an open upward proposal is a stopping point (no drift). |
| A-036 | Own and maintain the node's data and enforce the rules that data specifies | glossary `design-node` | Minimal node duties: hold own data, have authority over it, enforce its rules; a table is changed only through its author (RU-09). |

### R-03 — D1 Programmer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-037 | Implement the product code from the D1 Designer's implementation specification | Phase 5 §Item 3 | The design-to-programming handoff aims for a spec complete enough to implement without reconstructing the design process. |
| A-038 | Realize an understood design rather than discovering fundamental design through coding | Phase 2 §Principle 5 (5.3) | Implementation should primarily realize an understood design; implementation sketch permitted only to discover what is observable/testable. |
| A-039 | Build and run implementation-level tests / the verification harness | Phase 5 §Item 1; Phase 2 §Principle 4 | Harness-richness bias at the implementation layer; move failure discovery as early as practical. |
| A-040 | Detect, diagnose, and fix implementation defects surfaced by the harness | Phase 5 §Item 3 | Depth-frame: handle routine errors → diagnose → apply-fix. |
| A-041 | Package the implemented product for delivery | glossary `d1`; design-node-algorithm | Lifecycle-forced (implement → test → package); the package precedes install/deploy. |
| A-042 | Escalate to the D1 Designer when the implementation specification is insufficient or a design question arises | Phase 5 §Item 3 | Position hierarchy: do not resolve at the Programmer what requires design authority. |
| A-043 | Propose upward revision when implementation exposes a design contradiction, infeasibility, or error | Phase 5 §Item 2; Phase 4 §Item 2 | Upward revision allowed but exceptional; the farther up, the stronger the required justification. |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-044 | Perform code-free product upgrades: adjust authorized governed parameters, update release state, repackage, and distribute | Phase 5 §Item 3; RU-01 | Mechanical sub-steps of one upgrade responsibility, merged; without touching product code, to the extent plausible. |
| A-045 | Run the required validation/regression (upgrade smoke-test) harness for every change | Phase 5 §Item 3; RU-01; glossary `d1` | "No code change does not mean no harness." Kept distinct from the upgrade operation (Harness First). |
| A-046 | Configure product-level parameters and approved provider/packaging/release defaults (position-oriented configuration) | Phase 5 §Item 3 | Controls: product defaults, provider defaults, retry policy within ranges, resource profiles, release/packaging parameters. |
| A-047 | Monitor product-package technical health and release state | Phase 5 §Item 3; glossary `d1` | Harness-richness: make product-package health visible at this position's level. |
| A-048 | Detect a failed upgrade and recover / roll back to a prior release | glossary `d1`; Phase 5 §Item 3 | Lifecycle recover-from-a-failed-change; depth-frame diagnose → recover. |
| A-049 | Record the upgrade (maintain upgrade records) | glossary `d1` | Lifecycle: record; the D1 wrapper holds upgrade records. |
| A-050 | Escalate to the D1 Programmer / D1 Designer when a change requires code change or redesign | Phase 5 §Item 3 | Position hierarchy: do not perform at this position a change that alters code or requires substantive redesign. |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|---|---|---|---|
| A-051 | Perform routine operation of the deployed D0 product | Phase 5 §Item 3 | The position's core job function. |
| A-052 | Perform routine user-level monitoring of D0 | Phase 5 §Item 3 | User-level health/behavior visibility; distinct from the D0 Technical Manager's deployment-level monitoring (fundamentals' own distinction). |
| A-053 | Configure operator-level controls: daily spending limits, routine scheduling, collection scope, approved operating choices | Phase 5 §Item 3 | Position-oriented configuration bounded to operator authority. |
| A-054 | View the operator-level D0 health / operating-status report | Phase 4 §Item 3; Phase 5 §Item 3 | The same event is represented per position; "what will the D0 health report look like to the user." Harness-richness: make-visible. |
| A-055 | Detect and handle routine operating errors at the front line | Phase 5 §Item 3 | Depth-frame: handle routine errors; front-line support comes from the D0 Technical Manager (glossary `d0`). |
| A-056 | Escalate beyond-routine issues to the D0 Technical Manager | Phase 5 §Item 3; glossary `d0` | Position hierarchy / escalation to the front-line support position. |

### R-06 — D0 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-057 | Install / deploy a particular D0 deployment into its environment | Phase 5 §Item 3 | Lifecycle-forced transition: package → install/deploy. |
| A-058 | Run the deployment smoke-test to verify a healthy install and hand the deployment over to the D0 Operator | glossary `d1`; Phase 5 §Item 1; design-node-algorithm | Lifecycle verification gate + hand-off (produce/receive pair); cannot reach "operator running it" without it. |
| A-059 | Configure deployment-level settings: deployment paths, storage endpoints, service configuration, resource limits, credential integration, deployment health settings | Phase 5 §Item 3 | Position-oriented configuration for this deployment. |
| A-060 | Technically maintain the deployment | Phase 5 §Item 3 | Ongoing technical maintenance of the particular D0 deployment. |
| A-061 | Monitor deployment health and performance (e.g. D0-crash detection) | Phase 5 §Item 3; glossary `d1` | Deployment-level health monitoring (half a level above D0); distinct from the Operator's user-level monitoring. Harness-richness: detect hidden failures. |
| A-062 | Detect, diagnose, and recover from deployment failures | glossary `d1`; Phase 5 §Item 3 | Depth-frame diagnose → recover; lifecycle detect → diagnose → recover. |
| A-063 | Provide front-line support to the D0 Operator (receive and handle escalations) | glossary `d0`; Phase 5 §Item 3 | The receive side of the Operator's escalation (A-056). |
| A-064 | Escalate to the D1 layer when a fix requires a product-package change | Phase 5 §Item 3 | Position hierarchy: a change beyond deployment authority routes to the D1 Technical Manager / D1 layer. |

### R-07 — D2 Assistant

| ID | Action | Source | Notes |
|---|---|---|---|
| A-065 | Serve as the D1 Designer's single, unified point of contact with the entire D2 system | completions.md C-2026-07-19-1; Phase 2 §Principle 3 | The Designer never addresses an internal node, authority, or service directly. |
| A-066 | Conduct the design on the Designer's behalf and answer his queries | completions.md C-2026-07-19-1 | Real work that no other named position owns; occupied by a D2 agent, treated position-first. |
| A-067 | Interpret and route Designer input to the correct internal D2 function | completions.md C-2026-07-19-1; Phase 2 §Principle 3 (4.2) | D2 owns interaction routing; internal decomposition must not become Designer interaction complexity. |
| A-068 | Preserve interaction and design context across the Designer's interactions | completions.md C-2026-07-19-1; Phase 2 §Principle 3 (4.3) | The Designer should not repeatedly reconstruct context for different internal recipients. |
| A-069 | Present the Designer's output — Completion Reports, Review Stops, Clarification Requests, and human-readable summaries with drill-down | completions.md C-2026-07-19-1; Phase 3 §Phase-Wide Rule | Human-oriented presentation for design judgment, not machine records. |
| A-070 | Make the D2 process observable to the Designer through Designer-oriented reports, indicators, and investigative views | Phase 2 §Principle 2; Phase 3 §Item 5 | Harness-richness make-visible facet: observability enables informed Designer-initiated intervention (supports A-016…A-020). |
</content>
</invoke>
