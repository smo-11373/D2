# Role–Action Aggregate Table

*Clean-room derivation of the Action-Aggregate node. Roles derived from Phase 5 §Item 3 + the
Designer completions + the layer model (D2→D1→D0); actions derived per role by the four lenses
(job-function · intention · depth-frame · lifecycle) with the harness-richness bias and the
recall-first inclusion guard. Every row cites an in-package Source. `A-003` is retired (skipped).*

## Roles

Numbering honors the frozen `R-` namespace pinned by the glossary (`d2-designer` R-00, `d1-designer`
R-01, `d0` D0 Operator R-05 / D0 Technical Manager R-06) and by `rules.md` (R-04 D1 Technical
Manager); the intervening R-02 / R-03 are the remaining Phase 5 §Item 3 positions in
design→implement order, and the completion-added **D2 Assistant** is appended as R-07.

| ID | Role | Relationship | Description | Source |
|---|---|---|---|---|
| R-00 | D2 Designer | Intrinsic — D2 layer (builder/meta) | The human building the D2 product; not a user of D2. Authors and evolves D2's living design record and holds Designer-originated completion/clarification authority over D2's intentionally-open working sets. | glossary `d2-designer`; Phase 5 §Item 2 |
| R-01 | D1 Designer | Intrinsic — D1 layer (primary user) | The primary and only user of D2; directs the evolution of a Predecessor D1 into a successor D1 while retaining effective design authority and conserving his scarce attention. | glossary `d1-designer`; Phase 1 §2; Phase 5 §Item 3 |
| R-02 | Design Node Builder | Intrinsic — design mechanism | The position that builds the current Design Node — investigates, designs, checks, tests, justifies, submits, and (where the work decomposes) spawns children — treated as a person with a narrow, well-bounded skill set. | Phase 5 §Item 3; Phase 4 §Item 2; glossary `design-node` |
| R-03 | D1 Programmer | Default — D1 layer | Changes product code according to implementation specifications; implements a completed design without reconstructing the earlier design process. | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | Default — D1 layer | Maintains and upgrades the technical product package within the established design without changing product code; owns governed parameters, repackaging, the upgrade smoke-test suite, and upgrade records. | Phase 5 §Item 3; glossary `d1` |
| R-05 | D0 Operator | Default — D0 layer | Performs routine operation and routine user-level monitoring of the deployed D0 product within approved operating controls. | Phase 5 §Item 3; glossary `d0` |
| R-06 | D0 Technical Manager | Default — D0 layer | Installs and technically maintains a particular D0 deployment; owns deployment configuration, deployment health, and deployment-level recovery. | Phase 5 §Item 3; glossary `d1` |
| R-07 | D2 Assistant | Intrinsic — D2 layer (interaction front) | The D1 Designer's single unified point of contact with the entire D2 system; conducts the design on his behalf, interprets and routes his input, preserves context, and presents his output. A Human-Position-First position occupied by a D2 agent. | completions.md C-2026-07-19-1; Phase 2 §Principle 3 |

## Actions

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-001 | Author and evolve the D2 living design record | glossary `d2-designer`; Phase 5 §Item 2 | Maintains the constitution, method, rules, and catalogs as the canonical, authoritative design record. Job-function lens. |
| A-002 | Originate completions and clarifications of intentionally-open D2 working sets | Phase 5 §Item 2; completions.md C-2026-07-19-1 | Completes or clarifies the intentionally-open sets (glossary, query catalog, Phase 5, positions) at a low hurdle when consistent with established design. Intention lens (keep the open sets current). |
| A-004 | Approve or reject material revisions to Designer-governed D2 nodes | RU-02; Phase 4 §Item 2 | Holds top design authority; reviews submitted justifications and accepts or rejects, preventing silent revision of Designer-governed material. Job-function lens. |
| A-005 | Set D2 design principles, direction, and default posture | Phase 2 §6; Phase 5 §Item 1–5 | Establishes the governing principles (Harness First, Top-to-Bottom, Human Position First, Quality over Expediency, Modularization) that constrain all downstream D2 design. Intention lens. |

