# D2 Glossary

*Living. Definitions of D2 / D1 / D0 terms used across the design. Keyed by term-slug. Carried forward from Phase 5; open to Designer-originated completion. See `README.md` for ID conventions.*

### `d2` — D2 (product)

The product being built in this repository: the design system whose primary user is the D1 Designer. D2 provides setup defaults, a design tree, design node modules, and other tools for building a D1 product. Built by the D2 Designer. — related: `d1`, `d2-designer`

### `d1` — D1 (product)

What the D1 Designer builds using D2: a **thin operational wrapper around D0**. Usually thin — sometimes unnecessary — but kept by default. Holds "half a level above D0" concerns: performance/health monitoring (e.g. D0-crash detection), an upgrade smoke-test suite, upgrade records, and similar operational scaffolding. On delivery, a recipient (e.g. an IT manager) may deploy just D0 into production while retaining D1 to manage and upgrade it. — related: `d0`, `d1-designer`, `half-level`

### `d0` — D0 (product)

The core distributable product wrapped by D1 — the actual application/system deployed to production and run by the D0 Operator (R-05), with front-line support from the D0 Technical Manager (R-06). — related: `d1`

### `half-level` — "half a level above"

A recurring D2 notion: some concerns sit roughly *half a level above* the thing they govern rather than a full layer up. Examples: planning data sits half a level above the design it plans (Phase 6 Item 3); D0 health/performance monitoring sits half a level above D0, living in the D1 wrapper. — related: `d1`

### `d2-designer` — D2 Designer

Builds the **D2** product (currently the human developing D2). **Not** a user of D2. Holds Designer-originated completion/clarification authority over D2's living working sets (this is Phase 5's "the D2 Designer"). Catalog role **R-00** (meta / builder). — related: `d1-designer`, `designer`

### `d1-designer` — D1 Designer

The **primary and only user of the D2 product**. Uses D2's tools (setup defaults, design tree, design node modules) to build a **D1 product** (which wraps D0). This is Phase 1's "Designer" — the "primary user of D2." Catalog role **R-01**. — related: `d2-designer`, `designer`

### `designer` — "Designer" (bare term in the baseline)

Unqualified **"Designer"** in Phases 1–4 and most of 5–6 means the **D1 Designer** (D2's primary user). The one exception is Phase 5's "**the D2 Designer**" and "**Designer-originated completion**" of D2's own living sets, which mean the **D2 Designer** (the builder). Prefer the layer-qualified names. — related: `d2-designer`, `d1-designer`

### `user` — "user" (which layer)

"Primary **user** of D2" = the **D1 Designer**. "**D0 user(s)** / user priorities / user skill level / user-level monitoring" (Phase 5; Phase 6 Item 1) = the **D0 Operator** and other D0-facing roles. — related: `d1-designer`

### `designer-attention-cost` — Designer Attention Cost

The D1 Designer's scarce time and cognitive effort (Phase 1 §2.3). D2 aims to reduce the *total cognitive burden* of Designer participation, not merely the number of interactions. — related: `d1-designer`
