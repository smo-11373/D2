# Role–Action Aggregate Catalog — the Action-Aggregate node's result

*Product 1 of 3 (contract §1). The actions each recognized role performs, merged and grouped by
role, stable IDs, every row Source-cited in-namespace (`sources.md`). Target = the common,
anticipable set (open list). `[P]` passive / `[A]` active applies to the D1 Designer's journey;
facet tags (operate/monitor/configure/view/handle-errors/escalate; diagnose→fix→recover→record)
mark depth-frame derivations; `[H]` marks a harness-richness row (test / monitor / detect / make
visible). `A-003` is retired and skipped.*

## Roles

| ID | Role | Relationship | Description | Source |
|---|---|---|---|---|
| R-00 | D2 Designer | Intrinsic (meta / builder) | Builds and evolves the D2 product (setup defaults, design tree, design-node modules); **not** a user of D2. Holds Designer-originated completion authority over D2's living working sets and top acceptance authority over design results. | glossary `d2-designer`; Phase 5 §Item 3 |
| R-01 | D1 Designer | Intrinsic (primary user) | The **primary and only user of D2**. Directs the evolution of a Predecessor D1 into a successor D1, retaining effective design authority while D2 minimizes his attention cost; designs with D0-user optimization in view. | glossary `d1-designer`; Phase 1 §2; Phase 5 §Item 3 |
| R-02 | Design Node Builder | Intrinsic (D2-internal) | A D2-internal position that builds one bounded design node from a clear contract / inputs / harness — investigating, designing, testing, submitting, enforcing, and spawning within local autonomy. | Phase 5 §Item 3; Phase 4 §Item 2 |
| R-03 | D1 Programmer | Default (D1 project) | Implements D1/D0 product code from the implementation specification, ideally without reconstructing the earlier design process. | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | Default (D1 project) | Maintains and upgrades the technical product package **within the established design, without changing product code** — adjusting governed parameters, running the harness, repackaging, distributing. | Phase 5 §Item 3; RU-01 |
| R-05 | D0 Operator | Default (D0) | Performs **routine operation and routine user-level monitoring** of a running D0 deployment, within approved operating choices. | Phase 5 §Item 3; glossary `d0` |
| R-06 | D0 Technical Manager | Default (D0) | Installs and technically maintains a **particular D0 deployment**; front-line support for the D0 Operator. | Phase 5 §Item 3; glossary `d0` |
| R-07 | D2 Assistant | Intrinsic (D2 interaction) | The D1 Designer's **single unified point of contact** with the entire D2 system; conducts the design on his behalf, interprets and routes his input while preserving context, and presents his output. Designed position-first, occupied by a D2 agent. | completions.md C-2026-07-19-1; Phase 2 §Principle 3 |

## Actions

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-001 | Build and evolve the D2 product (setup defaults, design tree, design-node modules) | glossary `d2-designer`; glossary `d2` | Core job function |
| A-002 | Complete / clarify / expand D2's intentionally-open living working sets (low hurdle, consistent with established design) | Phase 5 §Item 2; glossary `d2-designer` | Designer-originated completion |
| A-004 | Review and approve / reject proposed D2 revisions surfaced by the optional D2-process audit (no silent modification of working sets) | Phase 3 §Item 5 | [A-003 retired] |
| A-005 | Exercise top acceptance authority — approve or reject design-node submission packages (parent-as-enforcer) | RU-02; Phase 1 §2.2 | |

