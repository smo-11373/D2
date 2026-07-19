# Role–Action Aggregate Catalog

*Deliverable 1 of the Action-Aggregate node (contract §1). The actions each recognized role
performs, merged and grouped by role, stable-ID'd, each row `Source`-cited within the namespace
(`environment/sources.md`), each role and each action carrying a substantial description. Target =
the common, anticipable set (open-list). Derived from the frozen inputs — Phases 1–5, method §1,
rules `RU-*`, glossary, framework — nothing invented.*

*ID discipline: roles `R-00…` in layer order (D2 → D1 → D0); actions `A-001…` sequential.
**`A-003` is retired and skipped.** The D1 Designer's actions sub-split passive `[P]` / active
`[A]` per method §1.*

## Roles

| ID | Role | Relationship | Description | Source |
|----|------|--------------|-------------|--------|
| R-00 | D2 Designer | Intrinsic (meta / builder; outside the D1 cast) | The human who builds the **D2** product — the design system the D1 Designer uses. **Not** a user of D2. Holds Designer-originated completion/clarification authority over D2's intentionally-open living working sets and effective design authority over D2's own design. Fixed by the layer model (D2 → D1 → D0), not a per-project configurable position. | glossary `d2-designer`; Phase 5 §Item 3 |
| R-01 | D1 Designer | Intrinsic | The **primary and only user** of D2. Directs the evolution of an existing D1 system into a materially revised successor, using D2's tools (setup defaults, design tree, design node modules) to build a **D1** product (which wraps D0). His authority and scarce attention are the top priorities; he supplies incremental intent rather than a full specification and retains effective authority over the material direction of D1. | glossary `d1-designer`; Phase 1 §2; Phase 5 §Item 3 |
| R-02 | Design Node Builder | Intrinsic (design-process position) | A position with a relatively narrow relevant skill set that **builds a single design node** from a sufficiently clear governing contract, environment, inputs, outputs, and harness, without broad knowledge of the whole D1 project. A self-contained design agent whose authority sits below the human Designer's; owns its data, enforces the rules its data specifies, and may spawn children. | Phase 5 §Item 3; glossary `design-node` |
| R-03 | D1 Programmer | Default (Designer-configurable) | The position that **changes product code according to implementation specifications** — realizing an understood D1/D0 design produced by the D1 Designer, without reconstructing the earlier design process. Whether a distinct programmer position exists, and how it is staffed, is configurable to the project. | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | Default (Designer-configurable) | The position that **maintains and upgrades the technical product package within the established design without changing product code** — e.g. adjusting a governed parameter, running the required harness, updating release state, repackaging, and distributing. Its existence imposes design consequences (governed controls must be exposed to it). | Phase 5 §Item 3; RU-01 |
| R-05 | D0 Operator | Default (Designer-configurable) | The position that **performs routine operation and routine user-level monitoring** of the deployed D0 product. The primary D0-facing "user" whose priorities and skill level the D1 Designer designs toward; holds operator-level controls (spend limits, scheduling, scope, approved operating choices). | Phase 5 §Item 3; glossary `d0`; glossary `user` |
| R-06 | D0 Technical Manager | Default (Designer-configurable) | The position that **installs and technically maintains a particular D0 deployment**, providing front-line technical support; holds deployment-level controls (paths, storage endpoints, service config, resource limits, credential integration, deployment health settings). | Phase 5 §Item 3; glossary `d0` |

## Actions

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|----|--------|--------|-------|
| A-001 | Build and author the D2 product | glossary `d2-designer` | Develops the D2 design system (setup defaults, design tree, design node modules) and authors its living design record. |
| A-002 | Perform Designer-originated completion / clarification / expansion of D2's living working sets | Phase 5 §Item 2; glossary `d2-designer` | Amends intentionally-open sets (glossary, query catalog, Phase 5 itself) at a low hurdle, consistent with established higher-level design; not bottom-up revision. |
| A-004 | Approve or reject material revisions to Designer-governed D2 design | Phase 5 §Item 2 | Retains effective authority over D2's own higher-level intent; upward revision faces a high hurdle. (`A-003` retired — skipped.) |

### R-01 — D1 Designer  *(passive `[P]` / active `[A]`, method §1)*

**Passive `[P]` — responds to something D2 brings him (review / stopping point, clarification point):**

