# Algorithm — deriving the Role–Action Aggregate (Step 1 activation product)

*The reproducible procedure the Action-Aggregate node runs to derive `role-action-catalog.md` from
the frozen inputs. It is a **product of running the module's method** over this contract — not the
module itself. Its purpose is reproducibility: contract + same frozen inputs + this procedure ⇒ a
**substantially matching** table (same roles; substantially the same actions modulo naming,
granularity, and the open-list tail). Derive from the inputs; invent nothing; cite Sources.*

## Inputs (read-only, frozen)

- **Constitution** — Phases 1–5 (`constitution/phase-1…5-*.md`). Positions live in **Phase 5 §Item 3**.
- **Method** — functional doc §1 (`method.md`): identify Designer actions → abstract the common element
  → split passive/active → keep the D0-user throughline → treat the list as open.
- **Rules** — `RU-01…RU-11` (`rules.md`).
- **Glossary / Framework** — `glossary.md`; `framework/{design-tree, design-node-algorithm, conformance}.md`.
- **Source namespace** — `sources.md` (cite only in-package Sources; resolve out-of-package pointers).

## Procedure

### Step 1 — Seek the roles

Spawn (conceptually) a **Roles** child. Sub-contract: *derive the role table from **Phase 5 §Item 3**
(Human Position First) + the **layer model** D2 → D1 → D0.*

1. Extract every named position from Phase 5 §Item 3: D1 Designer, Design Node Builder, D1 Programmer,
   D1 Technical Manager, D0 Technical Manager, D0 Operator.
2. Add the **D2 Designer** from the layer model + glossary `d2-designer` (the builder; `R-00`).
3. Assign IDs in layer order **R-00…R-06**, honoring the pinned IDs (glossary `R-00`/`R-01`/`R-05`/`R-06`;
   `RU-01` `R-04`); the free slots fill Phase 5 Item 3's own ordering (Design Node Builder `R-02`,
   D1 Programmer `R-03`).
4. Tag each **intrinsic** (fixed to the ecosystem) or **default** (a D2-provided default the D1 Designer
   can change at setup) per glossary `role`. Give each a substantial description. Cite the Source.
5. **Guard against invention:** a label named only in a scope-aside (e.g. "D2 Assistant" in the
   algorithm's depth-frame guard) with no Phase 5 Item 3 entry and no job function is **not**
   instantiated as a role — it would force invented actions. Record the judgment (see `declaration.md`).

### Step 2 — Actions per role

For each role, spawn (conceptually) an **action** child. Sub-contract: *derive this role's actions from
its **job function** and the relevant phase items; Source-cite each; name it; assign a stable `A-` id
(continue the sequence, **skip `A-003`**).* Apply the discipline appropriate to the role's kind:

- **D1 Designer (`R-01`) — walk the full journey; sub-split passive/active.** Lift each action from the
  method's ordered journey and Phases 1–4: entry (decide to use D2) → operating contract → setup
  (roles + posture) → design input → understanding/direction → foundational docs / D1 Constitution →
  operating framework → clarification responses → node reviews (passive [P]); and the active-interaction
  register — monitor, inspect, investigate, direct/intervene, audit (active [A]) (method §1; Phase 3;
  Phase 4 §Item 3).
- **Internal/meta roles (`R-00` D2 Designer, `R-02` Design Node Builder) — no depth frame.** Derive from
  their constitutional function (Phase 5 §Item 2; Phase 4 §Item 2; glossary). Apply the **harness-richness
  bias** (below).
- **Operational cast (`R-03` Programmer, `R-04`/`R-06` Technical Managers, `R-05` Operator) — apply the
  position-derived depth frame.** For each, elaborate the actions its Phase 5 §Item 3 job function
  *genuinely implies* across the recurring facets: **operate · monitor · configure · view/report ·
  handle routine errors · escalate**; maintenance/support positions also walk **diagnose → apply-fix →
  recover-from-a-failed-change → record-the-change**. The frame is a completeness *prompt*, not a
  checklist — never invent an action to fill a facet a position does not imply.
- **Every role — harness-richness bias (Harness First).** Hunt each position's harness facets: what does
  it **test**, **monitor**, **detect** (hidden errors/failures), and **make visible**? Surface these
  preferentially; a role thin on testing/monitoring/health-visibility is a deficiency to investigate.
  Bias ≠ padding (Quality over Expediency): do not manufacture a harness the fundamentals don't warrant,
  nor split one responsibility into mechanical steps. *(Phase 5 §Item 1; Phase 2 Principle 4; glossary `d1`.)*

### Step 3 — Aggregate

Merge the per-role action pieces into one `A-` table, **grouped by role** in layer order, IDs
contiguous (skipping `A-003`), deduplicated. The Action node **authors** this aggregate (`RU-09`/`RU-10`);
internal decomposition (e.g. passive/active sub-nodes) is discretionary but the **aggregate** is the
obligation.

### Step 4 — Acceptance self-check (the termination condition)

Run in order; on failure, revise (or propose-up-and-halt) — never emit-and-flag:

1. **Conformance (first, gating).** The deliverable contradicts **no** governing statement of the
   fundamentals — no principle, **named enumeration**, method discipline, or rule. Distinct from
   traceability (a cited Source is necessary but not sufficient). E.g. the role set must not collapse,
   drop, or re-cast Phase 5 Item 3's named position enumeration. On conflict: **revise to conform** or
   **propose up and halt** (`RU-04`/`RU-05`). *(framework `conformance`.)*
2. **Completeness (active).** Derive the *should-exist* set from the fundamentals and check each is
   present — **gating** for pieces the fundamentals name or explicitly list (the position enumeration,
   the passive/active journey, the position-oriented control lists, the depth-frame facets), a **strong
   bias** for what a competent derivation implies, open-list only at the genuine tail. On a gap, **derive**
   the missing piece.
3. **Distinctness guard (Quality over Expediency, Phase 5 §Item 4/5) — applied strictly.** Each row is a
   **distinct responsibility the role performs** — not a mechanical step, not a restatement of a governing
   rule the node merely operates under (e.g. adjacency `RU-07`, work-within-contract `RU-08`, decompose
   `RU-10`, coverage `RU-11` — folded into the actions they govern, not separate rows), not a
   re-granularization of one responsibility. **De-duplicate by responsibility.** Completeness is measured
   in *distinct responsibilities covered*, not row count.
4. **Traceability.** Every row cites a Source resolving inside the package namespace (`sources.md`).
5. **Integrity.** Stable IDs, grouped by role, deduplicated, `A-003` retired; the action↔capability map
   will resolve (`RU-11`).

### Step 5 — Submit (structure only; not exercised by this test)

Two-step submission: Step 1 submits **algorithm + declaration** (activation); on acceptance the node
spawns children and does the work; Step 2 submits the **table with substantial descriptions** (result),
each carrying an attached **justification** including an explicit conformance argument (`RU-02`). The
completed aggregate then drives the **Capability → Architecture → Implementation** successor cascade
(`RU-11`).

## Why it reproduces

The inputs are **frozen** (Phases 1–5), the method is fixed, and acceptance is coverage/conformance
against those inputs — so two competent runs converge on the **same roles** and substantially the same
actions. The residual "not identical" is confined to naming, granularity, which position-derived actions
get elaborated, and the open-list tail (contract §5).
</content>
