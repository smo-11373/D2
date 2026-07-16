# Capability Catalog

*Living. Capabilities across the stack, **tagged by layer**. One record per capability; heading shows `Layer · Serves (role)`. See `README.md` for ID conventions. The Action↔Capability join lives in `action-capability-map.md`.*

> **Layers.** **D2** = capabilities of the D2 product (serve the D1 Designer R-01 and D2-internal work R-02). **D1-product** = the thin D1 wrapper (serve the D1 Technical Manager R-04, produced via R-03). **D0-product** = the deployed product (serve the D0 Operator R-05 and D0 Technical Manager R-06).
>
> **Provenance.** C-01–C-19 were derived from the prior Phase 6 items; C-20–C-23 fill the D2 gaps the audit found (implied by Phases 2–4); C-24–C-33 are the D1/D0-product capabilities implied by the downstream roles' actions (Phase 5 Human Position First); C-34–C-36 abstract the active-monitoring subjects (progress, spend, health) implied by the Phase 4 Item 3 query set; C-37 abstracts pre-adoption orientation, C-38 the default roles table, C-39 the D1 foundational documents, C-40 the D1 rules and standards, and C-41 change evaluation (Phase 6 entry-point / setup / direction / design-tree passes). Some D2 capabilities are **autonomous** — D2 performs them to *serve* a role, with no 1:1 role action (audit finding F2).

---

## D2 capabilities

### C-01 — Provide default design choices · *D2 · Serves R-01*
Offer a Template Library + a few high-level postures (Standard / High Harness / Lean); one choice resolves into many settings. Each posture is **expandable to the settings it resolves, with each setting's definition and consequence viewable** — the inspectability floor, guaranteed regardless of how much change is allowed (cf. **C-03**). **Source:** Phase 6 Item 1 §1–2.

### C-02 — Produce the Selected Setup Configuration Package · *D2 · Serves R-01*
A centralized, versioned, traceable, reviewable record of the run's setup — the source of truth, distinct from the Library. **Source:** Phase 6 Item 1 §3.

### C-03 — Setup review with progressive disclosure · *D2 · Serves R-01*
Let the Designer inspect, summarize, compare, explain, or revise the setup before activation. **Source:** Phase 6 Item 1 §4.

### C-04 — Establish effective configuration across contexts · *D2 · Serves R-01 (autonomous)*
Materialize the confirmed setup into the appropriate contexts without losing traceability. **Source:** Phase 6 Item 1 §5.

### C-05 — Authority-aware setup governance & later revision · *D2 · Serves R-01*
Preserve distinct authorities (authority follows meaning); support governed later revision with impact analysis and history. **Source:** Phase 6 Item 1 §6–8. *Boundary:* governs **setup-item** authority & setup revision; cf. **C-17** for **design-result** revision authority.

### C-06 — Provisional D1 design plan & operating framework · *D2 · Serves R-01*
Maintain a plan (current defined, later provisional) and the D1 Design Operating Framework; advance as higher-level design settles. **Source:** Phase 6 Item 2 §1; Phase 4 Item 1.

### C-07 — Predecessor study & Reference Roadmap · *D2 · Serves R-02 (autonomous)*
Study the predecessor once broadly; preserve a revisable roadmap linking design subjects to reference locations. **Source:** Phase 6 Item 2 §2.

### C-08 — Per-work-unit context preparation · *D2 · Serves R-02 (autonomous)*
Assemble the bounded context before a work unit begins — "prepare the boundary before the work." The context/contract includes **input links** to material the parent can access — ancestors and the child's siblings (**RU-08**). **Source:** Phase 6 Item 2 §3.

### C-09 — Targeted predecessor investigation before design · *D2 · Serves R-02*
Investigate relevant predecessor material to the depth warranted by importance/posture/uncertainty. **Source:** Phase 6 Item 2 §4.

### C-10 — Bounded design construction · *D2 · Serves R-02*
Carry a bounded design responsibility from prepared input to an evaluated design result. **Source:** Phase 6 Item 2 §5.

### C-11 — Design-result evaluation · *D2 · Serves R-02*
Evaluate before submission (conformance, comparison, tests, semantic review), at local vs integration scopes, scaled by posture/importance. **Source:** Phase 6 Item 2 §6, §8, §9.

### C-12 — Submission & acceptance governance · *D2 · Serves R-02*
Treat submission and acceptance as distinct; the submission package carries the authoring (child) node's **justification**, which the **parent node reviews and approves / rejects** (**RU-02**); support outcomes (accept / return / conditional / escalate). **Source:** Phase 6 Item 2 §7.

### C-13 — Designer-oriented result reporting · *D2 · Serves R-01*
Concise Designer-oriented reports after major accepted work, with deeper material on demand. **Source:** Phase 6 Item 2 §10.

