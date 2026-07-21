# Role–Action Aggregate Catalog

*Derived by the design-node algorithm (`framework/design-node-algorithm.md`) from the frozen
fundamentals only — the constitution (Phases 1–5), the Designer completions
(`completions.md`), the method (`method §1`), the rules (`RU-*`), the glossary, and the
framework docs. Every row is Source-cited in-namespace (`sources.md`). Recall-first: every
plausible, traceable, distinct action is kept; only literal duplicates and rule-restatements
are removed. `A-003` is retired and skipped.*

## Roles

Roles are seeded from **Phase 5 §Item 3 (Human Position First)** — the named conceptual
positions — completed by **`completions.md C-2026-07-19-1`** (the D2 Assistant) and ordered by
the **layer model D2 → D1 → D0** (`method §1`; `glossary \`role\``). IDs follow the anchors the
fundamentals already pin: `R-00` D2 Designer and `R-01` D1 Designer (`glossary`), `R-04` D1
Technical Manager (`RU-01`), `R-05` D0 Operator and `R-06` D0 Technical Manager (`glossary \`d0\``).

| ID | Role | Relationship | Description | Source |
|---|---|---|---|---|
| R-00 | D2 Designer | intrinsic · D2 (meta / builder) | Builds the D2 product and authors its living design record; **not** a user of D2. Holds Designer-originated completion/clarification authority over D2's intentionally-open working sets and revision authority over Designer-governed D2 design. | `glossary \`d2-designer\``; Phase 5 §Item 2 |
| R-01 | D1 Designer | intrinsic · D1 (primary user of D2) | The primary and only user of D2. Directs the evolution of a Predecessor D1 into a materially revised successor D1; retains effective design authority while D2 reduces his attention cost. Designs D1 to serve the D0 users. | Phase 1 §2; `glossary \`d1-designer\``; Phase 5 §Item 3 |
| R-02 | Design Node Builder | intrinsic · D1 design mechanism | A bounded design worker treated position-first as a person with a narrow relevant skill set. Builds the current Design Node — investigate, design, check/test, submit, enforce, revise — within its governing contract and sandbox. | Phase 5 §Item 3; Phase 4 §Item 2; `glossary \`design-node\`` |
| R-03 | D1 Programmer | default · D1 (implementation) | Changes product code according to implementation specifications. Implements the completed design without reconstructing the earlier design process (the design→programming handoff). | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | default · D1 / D0 boundary (product package) | Maintains and upgrades the technical product package within the established design **without changing product code**: adjusts governed parameters, runs the validation/regression harness, updates release state, repackages, and distributes. | Phase 5 §Item 3; `RU-01`; `glossary \`d1\`` |
| R-05 | D0 Operator | default · D0 (operation) | Performs routine operation of the distributable D0 product and routine user-level monitoring, within operator-level control boundaries. | Phase 5 §Item 3; `glossary \`d0\`` |
| R-06 | D0 Technical Manager | default · D0 (deployment) | Installs and technically maintains a particular D0 deployment; provides front-line support to the D0 Operator. | Phase 5 §Item 3; `glossary \`d0\`` |
| R-07 | D2 Assistant | intrinsic · D2 (unified interaction point) | The D1 Designer's single, unified point of contact with the entire D2 system — designed position-first, occupied by a D2 agent. Conducts the design on the Designer's behalf, interprets and routes his input while preserving context, and presents his output. | `completions.md C-2026-07-19-1`; Phase 2 §Principle 3; Phase 4 §Item 3 |

## Actions

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-001 | Author and build the D2 design record | `glossary \`d2-designer\``; Phase 5 §Item 2 | Constructs D2's constitution, method, rules, and living catalogs — the design system the D1 Designer will use. |
| A-002 | Issue Designer-originated completions/clarifications to D2's open working sets | Phase 5 §Item 2; `completions.md C-2026-07-19-1` | Low-hurdle completion/clarification/expansion of intentionally-open sets (glossary, query catalog, Phase 5) when consistent with established design; these govern alongside the frozen baseline. |
| A-004 | Exercise revision authority over Designer-governed D2 design (approve/reject material revisions) | Phase 4 §Item 2; Phase 5 §Item 2 | The builder holds continuing revision authority; material change to Designer-governed D2 design requires his approval — `A-003` retired. |

### R-01 — D1 Designer

