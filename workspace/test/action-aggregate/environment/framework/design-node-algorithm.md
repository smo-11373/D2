# The design-node algorithm — contract generation & fulfilment (first cut)

*Provisional. Every node does two things: **emit its children's contracts** (downward) and **fulfil
its own contract** (upward, producing its deliverable). This works out both, on the case
Fundamentals → Action-Aggregate (a.k.a. the action integration node). A node is an **agent**
(glossary `design-node`); "automated" means **agent-executed**, and the acceptance test is what makes
it **terminate and reproduce**.*

*Naming (snapshot): this describes the **module's method** — module = design tree + design node
module; the run output `algorithm.md` is a *product* of running the module, not this file. **Pinned
pre-conformance snapshot** — it omits the module's later conformance acceptance requirement (source
module `conformance.md`); this benchmark measures the pre-conformance module.*

## Q1 — How the Fundamentals node delivers the contract (downward)

A parent does **not invent** a child's contract; it **instantiates** one from its own owned data.

The Fundamentals node owns three things: the **constitution** (Phases 1–5), the **method**
(functional doc §1), and the **rules** (`RU-*`). Two of them already contain everything the contract
needs:

- **The method is the plan.** §1 establishes the governing layering **Role → Action → Capability →
  Architecture** and the derivation discipline (identify the Designer's actions → abstract the common
  element → open-list). Reading its own method, Fundamentals knows the **next deliverable is the
  action layer** — a role-action aggregate table derived from the constitution.
- **The rules give the contract's form.** `RU-10` (deliver an *aggregate*), `RU-11` (coverage), `RU-08`
  (pass owned data down read-only), `RU-02` (justify at submission).

So the design-node algorithm at Fundamentals is: **read own plan (method) → identify the next
deliverable → fill the standard contract template → attach own data as read-only inputs → hand
down.** The result is exactly the action-aggregate contract (`../../input/contract.md`):

> deliverable = the role-action aggregate table · inputs = constitution + method + rules ·
> acceptance = coverage + traceability · (decomposition left to the child, `RU-10`)

**The point:** the contract is *derived*, not authored freehand — Fundamentals turns the method's
discipline into a pinned instruction. Any run over the same method+rules emits the same contract.

## Q2 — How the Action-Aggregate node fulfils it (upward)

The node receives the contract (deliverable + inputs + acceptance) and runs the algorithm's standard
decomposition, **deriving all substance from the frozen inputs** — nothing invented, everything
traced:

1. **Seek roles.** Spawn a **Roles** agent, sub-contract: *derive the positions from **Phase 5
   Item 3** + the layer model (D2→D1→D0)*. The agent **reads Phase 5**, extracts the positions
   (D1 Designer, D0 Operator, …), tags intrinsic/default, cites the Source. → the role table.
2. **Actions per role.** For each role, spawn an **action** agent, sub-contract: *derive this role's
   actions from its **job function** and the relevant phase items*. The agent **reads the
   constitution/method for that role** and extracts **what the role does** — for the D1 Designer, it
   walks the method's journey (entry → setup → input → … → checking) and lifts each action; for a
   downstream role, it lifts the actions implied by that position's job function. It names, assigns a
   stable ID, cites the Source; the D1 Designer's set sub-splits **passive / active**.
3. **Aggregate.** Merge the per-role pieces into the table.
4. **Self-check against acceptance.** Run **coverage** (every action a competent re-derivation would
   surface is present), **traceability** (every row Source-cited), **integrity** (IDs, dedup, map
   resolves). Gaps → derive more. This is the **termination condition**.
5. **Submit** with justification (`RU-02`) for Fundamentals' approval.

**Where the "substance" comes from:** each agent *reads the frozen constitution and extracts /
abstracts* the roles and actions. The substance is the extracted text + its `Source` (the derivation
trace). It is reproducible because the source is frozen and the stop condition is coverage against
that source.

## The self-similar insight

The **method (§1)** does double duty: it is the recipe D2 uses to design **D1**, *and* it is the
design-node algorithm's derivation procedure for designing **D2 itself**. A node's two jobs are the
same procedure pointed two ways — **emit contract** = instantiate the method for the child's layer;
**fulfil contract** = run the method's derivation over the frozen inputs until coverage is met.

## What is automatable, honestly

The extraction/abstraction is **LLM-agent reasoning**, not deterministic code — appropriate, since a
design node *is* an agent. "Automated" therefore means: agents execute contracts, derive from frozen
sources, and self-check against a coverage/traceability acceptance test. "**Substantially** the same"
follows: frozen inputs + fixed method + coverage pin convergence; naming, granularity, and the
open-list tail are the residual variation.
