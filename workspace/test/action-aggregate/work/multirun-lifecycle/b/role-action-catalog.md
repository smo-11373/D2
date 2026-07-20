# Role–Action Aggregate Table

*Derived from the frozen inputs only (constitution Phases 1–5, `completions.md`, `method §1`,
`RU-01…RU-11`, `glossary`, `framework/*`). Every row cites an in-namespace `Source` (`sources.md`).
`A-003` is retired and skipped. Roles ordered by layer; role IDs honor the frozen glossary pins
(R-00 D2 Designer, R-01 D1 Designer, R-05 D0 Operator, R-06 D0 Technical Manager), so the
completion-named **D2 Assistant** is appended as R-07 rather than renumbering the pinned IDs.*

## Roles

| ID | Role | Relationship | Description | Source |
|---|---|---|---|---|
| R-00 | D2 Designer | D2 layer — builder / meta (intrinsic); **not** a user of D2 | Builds the D2 product and holds Designer-originated completion/clarification authority over D2's intentionally-open working sets; the acceptance authority over D2's own design tree. | glossary `d2-designer`; Phase 5 §Item 3 |
| R-01 | D1 Designer | D2's primary and only user (intrinsic) | The Designer who directs the evolution of a Predecessor D1 into a successor D1 using D2's tools; D2 exists primarily for his benefit and preserves his effective authority while reducing his attention cost. | glossary `d1-designer`; Phase 1 §2; Phase 5 §Item 3 |
| R-02 | Design Node Builder | D2-internal engine position (intrinsic) | A narrowly-scoped position (occupied by an agent) that builds a single design node from a bounded contract — investigates, designs, verifies, submits, enforces, and spawns children within its sandbox. | Phase 5 §Item 3; Phase 4 §Item 2; glossary `design-node` |
| R-03 | D1 Programmer | D1 build layer (intrinsic) | Changes product code according to an implementation specification, realizing an understood design without reconstructing the design process. | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | D1 maintenance layer (intrinsic) | Maintains and upgrades the technical product package within the established design **without changing product code** — governed-parameter changes, validation harness, repackaging, release. | Phase 5 §Item 3; RU-01; glossary `d1` |
| R-05 | D0 Operator | D0 operation layer (intrinsic) | Performs routine operation and routine user-level monitoring of the deployed D0 product. | Phase 5 §Item 3; glossary `d0` |
| R-06 | D0 Technical Manager | D0 deployment layer (intrinsic) | Installs and technically maintains a particular D0 deployment; provides front-line technical support to the D0 Operator. | Phase 5 §Item 3; glossary `d0` |
| R-07 | D2 Assistant | D2-internal interaction front (intrinsic; completion-named) | A Human-Position-First position (occupied by a D2 agent) that is the D1 Designer's single unified point of contact — conducts the design on his behalf, interprets/routes his input while preserving context, and presents his output. | completions.md C-2026-07-19-1; Phase 2 §Principle 3 |

## Actions

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-001 | Build and author the D2 product (the design system) | glossary `d2-designer`; Phase 5 §Item 3 | Job function: constructs D2 for the D1 Designer. |
| A-002 | Complete / clarify / expand D2's intentionally-open working sets (Designer-originated completion) | Phase 5 §Item 2; completions.md C-2026-07-19-1 | Low-hurdle completion of open sets; the completions overlay is an instance (intention lens: keep the constitution current). |
| A-004 | Approve or reject upward revision proposals to Designer-governed D2 nodes | Phase 4 §Item 2; RU-02; RU-04 | Acceptance authority over D2's own design; submission ≠ acceptance. |
| A-005 | Author and govern D2 design rules (create / revise / retire Designer rules) | Phase 4 §Item 2; RU-01 | Designer rules require Designer permission. |
| A-006 | Initiate and evaluate a change (Designer-initiated) before officially proposing it | RU-06; framework `design-tree` | Evaluate-before-propose commits nothing; usually after discussion. |

### R-01 — D1 Designer

*Passive [P] — responds to what D2 brings him; Active [A] — acts on his own initiative (method §1).*

