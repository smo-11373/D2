# Algorithm — how this role–action aggregate was derived

*Submitted at **Step 1 (activation)**, alongside the declaration, for the parent
(Fundamentals / the D2 Designer) to approve the **approach** before the node spawns children
and does the work. This is the procedure that, run over the same frozen inputs, re-derives a
**substantially matching** table (`input/contract.md` §3, §5).*

## 0. Node identity and contract

This is the **Action Aggregate node** fulfilling `input/contract.md`. Its contracted deliverable
is a **role–action aggregate table with substantial descriptions** — actions merged, grouped by
role, stable IDs, every row Source-cited, each action and each role carrying a substantial
description. Governed by `RU-01…11`; decomposition left to the child (`RU-10`).

## 1. Inputs read (the frozen source of truth)

All substance is derived from these; nothing is invented (`design-node-algorithm.md` Q2). Read:

- **Constitution — Phases 1–5** (`constitution/phase-1…5-*.md`): primary user and provenance
  discipline (Phase 1), the four principles (Phase 2), the Designer↔D2 action model (Phase 3),
  the Designer↔D1 action model incl. node building and active inspection (Phase 4), and
  Human Position First + the position list (Phase 5 §Item 3).
- **Method — functional doc §1** (`method.md`): the derivation discipline — identify the
  Designer's actions → abstract the common element → split **passive/active** → keep the
  **D0-user throughline** → treat the list as **open**; plus the setup step (roles table + posture).
- **Rules — `RU-01…11`** (`rules.md`): `RU-10` (decompose freely, aggregate always),
  `RU-09` (author owns its table), `RU-11` (aggregate drives the capability layer),
  `RU-02` (justify at submission), `RU-01` (governed parameters → D1 Technical Manager).
- **Glossary** (`glossary.md`): role identities and the intrinsic/default distinction (`role`),
  D2/D1/D0 layer definitions, catalog role numbers (`d2-designer` R-00, `d1-designer` R-01).
- **Framework** (`framework/design-node-algorithm.md`, `framework/design-tree.md`): the standard
  decomposition (seek roles → per-role actions → aggregate → self-check) and dependency shape.
- **Traceability namespace** (`sources.md`): the authoritative Source list; `Phase 6 Item 1/2/3`
  pointers were resolved to their in-package basis (setup → `method §1` + Phase 3; node-building
  → Phase 4 §Item 2; operator/planning → Phase 5 §Item 3 + glossary `half-level`). **No Phase 6
  citation appears in the output.**

## 2. Decomposition (`RU-10` — decompose freely, aggregate always)

The node decomposes into one **Roles** child and one **action** child per role. Each child is a
sub-contract; the node merges their returns into the aggregate it authors and owns (`RU-09`).

### 2a. Roles child — sub-contract

*Derive the positions from **Phase 5 §Item 3 (Human Position First)** + the layer model
(D2 → D1 → D0). Add the **D2 Designer** (builder, Phase 5 §Item 2 / glossary `d2-designer`) and the
**D2 Assistant** (unified interaction point, Phase 2 §Principle 3 + Phase 4 §Item 3). Tag each role
**intrinsic** (ecosystem-fixed) or **default** (product-side, Designer-changeable, glossary `role`),
give a substantial description, cite a Source.*

Result — seven roles, ordered by layer:

| ID | Role | Tag | Anchor |
|---|---|---|---|
| R-00 | D2 Designer | Intrinsic | glossary `d2-designer`; Phase 5 §Item 2 |
| R-01 | D1 Designer | Intrinsic | Phase 1 §2; glossary `d1-designer` |
| R-02 | D2 Assistant | Intrinsic | Phase 2 §Principle 3; Phase 4 §Item 3 |
| R-03 | D1 Programmer | Default | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | Default | Phase 5 §Item 3; RU-01 |
| R-05 | D0 Operator | Default | Phase 5 §Item 3; glossary `d0` |
| R-06 | D0 Technical Manager | Default | Phase 5 §Item 3; glossary `d0` |

