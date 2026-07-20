# environment — the fundamentals + framework (what the node operates under)

Read-only material the node reads. **Self-contained** — everything is copied in; nothing outside the
package is needed.

- `constitution/` — the frozen **Phases 1–5** (the source of truth; positions live in Phase 5 Item 3),
  plus `constitution/completions.md` — **Designer-originated completions** that govern alongside the
  baseline (Phase 5 Item 2). C-2026-07-19-1 names the **D2 Assistant** a Human-Position-First position.
- `method.md` — the **Phase 6 method** (functional doc §1): the derivation discipline.
- `rules.md` — the **design-tree rules** `RU-01…RU-11`.
- `glossary.md` — supporting term definitions.
- `sources.md` — the **Source namespace / traceability contract**: exactly which Sources a derivation
  may cite, and how out-of-package `Phase 6 Item 1/2/3` provenance references resolve to in-package
  Sources. Makes the package **fully self-tracing**.
- `framework/` — the **module** (the design tree + design node module): `design-tree.md` (the tree +
  node governance), `design-node-algorithm.md` (the **module's method** — how a node reads its
  contract, decomposes, derives, and submits), and `conformance.md` (the **conformance** acceptance
  requirement). Run outputs like `algorithm.md` are *products* of running the module, not the module
  itself.

Snapshots of the D2 fundamentals and the D2 **module** (the design-tree tool). The `framework/` copies
are **synced to the conformant module**: they include the module's conformance acceptance requirement
(`framework/conformance.md`). Any doc-internal links inside these copies that point elsewhere are
provenance only — not operational dependencies.