| ID | Action | Source | Notes |
|---|---|---|---|
| A-007 | Decide whether to use D2 (the entry point) | method §1; Phase 3 §Item 1 | [P] First decision; D2 orients him with the concepts it needs. |
| A-008 | Establish the initial setup — the roles table and the default design posture | method §1; Phase 5 §Item 2 | [P] One setup step: cast of roles (intrinsic / changeable default) + default choices. |
| A-009 | Review and confirm the Designer–D2 operating contract (intervention posture) | Phase 3 §Item 1 | [P] Normally accept defaults; covers D2- and Designer-initiated intervention. |
| A-010 | Establish the initial design input — Predecessor D1 package + intended change | Phase 3 §Item 2; Phase 1 §4 | [P] Incremental intent; full specification not required. |
| A-011 | Confirm the initial design understanding and direction at a Review Stop | Phase 3 §Item 3 | [P] Courtesy / control review boundary, not a Clarification Request. |
| A-012 | Produce and confirm the D1 foundational documents (D1 Constitution) at a key Review Stop | method §1; Phase 4 §Item 1 | [P] Combine setup skeleton + predecessor V1 + intended change. |
| A-013 | Review and confirm the D1 Design Operating Framework | Phase 4 §Item 1 | [P] "Here is how I propose to conduct this D1 design." |
| A-014 | Review the current Design Node at a Review Stop per its significance | Phase 4 §Item 2 | [P] Designer attention increases with node height. |
| A-015 | Answer consolidated Clarification Requests (material judgment) | Phase 3 §Item 1; Phase 4 §Item 2 | [P] Judgment D2 cannot resolve through further investigation. |
| A-016 | Set node revision authority (Designer-governed vs D2-governed) | Phase 4 §Item 2 | [P] Review event vs continuing revision authority are distinct. |
| A-017 | Approve material revisions to Designer-governed nodes | Phase 4 §Item 2 | [P] Designer control prevents silent revision. |
| A-018 | Complete the D1 design and hand off an implementation specification to the D1 Programmer | Phase 5 §Item 3 | [P] Design-to-programming handoff: spec complete enough to implement without reconstructing the design. Lifecycle hand-off. |
| A-019 | Monitor design progress and elapsed time | Phase 4 §Item 3; Phase 1 §2.3 | [A] "How much time has D1 design consumed so far?" |
| A-020 | Monitor design cost / spend | Phase 4 §Item 3 | [A] Distinct responsibility from health (distinctness guard: cost vs health). |
| A-021 | Monitor D1 design-process health and detect abnormal process behavior | Phase 4 §Item 3; Phase 5 §Item 1 | [A] "Current D1 design health report"; "behaving abnormally." Harness-richness (monitor/detect). |
| A-022 | Inspect the emerging D0 design (structure, files, algorithms, diffs vs V1) | Phase 4 §Item 3 | [A] Ask / inspect via natural design requests. |
| A-023 | Inspect the Design Tree and what changed since last review | Phase 4 §Item 3 | [A] "Show me the Design Tree" / "what changed since my last review." |
| A-024 | Investigate a suspected design or process problem (critical drill-down) | Phase 4 §Item 3; Phase 2 §3.4 | [A] Investigation before intervention. |
| A-025 | Issue a Designer directive — impose, reserve approval, or suspend a branch | Phase 4 §Item 3 | [A] Authority action recognized and applied promptly. |
| A-026 | Redirect the design or lay down a rule / invariant | Phase 4 §Item 3; method §1 | [A] Active involvement — a governing rule elevated from repeated local issues. |
| A-027 | Initiate intervention independently of D2 | Phase 2 §Principle 2 (§3.3) | [A] Not dependent on D2 first detecting a problem. |
| A-028 | Tune the resolution / intervention depth to manage his attention budget | Phase 2 §Item 2.6; Phase 1 §2.3 | [A] Intention lens: intent to manage attention cost → tune investigation/intervention depth. |
| A-029 | Hold D0-user optimization in view when directing the design | method §1; Phase 5 §Item 3 | [A] Standing consideration — he designs D1 to serve the D0 users. |
| A-030 | Audit the completed D2 design process (cost, attention, improvement points) | Phase 3 §Item 5 | [A] "Checking how well D2 served him" — D2 audit ≠ D1 review. |

### R-02 — Design Node Builder

