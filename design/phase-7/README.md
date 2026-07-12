# Phase 7 — Architectural Design (scope)

*Active phase. Purpose: derive D2's **architecture** from the completed capability model — the next level in the hierarchy `Role → Action → Capability → **Architecture** → Implementation`. Architecture is designed here; **implementation is deferred** to a later phase.*

## Purpose

Phase 6 fixed *what D2 must be capable of* (33 capabilities). Phase 7 fixes *how D2 is structured* to provide them: the components/modules, their boundaries and relationships, the core data and control structures, and the governing mechanisms — to the point of being **implementation-ready**, without yet writing code.

## Governing principles (from Phase 5)

- **Top-to-Bottom** — architecture is *derived downward* from the capability model; it does not redefine capabilities from implementation convenience.
- **Modularization** — express the architecture as bounded units of responsibility with explicit boundaries and local autonomy.
- **Human Position First** — settle conceptual positions and their boundaries before assigning agents; the agentic mechanism comes *after* the position architecture.
- **Verification Before Realization / Harness First** — design how D2's own process is observed, evaluated, and tested *before* committing to implementation methods.
- **Quality over Expediency** — coherent structure over locally convenient shortcuts.

## Scope

**In scope — the architecture of D2 (the tool):**
- Structural realization of the **D2 capabilities** (C-01–C-23).
- The **core structures** D2 operates: Design Tree, Design Node, the data & working-area environment, the unified interaction point, governance/authority, the acceptance mechanism.
- The **scaffolding/templates D2 hands down** so the D1/D0-product capabilities (C-24–C-33) can be realized *per project* by the D1 Designer (e.g. the fractal layout, the Template Library structure).

**Out of scope:**
- Actual coding / realization (a later phase).
- The *specific* architecture of any particular D1 or D0 product — that's the D1 Designer's per-project work, done *using* D2.
- Choice of concrete implementation technologies where a capability defers them.

## Architectural subjects to resolve (the deferred questions, now due)

Drawn from the "open boundaries" recorded across the capability catalog:

1. **Design Tree** relationship model — single-parent vs multi-parent; governing vs spawning relationships.
2. **Design Node** internal architecture — the "conceptual sandbox" made concrete (contract, environment, inputs/outputs, evaluation boundary).
3. **Data & working-area architecture** — the eight functional data classes → concrete structure; build on the repo's existing fractal layout (`ref/design/workspace/product` + `d2/`).
4. **Unified interaction point** — query interpretation, routing, and context preservation (realizes C-20).
5. **Governance & authority architecture** — revision-authority routing, the rule/standard registry, and the **submission→acceptance** mechanism.
6. **Positions → agents** — how conceptual positions (R-02/R-03 internal; the agentic mechanism) are occupied by agents.
7. **Setup/template mechanism** — Template Library → Selected Setup Configuration Package → effective configuration.
8. **Observability & harness for D2's own process** — how the Designer monitors D2 (Phase 2 Principle 2), and how D2 self-evaluates (C-21).

## Proposed Phase 7 items (for confirmation)

A candidate decomposition — to be adjusted with the Designer:

- **Item 1 — Architectural decomposition.** Group the D2 capabilities into modules/components with explicit boundaries; produce a component map. (Modularization)
- **Item 2 — Core design structures.** Design Tree + Design Node architecture (subjects 1–2).
- **Item 3 — Data & interaction architecture.** Data/working-area structure + unified interaction point (subjects 3–4).
- **Item 4 — Governance & control architecture.** Authority, revision routing, rule registry, acceptance (subject 5).
- **Item 5 — Positions & agentic architecture.** Positions → agents (subject 6); setup/template mechanism (subject 7).
- **Item 6 — Observability & harness architecture.** D2 self-observability and self-evaluation (subject 8) — done *early* per Verification Before Realization.

## Deliverables & phase boundary

Phase 7 produces living architecture documents in `design/phase-7/`, derived top-down and traceable back to capabilities. **Phase 7 ends** with an implementation-ready architecture, triggering the implementation phase.

## Decisions to confirm before Phase 7 work begins

1. **Scope** — D2-architecture-focused as above, or also design the D1/D0-product architecture *templates* now?
2. **Item breakdown** — accept the six items, or reshape?
3. **Starting point** — begin with Item 1 (decomposition) top-down, or with Item 6 (observability/harness) per Harness-First?
4. **Candidate role** — confirm or omit the D1 system operator before it can affect architecture.
