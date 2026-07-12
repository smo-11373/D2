# Rules Catalog

*Living. Design rules and constraints, each with the role or principle it derives from. One record per rule. See `README.md` for ID conventions. Rules should be **derived, not invented** (Phase 5): D2 should be able to explain the quality concern or position a rule protects.*

## RU-01 — No hard-coded numbers (in most situations)

- **Rule:** Values that may legitimately require product-level adjustment without redesign or programming should be exposed as **explicitly governed parameters**, not hard-coded. *("In most situations" — not literally every value; Phase 5: it "does not require every literal value to become configurable.")*
- **Derived from:** **R-04 D1 Technical Manager** — *position existence creates design consequences* (Phase 5 §Item 3). The D1 Technical Manager must be able to upgrade the product by adjusting a governed parameter, without touching code, to the extent plausible.
- **Harness note:** *"No code change does not mean no harness."* A parameter change still runs the required validation/regression harness — the D1 wrapper's upgrade smoke-test suite (see glossary `d1`).
- **Scope:** D1 / D0 design.
- **Source:** Phase 5 §Item 3 (Human Position First); §Item 4 (Quality over Expediency — "avoid hard-coded adjustable values").
- **Status:** Accepted (baseline-derived).
