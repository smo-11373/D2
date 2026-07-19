# Algorithm — deriving the Role–Action Aggregate Table

*Deliverable 2 of the Action-Aggregate node (contract §1, delivered at Step 1 — activation). The
procedure this node committed to and ran to derive `role-action-catalog.md`, written to be
**re-runnable**: contract + the same frozen inputs + this procedure ⇒ a **substantially matching**
table (same roles, substantially the same actions modulo naming, granularity, and the open-list
tail — contract §5).*

## 0. Inputs (frozen, read-only) and the Source namespace

Derive everything from, and only from, these:

- **Constitution — Phases 1–5** (`environment/constitution/phase-1…5-*.md`). Positions live in
  **Phase 5 §Item 3 (Human Position First)**; actions are implied by each position's job function
  and the phase items.
- **Method — functional doc §1** (`environment/method.md`). The translation discipline: identify
  the Designer's actions → abstract the common element → split **passive `[P]` / active `[A]`** →
  keep the **D0-user throughline** → treat the list as **open**.
- **Rules — `RU-01…RU-11`** (`environment/rules.md`). Design-tree governance.
- **Glossary, framework, sources** (`environment/glossary.md`, `framework/*.md`, `sources.md`).

**Cite only the namespace in `sources.md`:** `Phase 1…5 §<Item>`, `method §1`, `RU-01…11`,
`glossary \`<slug>\``, `design-tree` / `design-node-algorithm`. **Never** cite `Phase 6 Item N` or
`Designer <date>` — resolve those to their in-package basis via the `sources.md` provenance map.

## 1. Seek the roles

1.1 Read **Phase 5 §Item 3** and lift its **named enumeration** of conceptual positions verbatim:
D1 Designer, Design Node Builder, D1 Programmer, D1 Technical Manager, D0 Technical Manager,
D0 Operator. *(Conformance: a named enumeration may not be dropped, collapsed, or re-cast — every
one becomes a role.)*

1.2 Add the position the **layer model (D2 → D1 → D0)** requires above the D1 Designer: the
**D2 Designer** (the meta/builder), which the glossary explicitly assigns to catalog role **R-00**.

1.3 Assign stable IDs `R-00…` in **layer order** (D2 → D1 → D0), pinned by the in-package anchors:
`R-00` D2 Designer (glossary `d2-designer`), `R-01` D1 Designer (glossary `d1-designer`),
`R-02` Design Node Builder, `R-03` D1 Programmer, `R-04` D1 Technical Manager (pinned by `RU-01`),
`R-05` D0 Operator (glossary `d0`), `R-06` D0 Technical Manager (glossary `d0`).

1.4 Tag each **intrinsic** (fixed to the ecosystem/layer model) or **default** (a D2-provided
starting position the D1 Designer can change), per glossary `role`: intrinsic = the design-side
positions fixed by the method/layer model (`R-00`, `R-01`, `R-02`); default = the product/deployment
cast the D1 Designer configures per project (`R-03`–`R-06`).

1.5 Give each role a substantial description (job function + relationship) and a namespace `Source`.

## 2. Actions per role

For each role, read the constitution/method **for that role** and extract *what the role does* —
naming each action, assigning a stable ID, writing a substantial description (what it *is*), and
citing a `Source`.

- **R-01 D1 Designer** — walk the **method §1 journey** (entry → operating contract → initial input →
  understanding/direction → setup roles+posture → D1 constitution → operating framework → node
  building/review → oversight → active inspection/monitoring/intervention → being asked → checking)
  cross-referenced with **Phase 3** (Designer–D2 model) and **Phase 4** (Designer–D1 model). **Sub-split
  passive `[P]` / active `[A]`** (method §1): `[P]` = he responds to something D2 brings (review/
  stopping point, clarification point); `[A]` = he initiates (monitor progress, monitor spend, inspect,
  investigate, redirect, lay down a rule, audit). Keep the **D0-user optimization** throughline as an
  explicit `[A]` action.