### R-01 — D1 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-006 | Decide whether to use D2 (entry point); D2 backs the decision by orienting him | method §1; Phase 3 §Item 1 | [P] entry |
| A-007 | Establish and confirm the Designer–D2 operating contract (how D2 seeks intervention, how he observes/intervenes; normally accept defaults) | Phase 3 §Item 1 | [P] |
| A-008 | Establish the initial design input — the Predecessor D1 package and the expression of intended change | Phase 3 §Item 2 | [P] |
| A-009 | Review the initial design understanding and direction at the default Review Stop | Phase 3 §Item 3 | [P] review/stop |
| A-010 | Acknowledge entry into D1 design mode (setup-complete notification) | Phase 3 §Item 4 | [P] completion report |
| A-011 | Review and confirm the D1 Design Operating Framework (skeleton, inherited rules, control points, revision-authority defaults) | Phase 4 §Item 1 | [P] |
| A-012 | Confirm the D1 Constitution / foundational documents at the strongly-encouraged key Review Stop | method §1; Phase 4 §Item 2 | [P] |
| A-013 | Respond to Clarification Requests — supply material design judgment D2 cannot resolve by investigation | Phase 3 §Phase-Wide Rule; Phase 4 §Item 2 | [P] clarification |
| A-014 | Review node designs at Review Stops, attention scaled to node height (higher nodes get more) | Phase 4 §Item 2 | [P] |
| A-015 | Inspect the emerging D0 design and D1 process — ask, show, explain, trace, compare, and drill down through the unified interaction point | Phase 4 §Item 3 | [A] inspect |
| A-016 | Investigate a suspected design or process problem — critically examine and recommend action | Phase 4 §Item 3 | [A] investigate |
| A-017 | Monitor D1 design **progress — time and cost** (elapsed time, spend, per-node consumption) | Phase 4 §Item 3 | [A][H] monitor cost |
| A-018 | Monitor D1/D0 design **health** (design health report, abnormal behavior, revision counts) | Phase 4 §Item 3; Phase 2 §Principle 2 | [A][H] monitor health (distinct from A-017) |
| A-019 | Issue Designer directives — impose/revise a rule, reserve approval authority, suspend or stop a branch | Phase 4 §Item 3; Phase 4 §Item 2 | [A] directive |
| A-020 | Propose and evaluate a Designer-initiated design change (evaluate-then-propose dry-run before committing) | RU-06 | [A] |
| A-021 | Direct D1 design toward D0-user optimization (specify user priorities, skill level, user-level concerns) | method §1; Phase 5 §Item 3 | [A] D0-user throughline |
| A-022 | Set D1 Designer-level product controls — semantic meaning, policy boundaries, algorithmic behavior, product invariants, supported operating models | Phase 5 §Item 3 | [A] configure |
| A-023 | Optionally audit the D2 design process after a completed run (process cost, time, attention cost, improvement points) | Phase 3 §Item 5 | [A][H] check how well D2 served him |

### R-02 — Design Node Builder

