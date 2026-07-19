# Algorithm — deriving the Role–Action aggregate table

*Product 2 of the Action-Aggregate node's output package (contract §1.2). The procedure this node
committed to, written so the table (`role-action-catalog.md`) can be **re-derived / reproduced** from
the same frozen inputs. This is the node's re-runnable recipe; running it over the pinned inputs
lands on the **same roles and substantially the same actions** modulo naming, granularity, and
open-list judgment (contract §5).*

## Inputs (read-only source of truth)

- **Constitution — Phases 1–5** (`constitution/phase-1…5-*.md`). Positions live in **Phase 5
  Item 3** (Human Position First); actions are implied by each position's job function and the phase
  items. Phase 3 (Designer–D2 action model) and Phase 4 (Designer–D1 action model) supply the D1
  Designer's journey; Phase 2 supplies the principles governing observability/intervention.
- **Method — functional doc §1** (`method.md`). The translation discipline: identify the Designer's
  actions → abstract the common element → split **passive / active** → keep the **D0-user
  throughline** → treat the list as **open**.
- **Rules — `RU-01…RU-11`** (`rules.md`).
- **Glossary** (`glossary.md`) and **framework** (`framework/*.md`) — role anchors, the design-node
  model, the position-derived depth frame, and the conformance requirement.
- **Source namespace** (`sources.md`) — a row's `Source` must resolve inside `environment/`.

## Procedure

### Step 1 — Seek roles

1. Read **Phase 5 Item 3** and extract the named conceptual positions: D1 Designer, Design Node
   Builder, D1 Programmer, D1 Technical Manager, D0 Technical Manager, D0 Operator.
2. Add the **D2 Designer** from the layer model (D2 → D1 → D0) and the glossary (`d2-designer`), which
   anchors it as catalog role **R-00**.
3. Assign IDs in **layer order** (D2 → D1 → D0), honouring the glossary/rules anchors:
   `R-00` D2 Designer, `R-01` D1 Designer (glossary), … `R-04` D1 Technical Manager (RU-01),
   `R-05` D0 Operator (glossary `d0`), `R-06` D0 Technical Manager (glossary `d0`). The middle band
   `R-02/R-03` takes Design Node Builder then D1 Programmer.
4. Tag each **intrinsic** (fixed to the ecosystem) or **default** (a D2-provided cast member the D1
   Designer can change): D2 Designer, D1 Designer, and Design Node Builder are intrinsic (meta /
   primary user / D2's design mechanism); the D0-facing and product-maintenance positions
   (D1 Programmer, D1 Technical Manager, D0 Operator, D0 Technical Manager) are Designer-changeable
   defaults.
5. Write each role a **substantial description** and cite its `Source`.

### Step 2 — Actions per role

For each role, read the constitution/method for that role and extract **what the role does**, naming
each action, assigning a stable global ID (`A-001…`, **skip retired `A-003`**), writing a substantial
description, and citing an in-namespace `Source`.

- **D1 Designer (R-01)** — walk the method's journey (entry → operating contract → initial input →
  setup → understanding/direction → foundational docs → operating framework → node review →
  oversee/monitor/inspect/intervene → being asked → checking) plus Phase 3 and Phase 4, and **sub-split
  passive [P] / active [A]**: [P] = he responds to something D2 brings (review/stop, clarification);
  [A] = he acts on his own initiative (inspect, monitor, investigate, direct, initiate a change,
  audit). Carry the **D0-user optimization throughline** as a standing consideration.
- **D2 Designer (R-00) and Design Node Builder (R-02)** — internal/meta roles: derive from Phase 5
  Item 2 (Designer-originated completion) and Phase 4 Item 2 (node-building flow) + `RU-02/04/05/09/10`.
  The position-derived depth frame is **not** applied to these.
- **Downstream operational roles (R-03 Programmer, R-04 D1 Tech Mgr, R-05 D0 Operator, R-06 D0 Tech
  Mgr)** — apply the **position-derived depth frame** (design-node-algorithm step 2) as a
  *completeness prompt, not a checklist*. For each, elaborate only the facets its **Phase 5 Item 3
  job function genuinely implies** across: **operate/perform · monitor/observe · configure/control ·
  view/report · handle routine errors · escalate/request support**; for the **maintenance/support**
  positions (D1 Technical Manager, D0 Technical Manager) also walk the **diagnose → apply-fix →
  recover-from-a-failed-change → record-the-change** cycle. **Never invent an action to fill a facet**
  a position does not imply (e.g. the Programmer gets no configure/monitor facet; the D0 Technical
  Manager gets no "upgrade record" action because only the D1 wrapper — glossary `d1` — names one).

### Step 3 — Aggregate

Merge the per-role pieces into one table grouped by role; global sequential action IDs across all
roles; deduplicate.

### Step 4 — Acceptance self-check (conformance FIRST and gating)

1. **Conformance (gating).** The deliverable contradicts **no** governing statement of the
   fundamentals — no principle, no **named enumeration**, no method discipline, no rule. In
   particular: the Phase 5 Item 3 position enumeration is present and **not collapsed/dropped/re-cast**;
   the D1 Designer passive/active split (method §1) is honoured; position-oriented configuration and
   the escalation/position-hierarchy discipline are reflected, not flattened; the depth-frame guards
   held (genuinely-implied facets only; no invented rows; meta roles exempt). A conflict → **revise to
   conform** or **propose up and halt** (`RU-04`/`RU-05`) — never emit-and-flag.
2. **Coverage (open-list).** Every action a competent re-derivation from the inputs would surface is
   present — the common, anticipable set; the tail stays open (method §1).
3. **Traceability.** Every row cites a `Source` resolving inside the namespace (`sources.md`).
4. **Integrity.** Stable IDs (A-003 skipped), grouped by role, deduplicated; the aggregate is ready to
   drive the capability map (`RU-11`).

Conformance passing first is the **termination condition**; other gaps → derive more.

### Step 5 — Submit

Submit the aggregate with the node's justification, including an explicit **conformance argument**,
for the parent's (Fundamentals') acceptance (`RU-02`) — a two-step submission (declaration + algorithm
at activation; the table as the result).

## Why it reproduces

The inputs are **frozen**, the method is **fixed**, and acceptance is **coverage + conformance
against those inputs**. Two competent runs land on the **same roles** (pinned by Phase 5 Item 3 + the
glossary anchors) and **substantially the same actions**. The residual "not identical" is the free
part: naming, granularity, which position-derived facets get elaborated, and the open-list tail
(contract §5).