*Passive [P] — he responds to what D2 brings him; Active [A] — he acts on his own initiative
(`method §1`; Phase 4 §Item 2–3).*

| ID | Action | Source | Notes |
|---|---|---|---|
| A-005 | Decide whether to use D2 (the entry point) [P] | `method §1`; Phase 1 §2 | His first decision; D2 backs it by orienting him with the concepts it needs. |
| A-006 | Review and confirm the Designer–D2 operating contract / intervention posture [P] | Phase 3 §Item 1 | Accept the default operating posture (how D2 seeks intervention and how he observes/intervenes) via a compact checklist; the normal action is to accept defaults. |
| A-007 | Establish/confirm the initial design input (Predecessor D1 package + intended change) [P] | Phase 3 §Item 2; Phase 1 §3–4 | Supply the Predecessor D1 and an incremental expression of intended change in any useful initial form; not a full specification. |
| A-008 | Confirm the setup: the roles table and design posture/defaults [P] | `method §1`; Phase 3 §Item 1 | Establish the run's cast of roles and default design choices in one setup step. |
| A-009 | Establish the cast of roles / change role defaults for the project [P] | `method §1`; `glossary \`role\`` | Each role is intrinsic (fixed) or a D2-provided default the Designer may change for this project. |
| A-010 | Review the initial design understanding and direction (Review Stop) [P] | Phase 3 §Item 3 | Optional courtesy/control review after D2 converges on its consolidated understanding and recommended direction. |
| A-011 | Confirm the D1 foundational documents / D1 Constitution at the key Review Stop [P] | `method §1`; Phase 4 §Item 1 | Combine setup skeleton + predecessor V1 + intended change into the D1 project's own constitution; strongly-encouraged Review Stop (a Constitution Node is a natural Designer-governed Review Stop). |
| A-012 | Review and confirm the D1 Design Operating Framework [P] | Phase 4 §Item 1 | One consolidated package — initial skeleton, inherited/derived D1 rules, D1-specific control points; accept, modify, request investigation, or discuss. |
| A-013 | Receive notification of entry into D1 design mode [P] | Phase 3 §Item 4 | D2 signals initial setup complete and D1 design begins. |
| A-014 | Answer a Clarification Request [P] | Phase 3; Phase 4 §Item 2 | Supply material design judgment D2 cannot reasonably resolve by further investigation; D2 consolidates high-leverage questions. |
| A-015 | Respond to a Review Stop (review now, or continue) [P] | Phase 3; Phase 4 §Item 2 | A control boundary for Designer-initiated intervention — no unresolved question is necessarily present. |
| A-016 | Receive and read Completion Reports [P] | Phase 3 | Every item is observable via a Designer-oriented completion report; response is optional unless a clarification is also requested. |
| A-017 | Review a Design Node's proposed design and spawning strategy [P] | Phase 4 §Item 2 | Attention generally increases with node height; higher nodes govern larger descendant regions. |
| A-018 | Set/confirm node revision authority (Designer-governed vs D2-governed), calling out exceptions [P] | Phase 4 §Item 2 | Framework supplies defaults by node level/class; the Designer mainly confirms recommended exceptions. Review and revision authority are represented separately. |
| A-019 | Monitor D1 design progress [A] | Phase 4 §Item 3; Phase 2 §Principle 2 | Independently determine whether the process is progressing as expected, not dependent on D2 detecting a problem first. |
| A-020 | Monitor design spend/cost and time consumption [A] | Phase 4 §Item 3 | E.g. how much time/cost the design has consumed, which nodes consumed the most. |
| A-021 | Monitor D1 design-process health and detect abnormal process behavior [A] | Phase 4 §Item 3; Phase 2 §Principle 2; Phase 5 §Item 1 | View the design health report; spot nodes with the most revisions or parts behaving abnormally (Harness First pointed at the process). |
| A-022 | Inspect/query the emerging D0 design (ask, inspect, drill down) [A] | Phase 4 §Item 3 | Natural-language design-oriented requests without identifying the internal node/service responsible. |
| A-023 | Investigate a suspected design or process problem (critical investigation) [A] | Phase 4 §Item 3; Phase 2 §Principle 2 | Ask D2 to critically examine a suspected flaw/assumption/failure condition and recommend action. |
| A-024 | View the Design Tree and what changed since the last review [A] | Phase 4 §Item 3 | Observe structure and recent evolution of the design. |
| A-025 | Request progressively deeper analysis (high-level → detail) [A] | Phase 2 §Principle 2; Phase 4 §Item 3 | Move from high-level observation toward detailed investigation before deciding whether to intervene. |
| A-026 | Issue a Designer directive (impose/reserve authority, suspend a branch, protect a design element) [A] | Phase 4 §Item 3 | Authority actions — e.g. "do not change Algorithm A without my approval", "stop the implementation branch until I review verification" — recognized and applied promptly. |
| A-027 | Lay down a design rule or invariant (redirect) [A] | Phase 4 §Item 3; `method §1` | Establish a governing rule/invariant; Designer intervention normally initiates governed action rather than directly mutating the tree. |
| A-028 | Propose a Designer-initiated change (usually after discussion) [A] | `RU-06`; Phase 4 §Item 2 | Evaluated (dry-run) before it is officially proposed; commits nothing until formalized. |
| A-029 | Tune the resolution-depth parameter (investigation / inference / intervention / deferral) [A] | Phase 2 §Item 6 (Principle 1) | Designer-controlled balance that alters investigation depth and attention cost without removing D2's duty to identify material uncertainty (manages his attention budget). |
| A-030 | Hold D0-user optimization as a standing design consideration [A] | `method §1`; Phase 5 §Item 3 | He designs D1 to serve the D0 users; the D0-user throughline shapes what the D1 system must do. |
| A-031 | Optionally audit the completed D2 design process [A] | Phase 3 §Item 5 | After the run, evaluate process cost, time, Designer attention cost, and candidate D2 improvements — asks whether D2 designed D1 well. |

