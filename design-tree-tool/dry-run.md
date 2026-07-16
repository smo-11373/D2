# Dry run — the D2 design tree up to the Role-Action table

*No code. A paper application of the design-tree framework to the D2 design we have actually
produced, stopping at the role-action table. Lay out the nodes first, then the contents of each,
then report what the exercise reveals. This is a **test of the framework** (`design-tree.md`),
not D2 design content.*

## 1. Nodes (laid out)

```
Fundamentals
├── Decision to use D2          [functional; independent of Setup]
└── Setup
    └── Roles                    [table node — owns the role table R-]
        └── Role-Action          [table node — owns the role-action table A-]
```

Stopping at **Role-Action** per the exercise; the Functionality (capabilities `C-`) and Architecture
layers are the next dependency step, out of scope here. Edges are **design dependency**, not the
Designer's action order (`RU`, design-tree.md).

## 2. Contents of each node

### Fundamentals (root)
- **Owns / enforces:** the governing method + rules for the whole tree.
  - D2 constitution — **Phases 1–5** (in `../ref/`), *referenced, not re-authored*.
  - Phase 6 method — functional doc **§1** (translate-to-actionable; passive/active; open-list;
    D0-user throughline; bookkeeping).
  - Design-tree rules — **`RU-01…RU-08`**.
- **Contract to children:** the method + rules + a link to Phases 1–5.
- **Justification (RU-02):** §1's argument, grounded in Phases 1–5.

### Decision to use D2  (child of Fundamentals)
- **Owns / refs:** functional doc **§2**. Action **`A-055`** (adopt / decline / defer); capability
  **`C-37`** (adoption orientation — the orientation summary + its key elements).
- **Contract received:** the fundamentals.
- **Justification:** §2 "Why" — Phase 1 authority; Phase 2 progressive disclosure.
- **Independent of Setup** — no dependency edge between them (both spawn from Fundamentals).

### Setup  (child of Fundamentals)
- **Owns / refs:** functional doc **§3** (the *posture + setup-package* part) + the inspectability
  floor. Actions **`A-015/A-019/A-016/A-017`**; capabilities **`C-01/C-22/C-02/C-03/C-05`**.
- **Contract received:** the fundamentals.
- **Contract to Roles (child):** the setup frame + link to fundamentals.
- **Justification:** §3 "Why" — Human Position First; accept-the-defaults.

### Roles  (child of Setup — table node)
- **Owns:** the **role table `R-`** — R-00 D2 Designer · R-01 D1 Designer · R-02 Design Node Builder ·
  R-03 D1 Programmer · R-04 D1 Technical Manager · R-05 D0 Operator · R-06 D0 Technical Manager ·
  R-07 D2 Assistant. Each tagged intrinsic / default (functional doc **§3a**). Action **`A-056`**;
  capability **`C-38`**.
- **Contract received (from Setup):** the setup frame + link to fundamentals.
- **Contract to Role-Action (RU-08):** the role table (read-only) + relevant links.
- **Justification:** §3a — Human Position First; the intrinsic/default provenance.

### Role-Action  (child of Roles — table node)
- **Owns:** the **role-action table `A-`** — `A-001…A-058` (A-003 retired), the actions each role
  performs. By role: R-00 meta (A-010/011); R-01 the D1 Designer's actions (setup, input, confirm,
  oversee, inspect, monitor, evaluate — incl. A-052–058); R-02 node-building (A-021–027); R-03–R-06
  the downstream product roles (A-028–051).
- **Contract received (from Roles, RU-08):** the role table (read-only) + links.
- **May propose up (RU-04/05):** to change the role table it proposes to Roles and **stops** until
  resolved.
- **Justification:** each row's **Source** column (baseline-derived / position-derived /
  Designer-dated).

## 3. Findings — what the dry run reveals

1. **Table-node vs functional-node overlap is real (the main finding).** `A-055` (Decision's data)
   and `A-015` (Setup's data) also live in the `A-` table owned by **Role-Action**, which sits
   *below* Setup in the tree. So Setup "references" rows owned by its own **descendant**. The
   reference model (`RU-04`) holds logically, but the *placement* is inverted: the aggregating table
   node is a leaf, while its rows' *meaning* originates in higher functional nodes.
   - Candidate resolutions: (a) Role-Action owns the table as **pure aggregation**; functional nodes
     own the *meaning* of their rows and add them via propose-up-then-down; (b) **invert** — the
     functional areas are children *of* Role-Action; (c) treat the table as a **shared artifact with
     per-row ownership**.

2. **§4 (foundational documents) and §5 (operating framework) have no node.** Their actions
   (`A-013/018/057`, `A-001/002/004`) sit in the `A-` table, but the functional areas aren't in the
   tree — the first cut only made nodes for Decision and Setup. Either add **Foundational-docs** and
   **Operating-framework** as Fundamentals-children (siblings of Decision/Setup), or accept that
   functional areas **dissolve into the table nodes**.

3. **The catalog-layer spine is clean.** `Roles → Role-Action` is a genuine one-directional
   dependency (actions need roles) and maps exactly onto Role → Action.

4. **Adjacency + links work.** Role-Action talks only to Roles (`RU-07`); to reach Fundamentals it
   relays up the chain, while contract links (`RU-08`) let it *read* ancestor data without direct
   communication.

5. **Justification is already present.** The design's existing "Why" sections and `Source` columns
   *are* the node justifications (`RU-02`); they simply attach at each node's submission.

## 4. Verdict

The framework **applies and largely holds** up to the role-action table: ownership, contracts,
adjacency, stopping-points, and justification all land on real content. The one genuine unresolved
structural question is **Findings #1 + #2 — how functional areas (Decision, Setup, Foundational-docs,
Operating-framework) relate to the catalog-table nodes (Roles, Role-Action)**: is the tree organized
by *functional area*, by *catalog layer*, or a hybrid? Recommend settling that before extending the
tree past Role-Action.
