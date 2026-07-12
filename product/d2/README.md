# d2/  —  the D2 tool (operating footprint)

Everything **owned by D2** inside a project. In `D2/product/` this is the master copy; once
copied into a D1 project it becomes that project's D2 footprint.

- `template-library/` — master default templates (the "default design choices")
- `defaults/`         — operating-contract defaults and design postures (Standard / Lean / High-Harness)
- (engine / runtime)  — added from Phase 7 onward

Provenance rule: D2-authored governance lives here and never blurs into the Designer's authored
D1 content (`../design/`).
