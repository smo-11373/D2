# Role–Action Catalog

*Derived from the frozen inputs (constitution Phases 1–5, method §1, rules RU-01…11,
glossary, framework) per `input/contract.md`. Every row cites an in-package Source
(namespace fixed by `environment/sources.md`). Action IDs are stable and unique; `A-003`
is retired and intentionally skipped. Roles are ordered by layer, D2 → D1 → D0.*

## Roles

| ID | Role | Relationship | Description | Source |
|------|------|--------------|-------------|--------|
| R-00 | D2 Designer | D2 builder (human) | The human who builds the D2 product — authoring its constitution (Phases 1–5), method, rules, and framework — and who holds Designer-originated completion and clarification authority over D2's living working sets. He is **not** a user of D2; he sits above D2's own design tree as its root authority. **Intrinsic.** | glossary `d2-designer`; Phase 5 §Item 2 |
| R-01 | D1 Designer | Primary user of D2 (human) | The primary and only user of the D2 product: the human directing the evolution of an existing D1 system into a materially revised successor. He uses D2's setup defaults, design tree, and design-node modules to build a D1 product (which wraps D0), supplying incremental intent and retaining effective design authority while D2 works to reduce his attention cost. **Intrinsic.** | Phase 1 §2; glossary `d1-designer` |
| R-02 | D2 Assistant | D2's unified interaction agent | D2's single primary interaction point and agent embodiment: it receives all Designer interaction, owns internal interpretation, routing, and coordination, investigates available evidence, builds design nodes, and presents human-oriented reports — so the Designer interacts with D2 as one system rather than choosing among internal components or channels. **Intrinsic.** | Phase 2 §Principle 3; Phase 4 §Item 3 |
| R-03 | D1 Programmer | D1 product position (implements code) | The position responsible for changing product code according to the D1 implementation specification. Ideally it receives a handoff spec complete enough to implement D0 without reconstructing the earlier design process, realizing an understood design rather than discovering the design through code. Provided by D2 as a default cast member the D1 Designer may reshape. **Default.** | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | D1 product position (non-code maintenance) | The position responsible for technical maintenance and controlled upgrade of the D0 product when the required change does not alter product code or require substantive redesign — adjusting governed parameters, running the required harness, updating release state, repackaging, and distributing. Its very existence imposes design consequences: governed controls must be exposed to it. A Designer-changeable default. **Default.** | Phase 5 §Item 3; RU-01 |
| R-05 | D0 Operator | D0 product position (routine operation) | The position that runs the deployed D0 product day to day and performs routine user-level monitoring, exercising position-appropriate operating controls such as daily spending limits, routine scheduling, collection scope, and approved operating choices. A Designer-changeable default in the delivered product's cast. **Default.** | Phase 5 §Item 3; glossary `d0` |
| R-06 | D0 Technical Manager | D0 product position (deployment maintenance) | The position that installs and technically maintains a particular D0 deployment, giving front-line support and controlling deployment-level settings (paths, storage endpoints, service configuration, resource limits, credential integration, health). May deploy just D0 into production while retaining D1 to manage and upgrade it. A Designer-changeable default. **Default.** | Phase 5 §Item 3; glossary `d0` |

## Actions

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-001 | Build and author the D2 product — the constitution (Phases 1–5), the method, the rules, and the framework that together define what D2 is and the principles it must honour. | glossary `d2-designer`; Phase 5 §Item 2 | position-derived |
| A-002 | Perform Designer-originated completion and clarification of D2's intentionally open living working sets (glossary, query catalog, Phase 5 itself) — adding an omitted philosophy, definition, or example at a low hurdle, without it counting as bottom-up revision. | Phase 5 §Item 2 | [A] |
| A-004 | Review and approve or reject a D2 design node's submission package as the root enforcer of D2's own design tree; submission is not acceptance. | RU-02 | [P] |
| A-005 | Initiate and direct changes to D2's own design (Designer-initiated change), usually after discussion, evaluating the change as a committing-nothing dry run before proposing it officially. | design-tree; RU-06 | [A] |

