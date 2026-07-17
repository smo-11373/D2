# Rules Catalog

*Living. Design rules and constraints, each with the role or principle it derives from. One record per rule. See `README.md` for ID conventions. Rules should be **derived, not invented** (Phase 5): D2 should be able to explain the quality concern or position a rule protects.*

## RU-01 — No hard-coded numbers (in most situations)

- **Rule:** Values that may legitimately require product-level adjustment without redesign or programming should be exposed as **explicitly governed parameters**, not hard-coded. *("In most situations" — not literally every value; Phase 5: it "does not require every literal value to become configurable.")*
- **Derived from:** **R-04 D1 Technical Manager** — *position existence creates design consequences* (Phase 5 §Item 3). The D1 Technical Manager must be able to upgrade the product by adjusting a governed parameter, without touching code, to the extent plausible.
- **Harness note:** *"No code change does not mean no harness."* A parameter change still runs the required validation/regression harness — the D1 wrapper's upgrade smoke-test suite (see glossary `d1`).
- **Scope:** D1 / D0 design.
- **Source:** Phase 5 §Item 3 (Human Position First); §Item 4 (Quality over Expediency — "avoid hard-coded adjustable values").
- **Status:** Accepted (baseline-derived).

## RU-02 — A node justifies its own result; the parent approves

