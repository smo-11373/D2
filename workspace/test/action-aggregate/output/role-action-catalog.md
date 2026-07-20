# Role–Action Aggregate Catalog

*Deliverable 1 of the Action-Aggregate node (contract §1.1) — the actions each recognized role
performs, merged, grouped by role, stable IDs, each row `Source`-cited, each role and each action
carrying a substantial description. Target = the common, anticipable set (open-list). Derived from
the frozen constitution (Phases 1–5) + Designer-originated completions + the method (§1) + the rules
(`RU-*`), inventing nothing.*

## Roles

Layer order D2 → D1 → D0. IDs `R-00…R-06` are **pinned by the inputs' own hints** — glossary fixes
`R-00` (D2 Designer), `R-01` (D1 Designer), `R-05` (D0 Operator), `R-06` (D0 Technical Manager);
`RU-01` fixes `R-04` (D1 Technical Manager); Phase 5 §Item 3's enumeration order fixes `R-02`
(Design Node Builder) before `R-03` (D1 Programmer). The completion-added **D2 Assistant** is
appended as `R-07` precisely to preserve those pinned IDs, though it is a D2-layer position.

| ID | Role | Relationship | Description | Source |
|---|---|---|---|---|
| R-00 | D2 Designer | intrinsic | Builds and governs the D2 product itself; **not** a user of D2. Holds Designer-originated completion/clarification authority over D2's intentionally-open working sets and retains effective authority over D2's own material direction. | glossary `d2-designer`; Phase 5 §Item 2 |
| R-01 | D1 Designer | intrinsic | The **primary and only user of D2**. Directs the evolution of a predecessor D1 into a materially revised successor D1, holding effective design authority while D2 minimizes his attention cost. Interacts passively (responds to what D2 brings) and actively (his own initiative). | glossary `d1-designer`; Phase 1 §2; Phase 5 §Item 3; method §1 |
| R-02 | Design Node Builder | intrinsic | A bounded design-node agent (sub-human authority) that investigates, designs, verifies/enforces, justifies, and submits a node result within its governing contract, and may spawn children. | Phase 5 §Item 3; Phase 4 §Item 2; glossary `design-node` |
| R-03 | D1 Programmer | default | Implements product code according to the implementation specification, without reconstructing the earlier design process. | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | default | Maintains and upgrades the technical product package **within the established design and without changing code** (governed parameters, packaging/release, wrapper health). | Phase 5 §Item 3; RU-01; glossary `d1` |
| R-05 | D0 Operator | default | Performs routine operation and routine user-level monitoring of a deployed D0 product within approved operating choices. | Phase 5 §Item 3; glossary `d0`, `user` |
| R-06 | D0 Technical Manager | default | Installs and technically maintains a particular D0 deployment; provides front-line support for that deployment. | Phase 5 §Item 3; glossary `d0` |
| R-07 | D2 Assistant | intrinsic | The D1 Designer's **single unified point of contact** with the entire D2 system (a Human-Position-First position occupied by a D2 agent): conducts the design on his behalf, interprets/routes his input while preserving context, and presents his output. | completions.md C-2026-07-19-1; Phase 2 §Principle 3 |

**Relationship tag.** *intrinsic* = structural to the D2→D1→D0 ecosystem regardless of project
(the D2-mechanism positions, always present); *default* = a D2-provided position the D1 Designer
may adapt to the specific D1/D0 he is building (the product-dependent worker cast). *(glossary
`role`.)*

## Actions

*Stable IDs `A-001…`; **`A-003` retired — skipped**. `[P]`/`[A]` mark the D1 Designer's
passive/active sub-split (method §1).*

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-001 | Build and govern the D2 product (setup defaults, design tree, design-node modules, tools). | glossary `d2`, `d2-designer` | Job function; the meta-builder work D2 exists as. |
| A-002 | Originate completion / clarification / expansion of D2's intentionally-open working sets at a low hurdle. | Phase 5 §Item 2; completions.md C-2026-07-19-1 | The mechanism the D2 Assistant completion itself used; distinct from bottom-up revision. |
| A-004 | Approve or reject material revision proposals to **Designer-governed** D2 design. | Phase 4 §Item 2; Phase 1 §2.2 | Retains effective authority; A-003 retired. |

### R-01 — D1 Designer

