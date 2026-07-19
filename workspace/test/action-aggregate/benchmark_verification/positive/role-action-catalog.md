# Role–Action Catalog — re-derived output

*The Action Aggregate node's **Step-2 result**: the actions each recognized role performs, merged and
grouped by role, each row Source-cited and carrying a substantial description. Re-derived from the
frozen inputs (`../environment/` — constitution Phases 1–5, method §1, rules `RU-*`) by running the
design-node algorithm (`../output/algorithm.md`). Open list — the **common, anticipable** set, not
claimed exhaustive.*

*ID scheme is this run's own (`A-1xx`), independent of any prior catalog; roles keep the layer-model
order `R-00…R-07`. Actions for the **D1 Designer (R-01)** are sub-split **[P] passive** / **[A] active**
per method §1.*

## Roles

*Positions = conceptual responsibility boundaries (Phase 5 Item 3, Human Position First). Each tagged
**intrinsic** (fixed in the D2/D1/D0 ecosystem) or **default** (product-side, Designer-changeable).*

| ID | Role | Relationship | Description | Source |
|------|------|--------------|-------------|--------|
| R-00 | D2 Designer | builds D2 | The human building the D2 product itself; not a user of D2. Holds completion and explicit-revision authority over D2's own living working sets (glossary, query catalog, philosophy). **Intrinsic.** | Phase 5 §Item 2; glossary `d2-designer` |
| R-01 | D1 Designer | uses D2 → builds D1 | D2's **primary and only user** (Phase 1's "Designer"). Directs the evolution of a Predecessor D1 into an upgraded D1 (which wraps D0), retaining effective design authority while D2 minimises his attention cost. **Intrinsic.** | Phase 1 §2; Phase 5 §Item 3 |
| R-02 | Design Node Builder | internal to D2 | A bounded design worker inside D2 with a relatively narrow relevant skill set, building one Design Node under the D1 Designer's direction within a governing contract and harness. Occupied by a D2 agent. **Intrinsic.** | Phase 5 §Item 3; Phase 4 §Item 2 |
| R-03 | D1 Programmer | implements code | Turns the implementation specification into D0 product code, ideally without reconstructing the earlier design. Changes code, not design intent. **Default.** | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | operates the D1 wrapper | Maintains and upgrades the delivered product within the established design **without changing code**: adjusts governed parameters, runs the upgrade harness, repackages and distributes, and monitors D0 health via the thin D1 wrapper. **Default.** | Phase 5 §Item 3; glossary `d1`, `half-level` |
| R-05 | D0 Operator | operates D0 | Runs the deployed D0 in production — routine operation and user-level monitoring — typically with low technical understanding. **D1/D0's primary beneficiary**: the product exists first for this position's convenience. **Default.** | Phase 5 §Item 3 |
| R-06 | D0 Technical Manager | supports D0 | Front-line technical owner of a particular D0 deployment: installs it, maintains its technical configuration, monitors deployment health, and gives first-line support to the D0 Operator. **Default.** | Phase 5 §Item 3 |
| R-07 | D2 Assistant | fronts D2 for the Designer | Non-human, LLM-based **single interaction point** between the D1 Designer and the whole D2 system: conducts the design on his behalf, routes his input, and presents human-oriented output; he never addresses an internal node or service directly. **Intrinsic.** | Phase 2 §P3; Phase 4 §Item 3 |

*D1 wraps D0: D0 is the core distributable; the thin D1 wrapper adds health/performance monitoring, an
upgrade smoke-test suite, and upgrade records — "half a level above D0" (glossary `d1`, `half-level`).*

## Actions

*Grouped by role. Each keeps a stable `A-` id in this run's scheme, a substantial description (what the
action **is**), and a Source in the frozen inputs. Actions tagged **position-derived** are elaborated
from the role's job function under Human Position First (Phase 5 Item 3), especially for the D0 side.*

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-101 | Complete, clarify, or expand D2's living working sets (glossary, query catalog, philosophy) at a low hurdle | Phase 5 §Item 2 | Designer-originated completion; lower hurdle than upward revision |
| A-102 | Revise D2's persistent working sets only through the explicit D2 design process | Phase 5 §Item 2 | Guards D2's own foundations against silent drift |
| A-103 | Review and adopt or reject D2 improvements proposed by the optional post-run D2 audit | Phase 3 §Item 5 | The audit may propose but must not silently modify D2 |