| ID | Action | Source | Notes |
|---|---|---|---|
| A-031 | Receive and interpret its governing contract (inherited data + input links) | Phase 4 §Item 2; RU-04; RU-08 | Works within a compiled, sandboxed contract. |
| A-032 | Investigate autonomously to resolve uncertainty before escalating | Phase 4 §Item 2; Phase 2 §2.1 | Dig into available evidence first. |
| A-033 | Develop candidate designs and evaluate alternatives | Phase 4 §Item 2 | Internal design and convergence. |
| A-034 | Produce the node design specification (the node result) | Phase 4 §Item 2 | Proposed Node Design Specification. |
| A-035 | Build the node's harness and verify / test the node | Phase 4 §Item 2; Phase 5 §Item 1; Phase 2 §Principle 4 | Checks and tests; harness before descent. Harness-richness (test). Lifecycle: test. |
| A-036 | Run the conformance / completeness self-check before spawning or submitting | framework `conformance`; framework `design-node-algorithm` | Contradict no governing statement; staged at each internal boundary (distinct from product testing). |
| A-037 | Prepare consolidated Clarification Requests when Designer judgment is required | Phase 4 §Item 2 | Accumulate high-leverage questions where practical. |
| A-038 | Produce the Designer-oriented node report | Phase 4 §Item 2; Phase 1 §2.4 | Human-oriented, not machine transcripts. |
| A-039 | Determine children and propose a spawning strategy (by supported actions) | Phase 4 §Item 2; RU-03; RU-10 | Spawn by the Designer's actions; passive-action spawning first. |
| A-040 | Compile each child's contract — filter rules, attach owned data + input links | Phase 4 §Item 2; RU-04; RU-08 | Lean sandboxed child contract. |
| A-041 | Author the node's justification and submit the package upward for acceptance | RU-02; glossary `submission-package` | Justification travels with the result; submission ≠ acceptance. |
| A-042 | Enforce the rules its owned data specifies | glossary `design-node` | Holds its data, has authority over it, enforces its rules. |
| A-043 | Aggregate children's deliverables at its boundary | RU-10 | Decompose freely, aggregate always. |
| A-044 | Evaluate a proposed change (dry-run up and down) before officially proposing | RU-06 | Evaluation commits nothing; returns an evaluation report. |
| A-045 | Propose upward revision of inherited data and halt until resolved | RU-04; RU-05 | An open upward proposal is a stopping point (no drift). |
| A-046 | Apply a parent's request-down change to its own table and re-submit | RU-09 | The author makes the change; no node edits a table it does not author. |

### R-03 — D1 Programmer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-047 | Receive the implementation specification handoff | Phase 5 §Item 3 | Implement without reconstructing the earlier design. Lifecycle receive. |
| A-048 | Implement / change product code per the specification | Phase 5 §Item 3 | Job function. Lifecycle: implement. |
| A-049 | Realize the spec within the established design without revising higher-level intent | Phase 5 §Item 2 | Find a conforming lower-level design; inconvenience is weak justification for upward revision. |
| A-050 | Test / verify the implementation against the design harness | Phase 5 §Item 1; Phase 2 §Principle 4; Phase 1 §3.5 | Representative inputs, expected outputs, evaluation cases. Harness-richness (test). Lifecycle: test. |
| A-051 | Detect and report / handle implementation defects | Phase 5 §Item 1; Phase 4 §Item 2 | Make failures visible (depth: handle errors; harness-richness: detect). |
| A-052 | Propose upward revision when the spec is materially defective or infeasible | Phase 5 §Item 2; Phase 4 §Item 2 | Escalate with strong justification (depth: escalate). |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-053 | Adjust authorized / governed product parameters without changing code | Phase 5 §Item 3; RU-01 | e.g. default timeout 5→10 min via a governed parameter (depth: configure). |
| A-054 | Configure product defaults, provider defaults, retry policy, resource profiles, feature-policy, release/packaging parameters | Phase 5 §Item 3 | The D1 Technical Manager control boundary. |
| A-055 | Run the required validation / regression (upgrade smoke-test) harness after a change | Phase 5 §Item 3; RU-01; glossary `d1` | "No code change does not mean no harness." Harness-richness; lifecycle: re-test. |
| A-056 | Update release state and version | Phase 5 §Item 3; RU-01 | Release-state maintenance. |
| A-057 | Repackage the product | Phase 5 §Item 3; RU-01 | Lifecycle: package. |
| A-058 | Distribute / release the product package | Phase 5 §Item 3; RU-01 | Hand-off to the D0 Technical Manager. Lifecycle: hand-over. |
| A-059 | Record the upgrade (upgrade records) | glossary `d1` | Wrapper upgrade records (depth: record; make-visible). |
| A-060 | Recover from a failed upgrade (roll back within the established design) | glossary `d1`; Phase 5 §Item 1; framework `design-node-algorithm` | Controlled upgrade implies rollback on smoke-test failure. Lifecycle: recover/rollback. |
| A-061 | Maintain the wrapper's D0 health / performance monitoring capability | glossary `d1`; glossary `half-level`; Phase 5 §Item 1 | Half-level-above health monitoring (e.g. D0-crash detection) the wrapper holds. Harness-richness (monitor). |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|---|---|---|---|
| A-062 | Operate the D0 product routinely | Phase 5 §Item 3 | Routine operation (depth: operate). Lifecycle: operate. |
| A-063 | Perform routine user-level monitoring | Phase 5 §Item 3 | Distinct from technical/deployment health monitoring (distinctness guard). Harness-richness (monitor). |
| A-064 | Set operator controls — daily spending limits, routine scheduling, collection scope, approved operating choices | Phase 5 §Item 3 | Position-oriented configuration (depth: configure). |
| A-065 | View operator-level status and the user-facing D0 health report | Phase 4 §Item 3; Phase 5 §Item 3 | Same underlying event represented per position (depth: view). |
| A-066 | Handle routine operational errors | Phase 5 §Item 3; Phase 5 §Item 1 | Within operator authority (depth: handle errors). |
| A-067 | Escalate / request support beyond routine authority (to the D0 Technical Manager) | Phase 5 §Item 3; glossary `d0` | Position hierarchy; front-line support (depth: escalate). |

