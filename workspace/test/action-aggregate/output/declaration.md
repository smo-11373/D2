# Declaration — the Action-Aggregate node

*Deliverable 3 of the Action-Aggregate node (contract §1.3 — the Step-1 activation artifact). The
node's manifest / plan / downstream interface: its identity, what it will deliver, and the interface
it offers the capability branch. First-cut meaning of "declaration" (contract §1.3): a node's
**manifest + plan + downstream interface**.*

## 1. Identity

- **Node:** Action-Aggregate (a.k.a. the action integration node).
- **Parent:** Fundamentals (the D2 Designer's frozen constitution + method + rules).
- **Position in the design tree:** `Fundamentals → Setup → Roles → **Role-Action** → Functionality`.
  It **depends on** the Roles node (reads the role table read-only via its contract) and **drives**
  the Functionality/Capability node (`RU-11`).
- **Authority:** a design-node agent with sub-human authority (glossary `design-node`). It
  **authors and owns** the role-action aggregate `A-` table (`RU-09`); it **reads** the role `R-`
  table but is **not** its author — changes to the role table are **proposed up** to the Roles node
  (`RU-04`).

## 2. What it will deliver (the output package — three products, two-step submission)

| # | Product | Submission step | Status |
|---|---|---|---|
| 1 | **Role–Action aggregate table** with substantial descriptions — actions per role, merged, grouped, stable IDs, `Source`-cited; each role and action described. | Step 2 — the result | delivered (`role-action-catalog.md`) |
| 2 | **The algorithm** — the reproducible derivation procedure. | Step 1 — activation | delivered (`algorithm.md`) |
| 3 | **The declaration** — this manifest / plan / downstream interface. | Step 1 — activation | this document |

**Decomposition (internal, `RU-10`).** The node may dissect the work by category — passive-action /
active-action sub-nodes, and per-role action sub-nodes (seek roles → per-role actions → aggregate) —
but is obligated only to return the **aggregate** `A-` table at its boundary. Internal shape is the
node's discretion; the aggregate is the obligation.

## 3. Downstream interface (offered to the capability branch)

Per `RU-11` (**coverage is the contract**): the completed aggregate `A-` table is the **read-only
input and driver** for the **Capability node**, whose contract is to design capabilities (`C-`) that
**support every action** in the aggregate (autonomous capabilities excepted). The interface this
node offers downstream:

- **The `A-` table** — 73 actions, `A-001…A-074` (`A-003` retired), grouped by 8 roles
  `R-00…R-07`, each row `Source`-cited and described.
- **A coverage handle** — every `A-` id is a coverage obligation for the Capability node; the
  action↔capability map is expected to resolve every id to ≥1 capability.
- **Change protocol** — the Capability node **reads** this table; to change it, it **requests down**
  through the author (this node re-derives and re-submits); it does not edit what it does not author
  (`RU-09`). To change the inherited role table, it proposes up through this node to the Roles node.

## 4. Conformance argument (contract §3, gating)

Submitted per `RU-02` with the node's own justification; the self-check (algorithm §Step 4) ran
**conformance first and gating** and passed:

- **Named enumerations honored.** All Phase 5 §Item 3 positions are present and distinct — D1
  Designer, Design Node Builder, D1 Programmer, D1 Technical Manager, D0 Technical Manager, D0
  Operator — plus the glossary's D2 Designer and the **completion-named D2 Assistant**
  (`completions.md C-2026-07-19-1`), which is **gating**. None collapsed, dropped, or re-cast.
- **Method disciplines honored.** The D1 Designer's actions carry the **passive/active** split; the
  **D0-user throughline** is present (A-027); the list is treated as **open** (common, anticipable
  set, not a closed enumeration).
- **Distinctions preserved (not over-merged).** Cost vs health monitoring kept distinct (A-017/A-018,
  A-055/A-056); wrapper vs deployment monitoring kept distinct (A-049/A-063) — per the distinctness
  guard, which merges only mechanical steps and rule-restatements.
- **Work-conservation holds.** Every action is owned by a role; **every lifecycle transition has an
  owning position** — foundational-docs → framework → implement → test → package → install →
  smoke-test → hand-over → operate → monitor → detect → diagnose → recover → record → upgrade →
  re-test → re-deploy — **no transition was left without an owner**, so no position had to be added
  beyond those the fundamentals and completions name.

No conformance conflict was found; therefore **no propose-up-and-halt** (`RU-04`/`RU-05`) was
raised. The deliverable is emitted as conformant, complete against the four lenses, work-conserving,
and de-duplicated at the fundamentals' own granularity — not emitted-and-flagged.

## 5. Scope note

This test **defines** the two-step submission structure but does **not exercise** submission,
approval, or the capability→architecture→implementation cascade (contract §6). This declaration
therefore states the interface and plan; it does not itself seek activation approval within this run.
