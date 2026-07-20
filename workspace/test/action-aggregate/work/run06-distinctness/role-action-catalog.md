# Role–Action Aggregate — the Action-Aggregate node's deliverable (Step 2 result)

*Authored & owned by the Action node (`A-` table). Roles are read-only input from the Roles child
(`R-` table). Every row is derived from the frozen inputs (constitution Phases 1–5, method §1, rules
`RU-*`, glossary, framework) and Source-cited; nothing invented. Open-list target = the common,
anticipable set. Actions `A-003` retired (skipped).*

## Roles

Derived from **Phase 5 §Item 3** (Human Position First — the named positions) + the layer model
**D2 → D1 → D0** (glossary `d2`/`d1`/`d0`, layer-anchoring roles). IDs pinned by the glossary
(`R-00` D2 Designer, `R-01` D1 Designer, `R-05` D0 Operator, `R-06` D0 Technical Manager) and `RU-01`
(`R-04` D1 Technical Manager); the remaining two fill Phase 5 Item 3's own ordering. `intrinsic` = fixed
to the ecosystem; `default` = a D2-provided default the D1 Designer can change at setup (glossary `role`).

| ID | Role | Relationship | Description | Source |
|---|---|---|---|---|
| R-00 | D2 Designer | D2 layer · intrinsic | The (human) builder of the D2 product; **not** a user of D2. Authors and maintains D2's governing fundamentals and holds Designer-originated completion/clarification authority over D2's intentionally-open working sets. | glossary `d2-designer`; Phase 5 §Item 2 |
| R-01 | D1 Designer | D1 layer · intrinsic | The **primary and only user of D2**. Directs the evolution of a Predecessor D1 into a materially revised successor D1, using D2's tools; retains effective design authority while D2 minimizes his attention cost. | glossary `d1-designer`; Phase 1 §2 |
| R-02 | Design Node Builder | D2-internal / design-work · intrinsic | The position that **builds a single Design Node** — investigates, designs, verifies, justifies, and submits a bounded design result within its governing contract; treated as one agent at its boundary and may spawn children. | Phase 5 §Item 3; Phase 4 §Item 2; glossary `design-node` |
| R-03 | D1 Programmer | D1 layer · default | Changes product **code** according to the D1 Designer's implementation specification, without reconstructing the earlier design; implements and verifies against the spec's harness. | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | D1 layer · default | Maintains and upgrades the technical **product package within the established design without changing product code** — adjusts governed parameters, runs the required harness, manages release. | Phase 5 §Item 3; RU-01 |
| R-05 | D0 Operator | D0 layer · default | Performs **routine operation and routine user-level monitoring** of a running D0 deployment within approved operating choices; escalates non-routine issues. | Phase 5 §Item 3; glossary `d0` |
| R-06 | D0 Technical Manager | D0 layer · default | **Installs and technically maintains** a particular D0 deployment and provides front-line support to the D0 Operator; configures, monitors, maintains, and recovers the deployment. | Phase 5 §Item 3; glossary `d0` |