### R-01 — D1 Designer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-104 | Evaluate D2 and decide whether to adopt it for this design (adopt / decline / defer) | Phase 1; Phase 2 | [P] entry decision; D2 supports it by orientation |
| A-105 | Confirm the Designer–D2 Operating Contract — how D2 seeks intervention and how he observes and intervenes | Phase 3 §Item 1 | [P] accept defaults or adjust |
| A-106 | Provide the initial design input — the Predecessor D1 package and the intended change | Phase 3 §Item 2 | [P] any useful initial form; need not be complete |
| A-107 | Review the consolidated initial design understanding and recommended direction | Phase 3 §Item 3 | [P] a Review Stop, not a Clarification Request |
| A-108 | Select a design posture that fixes many detailed setup defaults in one choice | method §1; Phase 5 §Item 1 | [P] one choice → many settings (Harness First) |
| A-109 | Review and revise the selected setup configuration package | method §1; Phase 4 §Item 1 | [P] progressive disclosure; accept / compare / revise |
| A-110 | Review and adjust the roles table for this project (the cast of positions) | Phase 5 §Item 3 | [P] intrinsic roles fixed; default roles changeable |
| A-111 | Review and confirm the D1 foundational documents (the D1 Constitution) | Phase 3 §Item 3; Phase 4 §Item 1 | [P] a key, strongly-encouraged Review Stop |
| A-112 | Accept the proposed D1 Design Operating Framework | Phase 4 §Item 1 | [P] low-cost default response |
| A-113 | Modify selected parts of the proposed framework | Phase 4 §Item 1 | [P] |
| A-114 | Review a Design Node and approve or say "continue" | Phase 4 §Item 2 | [P] review is an event, distinct from revision authority |
| A-115 | Reserve or assign revision authority over a design object (Designer-governed vs D2-governed) | Phase 4 §Item 2 | [P] a continuing governance property |
| A-116 | Answer a consolidated Clarification Request | Phase 3 phase-wide rule; Phase 4 §Item 2 | [P] distinct from a Review Stop |
| A-117 | Request and review an optional D2 audit after the design run completes | Phase 3 §Item 5 | [P] "did D2 design D1 well?" |
| A-118 | Revise setup or framework material later under governance, with impact analysis | Phase 4 §Item 1; Phase 5 §Item 2 | [P] history preserved |
| A-119 | Discuss a material concern with D2 | Phase 4 §Item 1 | [A] Designer-initiated |
| A-120 | Inquire or inspect — ask D2 to explain, report, trace, show, or compare design or process state | Phase 4 §Item 3 | [A] natural-language design queries |
| A-121 | Raise an investigation or concern — ask D2 to critically examine a suspected problem and recommend action | Phase 4 §Item 3 | [A] normally initiates investigation, not direct mutation |
| A-122 | Issue a Designer directive — impose, revise, reserve, suspend, or exercise authority (e.g. stop a branch) | Phase 4 §Item 3 | [A] recognised as an authority action, applied promptly |
| A-123 | Monitor design progress — advancement and what changed since the last review | Phase 4 §Item 3 | [A] standing monitoring subject |
| A-124 | Monitor resource and cost spend — time and cost, cumulative and per node | Phase 4 §Item 3 | [A] standing monitoring subject |
| A-125 | Monitor design-process health and anomalies — abnormal behaviour, rejection loops, high-impact open issues | Phase 4 §Item 3 | [A] escalates to investigation (A-121) |
| A-126 | Tune resolution depth and intervention posture (deeper investigation vs inference vs escalation vs deferral) | Phase 2 §2.6 | [A] adjusts depth vs attention cost |
| A-127 | Evaluate a proposed change before formalising it — an impact dry-run probing up and down | RU-06 | [A] commits nothing; precedes the official upward proposal |

### R-02 — Design Node Builder

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-128 | Investigate relevant predecessor and reference material within the node's contract | Phase 4 §Item 2; Phase 6 | Enters via curated read-links (RU-08) |
| A-129 | Develop, compare, and critique candidate design choices under the harness | Phase 4 §Item 2; Phase 5 §Item 5 | Bounded local autonomy — strong boundary, local freedom |
| A-130 | Produce the Node Design Specification or equivalent design result | Phase 4 §Item 2 | |
| A-131 | Internally evaluate and test the result before submission | Phase 4 §Item 2; RU-02 | "Submission is not the first evaluation" |
| A-132 | Submit the design result with its own justification for the parent's acceptance | RU-02; Phase 4 §Item 2 | Submission ≠ acceptance |
| A-133 | Propose a spawning strategy for descendant responsibilities | Phase 4 §Item 2 | Spawning ≠ advancement |
| A-134 | Propose an upward revision to governing design, routed by the affected node's authority | Phase 4 §Item 2; RU-04 | An open upward proposal is a stopping point (RU-05) |
| A-135 | Establish the node's verification harness and design evidence before committing the design | Phase 2 §P4; Phase 5 §Item 1 | Monitoring / evidence before realization |