| ID | Action | Source | Notes |
|---|---|---|---|
| A-024 | Work within the node's governing contract / sandbox (bounded inputs, harness, permitted changes, expected output) | Phase 5 §Item 5; Phase 4 §Item 2; RU-08 | |
| A-025 | Investigate autonomously to build the node, resolving material uncertainty before escalating | Phase 4 §Item 2; Phase 2 §Principle 1 | |
| A-026 | Develop candidate designs and author the Node Design Specification (the node's owned data) | Phase 4 §Item 2; RU-09 | author own table |
| A-027 | Verify and test the node design against its harness before advancing | Phase 4 §Item 2; Phase 2 §Principle 4; Phase 5 §Item 1 | [H] verify/test |
| A-028 | Enforce the rules its owned data specifies | glossary `design-node`; RU-09 | |
| A-029 | Accumulate and raise consolidated Clarification Requests when material Designer judgment is required | Phase 4 §Item 2 | |
| A-030 | Prepare the Designer-oriented node report and submit the package with its own justification for acceptance | Phase 4 §Item 2; RU-02 | submission ≠ acceptance |
| A-031 | Propose a spawning strategy and spawn child nodes driven by the Designer's passive/active actions | Phase 4 §Item 2; RU-03; RU-10 | |
| A-032 | Propose upward revision to governing design (evaluate-then-propose; stop on a pending upward proposal) | RU-04; RU-05; RU-06 | propose-up, no drift |

### R-03 — D1 Programmer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-033 | Implement product code per the implementation specification, without reconstructing the design | Phase 5 §Item 3 | operate/perform |
| A-034 | Verify and test the implementation against the specification and its harness | Phase 5 §Item 1; Phase 2 §Principle 4 | [H] test |
| A-035 | Handle and surface build / implementation failures (make failure visible) | Phase 5 §Item 1 | [H] handle-errors |
| A-036 | Escalate specification ambiguity or infeasibility upward to the D1 Designer | Phase 5 §Item 3; Phase 4 §Item 2 | escalate / upward feedback |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-037 | Adjust governed product parameters within the established design without changing code (defaults, provider defaults, retry policy within range, resource profiles, feature-policy, packaging params) | Phase 5 §Item 3; RU-01 | configure/control |
| A-038 | Run the required validation / regression harness (upgrade smoke-test suite) after a change | Phase 5 §Item 3; RU-01; glossary `d1` | [H] test — "no code change ≠ no harness" |
| A-039 | Update release state, repackage, and distribute the upgraded product | Phase 5 §Item 3 | fix/apply |
| A-040 | Record the change and maintain upgrade records | glossary `d1` | record-the-change |
| A-041 | Diagnose a technical maintenance issue and judge whether it is governable without code | Phase 5 §Item 3 | diagnose; lowest-position |
| A-042 | Recover from a failed upgrade (roll back release state) | glossary `d1`; Phase 5 §Item 3 | recover-from-failed-change |
| A-043 | Monitor product/package technical health and upgrade readiness | glossary `d1`; Phase 5 §Item 1 | [H] monitor |
| A-044 | Escalate to the D1 Designer / D1 Programmer when a change requires code or redesign | Phase 5 §Item 3 | escalate |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|---|---|---|---|
| A-045 | Operate the D0 product routinely, within approved operating choices | Phase 5 §Item 3; glossary `d0` | operate/perform |
| A-046 | Configure routine operating controls (daily spending limits, routine scheduling, collection scope, approved choices) | Phase 5 §Item 3 | configure |
| A-047 | Perform routine user-level monitoring | Phase 5 §Item 3 | [H] monitor |
| A-048 | View the D0 user-facing health / status report | Phase 4 §Item 3; Phase 5 §Item 1; glossary `d0` | [H] make-visible (distinct artifact from A-047) |
| A-049 | Handle routine operating errors | Phase 5 §Item 1 | handle-errors |
| A-050 | Escalate operational issues to the D0 Technical Manager (front-line support) | glossary `d0`; Phase 5 §Item 3 | escalate |

### R-06 — D0 Technical Manager

| ID | Action | Source | Notes |
|---|---|---|---|
| A-051 | Install / deploy a particular D0 deployment | Phase 5 §Item 3 | operate/perform |
| A-052 | Configure deployment-level controls (deployment paths, storage endpoints, service config, resource limits, credential integration, deployment health settings) | Phase 5 §Item 3 | configure/control |
| A-053 | Technically maintain the deployment within the established design | Phase 5 §Item 3 | maintain |
| A-054 | Monitor deployment health, including D0-crash detection | Phase 5 §Item 3; glossary `d1`; Phase 5 §Item 1 | [H] monitor |
| A-055 | Provide front-line support and handle deployment errors for the D0 Operator | glossary `d0`; Phase 5 §Item 3 | handle-errors |
| A-056 | Diagnose and recover a failed deployment | Phase 5 §Item 3 | diagnose→recover |
| A-057 | Escalate to the D1 Technical Manager when a fix requires product-package changes | Phase 5 §Item 3 | escalate |

### R-07 — D2 Assistant

| ID | Action | Source | Notes |
|---|---|---|---|
| A-058 | Serve as the single unified interaction point — receive the Designer's queries, instructions, criticism, and interventions | Phase 2 §Principle 3; Phase 4 §Item 3; completions.md C-2026-07-19-1 | unified front |
| A-059 | Conduct the design on the Designer's behalf and answer his queries | completions.md C-2026-07-19-1 | |
| A-060 | Interpret and route Designer input to the right D2 function | Phase 2 §4.2; completions.md C-2026-07-19-1 | routing |
| A-061 | Preserve interaction and design context across the interaction | Phase 2 §4.3; completions.md C-2026-07-19-1 | |
| A-062 | Present the Designer's output — completion reports, Review Stops, Clarification Requests, human-readable summaries — with drill-down | Phase 3 §Phase-Wide Rule; Phase 2 §3.2; completions.md C-2026-07-19-1 | [H] make-visible |
| A-063 | Surface Designer-oriented observability of the D2 process (progress, health, abnormal behavior) enabling Designer-initiated intervention | Phase 2 §Principle 2; completions.md C-2026-07-19-1 | [H] observability |

---

*Totals: **8 roles** (R-00…R-07), **62 actions** (A-001…A-063, A-003 retired). Per role — R-00: 4 ·
R-01: 18 · R-02: 9 · R-03: 4 · R-04: 8 · R-05: 6 · R-06: 7 · R-07: 6.*