- **Rule:** Each design node is responsible for the **justification** of its design result. The justification is authored by that (child) node and **attached to its submission package**; the **parent node — as enforcer — reviews and approves or rejects** it. Justification travels *with* the result, added once the node is designed, not maintained separately.
- **Derived from:** the **design node** as a self-contained agent with sub-human authority (glossary `design-node`); **submission ≠ acceptance** (a node may produce and justify, but acceptance authority sits with the parent); *authority follows meaning*.
- **Scope:** D2 and D1 design (design-tree governance; applies to D2's own design too — the Phase 6 "Why" narratives are node justifications in this sense).
- **Source:** Phase 4 §Item 2 (submission vs acceptance; upward proposals routed by authority); Phase 6 Item 2 §7; Designer 2026-07-15.
- **Status:** Accepted (Designer-directed).

## RU-03 — Spawn design-tree children by the Designer's actions

- **Rule:** A design node's **spawning** is driven by the relevant **Designer's potential actions** — each node determines its children by the actions its scope must support. The action set splits into **passive** (a *static* list derived from the approved setup/fundamentals — one child per passive action is straightforward) and **active** (dynamic and flexible — harder). **Passive-action spawning is implemented first; active-action spawning is deferred.**
- **Derived from:** the node's **spawning responsibility** (C-16; Phase 4 §Item 2 — spawning strategy) and the **passive/active action model** (functional doc §1). Actions are the common unit both the tree (nodes) and the capability model (support) hang on.
- **Scope:** D2 and D1 design (design-tree governance; applied to D2's own design first).
- **Source:** Phase 4 §Item 2; Phase 6 functional model (passive/active actions); Designer 2026-07-15.
- **Status:** Accepted (Designer-directed); active-action spawning deferred.

## RU-04 — Contract passes down; changes to inherited data are proposed up

- **Rule:** A parent node specifies a **contract** for each child, and the contract **includes the parent's owned data** that governs the child (e.g. the **Role node** owns the role table and passes it to the **Action node** as part of its contract). The child works **within** the contract. To change **inherited (ancestor-owned) data**, the child **proposes the change upward** to the owning node, which **accepts or rejects** — a node may not rewrite what it does not own.
- **Derived from:** *authority follows meaning*; the node owns-its-own-data rule (glossary `design-node`); Phase 4 §Item 2 (child contract; upward revision proposals — "Designer control prevents silent revision, **not** upward feedback").
- **Scope:** D2 and D1 design (design-tree governance).
- **Source:** Phase 4 §Item 2; Designer 2026-07-15.
- **Status:** Accepted (Designer-directed).

## RU-06 — Evaluate before you propose (evaluation is separate from the official proposal)

- **Rule:** A proposed change is **evaluated before it is officially proposed**, and evaluation is a **separate step/command** that **commits nothing**. Evaluation **dry-runs** the change: it probes **upward** (would the change land correctly on the ancestor?) and **downward** (how does it alter the child's contract / affect the child?), and returns an **evaluation report**. On the report, the initiator either **formalizes** the change or **revises** it. Only the **official proposal** propagates the change (up, then — if accepted — down) and firms it up (RU-04, RU-05).
- **Two initiation sources:** (a) **agent-initiated** — a node proposes a change while building under its contract, or in response to a child's proposal; (b) **Designer-initiated** — the D2 Designer (later the D1 Designer) proposes a change, usually after a round or more of **discussion**.
- **Derived from:** *Verification Before Realization* (evaluate before committing); impact analysis (C-05); the propose-up / stopping-point discipline (RU-04, RU-05).
- **Scope:** D2 and D1 design (design-tree governance).
- **Source:** Designer 2026-07-15.
- **Status:** Accepted (Designer-directed).

## RU-09 — A table is changed only through its author (propose-up or request-down)

- **Rule:** Each table is **authored and owned by exactly one node**: the **Role node** authors the role table (`R-`); the **Action node** authors the role-action table (`A-`). Other nodes — **including the parent** — may **read** the whole package but are **not the author**. A table is changed **only through its author**: a node **proposes up** to change an *ancestor-authored* table (`RU-04`), and a parent **requests down** to change a *child-authored* table (the author makes the change and re-submits). **No node edits a table it does not author.**
- **Resolves the ownership inversion:** an aggregating child keeps authorship of its own table; the parent reaches it by **read + request**, not by owning it.
- **Derived from:** authority follows meaning; RU-02 (justify at submission); RU-04 (contract / propose-up).
- **Scope:** D2 and D1 design (design-tree governance).
- **Source:** Designer 2026-07-15.
- **Status:** Accepted (Designer-directed).

## RU-10 — Contract sets the deliverable; decompose freely, aggregate always

- **Rule:** A parent's spawning **contract specifies the child's required deliverable** — e.g. the Role node demands "the **role-action table as an aggregate**." The child may **decompose the work internally to any depth** — sub-nodes by category/type (e.g. **passive-action**, **active-action**, each possibly with its own children) — as it sees fit, but it **must return the contracted aggregate**. Internal shape is the child's discretion; the aggregate is its obligation.
- **Derived from:** modularity (Phase 5 §Item 5); the contract model (RU-04); design advancement & spawning (C-16).
- **Scope:** D2 and D1 design (design-tree governance).
- **Source:** Designer 2026-07-15.
- **Status:** Accepted (Designer-directed).

## RU-11 — The action aggregate drives the capability design (coverage is the contract)

- **Rule:** The **capability design is driven by the action aggregate.** The action node's completed **aggregate `A-` table** is the read-only input (and driver) for the **Capability node**, whose contract is to **design the capabilities (`C-`) that support every action** in the aggregate. **Coverage is the contract:** every action must map to ≥1 capability (autonomous capabilities excepted); the action↔capability map records it and a coverage check verifies "nothing is missed."
- **Derived from:** the **Role → Action → Capability** dependency (Phase 6 governing hierarchy); RU-10 (aggregate at the boundary); the bookkeeping / coverage discipline (functional doc §1 "The bookkeeping").
- **Scope:** D2 and D1 design (design-tree governance).
- **Source:** Designer 2026-07-15.
- **Status:** Accepted (Designer-directed).

## RU-05 — An open upward proposal is a stopping point (no drift)

- **Rule:** Proposing a change to a parent/ancestor is a **stopping point**. The proposing node **must stop — it may not spawn children or advance — until the proposal is resolved** (approved or rejected). A change affecting an ancestor several levels up must be **approved by the owning node and confirmed down the intervening chain** before the proposer may proceed.
- **Rationale:** the design tree can be **long and deep**; halting on a pending upward proposal **prevents drift** — descendants never build on a change that has not yet been approved.
- **Derived from:** RU-04 (upward proposals); the submission/acceptance discipline (RU-02); *Verification Before Realization* — do not build on the unapproved.
- **Scope:** D2 and D1 design (design-tree governance).
- **Source:** Phase 4 §Item 2; Designer 2026-07-15.
- **Status:** Accepted (Designer-directed).

## RU-07 — Communicate only with your immediate parent or child (adjacency)

- **Rule:** Within the design tree a node **communicates only with the node immediately connected to it** — its **parent** or one of its **children**. There is **no direct communication across more than one level**: to reach a node two levels up, a node talks to its parent, which in turn talks to *its* parent (relay, level by level).
- **Rationale:** keeps the connection graph simple and the nodes **modular** — a node's only interface is its parent and its children.
- **Distinct from read-links.** This governs **communication** (proposals, submissions, negotiation). The read-only **input links** a parent hands down in the contract (`RU-08`) let a node *use* ancestor/sibling data without communicating with those nodes directly.
- **Derived from:** modularity (Phase 5 §Item 5); the contract / sandbox model (Phase 4 §Item 2).
- **Scope:** D2 and D1 design (design-tree governance).
- **Source:** Designer 2026-07-15.
- **Status:** Accepted (Designer-directed).

## RU-08 — The contract supplies the child's input links (ancestors + siblings)

- **Rule:** The **contract** a parent gives a child (at, and possibly after, spawning) includes the child's **relevant inputs** — chiefly **links** to material the parent can access: nodes **above the parent** (ancestors) and nodes **spawned by the parent** (the child's **siblings** / their subtrees). The parent **curates** which links are relevant. These are **read-context**, not communication channels (`RU-07`).
- **Derived from:** the contract model (`RU-04`; Phase 4 §Item 2 — "rules above it in the Design Tree are candidates for inclusion in the child contract … a compiled governing contract"); per-work-unit context preparation (`C-08`).
- **Scope:** D2 and D1 design (design-tree governance).
- **Source:** Designer 2026-07-15.
- **Status:** Accepted (Designer-directed).
