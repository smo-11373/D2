# Audit 1 — Role–Action table vs Capability list

*Date: 2026-07-12. A read-only cross-check. **Neither table was modified.***

## Method

The two tables were derived from **different sources, independently**:
- **Role–Action** (`../catalogs/role-action.md`) — roles from Phases 1 & 5, actions from Phases 2–5 and prior Phase 4 (R-00–R-06; A-001–A-039).
- **Capabilities** (`../catalogs/capabilities.md`) — derived only from the prior **Phase 6** items (C-01–C-19).

They were then cross-checked. Because the derivations were independent, agreement is evidence of coverage and disagreement is a real finding — not an artifact of circular derivation.

## Headline finding

**The two tables sit at different scopes.** The capability list is about **what D2 must do** (mostly serving the D1 Designer and D2-internal design work). The Role–Action table spans **four layers of roles** — the builder (R-00), D2's user (R-01), D2-internal workers (R-02–R-03), and the D1/D0 *product* operators (R-04–R-06). Many actions therefore have **no D2 capability by design**, because they aren't D2's job.

## Coverage matrix (role → D2-capability coverage)

| Role | Coverage | Comment |
|------|----------|---------|
| R-00 D2 Designer | **none (out of scope)** | A-010/011 are meta — designing D2 itself, not D2 operating |
| R-01 D1 Designer | **strong, with gaps** | setup/report/review actions map to C-01–05, C-13–15; **gaps below** |
| R-02 Design Node Builder | **strong** | A-021–027 map cleanly onto C-08–C-12, C-16, C-17 — best-aligned area |
| R-03 D1 Programmer | **none** | A-028 (implement code) is *past* Phase 6, which stops at implementation-ready design |
| R-04 D1 Technical Manager | **none** | A-029–033 operate the delivered **D1 product**, not D2 |
| R-05 D0 Operator | **none** | A-034–036 operate **D0** |
| R-06 D0 Technical Manager | **none** | A-037–039 support **D0** |

## Findings

**F1 — Scope/layer mismatch (structural).** Capabilities describe D2; the Role–Action table also lists downstream product roles (R-04–R-06), a meta role (R-00), and an implementation role (R-03) whose actions are *not* D2 capabilities. Either the Capability Catalog needs a **layer/scope tag** (D2 vs D1-product vs D0-product capability), or the downstream roles belong in a **separate, per-layer** catalog.

**F2 — Many D2 capabilities are autonomous and map to *no role action.*** C-04 (establish config), C-07 (roadmap), C-08 (context prep), C-06 (plan), C-11 (evaluation), C-18 (lineage) are things **D2 does on its own** to *support* a role, not things a role *does*. The handoff's "capabilities derive from actions" model doesn't fit these — they need to be keyed to a **supported role** (whom they serve) even without a 1:1 action. *(This is the same tension flagged earlier in the working notes.)*

**F3 — D1 Designer actions under-covered by Phase 6.** Several R-01 actions have **weak or no** capability in the Phase 6 items because they originate in Phases 2–4:
- A-007 / A-008 / A-009 — Designer inspection, investigation, and directive → no unified "Designer inspection & intervention" capability in Phase 6 (it lives in Phase 4).
- A-020 — request/review a D2 audit → no D2 self-audit capability (Phase 3 Item 5).
- A-019 — tune resolution depth / intervention posture → only weakly implied (Phase 2 §2.6).
- A-013 — establish the initial design input → no explicit intake capability (Phase 3 Item 2).
This **confirms the handoff's rationale**: Phase 6's prior "list of functionality" is incomplete as a capability model; the rewrite must pull these in.

**F4 — Strong alignment on the design-process core.** R-02 (Design Node Builder) actions A-021–027 map almost 1:1 onto C-08–C-12, C-16, C-17. Two independent derivations converging here is a good sign the design-process spine is sound.

**F5 — Intra-table overlaps to resolve during reconciliation.**
- Actions: A-003 (request investigation) ↔ A-008 (investigation/concern); A-012 (review operating contract) ↔ A-016 (review setup package). *(Already logged.)*
- Capabilities: the setup cluster (C-01–C-05) and the evaluation cluster (C-11–C-12) are close-knit; check for redundancy when wiring.

**F6 — Orphan-capability check.** No capability is a true orphan *within D2's scope*; but C-04 and C-08 (autonomous, see F2) will look orphaned under a strict action→capability mapping. This is a modeling gap (F2), not a spurious capability.

## Recommendations (for decision — not applied)

1. **Introduce a capability layer/scope tag** (D2 / D1-product / D0-product), or split the catalog by layer, to resolve F1.
2. **Allow capabilities to key on a *supported role*** even when D2-autonomous (no 1:1 action), resolving F2 and matching the handoff model to reality.
3. **Decide the Role–Action table's scope** — keep all four layers of roles, or restrict it to D2's served roles (R-01, R-02) and move downstream roles to a per-layer catalog.
4. **Add the missing D2 capabilities** implied by Phases 2–4 (inspection/intervention, self-audit, resolution-depth tuning, initial-input intake) — this is exactly the Phase 6 completion the handoff calls for.
5. **Reconcile the intra-table overlaps** (F5) during the coverage pass.

## Summary

The design-process core is well-covered and cross-validated (F4). The main issues are **structural**: the tables span different layers (F1), the action→capability model doesn't fit D2's autonomous functions (F2), and Phase 6's prior items miss D2 capabilities that Phases 2–4 require (F3). None of these are contradictions in the design — they are the expected seams the Phase 6 rewrite is meant to close.