### C-14 — Passive Designer intervention (consolidated clarifications) · *D2 · Serves R-01*
Investigate first, then batch high-leverage questions into a consolidated Clarification Request (distinct from a Review Stop). **Principle: minimal Designer attention** — multiple rounds are permitted but *not encouraged*, and each round is normally separated by deep D2 investigation, so the Designer is approached only when investigation genuinely cannot settle the point. **Source:** Phase 6 Item 2 §11; Phase 3 Item 3 & Phase 4 Item 2 (multiple rounds permitted when genuinely necessary). *Boundary:* **D2-initiated** (D2 asks the Designer); cf. **C-20** (Designer-initiated).

### C-15 — Review-stop provisioning · *D2 · Serves R-01*
Offer a review opportunity at appropriate points before continuation; tendency scales with level/posture. **Source:** Phase 6 Item 2 §12.

### C-16 — Design advancement & spawning · *D2 · Serves R-02*
Determine the next design work (advance / spawn / integrate / revisit); keep advancement and spawning distinct. **Spawning is driven by the Designer's actions (RU-03):** a *static* passive-action list (from the approved setup/fundamentals) spawns children first; active-action spawning is deferred. **Source:** Phase 6 Item 2 §13–14.

### C-17 — Revision-authority governance · *D2 · Serves R-01, R-02*
Carry a revision-authority status per result (D2-managed / Designer-governed); route revision proposals; prevent silent revision. An **open upward proposal is a stopping point** — the proposer halts until it is resolved (**RU-05**); the contract-down / propose-up discipline is **RU-04**. **Source:** Phase 6 Item 2 §15.

### C-18 — Design lineage & traceability · *D2 · Serves R-01 (autonomous)*
Preserve enough history to explain what is effective, where it came from, what governs it, and why it changed. **Source:** Phase 6 Item 2 §16.

### C-19 — Provision the D1 design data & working areas · *D2 · Serves all (autonomous)*
Establish, at setup, the eight functional data classes; preserve their distinctions. Observation-data class underpins Designer monitoring. **Source:** Phase 6 Item 3.

### C-20 — Unified Designer inspection & intervention · *D2 · Serves R-01*
Answer natural-language Designer queries about design/process state and route inspection, investigation, and directives through one interaction point. **Source:** Phase 2 P3; Phase 4 Item 3. *(Audit F3 gap-fill.)* *Boundary:* **Designer-initiated**; cf. **C-14** (D2-initiated).

### C-21 — D2 process self-audit · *D2 · Serves R-01*
After completion, evaluate process cost, time, and Designer Attention Cost; propose D2 improvements (governed, not silent). **Source:** Phase 3 Item 5. *(Audit F3 gap-fill.)*

### C-22 — Tunable resolution depth & intervention posture · *D2 · Serves R-01*
A Designer-controlled balance among investigation, inference, intervention, and deferral. **Source:** Phase 2 §2.6; Phase 6 Item 1 §2. *(Audit F3 gap-fill.)* *Boundary:* the fine tuning knob a design posture (C-01) presets.

### C-23 — Design-input intake & operating contract · *D2 · Serves R-01*
Establish the initial design input (Predecessor D1 package + intended change) and the Designer–D2 Operating Contract; help form a sufficient upgrade direction. **Source:** Phase 3 Item 1–2. *(Audit F3 gap-fill.)* *Boundary:* establishes the operating contract, which the setup package (**C-02**) then carries.

### C-34 — Design-progress monitoring · *D2 · Serves R-01*
Present how far the design has advanced — completed vs pending work, changes since the Designer's last review, per-node revision counts — on demand or as a standing view. **Source:** Phase 4 Item 3 (active-interaction pass); rests on observation data (**C-19**). *Boundary:* progress/advancement; cf. **C-35** (spend), **C-36** (health).

### C-35 — Resource & cost monitoring · *D2 · Serves R-01*
Present the time and cost the D1 design process has consumed — cumulative and per node. **Source:** Phase 4 Item 3 (active-interaction pass); rests on observation data (**C-19**). *Boundary:* resource/spend; cf. **C-34** (progress).

### C-36 — Design-process health & anomaly monitoring · *D2 · Serves R-01*
Surface abnormal process behavior, rejection loops, high-impact unresolved issues, and a consolidated design-health report. **Source:** Phase 4 Item 3 (active-interaction pass); rests on observation data (**C-19**). *Boundary:* health/risk signalling; a Designer concern escalates to investigation via **C-20** (A-008).

### C-38 — Provide the default roles table · *D2 · Serves R-01*
Seed the ecosystem's roles for the run, each marked **intrinsic** (fixed: the Designer, the D2 Assistant, the internal agents) or a **Designer-changeable default** (the product-side / downstream roles), and let the Designer accept or tailor the default set. The role set frames what the design will do (Human Position First). **Source:** Phase 5 Item 3; Phase 6 (setup pass). *Boundary:* the role set as a setup item, carried in the setup package (**C-02**); cf. **C-01** (posture / design-choice defaults).

### C-37 — Adoption orientation (orientation summary) · *D2 · Serves R-01*
Before adoption, provide an **orientation summary** — a short top-level document that, *in summary not detail*, presents what D2 is, the layer model (D2 → D1 → D0) and where the Designer's authority sits, **who is responsible for what** (the roles and their boundaries), what using D2 will ask of him, and what he gets out — a compact honest basis for the adopt / decline / defer decision. Progressive disclosure; a summary to act on, not a manual. **Key elements identified; full document content deferred to D2's later design (open list).** **Source:** Phase 1 (Designer authority & attention); Phase 2 (progressive disclosure). *(Phase 6 entry-point pass.)* *Boundary:* pre-adoption orientation; cf. **C-23** (post-adoption design-input intake).

