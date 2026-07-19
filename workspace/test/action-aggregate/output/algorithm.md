# Algorithm — deriving the Role–Action Aggregate table

*Product 2 of the Action-Aggregate node (contract §1.2). The procedure that derives the table
(`role-action-catalog.md`) from the frozen inputs, written so any competent run over the same inputs
reproduces a **substantially matching** table — the same roles and substantially the same actions
(modulo naming, granularity, open-list judgment). This is Step 1 (activation) material.*

## Inputs (read-only source of truth)

- **Constitution** — Phases 1–5 (`constitution/phase-1…5-*.md`). Positions live in **Phase 5 Item 3**
  (Human Position First); the Designer's journeys live in **Phase 3** (Designer↔D2) and **Phase 4**
  (Designer↔D1); Harness First is **Phase 5 Item 1**; Verification Before Realization is **Phase 2
  Principle 4**.
- **Method** — functional doc **§1** (`method.md`): identify actions → abstract the common element →
  passive/active split → D0-user throughline → open list.
- **Rules** — `RU-01…RU-11` (`rules.md`), **glossary** (`glossary.md`), **framework**
  (`design-tree.md`, `design-node-algorithm.md`, `conformance.md`).

Cite only the in-package Source namespace (`sources.md`); nothing is invented.

## Step 1 — Seek the roles

1. Extract the **named positions** from Phase 5 Item 3's enumeration: D1 Designer, Design Node
   Builder, D1 Programmer, D1 Technical Manager, D0 Technical Manager, D0 Operator.
2. Add the layer-model roles the glossary fixes: **D2 Designer** (`d2-designer`, R-00) as the meta
   builder; **D1 Designer** (`d1-designer`, R-01) as primary user. Walk the layer model **D2 → D1 →
   D0** to order them.
3. Fix IDs from the inputs where the inputs assign them: R-00/R-01 (glossary), **R-04** = D1 Technical
   Manager (RU-01), **R-05** D0 Operator / **R-06** D0 Technical Manager (glossary `d0`). Place the
   remainder (Design Node Builder R-02, D1 Programmer R-03) in design→implementation layer order.
4. Tag each role **intrinsic** (fixed to the ecosystem — the human authorities and D2's design
   mechanism) or **default** (a D2-provided cast member the D1 Designer may change — glossary `role`).
5. Write a substantial description and a Source for each. → the **role table** (`R-*`).

## Step 2 — Actions per role

For each role, read the constitution/method for that role's **job function** and extract what it
does; name it, assign a stable `A-` ID, cite the Source, write a substantial description. Three
depth-setting devices decide how far to elaborate:

- **D1 Designer — the journey scaffold + passive/active split (method §1).** Walk his full journey
  and split every action **[P] passive** (he responds to what D2 brings — Phase 3 Items 1–4, Phase 4
  Items 1–2, the entry decision) vs **[A] active** (own initiative — Phase 4 Item 3, the audit, the
  evaluate-before-propose dry-run). Keep the **D0-user optimization** throughline as a standing
  active consideration.
- **Operational cast — the position-derived depth frame** (Programmer, D1/D0 Technical Managers, D0
  Operator). These have no journey scaffold, so elaborate the actions their Phase 5 Item 3 function
  *genuinely implies* across the recurring facets: **operate · monitor · configure · view ·
  handle-routine-errors · escalate**, and for maintenance positions the **diagnose → apply-fix →
  recover-from-a-failed-change → record** cycle. The facets are a completeness prompt, not a
  checklist — elaborate only what a position implies; never invent to fill a facet. (Not applied to
  the D1 Designer or the internal/meta roles.)
- **Every role — the harness-richness bias** (Harness First, Phase 5 Item 1). Beyond core function,
  hunt each position's harness facets — what it **tests**, **monitors**, **detects (hidden
  errors/failures)**, and **makes visible** — and preferentially surface them (marked **[H]**). A
  design thin on testing/monitoring/health-visibility/failure-handling is a deficiency to
  investigate, not an acceptable minimum. Guard: bias ≠ padding; conformance and completeness still
  gate every row.

Internal/meta roles (D2 Designer, Design Node Builder) get their actions from Phase 5 Item 2 and
Phase 4 Item 2 respectively (no depth frame), plus the harness bias (the Builder's
check/test/verify; the Designer's process audit).

## Step 3 — Aggregate

Merge the per-role action pieces into one table grouped by role, in role/layer order R-00…R-06.
Deduplicate; keep IDs stable and contiguous (`A-003` retired — skipped).

## Step 4 — Acceptance self-check (the termination condition)

Run in order; a failure is fixed, not flagged (conformance.md — "flag and continue" is not legal):

1. **Conformance (first, gating).** The table contradicts **no governing statement** of the inherited
   fundamentals — no principle, no **named enumeration** (Phase 5 Item 3's positions; Phase 3's
   interaction classes and Items 1–5; Phase 4's Items 1–3; the position-oriented control lists), no
   method discipline (passive/active, open list, D0-user throughline), no rule. On a conflict:
   **revise to conform** or **propose up and halt** (`RU-04`/`RU-05`).
2. **Completeness (active).** *Actively derive the should-exist set from the fundamentals and check
   each is present.* **Gating** for named/explicitly-listed pieces (the named position enumeration,
   the passive/active journey Items, the depth-frame facets, the per-position control lists); **strong
   bias** for what a competent derivation implies; open-list only at the genuine tail. On a gap,
   **derive the missing piece** — a named omission is a gate failure.
3. **Traceability.** Every row cites a Source resolving inside the package namespace (`sources.md`).
4. **Integrity.** Stable IDs, grouped by role, deduplicated; the aggregate is ready to drive the
   Capability node (`RU-11` — coverage is the contract).

## Step 5 — Submit (structure only; not exercised by this test)

Two-step submission (contract §6): **Step 1** submits this algorithm + the declaration for activation
(`RU-02`); on acceptance the node spawns Roles → per-role action children and does the work; **Step 2**
submits the result table with substantial descriptions. Justification (including an explicit
conformance argument) travels with the submission for the parent's independent gate.

## Why it reproduces

Inputs are frozen, the method is fixed, and acceptance is coverage/conformance against those inputs.
Two competent runs land on the **same roles** (the enumeration is named) and **substantially the same
actions**; the residual variation is naming, granularity, which position-derived actions get
elaborated, and the open-list tail (contract §5).