| ID | Action | Source | Notes |
|----|--------|--------|-------|
| A-005 | `[P]` Decide whether to use D2 (the entry point) | method §1; glossary `d1-designer` | His first decision; D2 backs it by orienting him with the concepts it needs. |
| A-006 | `[P]` Establish the Designer–D2 operating contract | Phase 3 §Item 1 | Reviews and confirms how D2 will seek intervention and how he will observe/intervene; normally accepts compact defaults. |
| A-007 | `[P]` Establish the initial design input | Phase 3 §Item 2 | Settles the available Predecessor D1 package plus the available expression of intended change; a full specification is not required. |
| A-008 | `[P]` Supply incremental upgrade intent | Phase 1 §3.4 | Provides changes relative to the predecessor — behavior to preserve, defects, desired corrections/features, constraints, directions — not a restatement of unchanged parts. |
| A-009 | `[P]` Review the initial design understanding & direction (Review Stop) | Phase 3 §Item 3 | Optional courtesy/control review after D2 consolidates its understanding and proposed direction. |
| A-010 | `[P]` Build the initial setup — the roles table and the design posture | method §1 | Establishes the cast of roles (each intrinsic or a changeable default) and the run's default design choices in one setup step. |
| A-011 | `[P]` Confirm the D1 foundational documents (D1 Constitution) at the key Review Stop | method §1; Phase 4 §Item 1 | Confirms the D1 constitution/foundational set combined from setup skeleton + predecessor + intended change, at a strongly-encouraged Review Stop. |
| A-012 | `[P]` Review and confirm the D1 Design Operating Framework | Phase 4 §Item 1 | Low-cost review of the consolidated proposed framework (skeleton, inherited/derived rules, D1-specific control points); accept, modify, or discuss. |
| A-013 | `[P]` Set node revision authority (Designer-governed vs D2-governed) | Phase 4 §Item 2 | Determines whether later material node revisions need Designer approval; normally handled by defaults-by-level, with attention drawn only to exceptions. |
| A-014 | `[P]` Respond to a Clarification Request during node building | Phase 4 §Item 2; Phase 3 §Item 1 | Supplies material design judgment D2 cannot resolve by investigation; questions arrive consolidated and high-leverage. |
| A-015 | `[P]` Review a Design Node at a Review Stop | Phase 4 §Item 2 | Reviews a proposed node result; attention scales with node height (a Constitution Node warrants more than a low implementation node). |
| A-016 | `[P]` Respond to a high-leverage, D2-initiated intervention request | Phase 2 §Principle 1; Phase 1 §2.5 | Is asked only when Designer judgment justifies its attention cost, preferentially at a high-leverage principle/invariant/tradeoff. |

**Active `[A]` — acts on his own initiative (monitor, inspect, redirect, lay down a rule):**

| ID | Action | Source | Notes |
|----|--------|--------|-------|
| A-017 | `[A]` Exercise Designer authority — direct/redirect the design, suspend a branch, reserve approval | Phase 1 §2.2; Phase 4 §Item 3 | The standing authority over material D1 direction and concrete directives (impose, revise, reserve, suspend); applied promptly as authority actions. |
| A-018 | `[A]` Inspect / inquire into the emerging D0 design and D1 process | Phase 4 §Item 3; Phase 2 §Principle 2 | Ask, explain, report, trace, show, compare current design or process state through the unified interaction point, drilling down as desired. |
| A-019 | `[A]` Monitor design progress | method §1; Phase 4 §Item 3 | Time consumed, which nodes consumed most time/revisions, overall design health; enabled by Designer-oriented observability. |
| A-020 | `[A]` Monitor design spend / cost | method §1; Phase 4 §Item 3 | How much the D1 design process has cost, and where; distinct from D0 operator spend limits. |
| A-021 | `[A]` Investigate a suspected concern | Phase 4 §Item 3; Phase 2 §3.4 | Critically examine a suspected design/process problem, moving from high-level observation to deeper investigation before deciding whether to intervene. |
| A-022 | `[A]` Lay down a rule / invariant | Phase 4 §Item 3; method §1 | Impose a governing constraint (e.g. "do not materially change Algorithm A without my approval"); Designer rules require Designer permission to create/revise/retire. |
| A-023 | `[A]` Initiate a design change / propose upward revision (Designer-initiated) | Phase 4 §Item 2; RU-06 | Proposes a change, usually after discussion; evaluated (dry-run, commits nothing) before it is officially proposed. |
| A-024 | `[A]` Hold D0-user optimization in view | method §1; Phase 5 §Item 3 | The standing consideration cutting across both classes: he designs D1 to serve the D0 users (operators/users), and D2 must let him hold and act on it. |
| A-025 | `[A]` Check how well D2 served him — the optional D2-process audit | Phase 3 §Item 5; method §1 | After the run, evaluates process cost, time, Designer Attention Cost, and candidate D2 improvements ("did D2 design D1 well?"). |