*(On "D2 Assistant": it appears only in the algorithm's depth-frame scope guard as an internal/meta
label, is not named in Phase 5 §Item 3, and carries no job function or `R-` id in the frozen inputs.
Instantiating it would force invention; its interaction-fronting function is a capability concern under
D2's unified-interaction responsibility (Phase 2 Principle 3), not a distinct action-bearing position.
See `declaration.md` §self-check. The seven roles above match Phase 5 Item 3's enumeration exactly.)*

## Actions

Grouped by role. `Notes` records the derivation facet: **[P]** passive / **[A]** active (R-01 only);
depth-frame facet (operate / monitor / configure / view / handle-errors / escalate; diagnose→fix→
recover→record); **[H]** = harness-richness facet (test / monitor / detect-hidden-errors / make-visible).

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-001 | Build and maintain D2's governing fundamentals — the constitution, the method, and the rules that constitute the D2 product. | glossary `d2-designer`; Phase 5 (header) | core function |
| A-002 | Perform Designer-originated completion, clarification, and expansion of D2's intentionally-open working sets (glossary, query catalog, Phase 5 itself) at the lower amendment hurdle. | Phase 5 §Item 2 | core function |
| A-004 | Hold acceptance authority over Designer-governed D2 design — approve or reject material revision proposals and prevent lower-level convenience from silently revising higher intent. | Phase 5 §Item 2; RU-02 | [H] governance visibility |

### R-01 — D1 Designer

| ID | Action | Source | Notes |
|---|---|---|---|
| A-005 | Decide whether to use D2 for the project — the entry-point decision, backed by D2 orienting him with the concepts it needs. | method §1 (§2 entry point) | [P] |
| A-006 | Review and confirm the Designer–D2 operating contract — how D2 will seek intervention and how he intends to observe/intervene; normally accept the defaults. | Phase 3 §Item 1 | [P] |
| A-007 | Establish and confirm the initial setup — the cast of roles (each intrinsic or a changeable default) and the run's default design posture, in one setup step. | method §1 (§3 setup); Phase 5 §Item 3 | [P] |
| A-008 | Establish the initial design input — the available Predecessor D1 package and the (incremental) expression of intended change. | Phase 3 §Item 2; Phase 1 §4 | [P] |
| A-009 | Review and confirm D2's consolidated initial design understanding and recommended direction at the default Review Stop. | Phase 3 §Item 3 | [P] |
| A-010 | Review and confirm the D1 foundational documents (the D1 Constitution) produced from setup + predecessor + intended change, at the strongly-encouraged key Review Stop. | method §1 (§4 foundational docs) | [P] |
| A-011 | Review and confirm the D1 Design Operating Framework — the initial design skeleton, inherited/derived design rules, and D1-specific control points. | Phase 4 §Item 1 | [P] |
| A-012 | Respond to D2's clarification requests — supply the material design judgment D2 cannot reasonably resolve through further investigation. | Phase 3 (interaction classes); Phase 4 §Item 2 | [P] |
| A-013 | Review node submissions at Review Stops (attention scaled to node height), approve or continue, and set each node's revision authority (Designer- vs D2-governed). | Phase 4 §Item 2 | [P] |
| A-014 | Monitor the D1 design process — progress, elapsed time, cost/spend, and design health — and notice abnormal process behavior, independently of D2 raising a flag. | Phase 2 Principle 2 (§3.1); Phase 4 §Item 3 | [A][H] monitor |
| A-015 | Inspect and drill into the emerging D0 design and the ongoing D1 design process through the unified interaction point — ask, show, trace, compare — without naming the internal node. | Phase 4 §Item 3; Phase 2 Principle 3 | [A] |
| A-016 | Investigate a suspected design or process problem — request critical examination of a possible flaw, hidden assumption, or abnormal branch, and a recommended action. | Phase 4 §Item 3 | [A][H] detect |
| A-017 | Exercise Designer authority — impose, revise, reserve, or suspend: lay down a rule/invariant, reserve approval authority, or stop a branch (Designer directive / Designer-initiated change). | Phase 4 §Item 3; Phase 5 §Item 3 | [A] |
| A-018 | Audit how well D2 served him — the optional post-run D2-level process audit of time, cost, attention burden, and D2 improvement points. | Phase 3 §Item 5 | [A][H] make-visible |

### R-02 — Design Node Builder

| ID | Action | Source | Notes |
|---|---|---|---|
| A-019 | Investigate the assigned scope autonomously and develop candidate node designs within the governing contract. | Phase 4 §Item 2 | operate |
| A-020 | Establish the node's harness and verify/test the design before submission — constrain first, detect deviation early. | Phase 5 §Item 1; Phase 2 Principle 4; Phase 4 §Item 2 | [H] test |
| A-021 | Produce the Node Design Specification (or equivalent result) together with a Designer-oriented node report. | Phase 4 §Item 2 | operate |
| A-022 | Self-check the result against the acceptance criteria — conformance first and gating, then completeness, traceability, and integrity — before dependent children are spawned. | framework `conformance`; framework `design-node-algorithm` | [H] detect-hidden-errors |
| A-023 | Author the node's justification and submit the package upward for the parent's acceptance (submission is not acceptance). | RU-02; glossary `submission-package` | escalate |
| A-024 | Raise a consolidated Clarification Request when material Designer judgment remains necessary, bundling high-leverage questions. | Phase 4 §Item 2; Phase 3 (clarification class) | escalate |
| A-025 | Determine children by the relevant Designer actions and propose a spawning strategy — decomposing internally to any depth while returning the contracted aggregate. | RU-03; RU-10; Phase 4 §Item 2 | spawn |
| A-026 | Propose upward revision to inherited/governing design when warranted, and halt (no spawn, no advance) until the owning node resolves it. | RU-04; RU-05; Phase 4 §Item 2 | escalate |

### R-03 — D1 Programmer

*(operational position — depth frame applied; only the facets the code-implementation function genuinely implies.)*

| ID | Action | Source | Notes |
|---|---|---|---|
| A-027 | Implement the product code according to the D1 Designer's implementation specification, without reconstructing the earlier design process. | Phase 5 §Item 3 | operate |
| A-028 | Implement and run verification/tests of the code against the specification's harness, moving deviation discovery early. | Phase 2 Principle 4; Phase 5 §Item 1 | [H] test |
| A-029 | Diagnose and fix implementation defects surfaced by verification, without sacrificing correctness for expediency. | Phase 2 Principle 4; Phase 5 §Item 4 | handle-errors |
| A-030 | Escalate specification ambiguities or defects back to the D1 Designer (propose-up) when the spec is insufficient to implement. | Phase 4 §Item 2; RU-04; Phase 5 §Item 3 | escalate |

### R-04 — D1 Technical Manager

*(operational/maintenance position — depth frame + diagnose→fix→recover→record applied.)*

| ID | Action | Source | Notes |
|---|---|---|---|
| A-031 | Adjust governed product parameters/defaults within authorized ranges — the maintenance change, made without touching product code. | Phase 5 §Item 3; RU-01 | configure / fix |
| A-032 | Run the required validation/regression (upgrade smoke-test) harness after a change — "no code change does not mean no harness." | RU-01; Phase 5 §Item 3; glossary `d1` | [H] test |
| A-033 | Recover from a failed upgrade or parameter change — roll back / restore the package to a known-good state. | Phase 5 §Item 1 (failure visibility); glossary `d1` | recover |
| A-034 | Update release state, maintain upgrade records, and repackage/distribute the product. | Phase 5 §Item 3; glossary `d1` | record |
| A-035 | Monitor the upgrade-relevant technical health of the product package. | Phase 5 §Item 1; glossary `d1` | [H] monitor |
| A-036 | Escalate to the D1 Designer/Programmer when a change exceeds the no-code-change / authorized-parameter boundary. | Phase 5 §Item 3; RU-04 | escalate |

### R-05 — D0 Operator

*(operational position — depth frame applied; routine operation implies no maintenance cycle, it escalates.)*

| ID | Action | Source | Notes |
|---|---|---|---|
| A-037 | Perform routine operation of the running D0 product. | Phase 5 §Item 3 | operate |
| A-038 | Perform routine user-level monitoring of D0 health/status via the operator-level report. | Phase 5 §Item 3; Phase 4 §Item 3; Phase 5 §Item 1 | [H] monitor / view |
| A-039 | Set approved operating choices within authorized bounds — daily spending limits, routine scheduling, collection scope. | Phase 5 §Item 3 | configure |
| A-040 | Handle routine operational conditions/errors at the user level. | Phase 5 §Item 3 | handle-errors |
| A-041 | Escalate non-routine issues to the D0 Technical Manager (front-line support). | Phase 5 §Item 3; glossary `d0` | escalate |

### R-06 — D0 Technical Manager

*(operational/maintenance/support position — depth frame + diagnose→fix→recover→record applied.)*

| ID | Action | Source | Notes |
|---|---|---|---|
| A-042 | Install and deploy a particular D0 deployment. | Phase 5 §Item 3 | operate |
| A-043 | Configure deployment settings within authorized bounds — deployment paths, storage endpoints, service config, resource limits, credential integration, deployment health settings. | Phase 5 §Item 3 | configure |
| A-044 | Monitor deployment health. | Phase 5 §Item 3; Phase 5 §Item 1 | [H] monitor |
| A-045 | Provide front-line support — receive and handle escalations from the D0 Operator. | glossary `d0`; Phase 5 §Item 3 | handle / support |
| A-046 | Diagnose and apply technical maintenance/fixes to the deployment. | Phase 5 §Item 3 | diagnose / fix |
| A-047 | Recover the deployment from a failed change — restore to a known-good state. | Phase 5 §Item 3; Phase 5 §Item 1 (failure visibility) | recover |
| A-048 | Record the maintenance/change performed on the deployment. | Phase 5 §Item 3 | record |
| A-049 | Escalate to the D1 Technical Manager/Designer when the issue exceeds deployment-level authority (needs a product-level parameter change, redesign, or code). | Phase 5 §Item 3; RU-04 | escalate |

---

*Aggregate: 7 roles, 48 actions (`A-001…A-049`, `A-003` retired). Coverage target is the common,
anticipable open-list set; the genuine tail is left for D2 to interpret (method §1). This completed
`A-` table is the read-only driver for the Capability node — every action maps to ≥1 capability
(`RU-11`).*
</content>
</invoke>