### R-01 — D1 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-006 | Decide whether to use D2 | method §1 (entry point); Phase 1 §2 | [P] His first decision; D2 backs it by orienting him with the concepts it needs. Job-function / passive. |
| A-007 | Establish and confirm the Designer–D2 Operating Contract | Phase 3 §Item 1 | [P] Reviews and confirms how D2 will seek intervention and how he will observe/intervene; normally accepts or lightly modifies the defaults. |
| A-008 | Establish the initial design input | Phase 3 §Item 2; Phase 1 §4 | [P] Supplies the Predecessor D1 package and the available expression of intended change; not required to fully specify the change up front. |
| A-009 | Supply incremental Designer intent | Phase 1 §3.4; Phase 1 §4.2 | [A] States behavior to preserve, known problems, corrections, simplifications, new capabilities, constraints, and directions of improvement — incrementally, not by restating unchanged parts. |
| A-010 | Review the initial design understanding and direction at the Review Stop | Phase 3 §Item 3 | [P] Optional review/intervention on D2's consolidated understanding and recommended high-level direction. |
| A-011 | Receive notification of entering D1 design mode | Phase 3 §Item 4 | [P] Acknowledges that initial D2 setup is complete and D1 design begins. |
| A-012 | Establish the roles table and design posture (setup) | method §1 (setup); Phase 3 §Item 1 | [P] Establishes the cast of roles (each intrinsic or a changeable default) and the run's default design choices in one setup step. |
| A-013 | Review and confirm the D1 Design Operating Framework | Phase 4 §Item 1 | [P] Reviews the consolidated proposed framework (skeleton, inherited rules, control points); accepts, modifies parts, requests investigation, or discusses a concern. |
| A-014 | Confirm the D1 foundational documents (D1 Constitution) at the key Review Stop | method §1; Phase 4 §Item 1 | [P] Confirms the D1 project's own constitution/foundational set, combined from setup skeleton + predecessor V1 + intended change, at a strongly-encouraged Review Stop. |
| A-015 | Set the design in motion via the operating framework | method §1; Phase 4 §Item 1 | [P] Launches the governed design run once the framework and foundations are confirmed. |
| A-016 | Respond to consolidated Clarification Requests | Phase 4 §Item 2; Phase 3 (interaction classes) | [P] Answers high-leverage material questions D2 could not resolve by investigation, accumulated into one request where practical. |
| A-017 | Respond at Review Stops | Phase 3 (Review Stop); Phase 4 §Item 2 | [P] Chooses to review now or continue at optional stopping points; reporting and intervention boundaries are distinct. |
| A-018 | Set node revision-authority (Designer-governed vs D2-governed) | Phase 4 §Item 2 | [P] Determines, via framework defaults by node level/class, which nodes require his approval for later material revision. |
| A-019 | Approve material revisions to Designer-governed nodes | Phase 4 §Item 2 | [P] Approves changes to nodes he has reserved (e.g. the Constitution); Designer control prevents silent revision. |
| A-020 | Inspect and inquire into D0 design and D1 process state | Phase 4 §Item 3 | [A] Explains, reports, traces, shows, or compares current design or process state through the unified interaction point using natural requests. |
| A-021 | Investigate a suspected design or process problem | Phase 4 §Item 3; Phase 2 §4.4 | [A] Critically examines a suspected flaw, hidden assumption, or failure condition and recommends action (skeptical investigation). |
| A-022 | Monitor D1 design progress — time and cost consumed | Phase 4 §Item 3; Phase 3 §Item 5 | [A] Tracks elapsed time, process cost, and which nodes have consumed the most time or cost. Active + harness-richness (make-visible). |
| A-023 | Monitor design-process health and abnormal behavior | Phase 4 §Item 3; Phase 2 §Principle 2 | [A] Watches the D1 design health report and flags nodes behaving abnormally or with excessive rejections/revisions. Harness-richness (monitor/detect). |
| A-024 | Drill down from high-level views to detailed design state | Phase 2 §3.4; Phase 4 §Item 3 | [A] Moves progressively from high-level observation toward detailed investigation before deciding whether to intervene. |
| A-025 | Issue Designer directives | Phase 4 §Item 3 | [A] Imposes, revises, reserves, suspends, or otherwise exercises authority — e.g. reserve approval over an algorithm, stop a branch until review. |
| A-026 | Lay down a design rule | Phase 4 §Item 3; Phase 4 §Item 2 (Designer rules) | [A] Creates or revises a governing design rule (requires Designer permission for material rule changes). |
| A-027 | Redirect the design direction | Phase 4 §Item 3 | [A] Redirects the emerging D0 design or the D1 process; intervention normally initiates investigation rather than directly mutating the tree. |
| A-028 | Propose Designer-initiated changes (evaluate, then propose) | RU-06; Phase 4 §Item 2 | [A] Proposes a change, usually after discussion; a dry-run evaluation that commits nothing precedes the official proposal. |
| A-029 | Tune intervention/resolution depth | Phase 2 §2.6; Phase 1 §2.3 | [A] Adjusts the Designer-controlled parameter balancing investigation, inference, intervention, and deferral — managing his attention budget. Intention lens. |
| A-030 | Specify D0-user priorities and optimization targets | Phase 5 §Item 3; method §1 (D0-user throughline) | [A] Holds D0-user optimization in view and specifies user priorities/skill-level considerations the D1 system must serve. Intention lens. |
| A-031 | Optionally audit the completed D2 design process | Phase 3 §Item 5; method §1 (checking) | [A] After a run, reviews process cost, time, Designer Attention Cost, and candidate D2 improvements — checking whether D2 designed D1 well. |