### R-06 — D0 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-068 | Install / deploy a particular D0 deployment | Phase 5 §Item 3 | Installs a deployment. Lifecycle: install/deploy; re-deploy on upgrade. |
| A-069 | Configure the deployment — paths, storage endpoints, service config, resource limits, credential integration, deployment health settings | Phase 5 §Item 3 | The D0 Technical Manager control boundary (depth: configure). |
| A-070 | Run a deployment smoke-test after install or upgrade | glossary `d1`; Phase 5 §Item 1; framework `design-node-algorithm` | Smoke-test gate. Harness-richness; lifecycle: smoke-test. |
| A-071 | Technically maintain the deployment | Phase 5 §Item 3 | Ongoing technical maintenance (depth: operate/maintain). |
| A-072 | Monitor deployment health and detect technical failures (e.g. D0-crash detection) | Phase 5 §Item 3; glossary `d1`; glossary `half-level` | Deployment health settings; crash detection. Harness-richness (monitor/detect). |
| A-073 | Provide front-line technical support to the D0 Operator | glossary `d0` | Front-line support for escalations. |
| A-074 | Diagnose and recover from a failed deployment change (rollback) | Phase 5 §Item 3; framework `design-node-algorithm` | Diagnose→recover cycle. Lifecycle: recover. |
| A-075 | Record deployment changes | Phase 5 §Item 3; glossary `d1` | Make deployment changes visible (depth: record). |
| A-076 | Escalate beyond deployment authority (to the D1 Technical Manager) | Phase 5 §Item 3 | Position hierarchy; escalation (depth: escalate). |

### R-07 — D2 Assistant

| ID | Action | Source | Notes |
|---|---|---|---|
| A-077 | Serve as the Designer's single unified point of contact with D2 | completions.md C-2026-07-19-1; Phase 2 §Principle 3 | One interaction point; internal decomposition hidden from the Designer. |
| A-078 | Conduct the design on the Designer's behalf and answer his queries | completions.md C-2026-07-19-1 | Core responsibility of the position. |
| A-079 | Interpret and route Designer input to the right D2 function | completions.md C-2026-07-19-1; Phase 2 §4.2 | D2 owns interaction routing. |
| A-080 | Preserve interaction and design context across the interaction | completions.md C-2026-07-19-1; Phase 2 §4.3 | No repeated context reconstruction for different recipients. |
| A-081 | Present the Designer's output — completion reports, Review Stops, Clarification Requests, human-readable summaries with drill-down | completions.md C-2026-07-19-1; Phase 3 §Item 1; Phase 1 §2.4 | Human-oriented presentation of the three interaction classes. |
| A-082 | Surface D2 process observability / health so the Designer can initiate intervention | Phase 2 §Principle 2; Phase 4 §Item 3 | Observability enables Designer-initiated intervention. Harness-richness (make-visible). |
| A-083 | Support progressive drill-down / deeper investigation on request | Phase 2 §3.4; Phase 4 §Item 3 | Move from high-level observation toward detail before intervening. |