- **R-00 D2 Designer** — from glossary `d2-designer` + Phase 5 §Item 2: build/author D2; Designer-
  originated completion of D2's living sets; approve/reject revisions to Designer-governed D2 design.
- **R-02 Design Node Builder** — from **Phase 4 §Item 2 (Build the Current Design Node)** + glossary
  `design-node` + `RU-02/03/04/05/06`: build the node within its contract; produce the spec; report;
  submit with justification; enforce owned rules; spawn/propose spawning; propose-up-and-halt;
  evaluate-before-proposing.
- **R-03 D1 Programmer** — from Phase 5 §Item 3 (+ Phase 2 §5.3): implement product code per spec;
  realize an understood design without reconstructing it.
- **R-04 D1 Technical Manager** — from Phase 5 §Item 3 + `RU-01` + glossary `d1`: adjust a governed
  parameter (no code); run the required harness; update release/repackage/distribute; maintain
  position-oriented defaults/profiles.
- **R-05 D0 Operator** — from Phase 5 §Item 3 + glossary `d0`/`user`: routine operation; routine
  user-level monitoring; set operator-level controls.
- **R-06 D0 Technical Manager** — from Phase 5 §Item 3 + glossary `d0`: install/deploy; technically
  maintain; set deployment-level controls.

**ID discipline:** actions `A-001…` sequential in role order; **`A-003` is retired — skip it.**

## 3. Aggregate

Merge the per-role action sets into **one table grouped by role** (`RU-10` — decompose freely
internally, but the boundary deliverable is the aggregate). Each action row sits under its role's
`### R-NN — <name>` heading. Deduplicate semantically overlapping actions into a single row.

## 4. Acceptance self-check (conformance FIRST and gating, then coverage / traceability / integrity)

Run in this order; **conformance gates** — a non-conformant table is rejected regardless of the rest.

1. **Conformance** (contradict no governing statement of the fundamentals — distinct from citing a
   Source):
   - Every position in the Phase 5 §Item 3 **named enumeration** is present as a distinct role — none
     dropped, collapsed, or re-cast (this is the classic named-enumeration conformance trap).
   - The **D2 Designer / D1 Designer** distinction (glossary `designer`, `d2-designer`, `d1-designer`)
     is preserved — the two are not folded.
   - The D1 Designer's actions carry the **passive/active** split (method §1 discipline).
   - The **D0-user throughline** is present (method §1; Phase 5 §Item 3).
   - No row cites outside the `sources.md` namespace (no `Phase 6 Item N`, no `Designer <date>`).
   - On any conflict: **revise-to-conform**, or if the conflict is a genuine defect in the
     fundamentals, **propose-up-and-halt** (`RU-04`/`RU-05`) and record it in `declaration.md`.
     **Never emit-and-flag.**
2. **Coverage** — every action a competent re-derivation from the inputs would surface is present
   (open-list target: the common, anticipable set). Gaps → derive more.
3. **Traceability** — every row cites a `Source` resolving inside the namespace.
4. **Integrity** — stable IDs (`A-003` skipped), grouped by role, deduplicated; the table is shaped
   to let the downstream action↔capability map resolve (`RU-11`).

## 5. Submit

Emit the aggregate table (`role-action-catalog.md`) with an explicit **conformance argument** as part
of the node's justification (`RU-02`). Per the two-step submission (contract §6): this algorithm and
the declaration are the **Step 1 — activation** package; the table with substantial descriptions is
the **Step 2 — result**. *(This test defines the structure but does not exercise submission/approval.)*

## Why it reproduces (contract §5)

**Pinned → convergence:** frozen Phases 1–5, a fixed method, and acceptance measured as
coverage/conformance against those inputs make two competent runs land on the **same roles** (the
Phase 5 §Item 3 enumeration + the layer model) and **substantially the same actions**. **Free →
variation:** action naming, granularity, which position-derived actions get elaborated, and the
open-list `[A]` tail — that residual is the intended "not identical."
