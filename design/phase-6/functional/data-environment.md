# D2 Functional Design — The D1 Design Data Environment

*Substance document. Reframes prior Item 3 under the Phase 6 model. It describes the **data functionality D2 provides for the D1 Designer** — not where anything is stored. Directory structure, file formats, storage technology, and ownership mechanisms are architecture, and remain a later design question (Phase 7).*

## Purpose

For the D1 Designer's benefit, D2 provisions — at project setup — the data and working areas a D1 design project needs to be conducted, governed, observed, and preserved. The D1 Designer should begin inside a *prepared* environment and never have to invent storage, working areas, or shared locations while designing.

What must be fixed now is **which data functions exist** and **how they serve the D1 Designer**. The exact structure that realizes them is deferred to Phase 7.

**Why this serves the D1 Designer.** It removes work the Designer should never do (hand-building an environment), keeps the Designer's attention on design rather than data-wrangling (Phase 1 — Designer attention is the scarce resource), and guarantees that the distinctions the Designer relies on — evidence vs. decision, plan vs. design, scratch vs. accepted — are never silently blurred (Phase 1 §4.6).

## Governing tendencies

1. **Established through setup.** The areas come into being through the D2 setup process; the D1 Designer does not construct them by hand. Which areas exist, their initial contents, and applicable templates follow from the chosen setup.
2. **Functional distinctions are preserved regardless of physical arrangement.** Several kinds of data may, in the end, share one store; D2 must still keep them distinct, because they differ in **authority, lifecycle, and visibility to the Designer** — the things the Designer actually experiences.
3. **Central collection is not centralized authority.** Gathering things in one place for the Designer's convenience does not make the Designer (or D2) the authority over each item within it.
4. **Original evidence and D2's own notes stay distinguishable.** The Designer must always be able to tell predecessor fact from D2 interpretation.

## The eight data functions

Each is described by what it holds, why it is a distinct function, and — the point of it all — **how it serves the D1 Designer**.

### 1. Planning data
Holds the current phase, the provisional later phases, advancement decisions, completed phases, plan revisions, and enough history to explain how the plan developed. It is distinct because the *plan* governs the process that produces the design — it is not the design, and sits half a level above it. **For the Designer:** it answers "where are we, what comes next, and why did the plan change?" and lets the Designer steer the process without reconstructing it. Revised under Designer control points; continuously evolving; Designer-visible.

### 2. Project observation data
Holds current activity, completed and pending work, progress, resource / financial / time consumption, **Designer Attention Cost**, unresolved issues, abnormal conditions, and overall health. It is distinct because it describes the project's *condition*, not its content. **For the Designer:** this is the substrate of the Designer's own oversight — it answers "show me the resource consumption so far," "what is blocking progress?", "is anything behaving abnormally?" Without it, Designer-initiated monitoring (Phase 2) has nothing to read. D2-maintained; continuously updated; highly visible.

### 3. Design metadata
Holds Design Tree and Design Node information, design relationships, node status, governing relationships, revision authority, submission/acceptance status, spawning records, and design lineage. It is distinct because it *represents and governs* the developing design — the structural record of the design itself, separate from its content. **For the Designer:** it lets the Designer inspect the design's shape and history ("show me the Design Tree; what changed since my last review?") and underpins the governance the Designer depends on. D2-managed; the detailed model awaits Phase 7; Designer-inspectable.

### 4. Shared project data
Holds rules, standards, D1 design rules, applicable D2 concepts and philosophy, glossary and definitions, communication standards, conventions, representative usage and test examples, and shared evaluation material. It is distinct because it serves the whole project rather than one node. **For the Designer:** it gives one place of shared truth the Designer can set and rely on across the project — with authority distributed so the Designer governs what should be Designer-governed and no more. Central collection, distributed authority; partly Designer-governable.

### 5. Predecessor & reference data
Holds the original V1 package (source, documentation, configuration, tests, usage and historical material), revision proposals, supplementary Designer documents, and the Predecessor Reference Roadmap. It is distinct because it is *evidence, not authority* — read-first source the project refers to but does not author. **For the Designer:** it gives efficient, trustworthy access to the predecessor as evidence, with D2's notes kept separate from the originals so the Designer never mistakes D2's interpretation for the source. Read-only; original vs. derived kept distinguishable; entered efficiently via the Roadmap.

### 6. Project working area
Holds work that is not yet accepted design, is not local to one node, may span nodes, or is exploratory, consolidating, or temporary. It is distinct because it is project-level *scratch*, which must stay separable from accepted design. **For the Designer:** it lets exploratory and cross-node work proceed freely without polluting the accepted design the Designer trusts; intermediate artifacts are never mistaken for decisions. Ephemeral; non-authoritative; settled results are promoted.

### 7. Node-local working areas
Holds a Design Node's local notes, temporary analysis, candidate designs, local test material, evaluation results, and temporary extracts of reference material. It is distinct because modularization (Phase 5) gives each node a *local sandbox*: shared data provides common context, the node area provides local freedom. **For the Designer:** bounded local work is what lets each node proceed autonomously and lets D2 carry the design's internal complexity — so the Designer spends attention on high-leverage decisions, not node mechanics. Node-scoped; local autonomy under the node's contract; the sandbox model awaits Phase 7.

### 8. Shared Designer-relevant artifacts
Holds D0 prototypes, representative D0 package structures, sample health reports, monitoring examples, interface mockups, algorithm demonstrations, and comparison results. It is distinct because these are *promoted* byproducts, useful beyond the node that made them and especially relevant to Designer inspection. **For the Designer:** it surfaces exactly the things the Designer most wants to see and judge, rather than leaving them buried inside one node. Promoted from node-local work; highly visible to the Designer.

## How the functions relate

- **Plan, design, and condition stay separate** (functions 1, 3, 2). This is what lets the Designer ask a *process* question and a *design* question independently and get clean answers to each.
- **Shared vs. local** (4 vs. 7) is the modularization boundary: common context without smothering local freedom, local freedom without fragmenting the project.
- **Evidence vs. authored** (5 vs. 3/4) keeps provenance intact: the Designer never confuses predecessor fact with a design decision.
- **Ephemeral vs. accepted** (6/7 vs. 3/4) keeps trust intact: the Designer never confuses scratch with accepted design.

## What the D1 Designer gains

A prepared, navigable, trustworthy environment in which every kind of information has a clear place and clear standing — so the Designer can direct, observe, and inspect the project, ask process and design questions separately, rely on evidence and decisions never being blurred, and spend scarce attention on design rather than on managing data.

## Deferred to Phase 7 (architecture)

Directory structure, file formats, storage technology, ownership/authority mechanisms, the detailed Design-Node sandbox model, and the promotion mechanism (function 7 → 8).

---

*Registry: capability `C-19` currently collapses this document into one line; it will be re-indexed into the environment plus its eight data functions once the substance approach is confirmed.*