### R-02 — Design Node Builder

| ID | Action | Source | Notes |
|---|---|---|---|
| A-032 | Receive the node-building task and governing contract | Phase 4 §Item 2; RU-04 | Receives the task of building the current Design Node under a compiled governing contract with curated input links. Job-function / lifecycle receive. |
| A-033 | Investigate autonomously before escalating | Phase 4 §Item 2; Phase 2 §2.1 | Digs into the predecessor, Designer material, and reference resources to resolve material uncertainty before transferring work to the Designer. |
| A-034 | Develop candidate node designs | Phase 4 §Item 2 | Forms and compares candidate designs, evaluating alternatives and consequences. |
| A-035 | Establish the node's harness before detailed design | Phase 5 §Item 1; Phase 2 §Principle 4 | Establishes design generality and intent, then the governing harness, before allowing lower-level design to expand. Harness-richness. |
| A-036 | Design, check, and test the node internally | Phase 4 §Item 2; Phase 2 §Principle 4 | Designs, checks, tests, and revises internally as required by the node's governing process before submission. |
| A-037 | Build the node's verification/test harness | Phase 5 §Item 1; Phase 2 §5.2 | Builds representative inputs, expected outputs, smoke tests, comparison, and monitoring capabilities as design assets. Harness-richness (test/detect). |
| A-038 | Produce the Node Design Specification (node result) | Phase 4 §Item 2 | Produces the proposed Node Design Specification or equivalent node result. Lifecycle produce. |
| A-039 | Author the node's justification | RU-02 | Authors the justification and attaches it to the submission package; justification travels with the result. |
| A-040 | Accumulate and prepare a consolidated Clarification Request | Phase 4 §Item 2 | Accumulates high-leverage questions into one consolidated Clarification Request where practical when material Designer judgment is needed. |
| A-041 | Resolve the consequences of Designer answers and continue convergence | Phase 4 §Item 2 | Applies the Designer's answers and continues internal convergence toward a proposed node design. |
| A-042 | Prepare the Designer-oriented node report | Phase 4 §Item 2; Phase 1 §2.4 | Prepares a human-oriented node report organized for design judgment, not machine records. |
| A-043 | Propose a spawning strategy and spawn child nodes | Phase 4 §Item 2; RU-03 | Where the work decomposes, proposes a spawning strategy and spawns children driven by the passive (then active) action set. |
| A-044 | Enforce the rules its owned data specifies | glossary `design-node`; Phase 4 §Item 2 | Enforces the rules its own data specifies, within the authority granted by its contract. Job-function. |
| A-045 | Evaluate a candidate change before proposing (dry-run) | RU-06 | Dry-runs a change — probing up and down and returning an evaluation report — before any official proposal; commits nothing. Harness (verify before realize). |
| A-046 | Propose upward revision to governing design | Phase 4 §Item 2; RU-04; RU-05 | Proposes revision to governing design above it and stops (stopping point) until the owner resolves it; lower nodes retain the right to challenge higher design. |
| A-047 | Submit the node package upward for acceptance | RU-02 | Submits the result with its justification for the parent's review; submission is not acceptance. Lifecycle hand-off (produce/submit). |