### R-02 — Design Node Builder

| ID | Action | Source | Notes |
|---|---|---|---|
| A-032 | Receive the task of building the current Design Node | Phase 4 §Item 2 | Accepts a bounded design responsibility under its compiled governing contract. |
| A-033 | Investigate autonomously (study predecessor, inputs, and evidence) | Phase 4 §Item 2; Phase 2 §Principle 1 | Investigate before escalating; dig into available evidence to resolve material uncertainty early. |
| A-034 | Develop the node design / candidate design(s) | Phase 4 §Item 2 | Internal design and governance work toward a proposed node design. |
| A-035 | Check and test the node design internally (establish its verification harness) | Phase 4 §Item 2; Phase 2 §Principle 4; Phase 5 §Item 1 | Harness-richness: build the observation/testing/evaluation that makes deviation visible before realization. |
| A-036 | Produce the Node Design Specification / node result | Phase 4 §Item 2 | The proposed node design result, sufficiently explicit to hand down. |
| A-037 | Prepare a Designer-oriented node report | Phase 4 §Item 2; Phase 1 §2.4 | Human-oriented report (issue, rationale, alternatives, consequences) for review appropriate to the node's significance. |
| A-038 | Accumulate and prepare high-leverage Clarification Requests | Phase 4 §Item 2; Phase 2 §Principle 1 | Consolidate material questions into one high-leverage request where practical. |
| A-039 | Resolve the consequences of Designer answers and continue internal convergence | Phase 4 §Item 2 | Apply the answers and converge internally before returning. |
| A-040 | Author and own the node's data/table, enforcing the rules its data specifies | `RU-09`; `glossary \`design-node\`` | The node authors its own table and enforces its own rules; no node edits a table it does not author. |
| A-041 | Propose a spawning strategy | Phase 4 §Item 2; `RU-03` | Where node-building includes decomposition; spawning is distinct from general design advancement. |
| A-042 | Spawn child design nodes by the Designer's potential actions (passive/active) | `RU-03` | Children are determined by the actions the node's scope must support; passive-action spawning first. |
| A-043 | Compile/curate the child contract with owned data and read-only input links | `RU-04`; `RU-08` | Pass owned governing data down and curate relevant ancestor/sibling read-context links; filter non-applicable rules with traceable justification. |
| A-044 | Aggregate/integrate child pieces into the contracted deliverable | `RU-10` | Decompose internally to any depth but return the contracted aggregate at the boundary. |
| A-045 | Evaluate a proposed change before proposing it (dry-run: probe up and down) | `RU-06` | A separate step that commits nothing; returns an evaluation report before any official proposal. |
| A-046 | Propose upward revision to governing design and halt pending resolution | `RU-04`; `RU-05`; Phase 4 §Item 2 | Lower nodes may challenge higher design; an open upward proposal is a stopping point (no drift). |
| A-047 | Submit the submission package with its justification for parent acceptance | `RU-02`; `glossary \`submission-package\`` | The node justifies its own result; submission is not acceptance — the parent reviews and approves/rejects. |

