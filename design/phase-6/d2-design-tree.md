# The D2 Design Tree — first cut

*Provisional. D2's own design, laid out on the **design-tree framework it prescribes** (dogfooding).
See `working-notes.md` for the spawning mechanism (`RU-03`) and node definition (glossary
`design-node`); `../decisions/` for open questions.*

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

- **Ownership.** Each table-node owns its table: the **Role node** owns the role table (`R-`); the
  **Role-Action node** owns the role-action table (`A-`).
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

1. **Table nodes own their tables — resolved.** Each table-node owns its table (Roles → `R-`,
   Role-Action → `A-`); parents pass owned data down as a contract, children propose changes up
   (`RU-04`, `RU-05`). Functional nodes (Decision, Setup) therefore **reference** their `A-`/`C-`
   rows read-only rather than owning them. *(Confirm this reference model for the functional nodes.)*
2. **"Functionality" node** may be **omitted / folded** into Role-Action or Architecture.
3. **Roles under Setup?** The role table was part of setup in functional-doc §3; here Roles is a
   *child* of Setup. Confirm.
4. **Shared capabilities** (`C-13/C-14/C-15/C-20…`) sit in the Functionality layer; ownership
   within it still TBD.
