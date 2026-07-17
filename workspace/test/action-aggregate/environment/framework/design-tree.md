# The D2 Design Tree — first cut

*Provisional. D2's own design, laid out on the **design-tree framework it prescribes** (dogfooding).
Self-contained copy for this sandbox: the framework's formal rules `RU-01…RU-11` are in
`../rules.md`, the **design-node algorithm** is the sibling `design-node-algorithm.md`, and the terms
are in `../glossary.md`.*

## Principle — edges are design dependency, not action order

The tree records **design dependency**: an edge `A → B` means **B's design depends on A's**. It is
**not** the Designer's action order. Two steps adjacent in the Designer's journey can be
*independent* in design (e.g. *deciding to use D2* and *setup*), and a chain that reads as one
topic can be a real dependency (Roles → Role-Action → …). This supersedes the earlier
journey-cluster grouping: the **functional document's sections are a reading order; the design tree
is dependency-shaped.**

## The tree (first cut)

```
Fundamentals
├── Decision to use D2                     (independent of Setup)
└── Setup
    └── Roles  (role table)
        └── Role-Action  (role-action table)          depends on Roles
            └── Functionality  (capabilities)          depends on Role-Action   (optional)
                └── Architecture                        depends on Functionality (Phase 7)
```

The spine **Roles → Role-Action → Functionality → Architecture** mirrors the Phase 6 governing
hierarchy: *Role → Action → Capability → Architecture → Implementation.*

## Nodes and their own data (first cut)

| Node | Own data (owns & enforces) | Depends on |
|---|---|---|
| **Fundamentals** | D2 constitution (Phases 1–5) + Phase 6 method (§1) + rules `RU-01…03` | — (root) |
| **Decision to use D2** | `A-055`; `C-37` (orientation summary) | Fundamentals |
| **Setup** | posture + setup package: `A-015/A-016/A-017/A-019`; `C-01/C-02/C-03/C-05/C-22` | Fundamentals |
| **Roles** | the roles table `R-*`; `A-056`; `C-38` | Setup |
| **Role-Action** | the role-action table — the actions `A-*` each role performs | Roles |
| **Functionality** | the capabilities `C-*` + the Action↔Capability map | Role-Action |
| **Architecture** | Phase 7 architecture | Functionality |

## Node governance — contracts, proposals, stopping points

Worked out on the simplest case (Role node vs Action node):

- **Ownership = authorship.** Each table is **authored by exactly one node**, and the author owns it:
  the **Role node** authors the role table (`R-`); the **Action node** authors the role-action table
  (`A-`). A parent may **read** the child's whole package but is **not** the author. *(RU-09.)*
- **Contract down.** A parent specifies a **contract** for its child that **includes the parent's
  owned data**. The Role node's contract to the Role-Action node carries the **role table**; the
  Role-Action node works within it. *(RU-04.)*
- **Propose up.** To change inherited data, the child **proposes the change to the owning ancestor**,
  which accepts or rejects. The Role-Action node cannot rewrite the role table — it proposes; the
  Role node decides. *(RU-04.)*
- **Stop on a pending proposal.** An open upward proposal is a **stopping point**: the proposer may
  not spawn or advance until it is resolved. This prevents **drift** in a long, deep tree. *(RU-05.)*
- **Adjacency-only communication.** A node communicates only with its **immediate parent or child**;
  to reach two levels up it relays through its parent. Keeps connections simple and nodes modular.
  *(RU-07.)*
- **Contract input links.** The parent's contract to a child carries **read-only links** to material
  the parent can access — its **ancestors** and the child's **siblings** — curated by the parent.
  Links are read-context, not communication channels. *(RU-08, C-08.)*
- **Change through the author.** A table is changed **only through its author**: a node **proposes up**
  to change an *ancestor-authored* table (`RU-04`); a parent **requests down** to change a
  *child-authored* table — the author makes the change and re-submits. No node edits a table it does
  not author. *(RU-09.)*