### R-03 — D1 Programmer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-048 | Receive the implementation specification (design→programming handoff) | Phase 5 §Item 3 | The spec should be complete enough to implement without reconstructing the earlier design process. |
| A-049 | Implement product code per the implementation specification | Phase 5 §Item 3 | Changes product code according to the spec — realizes an understood design. |
| A-050 | Test the implementation against the specification | Phase 2 §Principle 4; Phase 5 §Item 1 | Verification before realization; harness-richness applied to code. |
| A-051 | Produce the built implementation (build artifact) | Phase 5 §Item 3; `framework/design-node-algorithm` | Lifecycle: implement → test → build; hands the result to the D1 Technical Manager for release. |
| A-052 | Hand over the built product to the D1 Technical Manager | `framework/design-node-algorithm`; Phase 5 §Item 3 | Forced lifecycle hand-off (produce/receive + verification gate) between implementation and product-package maintenance. |
| A-053 | Diagnose and fix implementation defects | Phase 5 §Item 3; Phase 2 §Principle 4 | Depth frame (handle errors): diagnose → fix within the code layer. |
| A-054 | Escalate to the D1 Designer when a change requires redesign, not just code | Phase 5 §Item 3 | Position hierarchy: do not resolve at the code layer a change that alters what the product is designed to be. |
| A-055 | Propose upward when the implementation spec is defective or infeasible | Phase 4 §Item 2 | Lower nodes retain the right to challenge higher design; Designer control prevents silent revision, not upward feedback. |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-056 | Adjust an authorized/governed product parameter without changing code | Phase 5 §Item 3; `RU-01` | The canonical example (timeout 5→10 min): modify the governed parameter within its control boundary, no code change. |
| A-057 | Run the required validation/regression harness after a change | Phase 5 §Item 3; `RU-01`; `glossary \`d1\`` | "No code change does not mean no harness" — the upgrade smoke-test / regression suite still runs. |
| A-058 | Update release state | Phase 5 §Item 3 | Advance the product's release/version state after an authorized change. |
| A-059 | Repackage the product | Phase 5 §Item 3 | Rebuild the distributable product package within the established design. |
| A-060 | Distribute/release the product package | Phase 5 §Item 3 | Deliver the repackaged product; a recipient may deploy just D0 while retaining D1 to manage it. |
| A-061 | Perform a controlled upgrade of the product within the established design | Phase 5 §Item 3; `glossary \`d1\`` | Technical maintenance/upgrade that does not alter product code or require substantive redesign. |
| A-062 | Re-test via the upgrade smoke-test suite after an upgrade | `glossary \`d1\``; Phase 5 §Item 1 | Lifecycle: upgrade → re-test before re-release. |
| A-063 | Roll back / recover from a failed upgrade or change | `framework/design-node-algorithm` (recover-from-a-failed-change); Phase 5 §Item 3 | Depth-frame recovery cycle for a maintenance/support position. |
| A-064 | Diagnose a product-package maintenance issue | Phase 5 §Item 3; `glossary \`d1\`` | Diagnose within the product-package scope before applying a fix. |
| A-065 | Maintain upgrade records | `glossary \`d1\``; `framework/design-node-algorithm` | Record the change — upgrade records are a wrapper-level lifecycle obligation. |
| A-066 | Configure product-level controls (defaults, provider defaults, retry policy within ranges, feature-policy choices, resource profiles, release/packaging parameters) | Phase 5 §Item 3 | Position-oriented configuration boundary for the D1 Technical Manager. |
| A-067 | Monitor product-level health/performance (D1 wrapper health-monitoring, D0-crash detection) | `glossary \`d1\``; `glossary \`half-level\``; Phase 5 §Item 1 | Half-a-level-above operational monitoring lives in the D1 wrapper; make failure visible (Harness First). |
| A-068 | Escalate to the D1 Designer/Programmer when a change requires redesign or code | Phase 5 §Item 3 | Position hierarchy: do not resolve at the package layer a change needing design or code change. |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|---|---|---|---|
| A-069 | Perform routine operation of the D0 product | Phase 5 §Item 3 | The position's core function — run the deployed distributable product. |
| A-070 | Perform routine user-level monitoring | Phase 5 §Item 3 | Routine user-level monitoring of ongoing operation. |
| A-071 | Detect/observe abnormal operation at the user level | Phase 5 §Item 3; Phase 5 §Item 1 | Harness-richness: surface user-visible failures/anomalies during operation. |
| A-072 | View the user-level D0 health report | Phase 4 §Item 3; Phase 5 §Item 3 | "What will the D0 health report look like to the user?" — the same event represented at operator level. |
| A-073 | Configure operator controls (daily spending limits, routine scheduling, collection scope, approved operating choices) | Phase 5 §Item 3 | Position-oriented configuration boundary for the D0 Operator. |
| A-074 | Handle routine operating errors within authority | Phase 5 §Item 3 | Depth frame (handle routine errors): resolve within the operator's authority. |
| A-075 | Escalate to the D0 Technical Manager for support beyond routine | Phase 5 §Item 3; `glossary \`d0\`` | Front-line support comes from the D0 Technical Manager; escalate rather than exceed authority. |