### C-39 — Establish the D1 foundational documents (D1 Constitution) · *D2 · Serves R-01*
Combine the setup skeleton, the predecessor V1, and the intended change into the D1 project's foundational set — a D1-level analogue of Phases 1–5, **seeded from a default template modeled on D2's own foundational documents** and then revised/extended by the Designer, centered on a **D1 Constitution** (scope, principles, invariants, initial direction) — surfacing understanding, what to preserve / change / add, and residual uncertainties, for a strongly-encouraged confirmation (A-057). **Source:** Phase 3 Item 3; Phase 4 Item 1 (first node establishes the D1 Constitution). *(Phase 6 direction pass.)* *Boundary:* the initial foundational set; ongoing design builds beneath it, and the Constitution's revision authority is Designer-governed (**C-17**).

### C-41 — Change evaluation (impact dry-run) · *D2 · Serves R-01, R-02*
Dry-run a proposed change **without committing it**: probe **upward** for ancestor effects (would the change land correctly on the parent?) and **downward** for contract/child effects (how is the child's contract altered?), and return an **evaluation report** on which the initiator formalizes or revises. **Separate from the official proposal** (RU-06); the proposal itself propagates up / down and firms up (RU-04, RU-05). Change may be **agent-initiated** (a node) or **Designer-initiated** (R-00 while building D2; R-01 in the product). **Source:** Designer 2026-07-15; cf. **C-05** (impact analysis), **C-11** (result evaluation). *(Phase 6 design-tree pass.)*

### C-40 — Establish and govern the D1 rules and standards · *D2 · Serves R-01, R-02*
Create the D1 project's **rules and standards** as an active, versioned governing document within the foundational set, **seeded by merging the predecessor's existing rules with the default rules of the D2-provided template** — **most established up front (§4), since the design work cannot proceed without them** — and support governed updates and additions later (the operating framework, §5, may refine them; Designer rules require Designer permission; a central versioned registry). **Source:** Phase 4 Item 1 (inherited / derived rules), Phase 4 Item 2 (rule & sandbox model, versioned registry); `rules.md` (RU-). *Boundary:* the D1 rules & standards artifact — created in §4, refinable in §5; individual rules are catalogued as `RU-` in `rules.md`.

---

## D1-product capabilities

### C-24 — Governed product parameters · *D1-product · Serves R-04*
Expose adjustable values as explicitly governed parameters so they can be tuned without code changes. Constrained by **RU-01**. **Source:** Phase 5 §Item 3; `rules.md`.

### C-25 — Upgrade, release & rollback management · *D1-product · Serves R-04*
Upgrade smoke-test suite, repackage/distribute, upgrade records, and rollback on failure. **Source:** Phase 5 §Item 3; D1 wrapper (Designer 2026-07-12).

### C-26 — D0 deployment & health monitoring · *D1-product · Serves R-04*
Deploy D0 (optionally retaining D1) and monitor D0 health/performance (~half a level above D0). **Source:** Designer 2026-07-12; glossary `d1`, `half-level`.

### C-27 — Implementation from specification · *D1-product · Serves R-03*
Produce the D0 code from the implementation specification, with implementation-level tests and defect fixes. **Source:** Phase 5 §Item 3.

---

## D0-product capabilities

*D0 exists first for the D0 Operator (primary-user principle). Specific features are set per project by the D1 Designer; these are the generic capability categories any D0 should provide.*

### C-28 — Routine D0 operation · *D0-product · Serves R-05*
Start, run, stop, schedule, pause/resume, or cancel D0 jobs. **Source:** Phase 5 §Item 3.

### C-29 — Operator-level configuration · *D0-product · Serves R-05*
Operator controls within approved limits (spending limits, scheduling, collection scope, approved operating choices). **Source:** Phase 5 §Item 3.

### C-30 — D0 status, monitoring & results · *D0-product · Serves R-05*
User-level health monitoring, plus viewing results/outputs/reports and activity/usage/cost-to-date. **Source:** Phase 5 §Item 3; Phase 6 Item 3.

### C-31 — Operator notifications & routine error handling · *D0-product · Serves R-05*
Surface notifications/prompts/approvals for a low-technical operator; support routine retry/restart. **Source:** Phase 5 §Item 3 (position-derived).

### C-32 — D0 deployment install & technical maintenance · *D0-product · Serves R-06*
Install and technically maintain a deployment (paths, endpoints, service config, resource limits, credentials, health); diagnose and apply fixes/patches within the established design. **Source:** Phase 5 §Item 3.

### C-33 — Technical support & escalation · *D0-product · Serves R-05, R-06*
Front-line technical support for the operator, with an escalation chain (Operator → D0 Technical Manager → D1 Technical Manager). **Source:** Phase 5 §Item 3 (position-derived).
