# Algorithm — how the Role–Action Aggregate table is derived

*Deliverable 2 of the Action-Aggregate node (contract §1.2 — the Step-1 activation artifact). The
procedure that derives the table (seek roles → per-role actions → aggregate → self-check), written
so the table can be **re-derived / reproduced** from the frozen inputs. It invents nothing: every
row's substance is extracted/abstracted from the constitution (Phases 1–5) + completions + method §1
+ rules `RU-*`, and carries a `Source` — the derivation trace.*

## Inputs (read-only source of truth)

- Constitution — **Phases 1–5** (frozen). Positions live in **Phase 5 §Item 3** (Human Position
  First); actions are implied by each position's job function and the phase items.
- **Completions** (`completions.md C-*`) — Designer-originated, govern alongside the baseline; may
  name gating positions/requirements (here: the **D2 Assistant**).
- **Method §1** — the translation discipline: identify actions → abstract the common element →
  split passive/active → keep the D0-user throughline → treat the list as **open**.
- **Rules `RU-01…RU-11`** — design-tree governance (author owns its table; aggregate at the
  boundary; propose-up; coverage).
- Source namespace (`sources.md`) fixes the legal citations and resolves out-of-package references
  to their in-package basis.

## Procedure

### Step 1 — Seek the roles

Extract the named **positions** from Phase 5 §Item 3, add the layer-model positions from the
glossary (D2 → D1 → D0), and add any **completion-named** position. Tag each **intrinsic**
(structural to the ecosystem) or **default** (a D2-provided position the D1 Designer may change).
Cite the `Source`. **Named positions are gating for conformance** — omitting one is a gate failure.

The role set that results: `R-00` D2 Designer, `R-01` D1 Designer, `R-02` Design Node Builder,
`R-03` D1 Programmer, `R-04` D1 Technical Manager, `R-05` D0 Operator, `R-06` D0 Technical Manager,
`R-07` D2 Assistant. IDs `R-00…R-06` are **pinned by the inputs' own hints** (glossary → R-00/01/05/06;
`RU-01` → R-04; Phase 5 §Item 3 order → R-02 before R-03); the completion-added D2 Assistant is
appended as `R-07` to preserve those pinned IDs.

### Step 2 — Derive actions per role, by all four lenses, then attach to positions

For each role, derive the actions its role *genuinely implies* — never manufactured to fill a slot —
using **four lenses**, then apply the **harness-richness bias** across every role. Name, assign a
stable ID (`A-001…`, **`A-003` retired/skipped**), cite the `Source`.

1. **Job function** — what the position does (Phase 5 §Item 3 and the relevant phase items).
2. **Intention** — the *result the position is responsible for producing* (Phase 5 §Item 3);
   derive the actions necessary to achieve it. (E.g. the D1 Designer's intent to govern his own
   attention budget → **tune intervention depth**, A-024; his purpose to serve the D0 users →
   **hold D0-user optimization**, A-027; his responsibility that D2 served him well → **audit the
   D2 process**, A-028. The Design Node Builder's intended result → **produce + justify + submit the
   node spec**. The D2 Assistant's intended result → **conduct the design and answer queries**.)
3. **Depth frame** — for the **operational cast only** (D1 Programmer, D1/D0 Technical Managers, D0
   Operator; **not** the D1 Designer, D2 Designer, Design Node Builder, or D2 Assistant), elaborate
   the facets the job function genuinely implies: **operate/perform · monitor/observe ·
   configure/control · view/report · handle routine errors · escalate/request support**, plus the
   **diagnose → apply-fix → recover-from-a-failed-change → record** cycle for maintenance/support
   positions (R-04, R-06). Completeness prompt, not a checklist.
4. **Lifecycle (cross-role, logically forced)** — walk the product's necessary transitions and read
   off each forced action + hand-off (produce/receive pair + verification gate), attaching each to
   the position that performs it:

   > foundational docs (A-010) → operating framework (A-011) → implement (A-040) → test (A-041) →
   > **package** (A-047) → install/deploy (A-059) → **smoke-test** (A-060, the hand-off gate) →
   > hand-over (A-047 produce / A-059 receive) → operate (A-052) → monitor health (A-053 · A-063 ·
   > A-049) → **detect** (A-049 wrapper crash-detection) → diagnose (A-064 · A-042) →
   > recover/rollback (A-050 · A-065) → record (A-048) → upgrade (A-045) → re-test (A-046) →
   > re-deploy (A-066).

   This walk is **deductively closed**: "operator running it" is unreachable from "package produced"
   without install + smoke-test + hand-over, so these post-production steps are unmissable. **Every
   transition must have an owning position** (work-conservation on process) — a forced step with no
   owner means a position is missing or must be added.

**Harness-richness bias (every role).** Beyond core function, hunt what each position **tests /
monitors / detects / makes visible** (Harness First, Phase 5 §Item 1; Verification Before
Realization, Phase 2 §Principle 4; glossary `d1`). Bias ≠ padding: never manufacture a harness the
fundamentals don't warrant, nor split one responsibility into mechanical steps.

**D1 Designer sub-split.** The D1 Designer's set splits **passive `[P]`** (responds to what D2
brings — review points, clarification points, reports) and **active `[A]`** (own initiative —
monitor, inspect, redirect, lay down a rule, tune depth). (method §1; Phase 4 §Item 2/3.)

### Step 3 — Aggregate

Merge the per-role pieces into one table, grouped by role in `R-00…R-07` order.

### Step 4 — Acceptance self-check (gating, in order)

1. **Conformance (first, gating).** The deliverable **contradicts no governing statement** of the
   fundamentals or completions — no named enumeration, principle, method discipline, or rule. (All
   Phase 5 §Item 3 positions present; the completion's D2 Assistant present; passive/active split
   honored; position-oriented configuration lists honored; open-list respected.) Distinct from
   traceability. On a conflict: **revise to conform** or **propose up and halt** (`RU-04`/`RU-05`) —
   never emit-and-flag.
2. **Completeness (four lenses + work-conservation).** Actively derive the *should-exist* set and
   check each present: every **job function**, every **intention** (result each position must
   produce), every **depth-frame facet** the operational cast implies, and every **lifecycle
   transition**. **Work-conservation:** every action owned by a role; every lifecycle transition
   owned by a position; no orphans.
3. **Distinctness guard (calibrated).** Each row = a distinct responsibility the role performs, not
   a mechanical step or a rule-restatement. **Merge** only mechanical steps and rule-restatements
   (e.g. "halt on an open proposal" folded into A-038; "repackage + update release state +
   distribute" merged into A-047). **Preserve** distinctions the fundamentals make — monitor **cost**
   (A-017, A-055) vs **health** (A-018, A-056); D1-wrapper monitoring (A-049) vs deployment
   monitoring (A-063). Completeness = distinct responsibilities covered, not row count.
4. **Traceability + integrity.** Every row cites a `Source` in the namespace (completions allowed);
   IDs stable, grouped by role, deduplicated; A-003 skipped; the action set is ready to drive the
   capability layer (`RU-11`, coverage-is-the-contract).

Passing all four is the **termination condition**. If any fails and cannot be resolved by
derive-the-missing-piece / revise-to-conform, **propose up and halt** rather than emit.

## Why it reproduces

The inputs are frozen, the method is fixed, and acceptance is coverage/conformance against those
inputs. Two competent runs land on the **same roles** and **substantially the same actions**; the
residual variation is naming, granularity, and which position-derived actions get elaborated in the
open-list tail (contract §5). The `Source` on every row is the derivation trace that lets any run
re-walk the same extraction.
