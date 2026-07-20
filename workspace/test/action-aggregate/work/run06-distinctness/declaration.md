# Declaration — the Action-Aggregate node's manifest (Step 1 activation product)

*The node's identity, plan, deliverable, downstream interface, and acceptance self-check record.
Submitted with `algorithm.md` at **Step 1 (activation)**, before children are spawned. First-cut
meaning of "declaration": the node's manifest / plan / downstream interface (contract §1.3).*

## 1. Identity

- **Node:** Action-Aggregate (a.k.a. the Action / action-integration node) — the **Role-Action** node
  of the D2 design tree (`framework/design-tree.md`).
- **Position in the tree:** child of **Roles**, which is a child of **Setup → Fundamentals**. Depends
  on Roles (reads its `R-` table read-only); drives **Functionality (Capability)** downstream.
- **Owns & authors:** the **role-action aggregate `A-` table** (`RU-09`/`RU-10`). It does **not** own the
  role table — that is inherited read-only from the Roles node; changes to it are proposed up (`RU-04`).
- **Authority:** sub-human design-node authority; justifies its own result, the parent (Fundamentals)
  accepts or rejects (`RU-02`; submission ≠ acceptance).

## 2. Deliverable (what it will produce)

An **output package of three products** (contract §1), across a two-step submission:

1. **`role-action-catalog.md`** — the role-action aggregate table with **substantial descriptions**:
   the actions each recognized role performs, merged, grouped by role, stable IDs, each row
   Source-cited; each action and each role carrying a substantial description. *(Step 2 — result.)*
2. **`algorithm.md`** — the reproducible derivation procedure (seek roles → per-role actions →
   aggregate → self-check). *(Step 1 — activation.)*
3. **`declaration.md`** — this manifest. *(Step 1 — activation.)*

## 3. Method summary

Seek roles from Phase 5 §Item 3 + the layer model (tag intrinsic/default); derive per-role actions from
each role's job function and the relevant phase items — the D1 Designer's full journey sub-split
passive/active, the operational cast via the position-derived depth frame, and the harness-richness bias
across every role; aggregate grouped by role; self-check conformance → completeness → distinctness →
traceability → integrity. Full detail in `algorithm.md`.

## 4. Downstream interface (to the capability branch)

The completed, accepted **`A-` aggregate table is the read-only input and driver for the Capability
node** (`RU-11`): its contract is to design the capabilities (`C-`) that **cover every action** in the
aggregate — coverage is the contract (every action → ≥1 capability, autonomous capabilities excepted);
the action↔capability map records it and a coverage check verifies nothing is missed. The interface the
Action node offers is therefore: a **stable, IDed, Source-cited, deduplicated action set** whose rows
are distinct responsibilities, sized so each is a coherent unit for capability derivation. Successor
cascade: **Capability → Architecture → Implementation** (`RU-11`; out of scope for this test).

## 5. Acceptance self-check record

Run per `algorithm.md` Step 4. **Result: PASS — no conformance conflict; no propose-up-and-halt required.**

- **Conformance (gating): PASS.** No governing statement contradicted. The role set reproduces Phase 5
  §Item 3's named position enumeration exactly (six named positions + D2 Designer from the layer model)
  — none collapsed, dropped, or re-cast. The passive/active split, the position-oriented control lists
  (spending limits/scheduling for the Operator; deployment settings for the D0 TM; product
  defaults/release params for the D1 TM), and Harness First ("no code change does not mean no harness")
  are all honored, not contradicted.
- **Completeness (active): PASS.** The should-exist set was derived and checked present: the seven
  positions; the D1 Designer's full journey (entry → setup → input → understanding → foundational docs →
  operating framework → clarification → node review) plus the active register (monitor/inspect/
  investigate/direct/audit); the depth-frame facets for each operational role; the maintenance cycle
  (diagnose→fix→recover→record) for both Technical Managers; and the harness facets (test/monitor/
  detect/make-visible) surfaced across roles.
- **Distinctness guard (strict): PASS.** See §6.
- **Traceability: PASS.** Every row cites an in-package Source (`sources.md` namespace).
- **Integrity: PASS.** 7 roles `R-00…R-06`; 48 actions `A-001…A-049` with **`A-003` retired**; contiguous,
  grouped by role, deduplicated; the action↔capability map will resolve (`RU-11`).

## 6. Distinctness guard — what was merged or dropped (vs a maximal enumeration)

Per Quality over Expediency (Phase 5 §Item 4/5), completeness is *distinct responsibilities covered*,
not row count. Relative to a maximal enumeration, this table:

- **Did not create standalone rows for governing rules the roles merely operate under** — adjacency
  (`RU-07`), work-within-contract (`RU-08`), decompose-internally (`RU-10`), coverage-is-the-contract
  (`RU-11`). These are folded into the actions they govern (e.g. into the Design Node Builder's
  spawn/submit rows), not enumerated as actions.
- **D1 Designer:** dropped "confirm entry into D1 design mode" (Phase 3 Item 4 is a D2 notification, not a
  distinct Designer responsibility); folded "being asked only when it's worth it" (a D2 quality, not an
  action); folded "lay down a rule" and the Designer-initiated-change flow (`RU-06`) into **A-017**
  (exercise Designer authority); merged progress-monitoring and health/abnormality-monitoring into **A-014**.
- **D0 Operator:** merged "routine monitoring" and "view the operator-level health report" into one
  monitoring responsibility (**A-038**) rather than two rows.
- **Operational cast:** elaborated only the depth-frame facets each function genuinely implies — the
  Programmer has no configure/view/maintenance-cycle rows; the Operator escalates rather than running a
  maintenance cycle — never inventing an action to fill a facet.
- **Kept as distinct** (not over-granular) the harness/safety facets Harness First elevates to
  first-class: **run-the-harness**, **recover-from-a-failed-change**, and **record-the-change** for the
  maintenance positions are separate responsibilities (verification, failure-safety, traceability), not
  micro-steps of a single "maintain" action.

## 7. Open item recorded (judgment, not a propose-up)

**"D2 Assistant"** appears only in the algorithm's depth-frame scope guard as an internal/meta label. It
is **not** named in Phase 5 §Item 3 (the authoritative position enumeration), has no job function in the
frozen constitution, and carries no glossary `R-` id. Instantiating it would force invented actions
(violating derive-from-frozen-inputs). Its assistance/interaction-fronting function is covered by D2's
**unified-interaction** responsibility (Phase 2 Principle 3), which at this layer is a **capability**
concern, not a distinct action-bearing position. It is therefore **not instantiated as a role**. This is
a conformance-preserving **judgment** (Phase 5 Item 3's named enumeration is honored exactly), not a
conformance conflict — so **no upward proposal / halt** is raised (`RU-04`/`RU-05` not triggered).
</content>
