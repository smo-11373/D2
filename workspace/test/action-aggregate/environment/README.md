# environment — the fundamentals + framework (what the node operates under)

Read-only material the node reads. **Self-contained** — everything is copied in; nothing outside the
package is needed.

- `constitution/` — the frozen **Phases 1–5** (the source of truth; positions live in Phase 5 Item 3).
- `method.md` — the **Phase 6 method** (functional doc §1): the derivation discipline.
- `rules.md` — the **design-tree rules** `RU-01…RU-11`.
- `glossary.md` — supporting term definitions.
- `sources.md` — the **Source namespace / traceability contract**: exactly which Sources a derivation
  may cite, and how out-of-package `Phase 6 Item 1/2/3` provenance references resolve to in-package
  Sources. Makes the package **fully self-tracing**.
- `framework/` — the **module** (the design tree + design node module): `design-tree.md` (the tree +
  node governance) and `design-node-algorithm.md` (the **module's method** — how a node reads its
  contract, decomposes, derives, and submits). Run outputs like `algorithm.md` are *products* of
  running the module, not the module itself.

Snapshots of the D2 fundamentals and the D2 **module** (the design-tree tool). The `framework/` copies
are a **pinned pre-conformance snapshot**: they intentionally omit the module's later conformance
acceptance requirement (source module `conformance.md`), because this benchmark measures the
*pre-conformance* module. Any doc-internal links inside these copies that point elsewhere are
provenance only — not operational dependencies.