### R-03 — D1 Programmer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-136 | Implement the D0 product code from the implementation specification | Phase 5 §Item 3 | Should not need to reconstruct the design |
| A-137 | Write and run implementation-level tests against the code | Phase 5 §Item 3; Phase 2 §P4 | position-derived; verification support |
| A-138 | Diagnose and fix implementation defects within the specification | Phase 5 §Item 3 | position-derived; code changes within the spec |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-139 | Adjust a governed product parameter without changing code | Phase 5 §Item 3 | Derives RU-01 (no hard-coded adjustable values) |
| A-140 | Run the upgrade validation / regression (smoke-test) harness | Phase 5 §Item 3; glossary `d1` | "No code change does not mean no harness" |
| A-141 | Update release state, repackage, and distribute the product | Phase 5 §Item 3 | |
| A-142 | Deploy D0 into production, optionally retaining D1 to manage it | glossary `d1` | Recipient may run just D0 while keeping D1 |
| A-143 | Monitor D0 health and performance via the D1 wrapper | glossary `d1`, `half-level` | ~half a level above D0 |
| A-144 | Roll back to a previous release on a failed upgrade | glossary `d1` | position-derived; uses the upgrade record |
| A-145 | Review upgrade records and release history | glossary `d1` | position-derived; D1-wrapper records |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-146 | Perform routine operation — start, run, stop, schedule, pause/resume, or cancel D0 jobs | Phase 5 §Item 3 | Typically low technical understanding |
| A-147 | Perform routine user-level monitoring — observe whether D0 is working and healthy | Phase 5 §Item 3 | |
| A-148 | Set operator-level controls — spending limits, scheduling, collection scope, approved operating choices | Phase 5 §Item 3 | Position-oriented configuration |
| A-149 | View D0 results, outputs, and reports | Phase 5 §Item 3 | position-derived; the point of running D0 |
| A-150 | Acknowledge and respond to D0 notifications, prompts, and routine approvals | Phase 5 §Item 3 | position-derived; simple non-technical decisions |
| A-151 | Handle routine, non-technical error conditions — retry or restart within competence | Phase 5 §Item 3 | position-derived; escalates via A-153 |
| A-152 | View routine activity, usage, and cost-to-date at operator level | Phase 5 §Item 3; Phase 6 Item 3 | position-derived; uses observation data |
| A-153 | Request front-line technical support / escalate a problem to the D0 Technical Manager | Phase 5 §Item 3 | position-derived; the low-technical operator's escape hatch |

### R-06 — D0 Technical Manager

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-154 | Install a D0 deployment | Phase 5 §Item 3 | |
| A-155 | Technically maintain a D0 deployment — deployment paths, storage endpoints, service config, resource limits, credentials, health settings | Phase 5 §Item 3 | Position-oriented configuration |
| A-156 | Provide front-line technical support to the D0 Operator | Phase 5 §Item 3 | Serves A-153 |
| A-157 | Diagnose a D0 deployment issue | Phase 5 §Item 3 | position-derived |
| A-158 | Apply a fix, patch, or configuration change within the established design | Phase 5 §Item 3 | position-derived; no product redesign |
| A-159 | Escalate to the D1 Technical Manager when a problem exceeds front-line support | Phase 5 §Item 3 | position-derived |
| A-160 | Monitor and observe D0 deployment health and status (standing, proactive) | Phase 5 §Item 3 | position-derived; distinct from reactive diagnosis A-157 |

### R-07 — D2 Assistant

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-161 | Conduct the design on the Designer's behalf and answer his queries through the single interaction point | Phase 2 §P3; Phase 4 §Item 3 | The D2 Assistant's core function |
| A-162 | Interpret and route the Designer's input to the right D2 function and preserve interaction context | Phase 2 §4.1–4.3 | D2 owns the routing burden |
| A-163 | Present Designer-oriented output — completion reports, Review Stops, Clarification Requests, summaries — with drill-down on request | Phase 1 §2.4; Phase 2 §3.2; Phase 3 phase-wide rule | The reporting side of every item |