### R-02 — Design Node Builder

| ID | Action | Source | Notes |
|----|--------|--------|-------|
| A-026 | Build the current design node within its governing contract | Phase 4 §Item 2; Phase 5 §Item 3 | Investigate, design, check, test, and converge internally under the compiled contract/sandbox, largely from local context. |
| A-027 | Produce the Node Design Specification (node result) | Phase 4 §Item 2 | The proposed node design/implementation specification or equivalent node result. |
| A-028 | Prepare a Designer-oriented node report | Phase 4 §Item 2; Phase 1 §2.4 | A human-oriented report of the node result for review appropriate to the node's significance. |
| A-029 | Submit the result with its own justification (submission package) | RU-02; glossary `submission-package` | Authors the justification and attaches it to the submission; submission is not acceptance — the parent approves or rejects. |
| A-030 | Enforce the rules its owned data specifies | glossary `design-node`; Phase 4 §Item 2 | Owns its data and enforces the rules that data specifies within its granted authority. |
| A-031 | Spawn child design nodes / propose a spawning strategy | RU-03; Phase 4 §Item 2 | Determines children by the Designer's potential actions (passive-action spawning first; active deferred); proposes the spawning strategy where the work decomposes. |
| A-032 | Propose an upward revision to ancestor-owned data and halt until resolved | RU-04; RU-05; Phase 4 §Item 2 | May challenge higher design but cannot rewrite what it does not own; an open upward proposal is a stopping point (no drift). |
| A-033 | Evaluate a proposed change before officially proposing it (dry-run) | RU-06 | A separate step that commits nothing — probes up and down, returns an evaluation report; then formalize or revise. |

### R-03 — D1 Programmer

| ID | Action | Source | Notes |
|----|--------|--------|-------|
| A-034 | Implement the D0 product code from the D1 implementation specification | Phase 5 §Item 3 | Changes product code according to implementation specifications. |
| A-035 | Realize an understood design without reconstructing the design process | Phase 5 §Item 3; Phase 2 §5.3 | Implementation primarily realizes an understood design rather than being the environment for discovering it; continuous Designer–Programmer entanglement is not assumed. |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|----|--------|--------|-------|
| A-036 | Adjust a governed product parameter within its authorized range (no code change) | Phase 5 §Item 3; RU-01 | Modifies an explicitly governed parameter (e.g. a timeout 5→10 min) without touching code. |
| A-037 | Run the required validation / regression harness after a change | Phase 5 §Item 3; glossary `d1` | "No code change does not mean no harness" — runs the D1 wrapper's upgrade smoke-test/regression suite. |
| A-038 | Update release state, repackage, and distribute the upgraded product | Phase 5 §Item 3 | Completes the controlled upgrade cycle within the established design. |
| A-039 | Maintain product/provider defaults, retry policy, and resource/release profiles | Phase 5 §Item 3 | Position-oriented configuration: product defaults, approved provider defaults, retry within accepted ranges, resource profiles, packaging parameters. |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|----|--------|--------|-------|
| A-040 | Perform routine operation of the deployed D0 product | Phase 5 §Item 3; glossary `d0` | Day-to-day running of the distributable product. |
| A-041 | Perform routine user-level monitoring of D0 | Phase 5 §Item 3; glossary `user` | Routine user-level health/behaviour monitoring, represented at the operator's level. |
| A-042 | Set operator-level controls | Phase 5 §Item 3 | Position-oriented configuration: daily spending limits, routine scheduling, collection scope, approved operating choices. |

### R-06 — D0 Technical Manager

| ID | Action | Source | Notes |
|----|--------|--------|-------|
| A-043 | Install / deploy a particular D0 deployment | Phase 5 §Item 3; glossary `d0` | Stands up a specific deployment of the D0 product. |
| A-044 | Technically maintain the D0 deployment (front-line support) | Phase 5 §Item 3; glossary `d0` | Ongoing technical maintenance and front-line support of the specific deployment. |
| A-045 | Set deployment-level controls | Phase 5 §Item 3 | Position-oriented configuration: deployment paths, storage endpoints, service configuration, resource limits, credential integration, deployment health settings. |

---

*Open-list note (method §1): this is the common, anticipable skeleton the frozen inputs give,
not a claim of 100% coverage of every project. The active-`[A]` tail for the D1 Designer is
fluid and project-dependent by nature; D2 interprets the remainder rather than pre-enumerating it.*
