# Audit 2 — Substance gap: capability model vs. prior Phase 6 items

*2026-07-12. Triggered by the Designer's concern that "we are not doing it right." A cross-check of our capability model + the new Phase 6 document against the substance of the prior items (`prior-items/` Item 1–3).*

## Verdict

**We indexed the design instead of doing it.** The prior items are dense functional specifications; our capability model reduced them to ~19 one-line registry entries plus a high-level narrative. The one-liners are a *table of contents* for the prior items, not a redesign of them. The substance was compressed away, not carried forward.

## Cross-check — what each item contained vs. what we kept

### Item 1 — Template Library (8 sections, ~35 specific declarations)
Lost or flattened to one line:
- The **13 template categories** the Library must cover (Designer–D2 relationship, D1 posture, D0 positions, D0 user priorities, harness/monitoring/evaluation posture, investigation depth, Design Node defaults, resource/budget, reporting, Review Stop, authority defaults) → C-01 "reusable prepared material."
- The **7 package properties** (centralized, human-readable, versioned, reviewable, traceable, explicit about modifications, retrievable) → a phrase in C-02.
- The **7 review request types** (summary / full / D0-user-only / harness-only / comparison / explanation / revision) → C-03 "inspect, compare, revise."
- **Authority-by-material** (Designer–D2 vs D1 vs D0 material governed differently, with worked examples) → C-05 "authority follows meaning."

### Item 2 — Support the D1 Design Process (16 functions, each with sub-lists)
Each function carried the *actual design* in its bullets, and those bullets are gone:
- Context preparation's **11 context elements** → C-08 "prepare the boundary."
- Internal evaluation's **~10 evaluation types** → C-11 one line.
- The result report's **9 contents** → C-13 one line.
- Spawning's **8 proposal elements**, revision authority's classes, history's **8 preserved items** → one line each.

### Item 3 — D1 Design Data & Working Areas (8 data classes + principles)
The worst compression: **all 8 functional data classes**, each with candidate contents, plus "established through setup" and "preserve functional distinctions" → **a single capability, C-19.**

**Scale of the gap:** the prior items hold on the order of **100+ specific functional declarations**; our model has ~19 one-line capabilities. Roughly a 5–6× loss of design content — and the lost content *is* the design.

## 1. Major missing elements

1. **Per-capability functional detail.** Every capability needs the depth a prior-item section had (requirements, considerations, boundaries, examples). We have headlines.
2. **Item 3 is essentially unspecified** — the 8 data classes collapsed to one line; the data environment is the least-designed and arguably most concrete area.
3. **Rationale / "why."** The prior items justify each requirement; our records assert without reasoning.
4. **Worked examples.** The examples that make the design testable (the timeout example, the roadmap examples, the query examples) are absent from the capability treatment.
5. **Cross-item threads.** The Setup Package runs through all three items; authority-follows-meaning recurs; the harness posture propagates. These connective tissues aren't designed, only named.
6. **Implementation-readiness.** A reader could *nearly build* from the prior items. From our one-liners, they cannot. That is the real test we fail.

## 2. Why this happened — and how to fix the process

### Root cause

- **We optimized the scaffolding, not the substance.** Tables, stable IDs, FKs, join integrity, dedup, coverage audits — all satisfying and *measurable* — became the visible "progress." Passing an integrity check *felt* like completion and masked that the design itself was never written.
- **We conflated *identifying* capabilities with *designing* them.** The handoff said "identify what D2 must be capable of"; we named them and stopped, treating naming as the deliverable.
- **We inverted the order.** We built the index first and left substance as placeholders. Substance should come first; the index is extracted from it.
- **We summarized the source instead of carrying it.** The prior items should have been *reframed and preserved* under the capability model, not reduced to pointers.
- **My reviews checked the wrong thing.** Both audits verified *structure* (do FKs resolve? any orphans?). Neither asked *is each capability specified well enough to build?* — the only question that matters for substance.

### How to improve

1. **Substance-first.** Write the functional design for each capability — at the prior items' depth — in the **document(s)**; then extract IDs/FKs into the catalogs as an index. Never let the table carry the design.
2. **One capability = one proper section**, not one line. Requirements, considerations, boundaries, examples, rationale.
3. **Right-size granularity.** Item 3 alone is ≥8 capabilities (one per data class). Don't collapse.
4. **Carry forward, then reframe.** Treat the prior items as source substance to preserve and reorganize, not to abstract away.
5. **Audit for adequacy, not just integrity.** Add the question: *could a competent builder produce this from the spec?* Structure checks stay, but they are necessary, not sufficient.
6. **Name the trap.** "Clean tables" is a false signal of done. Guard against optimizing what's easy to measure over what's hard to write.

## Recommendation

Redo Phase 6 **substance-first**: rebuild the capability treatment as proper functional documents (carrying the prior items' depth, reorganized by role/layer/capability), and demote the current catalogs to what they are — the registry. The role/layer model, primary-user principle, and coverage method we established are sound and worth keeping; they are the *frame*, not the *content*.