### R-01 — D1 Designer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-006 | Decide whether to use D2 for an intended D1 upgrade — his first decision, which D2 backs by orienting him with the concepts the decision needs. | method §1; Phase 1 §2 | [P] |
| A-007 | Review and confirm the Designer–D2 Operating Contract — how D2 will seek his intervention and how he will observe and intervene — normally by accepting the compact human-oriented defaults. | Phase 3 §Item 1 | [P] |
| A-008 | Establish the initial design input: supply the available Predecessor D1 package and the intended D1 change in whatever initial form is useful (revision notes, bug lists, complaints, desired features, rough direction). | Phase 3 §Item 2 | [P] |
| A-009 | Review, at the Review Stop, D2's consolidated initial design understanding and recommended high-level design direction, and choose to review now or continue. | Phase 3 §Item 3 | [P] |
| A-010 | Acknowledge D2's notification that initial setup is complete and that D2 is entering D1 design mode. | Phase 3 §Item 4 | [P] |
| A-011 | Review and confirm the proposed D1 Design Operating Framework (initial skeleton, inherited/derived design rules, and D1-specific control points) — accept, modify selected parts, request investigation, or raise a concern. | Phase 4 §Item 1 | [P] |
| A-012 | Establish and confirm the setup cast — the roles table (each role intrinsic or a Designer-changeable default) and the run's default design posture — in one low-cost setup step. | method §1 | [P] |
| A-013 | Confirm the D1 foundational documents (the D1 Constitution), combined from the setup skeleton, the predecessor, and the intended change, at the strongly-encouraged key Review Stop. | method §1; Phase 4 §Item 2 | [P] |
| A-014 | Respond to consolidated Clarification Requests during node building — supply the material design judgment D2 cannot reasonably resolve through further investigation. | Phase 4 §Item 2; Phase 3 §Item 2 | [P] |
| A-015 | Review Design Node reports and their proposed spawning strategies at Review Stops, with attention scaled to node height (higher, governing nodes such as the Constitution receive more attention; lower nodes may proceed with D2 autonomy). | Phase 4 §Item 2 | [P] |
| A-016 | Receive and observe item Completion Reports, to which a Designer response is optional unless a Clarification Request accompanies them. | Phase 3 §Item 1 | [P] |
| A-017 | Monitor the D1 design's progress and behavioral health independently of D2 first raising a concern, using Designer-oriented observability. | Phase 2 §Principle 2; Phase 4 §Item 3 | [A] |
| A-018 | Monitor the time and cost/spend consumed by the design process, including which nodes have consumed the most time, cost, or revisions. | Phase 4 §Item 3 | [A] |
| A-019 | Inspect the emerging D0 design through natural design-oriented requests (directory structure, package files, health report, monitoring design, algorithm design and its diff from V1) without naming the responsible internal node or service. | Phase 4 §Item 3 | [A] |
| A-020 | Inspect the ongoing D1 design process and the Design Tree — view the tree, what changed since the last review, and which unresolved issues are most likely to affect major parts of the design. | Phase 4 §Item 3 | [A] |
| A-021 | Drill down and investigate a suspected design or process concern, moving from high-level observation toward progressively deeper information before deciding whether to intervene. | Phase 4 §Item 3; Phase 2 §Principle 2 | [A] |
| A-022 | Issue a Designer directive — redirect the work, stop a branch until he reviews, or reserve personal approval authority over a specified design object — recognized as an authority action and applied promptly. | Phase 4 §Item 3 | [A] |
| A-023 | Lay down or revise a design rule or policy boundary (semantic meaning, policy boundaries, algorithmic behavior, product invariants), which Designer rules require his permission to materially change. | Phase 4 §Item 3; Phase 4 §Item 2 | [A] |
| A-024 | Initiate a change proposal (Designer-initiated), usually after a round of discussion, and evaluate it as a committing-nothing dry run (probe up / probe down) before it is officially proposed. | design-tree; RU-06 | [A] |
| A-025 | Design with D0-user optimization in mind — a standing, cross-cutting consideration that shapes what the D1 system must do so it serves the D0 operators and users. | method §1; Phase 5 §Item 3 | [A] cross-cutting |
| A-026 | Optionally audit, after the run, how well D2 served him — process cost, time, Designer Attention Cost, late discoveries, and candidate D2 improvements — distinct from asking whether D1 itself is good. | Phase 3 §Item 5; method §1 | [A] |

