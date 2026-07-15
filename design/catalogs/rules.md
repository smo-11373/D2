# Rules Catalog

*Living. Design rules and constraints, each with the role or principle it derives from. One record per rule. See `README.md` for ID conventions. Rules should be **derived, not invented** (Phase 5): D2 should be able to explain the quality concern or position a rule protects.*

## RU-01 — No hard-coded numbers (in most situations)

- **Rule:** Values that may legitimately require product-level adjustment without redesign or programming should be exposed as **explicitly governed parameters**, not hard-coded. *("In most situations" — not literally every value; Phase 5: it "does not require every literal value to become configurable.")*
- **Derived from:** **R-04 D1 Technical Manager** — *position existence creates design consequences* (Phase 5 §Item 3). The D1 Technical Manager must be able to upgrade the product by adjusting a governed parameter, without touching code, to the extent plausible.
- **Harness note:** *"No code change does not mean no harness."* A parameter change still runs the required validation/regression harness — the D1 wrapper's upgrade smoke-test suite (see glossary `d1`).
- **Scope:** D1 / D0 design.
- **Source:** Phase 5 §Item 3 (Human Position First); §Item 4 (Quality over Expediency — "avoid hard-coded adjustable values").
- **Status:** Accepted (baseline-derived).

## RU-02 — A node justifies its own result; the parent approves

- **Rule:** Each design node is responsible for the **justification** of its design result. The justification is authored by that (child) node and **attached to its submission package**; the **parent node — as enforcer — reviews and approves or rejects** it. Justification travels *with* the result, added once the node is designed, not maintained separately.
- **Derived from:** the **design node** as a self-contained agent with sub-human authority (glossary `design-node`); **submission ≠ acceptance** (a node may produce and justify, but acceptance authority sits with the parent); *authority follows meaning*.
- **Scope:** D2 and D1 design (design-tree governance; applies to D2's own design too — the Phase 6 "Why" narratives are node justifications in this sense).
- **Source:** Phase 4 §Item 2 (submission vs acceptance; upward proposals routed by authority); Phase 6 Item 2 §7; Designer 2026-07-15.
- **Status:** Accepted (Designer-directed).

## RU-03 — Spawn design-tree children by the Designer's actions

- **Rule:** A design node's **spawning** is driven by the relevant **Designer's potential actions** — each node determines its children by the actions its scope must support. The action set splits into **passive** (a *static* list derived from the approved setup/fundamentals — one child per passive action is straightforward) and **active** (dynamic and flexible — harder). **Passive-action spawning is implemented first; active-action spawning is deferred.**
- **Derived from:** the node's **spawning responsibility** (C-16; Phase 4 §Item 2 — spawning strategy) and the **passive/active action model** (functional doc §1). Actions are the common unit both the tree (nodes) and the capability model (support) hang on.
- **Scope:** D2 and D1 design (design-tree governance; applied to D2's own design first).
- **Source:** Phase 4 §Item 2; Phase 6 functional model (passive/active actions); Designer 2026-07-15.
- **Status:** Accepted (Designer-directed); active-action spawning deferred (see `../phase-6/working-notes.md`).
