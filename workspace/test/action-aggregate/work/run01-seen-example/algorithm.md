# Output product 2 — the algorithm (re-derived) · submitted at **Step 1 (activation)**

*The concrete procedure this node commits to run to produce the role-action table. Written to be
**re-run** and to yield a substantially-matching table each time. Submitted with the declaration for
the parent's approval; the node is activated (may spawn children) only once accepted.*

## 0. Inputs read (from `../environment/`)

- `constitution/phase-5-…` **Item 3 (Human Position First)** — the **positions** (roles) and their
  job functions; **Item 1 (Harness First)**, **Item 2 (Top-to-Bottom)**, **Item 5 (Modularization)**
  as shaping principles.
- `constitution/phase-3-…` — the Designer's **D2-facing** action model (operating contract, initial
  input, understanding/direction, audit).
- `constitution/phase-4-…` — the Designer's **D1-facing** action model (framework, node building,
  active inspection/intervention) — the main source of the D1 Designer's actions.
- `constitution/phase-1-…`, `phase-2-…` — primary user, authority, attention cost, the four
  principles (incl. §P3 unified interaction → the D2 Assistant, §P4 verification, §2.6 tunable depth).
- `method.md` (§1) — the derivation discipline: **identify actions → abstract the common element →
  split passive / active → open-list → keep the D0-user throughline**.
- `rules.md` (`RU-01…RU-11`), `glossary.md` — governance and terms.

## 1. Decomposition — children spawned, with sub-contracts

1. **Roles node.** *"Derive the role table from Phase 5 Item 3 + the layer model (D2→D1→D0). For each
   position: stable ID, name, relationship, a substantial description, an **intrinsic / default** tag,
   each Source-cited. Deliver the role table."*
2. **Per-role action nodes** (one per role returned). *"For role R, derive the actions R performs from
   its **job function** (Phase 5) and the relevant phase items. For each action: stable ID, a
   substantial description, Source. For the **D1 Designer**, sub-split **passive / active**. Deliver
   R's action pieces."*

## 2. Derivation method (extract, do not invent)

- **Roles.** Take the positions named in Phase 5 Item 3 (D1 Designer, Design Node Builder, D1
  Programmer, D1 Technical Manager, D0 Technical Manager, D0 Operator); add the **D2 Designer**
  (Phase 5 Item 2, completion authority over D2's own sets) and the **D2 Assistant** (Phase 2 §P3 +
  Phase 4 Item 3, the unified interaction point). Tag **intrinsic** (ecosystem-fixed: D1 Designer, D2
  Assistant, internal agents, D2 Designer) vs **default** (product-side, changeable: the D0 roles, the
  D1 Programmer, the D1 Technical Manager).
- **D1 Designer actions.** Walk his journey across Phases 3–4 and the method — *entry decision →
  operating contract → initial input → understanding → setup/posture → foundational docs → framework →
  oversee/review nodes → inspect / monitor / intervene → answer when asked → check via audit* — and
  lift each action; classify **[P] passive** (responds to something D2 brings) vs **[A] active** (own
  initiative).
- **Downstream-role actions.** Lift from each position's job function in Phase 5 Item 3, elaborating
  **position-derived** actions where the job function implies them: D0 Operator (run / monitor /
  configure / view / notify / support-request), D0 Technical Manager (install / maintain / diagnose /
  patch / escalate / monitor), D1 Technical Manager (parameter / harness / release / deploy / monitor /
  rollback / records), D1 Programmer (implement / test / fix), Design Node Builder (investigate /
  design / evaluate / submit / spawn / propose-up / harness-first).

## 3. Aggregate

Merge all per-role pieces into one table, grouped by role, stable IDs (this run's own `A-1xx`
scheme), deduplicated.

## 4. Acceptance / stop condition (coverage — makes it terminate & reproduce)

- **Coverage** — every action a competent re-derivation from the inputs would surface is present
  (open-list target, not claimed exhaustive).
- **Traceability** — every action and role Source-cited.
- **Integrity** — IDs stable & unique, grouped by role, deduplicated.
- **Substance** — a substantial description per action and per role.
- If a gap is found, return to step 2 for the affected role; otherwise stop.

## 5. Package

Emit the three products. **Step 1:** this algorithm + the declaration (now). **Step 2:** the
role-action table with descriptions (after the work). Submission / approval is out of this test's scope.