### R-03 — D1 Programmer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-048 | Receive the implementation specification (design→programming hand-off) | Phase 5 §Item 3 (design-to-programming handoff) | Receives an implementation specification complete enough to implement without reconstructing the earlier design process. Lifecycle hand-off receive + verification gate. |
| A-049 | Implement product code per the implementation specification | Phase 5 §Item 3 | Changes/produces product code according to the implementation specifications. Depth-frame operate/perform; lifecycle implement. |
| A-050 | Test and verify the implementation against spec and harness | Phase 2 §Principle 4; Phase 5 §Item 1 | Tests the implementation against the specification and the established harness. Depth-frame test; harness-richness; lifecycle test. |
| A-051 | Diagnose and fix implementation defects | Phase 5 §Item 3; Phase 2 §Principle 4 | Diagnoses failing behavior and applies code fixes. Depth-frame handle-errors (diagnose→fix). |
| A-052 | Report implementation status and completion | Phase 1 §2.4; Phase 4 §Item 2 | Reports implementation progress/completion back for the design record. Depth-frame view/report. |
| A-053 | Escalate specification gaps, ambiguities, or infeasibility upward | Phase 5 §Item 3 (position hierarchy); Phase 5 §Item 2 (upward revision) | Escalates a spec gap or infeasibility to the D1 Designer rather than silently reinterpreting higher-level intent. Depth-frame escalate. |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-054 | Adjust authorized/governed product parameters (no code change) | Phase 5 §Item 3; RU-01 | Modifies product defaults, provider defaults, retry policy within ranges, feature-policy, resource profiles, and release/packaging parameters — governed, without touching code. Depth-frame configure/control. |
| A-055 | Run the required validation/regression harness after a change | Phase 5 §Item 3; RU-01 (harness note) | Runs the required validation or regression harness after a parameter change — no code change does not mean no harness. Harness-richness; lifecycle re-test. |
| A-056 | Update release state, repackage, and distribute the product | Phase 5 §Item 3 | Updates release state, repackages, and distributes the upgraded product package. Lifecycle package/re-deploy; produces the hand-off to the D0 Technical Manager. |
| A-057 | Maintain and run the upgrade smoke-test suite | glossary `d1`; Phase 5 §Item 1 | Owns and runs the D1 wrapper's upgrade smoke-test suite. Harness-richness; lifecycle smoke-test. |
| A-058 | Monitor D0 product health and performance | glossary `d1`; Phase 5 §Item 1 (monitoring before usage) | Monitors D0 health/performance (e.g. crash detection) from the D1 wrapper, half a level above D0. Depth-frame monitor; harness-richness. |
| A-059 | Diagnose a failed upgrade or regression | Phase 5 §Item 3; glossary `d1` | Diagnoses a failed upgrade or regression detected by the harness/monitoring. Maintenance cycle diagnose. |
| A-060 | Recover / roll back from a failed change or upgrade | glossary `d1`; Phase 5 §Item 3 | Recovers from or rolls back a failed parameter change or upgrade. Maintenance cycle recover; lifecycle rollback. |
| A-061 | Record the upgrade and maintain upgrade records | glossary `d1` | Maintains the upgrade records the D1 wrapper holds. Maintenance cycle record; lifecycle record. |
| A-062 | Report release, upgrade, and product-health state | Phase 5 §Item 3 (position-oriented reporting) | Reports release/upgrade state and product health for the responsible positions. Depth-frame view/report. |
| A-063 | Escalate changes requiring code or redesign to the D1 Designer/Programmer | Phase 5 §Item 3 (position hierarchy) | Escalates upward when a required change alters product code or requires substantive redesign, rather than exceeding its no-code authority. Depth-frame escalate. |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|---|---|---|---|
| A-064 | Perform routine operation of the D0 product | Phase 5 §Item 3 | Runs the deployed product in routine operation. Depth-frame operate/perform; lifecycle operate. |
| A-065 | Perform routine user-level monitoring of D0 | Phase 5 §Item 3; Phase 5 §Item 1 | Performs routine user-level monitoring of the running product. Depth-frame monitor; harness-richness. |
| A-066 | Set operator-level controls | Phase 5 §Item 3 | Sets daily spending limits, routine scheduling, collection scope, and approved operating choices within the operator control boundary. Depth-frame configure/control. |
| A-067 | View the D0 health report / status | Phase 4 §Item 3; glossary `d1` | Views the D0 health report presented to the user at operator level. Depth-frame view/report; harness-richness (make-visible). |
| A-068 | Handle routine operating errors | Phase 5 §Item 3 | Handles routine operating errors within its authority. Depth-frame handle-errors. |
| A-069 | Escalate non-routine issues to the D0 Technical Manager | Phase 5 §Item 3 (position hierarchy) | Escalates issues beyond routine operation to the front-line D0 Technical Manager. Depth-frame escalate. |