### R-02 — D2 Assistant

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-027 | Present one unified primary interaction point and own the internal interpretation, routing, and coordination of Designer input, so the Designer never has to choose which internal D2 component should receive a question, instruction, or criticism. | Phase 2 §Principle 3; Phase 4 §Item 3 | position-derived |
| A-028 | Actively investigate the Predecessor D1, Designer material, and reference resources before transferring investigative work to the Designer or escalating an uncertainty. | Phase 2 §Principle 1 | position-derived |
| A-029 | Seek Designer intervention only at high-leverage points — consolidated, high-semantic-level questions whose design value justifies the attention cost — rather than many low-level approvals. | Phase 2 §Principle 1; Phase 1 §2.5 | position-derived |
| A-030 | Produce and present human-oriented reports, summaries, and views — Completion Reports, Review Stops, and consolidated Clarification Requests — organized for design judgment rather than machine records. | Phase 1 §2.4; Phase 3 §Item 1 | position-derived |
| A-031 | Provide Designer-oriented observability with progressively deeper investigative access, so the Designer can independently recognize concerns and move from high-level observation toward detail. | Phase 2 §Principle 2 | position-derived |
| A-032 | Preserve sufficient interaction and design context so the Designer can interact without repeatedly reconstructing context for different internal recipients. | Phase 2 §Principle 3 | position-derived |
| A-033 | Build the current Design Node — investigate, design, check, test, submit, enforce, and revise internally — then produce a Designer-oriented node report and a proposed spawning strategy. | Phase 4 §Item 2 | position-derived (absorbs the Design Node Builder function) |
| A-034 | Locate the relevant design state, interpret a natural-language inspection or intervention request, and route any resulting action through the appropriate governance process. | Phase 4 §Item 3 | position-derived |
| A-035 | Preserve provenance and uncertainty — keep Designer intent, observed predecessor behavior, reference material, derived evidence, and inference distinguishable, and never silently convert inference into Designer intent. | Phase 1 §4.6 | position-derived |

### R-03 — D1 Programmer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-036 | Implement the D0 product code according to the D1 implementation specification. | Phase 5 §Item 3 | position-derived |
| A-037 | Realize an understood design rather than use coding as the default environment for discovering fundamental design questions. | Phase 2 §Principle 4; Phase 5 §Item 3 | position-derived |
| A-038 | Work from a design-to-programming handoff spec complete enough to implement without reconstructing the earlier design process. | Phase 5 §Item 3 | position-derived |
| A-039 | Propose upward when the specification is defective, inconsistent, or infeasible — a lower node retains the right to challenge higher design (Designer control prevents silent revision, not upward feedback). | Phase 4 §Item 2 | position-derived |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-040 | Adjust an explicitly governed product-level parameter, within its accepted range, without touching code — the legitimate controller of a variable technical decision. | Phase 5 §Item 3; RU-01 | position-derived |
| A-041 | Run the required validation or regression harness after a parameter change — "no code change does not mean no harness" — using the D1 wrapper's upgrade smoke-test suite. | Phase 5 §Item 3; glossary `d1` | position-derived |
| A-042 | Update release state, repackage, and distribute the upgraded product after an authorized non-code change. | Phase 5 §Item 3 | position-derived |
| A-043 | Manage position-appropriate technical controls — product defaults, approved provider defaults, retry policy within accepted ranges, resource profiles, and release/packaging parameters. | Phase 5 §Item 3 | position-derived |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-044 | Perform routine operation of the deployed D0 product. | Phase 5 §Item 3 | position-derived |
| A-045 | Perform routine user-level monitoring of D0 — reading health and status at the operator's level of representation. | Phase 5 §Item 3 | position-derived |
| A-046 | Exercise position-appropriate operating controls — daily spending limits, routine scheduling, collection scope, and approved operating choices. | Phase 5 §Item 3 | position-derived |
| A-047 | Consume D0 health/status information represented for the operator position (the same underlying event may be shown differently to different positions). | Phase 5 §Item 3; glossary `d0` | position-derived |

### R-06 — D0 Technical Manager

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-048 | Install and deploy a particular D0 deployment into its target environment. | Phase 5 §Item 3 | position-derived |
| A-049 | Technically maintain the D0 deployment and provide front-line support for it. | Phase 5 §Item 3; glossary `d0` | position-derived |
| A-050 | Configure deployment-level settings — deployment paths, storage endpoints, service configuration, resource limits, credential integration, and deployment health settings. | Phase 5 §Item 3 | position-derived |
| A-051 | Deploy just D0 into production while retaining D1 to manage and upgrade it (the half-level operational wrapper). | glossary `d1`; Phase 5 §Item 3 | position-derived |