- **Contract sets the deliverable; decompose freely, aggregate always.** The parent's contract states
  the child's **required deliverable** — e.g. the Role node demands "the role-action table **as an
  aggregate**." The child may **decompose internally to any depth** (sub-nodes by type —
  *passive-action*, *active-action*, …) but must return the aggregate. *(RU-10.)*

**Action-node decomposition (illustration).** Within the Action node:

```
Role-Action  (authors the aggregate A- table)
├── passive-action node   →  entry · setup · foundational-docs · operating-framework · …
└── active-action node    →  inspecting/monitoring · checking · …   (may have its own children)
```

The Action node may dissect the actions by category and **merge** them; the contract only requires
the **aggregate** `A-` table at the Action node's boundary. This resolves the earlier inversion —
the aggregating node **authors** its own table, and the Role node reaches it by read + request.

- **The aggregate drives the next layer (`RU-11`).** A completed aggregate **drives its dependency
  successor**: the **action aggregate drives the capability design**, whose contract is to **cover
  every action** (coverage is the contract). Distinguish a node's **internal-decomposition** children
  (which *produce* its aggregate — e.g. passive/active-action) from its **dependency** children
  (which *consume* it — e.g. the Capability node). *(Two edge kinds under one parent — flagged.)*

**Worked example (A → B → C).**

- **B** proposes a change to **A** → B stops; A accepts or rejects.
- **C** proposes a change that affects **both B and A** → C stops; the change is approved by **A**
  (the owner) and confirmed **down through B**; only then may C proceed — e.g. spawn **D**.

### Change process — evaluate, then propose

**Initiation — two sources.**

- **Agent-initiated** — a node (e.g. B) proposes a change while building under its contract, *or* in
  response to a child's (C's) proposal. B decides, then submits the proposal upward.
- **Designer-initiated** — the **D2 Designer** (later the D1 Designer) proposes a change to a node,
  usually after a round or more of **discussion**.

**Evaluate before proposing** — a *separate command* that **commits nothing** (`RU-06`, `C-41`).
Once a change is roughly formulated, evaluate it as a **dry-run**:

- **Probe up** (to A): would the change land correctly on the ancestor?
- **Probe down** (to C): how would C's contract change, and what is the effect on C?
- Returns an **evaluation report**. On it, the initiator **formalizes** the change or **revises** it.

**Official proposal** — on a decision to proceed (`RU-04`, `RU-05`): the change **propagates
upward**; if accepted, **propagates downward**; then it is **firmed up**. Upward proposals are
stopping points (`RU-05`). Keeping evaluation separate lets the initiator learn the impact *before*
committing to the stopping-point proposal.

## To resolve next (the "own data" question)

1. **Authorship = ownership — resolved (`RU-09`, `RU-10`).** The **author owns its table**: the Action
   node authors the `A-` table; the Role node reads it but is not the author. Changes route through
   the author (propose-up / request-down). This removes the earlier inversion — the aggregating node
   is no longer a "referenced leaf."
2. **Functional areas dissolve into the Action node — resolved (`RU-10`).** Decision / Setup /
   foundational-docs / operating-framework are **not** separate top-level nodes; they are the Action
   node's **internal decomposition** (under passive-action / active-action sub-nodes), merged into the
   aggregate `A-` table the contract demands. *(Fundamentals as a 5-phase node is the harder case,
   deferred — see below.)*
3. **"Functionality" node** may be **omitted / folded** into Role-Action or Architecture.
4. **Roles under Setup?** The role table was part of setup in functional-doc §3; here Roles is a
   *child* of Setup. Confirm.
5. **Shared capabilities** (`C-13/C-14/C-15/C-20…`) sit in the Functionality layer; ownership
   within it still TBD.
6. **Fundamentals as a multi-node (the harder case).** The Fundamentals node holds five phases —
   a significant piece of work — and likely decomposes into its own subtree, on the same rules. Deferred.