### R-06 — D0 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-070 | Receive the distributed product package | Phase 5 §Item 3; glossary `d1` | Receives the distributed product package for a particular deployment (possibly deploying just D0 while retaining D1). Lifecycle hand-over receive + verification gate. |
| A-071 | Install / deploy a particular D0 deployment | Phase 5 §Item 3; glossary `d1` | Installs and deploys a particular D0 deployment into production. Depth-frame operate/perform; lifecycle install/deploy. |
| A-072 | Run the deployment smoke-test after install | glossary `d1`; Phase 5 §Item 1 | Runs a deployment smoke-test after installation to confirm the deployment is healthy. Harness-richness; lifecycle smoke-test. |
| A-073 | Configure the deployment | Phase 5 §Item 3 | Configures deployment paths, storage endpoints, service configuration, resource limits, credential integration, and deployment health settings. Depth-frame configure/control. |
| A-074 | Monitor deployment health | Phase 5 §Item 3 (deployment health settings); Phase 5 §Item 1 | Monitors the health of the particular deployment. Depth-frame monitor; harness-richness. |
| A-075 | Technically maintain the deployment | Phase 5 §Item 3 | Performs ongoing technical maintenance of the deployment. Depth-frame operate/perform. |
| A-076 | Diagnose and resolve deployment failures | Phase 5 §Item 3; Phase 5 §Item 1 | Diagnoses deployment-level failures surfaced by monitoring. Maintenance cycle diagnose→fix. |
| A-077 | Recover / roll back a failed deployment or configuration change | glossary `d1`; Phase 5 §Item 3 | Recovers from or rolls back a failed deployment or configuration change. Maintenance cycle recover; lifecycle rollback. |
| A-078 | Record deployment changes | glossary `d1`; Phase 5 §Item 3 | Records deployment and configuration changes for the deployment. Maintenance cycle record; lifecycle record. |
| A-079 | Report deployment health and status | Phase 5 §Item 3 (position-oriented reporting) | Reports deployment health and status at the appropriate position level. Depth-frame view/report. |
| A-080 | Escalate product-level defects upward to the D1 Technical Manager | Phase 5 §Item 3 (position hierarchy) | Escalates defects that are product-level (not deployment-specific) to the D1 Technical Manager or upward. Depth-frame escalate. |

### R-07 — D2 Assistant

| ID | Action | Source | Notes |
|---|---|---|---|
| A-081 | Conduct the design on the Designer's behalf | completions.md C-2026-07-19-1; Phase 4 §Item 2 | Drives the D2 design process for the Designer so he never addresses an internal node or service directly. Job-function. |
| A-082 | Answer the Designer's queries | completions.md C-2026-07-19-1; Phase 4 §Item 3 | Answers his natural-language design-inspection and status queries, locating the relevant design state. Intention lens (single point of contact). |
| A-083 | Interpret and route Designer input to the right D2 function | completions.md C-2026-07-19-1; Phase 2 §4.2 | Interprets input (direction, clarification, criticism, investigation, intervention) and routes it internally; D2 owns interaction routing. |
| A-084 | Preserve interaction context across the design run | completions.md C-2026-07-19-1; Phase 2 §4.3 | Preserves sufficient interaction and design context so the Designer need not reconstruct it for different internal recipients. |
| A-085 | Present the Designer's output | completions.md C-2026-07-19-1; Phase 3 (interaction classes) | Presents completion reports, Review Stops, Clarification Requests, and human-readable summaries organized for design judgment. |
| A-086 | Provide progressive drill-down / deeper information on request | Phase 2 §3.4; Phase 4 §Item 3 | Lets the Designer move from high-level observation toward progressively deeper investigative views. Harness-richness (make-visible). |
| A-087 | Orient the Designer at the entry point | method §1 (entry point); completions.md C-2026-07-19-1 | Orients him with the concepts D2 needs so he can decide whether to use D2. |
| A-088 | Make the D2 process observable to the Designer | Phase 2 §Principle 2; Phase 2 §3.2 | Surfaces human-oriented progress and behavioral-health views so the Designer can independently recognize when intervention is warranted. Harness-richness (monitor/make-visible). |