*Passive `[P]` — he responds to something D2 brings (a review point, a clarification point, a
report). Active `[A]` — he acts on his own initiative. (method §1; Phase 4 §Item 2/3.)*

| ID | Action | Source | Notes |
|---|---|---|---|
| A-005 | Decide whether to use D2 for this upgrade (the entry point). | method §1; Phase 1 §2 | [P] First decision; D2 orients him. |
| A-006 | Establish / confirm the Designer–D2 operating contract (intervention posture, defaults). | Phase 3 §Item 1 | [P] Normal action = accept defaults. |
| A-007 | Establish the roles table and the run's default design posture (setup). | method §1; Phase 3 §Item 1 | [P] Cast of roles, each intrinsic or changeable default. |
| A-008 | Establish the initial design input — the predecessor D1 package and the intended change. | Phase 3 §Item 2; Phase 1 §3–4 | [P] Change may be loosely structured; not fully specified. |
| A-009 | Review / confirm the initial design understanding and direction at the Review Stop. | Phase 3 §Item 3 | [P] Optional courtesy/control boundary. |
| A-010 | Confirm the D1 foundational documents / D1 Constitution at the key Review Stop. | method §1; Phase 4 §Item 2 | [P] Constitution node = natural Review Stop. Lifecycle: *foundational docs*. |
| A-011 | Confirm the D1 Design Operating Framework (skeleton, inherited rules, control points). | Phase 4 §Item 1 | [P] Lifecycle: *operating framework* (D2-prepared, Designer-confirmed). |
| A-012 | Respond to Clarification Requests (material judgment D2 cannot resolve by investigation). | Phase 3 §Phase-Wide Rule; Phase 4 §Item 2 | [P] |
| A-013 | Review a proposed node design and its proposed spawning strategy. | Phase 4 §Item 2 | [P] Attention increases with node height. |
| A-014 | Receive and read the Designer-oriented completion reports. | Phase 3 §Phase-Wide Rule | [P] Every item observable; response optional. |
| A-015 | Approve or reject upward revision proposals affecting **Designer-governed** nodes. | Phase 4 §Item 2 | [P] Designer control prevents silent revision, not upward feedback. |
| A-016 | Monitor the D1 design process's progress and evolution. | Phase 2 §Principle 2; Phase 4 §Item 3 | [A] |
| A-017 | Monitor design-process **cost and time** (elapsed time, spend, costliest nodes). | Phase 4 §Item 3 | [A] Distinct from health (distinctness guard). |
| A-018 | Monitor design-process **health** / detect abnormal process behavior. | Phase 4 §Item 3; Phase 2 §3.1 | [A] Harness bias; distinct from cost. |
| A-019 | Inspect / inquire into the emerging D0 design (structure, files, algorithms, monitoring design). | Phase 4 §Item 3 | [A] Natural-language ask; D2 locates state. |
| A-020 | Drill down / investigate progressively from high-level observation toward detail. | Phase 2 §3.4; Phase 4 §Item 3 | [A] Observability enables informed intervention. |
| A-021 | Critically investigate a suspected design or process problem. | Phase 4 §Item 3; Phase 2 §4.4 | [A] Skeptical/critical investigation mode. Harness bias. |
| A-022 | Issue Designer directives — suspend a branch, reserve approval authority, redirect. | Phase 4 §Item 3 | [A] Recognized as authority actions, applied promptly. |
| A-023 | Lay down a rule / policy boundary governing the design. | Phase 4 §Item 3; Phase 5 §Item 3 | [A] D1 Designer controls = policy boundaries, invariants. |
| A-024 | Tune the resolution / intervention-depth parameter (manage his own attention budget). | Phase 2 §2.6 | [A] **Intention lens**: intent to govern attention cost → tune depth. |
| A-025 | Propose a Designer-initiated change (evaluate as a dry-run, then formally propose). | RU-06; Phase 4 §Item 2 | [A] Usually after discussion; evaluation commits nothing. |
| A-026 | Configure D1 Designer controls — semantic meaning, policy boundaries, algorithmic behavior, product invariants, supported operating models. | Phase 5 §Item 3 | [A] Position-oriented configuration. |
| A-027 | Hold and act on D0-user optimization — design the D1/D0 with the D0 users in view. | method §1; Phase 5 §Item 3 | [A] **Intention lens**: standing consideration his purpose demands. |
| A-028 | Audit the completed D2 design process (was D1 designed well — cost, attention cost, improvements). | Phase 3 §Item 5 | [A] **Intention lens**: distinct from reviewing whether D1 itself is good. |

