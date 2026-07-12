# Phase 6 — Role–Action and Capability Model

*The substantive Phase 6 design document. The catalogs in `../catalogs/` (role-action, capabilities, action-capability-map, designer-queries, rules) are the **bookkeeping registries** for this model — stable IDs, foreign keys, status — for traceability. This document holds the **substance**: the model, its reasoning, and its design decisions.*

## Purpose and framing

Phase 6 answers **what D2 must be capable of**, before Phase 7 asks how it is built. It replaces the prior "list of functionality" formulation (preserved verbatim in `prior-items/`) with a model governed by a deliberately top-down chain:

> Role / Position → Action → Capability → Architecture → Implementation

**Positions** define responsibilities (Human Position First); **actions** are what each position does; **capabilities** are what D2 — and the products it helps build — must provide so those actions are possible. Architecture and implementation come later.

## 1. The layered role model

D2, D1, and D0 form a stack in which each layer's product is built by the layer above and serves the layer below:

- The **D2 Designer** builds **D2** (this is us, now).
- The **D1 Designer** is D2's **primary and only user**; using D2, they build a **D1 product**.
- The **D1 product wraps a D0 product** — D0 is the core distributable; D1 is a *thin operational wrapper* (health/crash monitoring, upgrade smoke-tests, upgrade records) sitting "half a level above D0."
- The **D0 product** is run by the **D0 Operator** (normally low technical understanding), with **D0 Technical Manager** support; the **D1 Technical Manager** administers the wrapper.

Two principles shape the model:

**Human Position First.** Positions — conceptual responsibility boundaries — are defined before agents are assigned. A position is defined by what it receives, what it is responsible for, what authority it holds, and what it must produce. Agents (human or automated) occupy positions later.

**The primary-user principle (self-similar).** Each layer's product exists first for its primary user. D2 exists for the D1 Designer (Phase 1). By the same logic, **D1/D0 exists first for the D0 Operator** — the D1 Designer builds for the operator's convenience above all. This is why the D0 Operator's job functions are covered most thoroughly.

A terminological trap resolved here: unqualified **"Designer"** in the frozen baseline means the **D1 Designer** (D2's user), *not* the D2 Designer (the builder) — pinned in the glossary. Roles are enumerated in `role-action.md` (R-00–R-06).

## 2. Actions by role

Actions are the bridge from role to capability — what each position does.

- **The D1 Designer** (D2's user) interacts with D2 across the design run: establishing the setup and operating relationship, providing the predecessor and the intended change, directing and reviewing the emerging design, inspecting and intervening through a *single* interaction point, and auditing the process afterward. Their attention is the scarce resource D2 exists to conserve.
- **Internal D2 positions** — the **Design Node Builder** and **D1 Programmer** — carry bounded design and implementation work under the D1 Designer's direction; in an automated D2 these are occupied by agents.
- **Product-operation positions** operate what the D1 Designer builds: the **D1 Technical Manager** administers the wrapper (parameters, upgrades, deployment, monitoring); the **D0 Operator** runs D0 and the **D0 Technical Manager** supports it. The operator's actions — operate, monitor, view results, respond to prompts, handle routine errors, escalate — define the experience D1 must deliver.

Provenance note: baseline-cited actions are distinguished from **position-derived** ones (elaborated from a role's job function under Human Position First), so origin stays traceable (Phase 1 §4.6).

## 3. The capability model

Capabilities are what must exist so the actions are possible. They are **tagged by layer**, because the stack spans three products and a capability belongs to whichever product provides it (`capabilities.md`, C-01–C-33).

### D2 capabilities (C-01–C-23) — what the D2 product must do

- **Setup & default choices** (C-01–C-05, C-22, C-23). D2 lets the D1 Designer start from a few high-level *postures* rather than configuring everything, produces one reviewable **Selected Setup Configuration Package** as the source of truth, and preserves distinct authorities over its items. This is Phase 1's goal in practice: minimize Designer attention while preserving control.
- **The D1 design process** (C-06–C-12, C-16–C-18). The core: maintain a provisional plan, study the predecessor once and keep a reference roadmap, prepare each work unit's boundary *before* work begins, construct bounded designs, evaluate before submission (distinct from acceptance), advance/spawn, govern revision authority, and preserve design lineage. Largest area; best cross-validated.
- **Reporting, intervention & review** (C-13–C-15, C-20). Designer-oriented reports, consolidated *D2-initiated* clarifications, review stops, and a unified *Designer-initiated* inspection & intervention point. The two intervention directions are deliberately kept distinct.
- **Data environment** (C-19). Provision the eight functional data classes at setup, preserving their distinctions.
- **Self-observation & audit** (C-21). Let the Designer see D2's health and audit the completed process.

A structural finding from the coverage work: several D2 capabilities are **autonomous** — D2 performs them to *serve* a role, with no single role action (C-04, C-07, C-08, C-18, C-19). The model therefore keys capabilities on the **role served**, not solely on a one-to-one action.

### D1-product capabilities (C-24–C-27) — the wrapper

Serving the D1 Technical Manager, produced via the D1 Programmer: **governed product parameters** (tuning without code changes — the basis of rule **RU-01**), **upgrade / release / rollback management** (smoke-test suite, records), **D0 deployment & health monitoring**, and **implementation from specification**.

### D0-product capabilities (C-28–C-33) — the deployed product

Serving the D0 Operator first: **routine operation**, **operator-level configuration**, **status / monitoring / results visibility**, **notifications & routine error handling**, plus **deployment install / maintenance** and **technical support & escalation** for the technical roles. Specific features are set per project by the D1 Designer; these are the generic categories any D0 should provide for a low-technical operator.

## 4. Coverage and traceability

The bookkeeping exists to guarantee completeness. Because roles/actions were derived from Phases 1–5 and capabilities *independently* from Phase 6, their cross-check (`audit-1-role-action-vs-capabilities.md`) is a genuine coverage test rather than a circular one. After reconciliation: **every action maps to a capability** (the two meta D2-Designer actions excepted), **no capability is a true orphan** (action-less ones are autonomous), and the model is layer-consistent and de-duplicated. The map is the join that keeps this traceable.

## 5. Key design decisions

- **Role layering** — the D2 Designer builds D2; the D1 Designer is D2's only user; product operators are downstream.
- **D1 / D0 boundary** — D1 is a thin wrapper around D0.
- **Primary-user principle** — D1/D0 serves the D0 Operator first.
- **Capability layers** — every capability tagged D2 / D1-product / D0-product.
- **Autonomous capabilities** — recognized as capabilities keyed to a served role, not forced into the action model.
- **Rules derive from roles** — RU-01 (no hard-coded numbers) from the D1 Technical Manager.

## 6. Deferred to Phase 7 (architecture)

The capability records carry "open boundaries" — the deferred mechanisms: the Design Tree relationship model, Design Node internal architecture, the data/working-area structure, the unified interaction point, governance/authority/acceptance mechanisms, positions→agents, the setup/template mechanism, and self-observability. Phase 7 derives these from this model. See `../phase-7/README.md`.