### R-06 — D0 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-076 | Install/deploy a particular D0 deployment | Phase 5 §Item 3; `glossary \`d0\`` | Installs and stands up a specific deployment of the distributable product. |
| A-077 | Smoke-test the deployment after install | `glossary \`d1\``; `framework/design-node-algorithm`; Phase 5 §Item 1 | Forced lifecycle step: you cannot reach "operator running it" from "installed" without a smoke-test gate. |
| A-078 | Configure deployment controls (deployment paths, storage endpoints, service configuration, resource limits, credential integration, deployment health settings) | Phase 5 §Item 3 | Position-oriented configuration boundary for the D0 Technical Manager. |
| A-079 | Technically maintain the deployment | Phase 5 §Item 3; `glossary \`d0\`` | Ongoing technical maintenance of the particular deployment. |
| A-080 | Monitor deployment health | Phase 5 §Item 3; Phase 5 §Item 1 | Deployment health settings imply monitoring the specific deployment's health (Harness First). |
| A-081 | Provide front-line support to the D0 Operator | `glossary \`d0\``; Phase 5 §Item 3 | First point of technical support for operator-raised issues. |
| A-082 | Diagnose a deployment issue | Phase 5 §Item 3 | Depth-frame diagnose step within deployment scope. |
| A-083 | Recover the deployment from a failed change | `framework/design-node-algorithm` (recover-from-a-failed-change) | Depth-frame recovery for a support/maintenance position. |
| A-084 | Record deployment changes | `framework/design-node-algorithm`; `glossary \`d1\`` | Record-the-change step of the maintenance cycle. |
| A-085 | Escalate to the D1 Technical Manager for product-package issues beyond the deployment | Phase 5 §Item 3 | Position hierarchy: route product-package problems up from the deployment layer. |

### R-07 — D2 Assistant

| ID | Action | Source | Notes |
|---|---|---|---|
| A-086 | Conduct the design on the Designer's behalf and answer his queries | `completions.md C-2026-07-19-1` | The interaction front does real work — conducting and answering — that no other named position owns. |
| A-087 | Interpret and route Designer input to the right D2 function | `completions.md C-2026-07-19-1`; Phase 2 §Principle 3 | D2 owns interaction routing; the Designer need not select among internal components. |
| A-088 | Preserve interaction and design context across interactions | `completions.md C-2026-07-19-1`; Phase 2 §4.3 | The Designer interacts without repeatedly reconstructing context for different internal recipients. |
| A-089 | Present the Designer's output (completion reports, Review Stops, Clarification Requests, human-readable summaries) | `completions.md C-2026-07-19-1`; Phase 3 | Human-oriented presentation with drill-down; the Designer never addresses an internal node directly. |
| A-090 | Locate the relevant design state for a natural-language request | Phase 4 §Item 3; `completions.md C-2026-07-19-1` | D2 bears the burden of finding the relevant design state and interpreting the request. |
| A-091 | Support progressive drill-down from high-level to detail | Phase 2 §Principle 2; Phase 4 §Item 3 | Observability that enables informed Designer-initiated intervention, not merely passive reporting (Harness First on visibility). |
| A-092 | Own the interaction burden as the single unified point of contact | `completions.md C-2026-07-19-1`; Phase 2 §Principle 3 | D2 owns the interaction burden so the Designer addresses one system, not internal nodes/services. |
