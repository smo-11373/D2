# Capability Catalog

*Living. Capabilities the D2 product must provide — derived here **from the Phase 6 design** (`../phase-6/prior-items/`), independently of the Role–Action table. One record per capability. See `README.md` for ID conventions.*

> **Scope & method note.** These are **D2** capabilities (what D2 must do), derived only from the three prior Phase 6 items. Role/action foreign keys (supported roles/actions) are **intentionally not wired yet** — that reconciliation follows the audit (`../phase-6/audit-1-role-action-vs-capabilities.md`). Each record cites its Phase 6 source.

## From Item 1 — Template Library / Setup

### C-01 — Provide default design choices
- **Purpose:** Offer prepared, reusable design material and a small set of high-level postures (e.g. Standard / High Harness / Lean) so one choice resolves into many detailed settings.
- **Scope:** The Template Library (extensible; human-readable) + simple posture selection.
- **Open boundaries:** exact formats deferred.
- **Source:** Phase 6 Item 1 §1–2. **Status:** Derived.

### C-02 — Produce the Selected Setup Configuration Package
- **Purpose:** Turn the posture choice into a centralized, versioned, traceable, reviewable record of the actual setup for the run — the source of truth, distinct from the Library.
- **Scope:** Package created before activation; traceable to template sources; explicit about Designer modifications.
- **Source:** Phase 6 Item 1 §3. **Status:** Derived.

### C-03 — Setup review with progressive disclosure
- **Purpose:** Let the Designer inspect, summarize, compare, explain, or revise the setup package before activation, without forcing full inspection.
- **Source:** Phase 6 Item 1 §4. **Status:** Derived.

### C-04 — Establish effective configuration across contexts
- **Purpose:** Materialize the confirmed setup into the appropriate D2/D1/D0 contexts (copy/generate/reference/…) without losing traceability to the central package.
- **Open boundaries:** mechanism deferred (no required CLI/tech).
- **Source:** Phase 6 Item 1 §5. **Status:** Derived.

### C-05 — Authority-aware setup governance & later revision
- **Purpose:** Preserve distinct authorities over setup items (authority follows meaning); support governed later revision with impact analysis and preserved history.
- **Source:** Phase 6 Item 1 §6–8. **Status:** Derived.

## From Item 2 — Support the D1 Design Process

### C-06 — Provisional D1 design plan management
- **Purpose:** Maintain a plan with the current phase defined and later phases provisional (top-to-bottom); advance it as higher-level design settles.
- **Source:** Phase 6 Item 2 §1. **Status:** Derived.

### C-07 — Predecessor study & Reference Roadmap
- **Purpose:** Study the predecessor package once broadly and preserve a roadmap linking design subjects to reference locations (pointers, revisable).
- **Source:** Phase 6 Item 2 §2. **Status:** Derived.

### C-08 — Per-work-unit context preparation
- **Purpose:** Assemble the bounded context (responsibility, intent, rules, harness, references, expected outputs, authority, open issues) before a design work unit begins — "prepare the boundary before the work."
- **Source:** Phase 6 Item 2 §3. **Status:** Derived.

### C-09 — Targeted predecessor investigation before design
- **Purpose:** Investigate the relevant predecessor material to the depth warranted by importance/posture/uncertainty before substantial design.
- **Source:** Phase 6 Item 2 §4. **Status:** Derived.

### C-10 — Bounded design construction
- **Purpose:** Carry a bounded design responsibility from prepared input to an evaluated design result (investigate, develop, compare, critique, specify).
- **Open boundaries:** internal agentic mechanism deferred.
- **Source:** Phase 6 Item 2 §5. **Status:** Derived.

### C-11 — Design-result evaluation
- **Purpose:** Evaluate a result before submission (conformance, predecessor comparison, tests, semantic review…), at local vs integration scopes, scaled by posture and importance.
- **Source:** Phase 6 Item 2 §6, §8, §9. **Status:** Derived. *(Merges internal-evaluation, local-vs-integration scope, and posture-scaling.)*

### C-12 — Submission & acceptance governance
- **Purpose:** Treat submission and acceptance as distinct steps; support acceptance outcomes (accept / return / conditional / escalate).
- **Open boundaries:** acceptance mechanism deferred.
- **Source:** Phase 6 Item 2 §7. **Status:** Derived.

### C-13 — Designer-oriented result reporting
- **Purpose:** Produce concise Designer-oriented reports after major accepted work (what was designed, key decisions, V1 changes, unresolved issues, harness results, next actions), with deeper material on demand.
- **Source:** Phase 6 Item 2 §10. **Status:** Derived.

### C-14 — Passive Designer intervention (consolidated clarifications)
- **Purpose:** Investigate first, then batch remaining high-leverage questions into a consolidated Clarification Request (distinct from a Review Stop); threshold set by posture.
- **Source:** Phase 6 Item 2 §11. **Status:** Derived.

### C-15 — Review-stop provisioning
- **Purpose:** Offer the Designer a review opportunity at appropriate design points before continuation; tendency scales with design level and posture.
- **Source:** Phase 6 Item 2 §12. **Status:** Derived.

### C-16 — Design advancement & spawning
- **Purpose:** Determine the next design work at a unit's completion (advance / spawn descendants / integrate / revisit), keeping advancement and spawning distinct; propose a spawning strategy.
- **Open boundaries:** Design Tree mechanics deferred.
- **Source:** Phase 6 Item 2 §13–14. **Status:** Derived.

### C-17 — Revision-authority governance
- **Purpose:** Carry a revision-authority status per design result (D2-managed / Designer-governed); route revision proposals accordingly; prevent silent revision of Designer-governed design.
- **Source:** Phase 6 Item 2 §15. **Status:** Derived.

### C-18 — Design lineage & traceability
- **Purpose:** Preserve enough design history to explain what is effective, where it came from, what governs it, what predecessor references and harness informed it, and why major changes were made.
- **Source:** Phase 6 Item 2 §16. **Status:** Derived.

## From Item 3 — D1 Design Data & Working Areas

### C-19 — Provision the D1 design data & working areas
- **Purpose:** Establish, at setup, a prepared data environment with the eight functional data classes (planning, observation, metadata, shared project data, reference, project working, node-local working, Designer-relevant artifacts); preserve their functional distinctions.
- **Open boundaries:** exact directory structure / storage tech deferred.
- **Source:** Phase 6 Item 3. **Status:** Derived. *(The "project observation data" class underpins Designer monitoring queries — relates to Phase 2 Principle 2.)*