Rule for tagging: the **D2-layer** roles (builder, primary user, D2's own interaction agent) are
**intrinsic** — fixed by the ecosystem's structure. The **D1/D0 product-cast** positions are
**default** — D2 supplies them as a starting cast the D1 Designer may reshape for his particular
product (glossary `role`; method §1 setup step). The **Design Node Builder** named in Phase 5
§Item 3 is represented by the D2 Assistant's node-building actions (A-033) rather than as a separate
role — a judgment call flagged for the parent.

### 2b. Per-role action children — sub-contracts

For each role, *derive the actions from its job function and the relevant phase items; name, assign
a stable ID (`A-<digits>`, `A-003` retired/skipped), give a substantial description of what the
action **is**, cite a Source.*

- **R-01 D1 Designer — the walk-the-journey case.** Walk his journey across **Phases 3–4 + method
  §1** (entry → operating contract → initial input → understanding/direction → enter D1 mode →
  operating framework → setup roles/posture → foundational docs → node-building review →
  oversight/inspection → audit) and **sub-split each action** `[P] passive` (he responds to
  something D2 brings — a review/stopping point, a clarification point; the near-universal,
  anticipable forms, method §1 / Phase 4 §Item 2) vs `[A] active` (his own initiative — monitor,
  inspect, drill down, redirect, lay down a rule, propose a change, audit; fluid, project-dependent,
  Phase 4 §Item 3). The **D0-user optimization** throughline (A-025) is carried as a standing
  cross-cutting action (method §1; Phase 5 §Item 3).
- **R-00 D2 Designer / R-02 D2 Assistant — obligation-derived.** Lift the builder's actions from
  glossary `d2-designer` + Phase 5 §Item 2 + `RU-02`/design-tree; lift the Assistant's actions from
  D2's standing obligations in Phases 1–4 (unified interaction, investigate-before-escalate,
  human-oriented reporting, observability, node building, provenance discipline).
- **R-03…R-06 downstream product roles — position-derived.** Elaborate the actions implied by each
  position's Phase 5 §Item 3 **job function** (implement code; adjust governed parameters + run the
  harness + repackage; routine operation + user-level monitoring + operating controls; install +
  maintain + configure the deployment), tagging every elaborated row **position-derived** and
  anchoring it on Phase 5 §Item 3 (with RU-01 / glossary `d0` / `d1` where they sharpen it).

## 3. Aggregate

Merge the per-role returns into a single `A-` table grouped by role, in R-00 → R-06 order.
De-duplicate; assign stable, unique IDs sequentially, **skipping the retired `A-003`**. The
Action node **authors and owns** this aggregate (`RU-09`); the Roles table is inherited context.

Scope produced: **7 roles**, **50 actions**, IDs **A-001…A-051** (A-003 skipped). The D1 Designer
carries **21** actions, split **11 [P] / 10 [A]**.

## 4. Self-check against acceptance (the termination condition)

Per `input/contract.md` §3 and `design-node-algorithm.md` step 4:

- **Coverage** (open-list). Every action a competent re-derivation would surface is present: the
  full passive journey (entry, operating contract, input, understanding, mode-entry, framework,
  setup, foundational docs, clarification, node review, completion reports), the common active set
  (monitor progress, monitor cost, inspect D0, inspect the tree, drill down, directive, rule,
  propose, audit), the D0-user throughline, D2's standing obligations, and each downstream
  position's job function. Aim = the **common, anticipable** set, not exhaustive enumeration.
- **Traceability.** Every role and every action row cites a `Source` inside the `sources.md`
  namespace; no `Phase 6` or bare `Designer <date>` citation is used.
- **Integrity.** IDs unique and stable, grouped by role, deduplicated; `A-003` retired; the table
  is shaped so `RU-11` (action → capability coverage) can consume it downstream.
- **Substance.** Each role and each action carries a real descriptive phrase (what it **is**), not
  a one-word label.

Gaps found → derive more; when the four checks pass, the node **terminates** and submits.

## 5. Submit (`RU-02`)

Two-step submission (structure defined, not exercised by this test): **Step 1** submits this
algorithm + the declaration for activation; **Step 2** submits the result (the catalog with
substantial descriptions) for acceptance. On acceptance the aggregate drives the successor
**capability → architecture → implementation** cascade (`RU-11`).