### R-02 — Design Node Builder

| ID | Action | Source | Notes |
|---|---|---|---|
| A-029 | Investigate autonomously (study the predecessor D1, evidence, and material uncertainty) before escalating. | Phase 4 §Item 2; Phase 2 §2.1 | Investigate-before-escalate bias. |
| A-030 | Develop candidate designs and design the node internally. | Phase 4 §Item 2 | |
| A-031 | Produce the Node Design Specification (the node result). | Phase 4 §Item 2 | Intention lens: the result the position must produce. |
| A-032 | Check, test, and verify the node against its harness before advancing. | Phase 5 §Item 1; Phase 2 §Principle 4; Phase 4 §Item 2 | Harness bias; conformance staged before spawning. |
| A-033 | Enforce the rules the node's own data specifies. | glossary `design-node`; Phase 4 §Item 2 | Standard-enforcer facet of the node. |
| A-034 | Justify the result and submit the submission package upward for acceptance. | RU-02; glossary `submission-package` | Submission ≠ acceptance. |
| A-035 | Accumulate and prepare consolidated, high-leverage Clarification Requests. | Phase 4 §Item 2; Phase 2 §2.3 | Elevate repeated local questions into one high-level decision. |
| A-036 | Prepare the Designer-oriented node report. | Phase 4 §Item 2; Phase 1 §2.4 | Human-oriented, not machine records. |
| A-037 | Spawn children (by the Designer's potential actions) and compile their governing contracts with read-only input links. | RU-03; RU-04; RU-08; RU-10 | Decompose freely, aggregate always; passive-spawn first. |
| A-038 | Propose upward revision to governing design (evaluate, then propose) and **halt** on an open proposal. | Phase 4 §Item 2; RU-04; RU-05; RU-06 | Halt is the rule's constraint on this action, not a separate row. |

### R-03 — D1 Programmer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-039 | Receive the implementation specification (design→programming hand-off). | Phase 5 §Item 3 | Lifecycle hand-off (receive side); implement without reconstructing design. |
| A-040 | Implement product code according to the implementation specification. | Phase 5 §Item 3 | Lifecycle: *implement*. Depth frame: operate/perform. |
| A-041 | Test and verify the implementation against the specification and harness. | Phase 5 §Item 1; Phase 2 §Principle 4 | Lifecycle: *test*. Harness bias. |
| A-042 | Diagnose and handle implementation errors surfaced in testing. | Phase 5 §Item 1; Phase 4 §Item 2 | Depth frame: handle routine errors; failure visibility. |
| A-043 | Escalate / propose upward when the specification is insufficient or infeasible. | Phase 5 §Item 3; Phase 4 §Item 2 | Depth frame: escalate; position hierarchy. |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-044 | Configure product-level controls — product/provider defaults, retry policy within ranges, resource profiles, supported feature-policy. | Phase 5 §Item 3 | Position-oriented configuration. |
| A-045 | Upgrade the product by adjusting an authorized governed parameter **without changing code**. | Phase 5 §Item 3; RU-01 | Lifecycle: *upgrade*. Depth frame: operate/perform. |
| A-046 | Run the required validation / regression (upgrade smoke-test) harness on a change. | Phase 5 §Item 3; glossary `d1`; RU-01 | "No code change does not mean no harness." Lifecycle: *re-test*. |
| A-047 | Repackage, update release state, and distribute the product (release/packaging parameters). | Phase 5 §Item 3 | Lifecycle: *package* + hand-off (produce side) to R-06. |
| A-048 | Record the upgrade / maintain the upgrade records. | glossary `d1`; Phase 5 §Item 3 | Lifecycle: *record*. Maintenance cycle. |
| A-049 | Maintain the D1 wrapper's health/performance monitoring (e.g. D0-crash detection). | glossary `d1`, `half-level`; Phase 5 §Item 1 | Harness bias; owns the *detect* transition (half a level above D0). |
| A-050 | Recover from a failed upgrade — roll back within the established design. | Phase 5 §Item 3; glossary `d1` | Lifecycle: *recover/rollback* (product level). Maintenance cycle. |
| A-051 | Escalate to the D1 Designer / D1 Programmer when a change requires redesign or code. | Phase 5 §Item 3 | Position hierarchy; do not perform above authority. |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|---|---|---|---|
| A-052 | Operate the D0 product (routine operation). | Phase 5 §Item 3 | Lifecycle: *operate*. Depth frame: operate/perform. |
| A-053 | Perform routine user-level monitoring of D0. | Phase 5 §Item 3 | Lifecycle: *monitor*. Harness bias. |
| A-054 | Configure operator controls — routine scheduling, collection scope, approved operating choices. | Phase 5 §Item 3 | Position-oriented configuration. |
| A-055 | Monitor D0 spend against the daily spending limit. | Phase 5 §Item 3 | Cost monitoring — distinct from health (distinctness guard). |
| A-056 | View the user-level D0 health report / health status. | Phase 5 §Item 3; Phase 4 §Item 3; glossary `d1` | Health-visibility (harness); distinct from spend. |
| A-057 | Handle routine operating errors / respond to routine failures. | Phase 5 §Item 3; Phase 5 §Item 1 | Depth frame: handle routine errors. |
| A-058 | Escalate to the D0 Technical Manager for issues beyond routine operation. | Phase 5 §Item 3; glossary `d0` | Depth frame: escalate; front-line support sits above. |

### R-06 — D0 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-059 | Install the D0 deployment (receive the distributed package and deploy it). | Phase 5 §Item 3; glossary `d1` | Lifecycle: *install/deploy* + hand-off (receive side) from R-04. |
| A-060 | Smoke-test the deployment / verify deployment health on install (the hand-off gate). | Phase 5 §Item 3; Phase 2 §Principle 4; glossary `d1` | Lifecycle: *smoke-test*; the verification gate of the hand-over. |
| A-061 | Technically maintain the deployment on an ongoing basis. | Phase 5 §Item 3 | Depth frame: operate/perform. |
| A-062 | Configure deployment controls — paths, storage endpoints, service config, resource limits, credential integration, deployment health settings. | Phase 5 §Item 3 | Position-oriented configuration. |
| A-063 | Monitor deployment health. | Phase 5 §Item 3 | Harness bias; distinct from D1-wrapper monitoring (A-049). |
| A-064 | Provide front-line support / diagnose deployment issues. | glossary `d0`; Phase 5 §Item 3 | Maintenance cycle: diagnose. |
| A-065 | Recover the deployment from a failed change (rollback the deployment). | Phase 5 §Item 3 | Lifecycle: *recover/rollback* (deployment level). Maintenance cycle. |
| A-066 | Re-deploy the upgraded package. | glossary `d1`; Phase 5 §Item 3 | Lifecycle: *re-deploy*. |
| A-067 | Escalate upstream when an issue exceeds deployment maintenance (needs a product change). | Phase 5 §Item 3 | Position hierarchy: escalate to R-04/upstream. |

### R-07 — D2 Assistant

| ID | Action | Source | Notes |
|---|---|---|---|
| A-068 | Serve as the single unified Designer interaction point (the Designer never addresses an internal node directly). | completions.md C-2026-07-19-1; Phase 2 §Principle 3 | Gating position; D2 owns the interaction burden. |
| A-069 | Conduct the design on the Designer's behalf and answer his queries. | completions.md C-2026-07-19-1 | Intention lens: the result this position must produce. |
| A-070 | Interpret and route the Designer's input to the right D2 function. | completions.md C-2026-07-19-1; Phase 2 §4.2 | D2 owns interaction routing. |
| A-071 | Preserve interaction and design context across interactions. | completions.md C-2026-07-19-1; Phase 2 §4.3 | So the Designer need not reconstruct context. |
| A-072 | Present the Designer's output — completion reports, Review Stops, Clarification Requests, human-readable summaries. | completions.md C-2026-07-19-1; Phase 3 §Phase-Wide Rule | Human-oriented presentation. |
| A-073 | Support progressive drill-down / deeper investigation on request. | completions.md C-2026-07-19-1; Phase 2 §3.4 | From summary toward detail. |
| A-074 | Present human-readable observability of D2's progress and behavioral health (make the process visible). | Phase 2 §Principle 2 (§3.1–3.2) | Harness bias: make-visible, so the Designer can initiate intervention. |

---

*Open-list (method §1): this is the common, anticipable set, not a closed enumeration. Naming,
granularity, and the elaborated tail are the permitted residual variation; the roles and the
distinct responsibilities are the pinned core.*
