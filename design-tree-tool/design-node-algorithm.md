# The design-node algorithm — contract generation & fulfilment (first cut)

*Provisional. Every node does two things: **emit its children's contracts** (downward) and **fulfil
its own contract** (upward, producing its deliverable). This works out both, on the case
Fundamentals → Action-Aggregate (a.k.a. the action integration node). A node is an **agent**
(glossary `design-node`); "automated" means **agent-executed**, and the acceptance test is what makes
it **terminate and reproduce**.*

*Naming: this describes the **module's method** — one component of the **module** (design tree +
design node module), alongside the enforcer, acceptance, and submission. It is **not** the run output
`algorithm.md`, which is a *product* of running the module. See `conformance.md` for the module's
conformance acceptance requirement.*

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
down.** The result is exactly `action-aggregate/contract.md`:

> deliverable = the role-action aggregate table · inputs = constitution + method + rules ·
> acceptance = **conformance** (gating) + **completeness** + traceability · (decomposition left to the child, `RU-10`)

The contract carries **conformance to the governing layer** as its first, gating acceptance criterion
(see `conformance.md`) — the child must contradict no governing statement of the inherited fundamentals,
not merely cite them. This is layer-relative: the same clause emitted by the D1 module reads "conform to
the D1 constitution."

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
   downstream **operational** role it walks the **position-derived depth frame** (below). It names,
   assigns a stable ID, cites the Source; the D1 Designer's set sub-splits **passive / active**.

   **Position-derived depth frame** — a *derivation-depth harness* (not a closed list). Downstream
   operational positions (Programmer, D1/D0 Technical Managers, D0 Operator) have no journey scaffold,
   so two runs otherwise stop at different depths. For each such position, elaborate the actions its
   Phase-5 Item-3 job function *genuinely implies* across the recurring facets — **operate/perform ·
   monitor/observe · configure/control · view/report · handle routine errors · escalate/request
   support** (maintenance/support positions also walk the **diagnose → apply-fix → recover-from-a-failed
   -change → record-the-change** cycle their function implies). The facets are **abstracted from Phase 5
   Item 3's own position language** (routine operation & monitoring; position-oriented configuration;
   escalation; position hierarchy) — *not* manufactured. **Guards:** *(open list, method §1)* the frame
   is a **completeness prompt, not a checklist** — elaborate only the facets a position genuinely
   implies, never invent an action to fill one, and conformance/traceability still gate every row;
   *(scope)* the operational cast only — **not** the D1 Designer (scaffolded above) nor the internal/meta
   roles (D2 Designer, Design Node Builder, D2 Assistant); *(layer-relative)* general to operational
   positions at any layer, so the D1 module reuses it unchanged.

   **Harness-richness bias** (Harness First, pointed at the product) — beyond each position's core
   function, **hunt the harness facets**: what does this position **test**, **monitor**, **detect**
   (hidden errors / failures), and **make visible**? Preferentially surface these; a D1/D0 design thin
   on testing, monitoring, health-visibility, or failure-handling is a **Harness-First deficiency to
   investigate**, not an acceptable minimum. Applies to **every** role (the Builder's verification
   harness, the Designer's process monitoring, the operational cast's health/error handling) — not only
   the operational cast — and **propagates to the capability / architecture successors**, where the
   actual test suites, monitors, and health checks are designed. *Grounding:* Phase 5 Item 1 (Harness
   First; monitoring before usage — health status, monitoring behavior, failure visibility), Phase 2
   (Verification Before Realization), glossary `d1` (wrapper health-monitoring, upgrade smoke-tests).
   *Guard (Quality over Expediency):* bias ≠ padding — do **not** manufacture a harness the fundamentals
   don't warrant, **nor split one responsibility into mechanical steps**; conformance, completeness, and
   the distinctness guard still gate every row.
3. **Aggregate.** Merge the per-role pieces into the table.
4. **Self-check against acceptance.** Run **conformance first and gating** (the deliverable
   contradicts no governing statement of the inherited fundamentals — a named enumeration, principle,
   method discipline, or rule; distinct from traceability, which only checks a `Source` is cited — see
   `conformance.md`), then **completeness** — the omission-counterpart to conformance: *actively derive
   the should-exist set from the fundamentals and check each is present.* **Gating** for pieces the
   fundamentals **name or explicitly list** (named enumerations, position-oriented control lists, the
   passive/active journey, the depth-frame facets); a **strong bias** for pieces a competent derivation
   implies; open-list only at the genuine tail (method §1). **Distinctness guard (Quality over Expediency,
   Phase 5 §Item 4/5):** each row must be a *distinct responsibility the role performs* — **not** a
   mechanical step or a restatement of a governing rule the node merely operates under. **Merge only**
   mechanical steps and rule-restatements; **preserve any distinction the fundamentals themselves make** —
   where the fundamentals give two concerns distinct treatment (distinct data, concern, or Source; e.g.
   monitoring *cost* vs *health*, Phase 4 §Item 3), they are **distinct responsibilities**, not one to be
   merged on a shared verb. De-duplicate by responsibility **at the fundamentals' own granularity**;
   completeness is *distinct responsibilities covered*, not row count. Then **traceability** (every row
   Source-cited) and **integrity** (IDs, dedup, map resolves). On a conformance conflict, **revise to
   conform** or **propose up and halt** (`RU-04`/`RU-05`); on a completeness gap, **derive the missing
   piece** (a named/specified omission is a gate failure) — never emit-and-flag. This is the
   **termination condition**.
5. **Submit** with justification (`RU-02`) — including an explicit **conformance argument** — for
   Fundamentals' approval, which independently runs the conformance gate before accepting.

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
