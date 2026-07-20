# Declaration — the Action-Aggregate node

*Product 3 of 3 (contract §1; Step-1 activation product). The node's manifest / plan / downstream
interface: its identity, what it will deliver, and the interface it offers the capability branch.
First-cut meaning of "declaration" per contract §1.3 — **to confirm** with the parent.*

## Identity

- **Node:** the **Action-Aggregate node** (a.k.a. the action-integration node) — a design node
  (glossary `design-node`): a self-contained unit of design responsibility, one agent at its
  boundary, authority below the human Designer's.
- **Position in the tree:** child of **Roles**, itself under Setup → Fundamentals; parent of the
  **Functionality (capability)** node it drives (`framework/design-tree.md`).
- **Owned data:** it **authors and owns** the role-action aggregate `A-` table (`RU-09`). It **reads**
  the role table `R-` handed down in its contract but does not author it — a change to the role table
  is a **propose-up** to the Roles node (`RU-04`), never a local rewrite.

## What it will deliver (the output package — contract §1)

1. **`role-action-catalog.md`** — the role-action aggregate table with substantial descriptions:
   the actions each recognized role performs, **merged, grouped by role**, stable IDs, each row
   Source-cited, each action and each role carrying a substantial description. *(Step 2 — the result.)*
2. **`algorithm.md`** — the reproducible derivation procedure (seek roles → per-role actions →
   aggregate → acceptance self-check). *(Step 1 — activation.)*
3. **`declaration.md`** — this manifest. *(Step 1 — activation.)*

**Delivered set (this run):** **8 roles** (R-00…R-07), **62 actions** (A-001…A-063, A-003 retired).
Per role — R-00 D2 Designer 4 · R-01 D1 Designer 18 · R-02 Design Node Builder 9 · R-03 D1 Programmer
4 · R-04 D1 Technical Manager 8 · R-05 D0 Operator 6 · R-06 D0 Technical Manager 7 · R-07 D2 Assistant 6.

## Inputs consumed (read-only)

The constitution (Phases 1–5) **and its completions**, the method (functional doc §1), the rules
`RU-01…RU-11`, the framework (design tree, design-node algorithm, conformance), the glossary, under
the `sources.md` citation namespace. Nothing outside this namespace is cited or invented.

## Acceptance the node commits to (contract §3)

**Conformance** (first, gating) · **Completeness** (active, incl. work-conservation) · **Distinctness**
(de-dup by responsibility at the fundamentals' own granularity) · **Coverage** (open-list target) ·
**Traceability** (in-namespace Source per row) · **Integrity** (stable IDs, grouped, deduplicated) ·
**Substantial reproducibility**. On a conformance conflict the only legal moves are revise-to-conform
or propose-up-and-halt (`RU-04`/`RU-05`) — never emit-and-flag.

## Downstream interface (the interface offered the capability branch)

- **The aggregate drives the next layer (`RU-11`).** The completed `A-` table is the **read-only
  input and driver** for the **Capability node**, whose contract is to design the capabilities (`C-`)
  that **cover every action** — coverage is the contract; every action maps to ≥1 capability
  (autonomous capabilities excepted), recorded in the action↔capability map and verified by a coverage
  check.
- **Harness propagation.** The harness-rich rows (test / monitor / detect / make-visible — e.g.
  A-027, A-034, A-038, A-043, A-047/048, A-054, A-062/063) carry the Harness-First emphasis **forward**
  to capability → architecture, where the actual test suites, monitors, and health checks are designed.
- **Change discipline at the boundary.** The parent (Roles / Fundamentals) may **read** the whole
  package and **request-down** changes to this node's `A-` table (the node re-authors and re-submits);
  the node **proposes-up** to change the inherited `R-` table (`RU-09`). Communication is
  adjacency-only (`RU-07`); read-context links arrive via the contract (`RU-08`).

## Two-step submission (structure defined; not exercised by this test — contract §6)

- **Step 1 — activation:** submit `algorithm.md` + this `declaration.md` to the parent (Fundamentals)
  for approval (`RU-02`). Only on acceptance is the node activated to spawn its children (Roles →
  per-role actions) and do the work.
- **Step 2 — result:** submit `role-action-catalog.md` with substantial descriptions. On acceptance
  the deliverable is final. Thereafter (out of scope) the successor cascade capability → architecture
  → implementation is called out (`RU-11`).

## Self-check outcome (no propose-up-and-halt raised)

The acceptance self-check **passed**; no conformance conflict required a propose-up-and-halt.

- **Conformance:** all named positions present and distinct — the six Phase 5 §Item 3 positions, the
  D2 Designer (R-00), and the **completion-named D2 Assistant** (R-07, `completions.md C-2026-07-19-1`).
  No enumeration collapsed; the passive/active split and the position-oriented control lists are honored.
- **Completeness / work-conservation:** every candidate position was **kept** — none folded — so no
  actions were orphaned or redistributed. The D2 Assistant was **taken from the completion** as a
  first-class position and its stated responsibility (route / present / preserve-context / answer)
  derived into A-058…A-063; without it, that interaction work would be orphaned (the completion's own
  basis).
- **Distinctness (calibrated):** merged only mechanics and rule-restatements (e.g. the Designer's
  "reserve revision authority" folded into A-011 framework-confirmation + A-019 directive; the Builder's
  node-report and submission folded into A-030). **Preserved** the fundamentals' own distinctions —
  the D1 Designer's **monitor cost (A-017) vs monitor health (A-018)** are kept separate per Phase 4
  §Item 3; the D0 Operator's **routine monitoring (A-047) vs user-facing health report (A-048)** are
  kept separate (distinct Source/artifact).
