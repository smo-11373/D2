# D2 Functional Design — The D1 Design Data Environment

*Substance document (part of the substance-first rebuild). Carries forward and reframes prior Item 3 (`../prior-items/item-3-d1-design-data-and-working-areas.md`). The capability registry (`../../catalogs/capabilities.md`) indexes this document; it does not replace it. Architecture — exact directory structure, formats, storage technology — is derived in Phase 7; this document fixes **what data functions must exist** and **why**.*

## Purpose

At project setup, D2 must provision the major data and working areas a D1 design project needs to be **conducted, governed, observed, and preserved**. D1 design work should begin inside a *prepared* data environment rather than inventing storage, working areas, and shared locations as it goes.

**Why this matters.** Three baseline commitments force it: reducing Designer burden (Phase 1 — the Designer should not hand-build the environment); modularization (Phase 5 — bounded work needs bounded places); and provenance (Phase 1 §4.6 — different kinds of information must stay distinguishable). An ad-hoc environment silently violates all three.

## Governing principles for the environment

Four rules govern the whole environment, independent of the eventual physical layout:

1. **Established through setup.** The areas are created by the D2 setup process; the Selected Setup Configuration Package determines which areas exist, their default structure, initial contents, applicable templates, and access expectations. The D1 Designer does not manually construct the environment.
2. **Functional distinctions are preserved even when physically co-located.** Different classes may share storage or a directory tree, but D2 must preserve the differences among them, because those differences drive **authority, lifecycle, visibility, retrieval, and modification** — and later architecture.
3. **Central collection ≠ centralized authority.** A shared area does not confer uniform authority over its contents; items within it may have different creation/modification authorities.
4. **Original vs. derived must stay distinguishable.** Externally-provided reference material and D2-created notes *about* that material must remain separable (this is Phase 1 §4.6 applied to storage).

## The eight functional data classes

Each class below states what it holds, why it is a distinct class, its authority/lifecycle/visibility character, and a **candidate home** in this repository's fractal layout (`ref/ · design/ · workspace/ · product/` + the `d2/` footprint). The candidate homes are a *pre-architecture* mapping — an early answer to Item 3's deferred structure question — to be confirmed or refined in Phase 7.

### 1. Planning data
- **Holds:** the current phase; the provisional list of later phases; phase-advancement decisions; completed phases; plan revisions; enough planning history to explain how the current plan developed.
- **Distinct because:** the *plan* governs the process that produces the design — it is not the design itself. It sits roughly **half a level above** the design work (see glossary `half-level`).
- **Authority · lifecycle · visibility:** revised through the design process under Designer control points; evolves continuously as phases advance; the Designer must be able to ask "where are we in the plan?"
- **Candidate home:** `d2/` footprint (D2-managed process governance), e.g. `d2/planning/`.

### 2. Project observation data
- **Holds:** current design activity; completed and pending work; progress; resource, financial, and time consumption; **Designer Attention Cost**; unresolved issues; abnormal process conditions; other project-health information.
- **Distinct because:** it describes the *condition and progress* of the project, not its design content — the substrate for Designer monitoring (Phase 2 Principle 2).
- **Authority · lifecycle · visibility:** D2-maintained; continuously updated; **highly Designer-visible** — it answers "show me resource consumption," "what is blocking progress?" Monitoring responsibility (D1 / D2 / shared) is deferred, but the data function must exist.
- **Candidate home:** `d2/` footprint, e.g. `d2/observation/` (telemetry/health).

### 3. Design metadata
- **Holds:** Design Tree information; Design Node information; design relationships; node status; governing relationships; revision authority; submission/acceptance status; spawning records; design lineage.
- **Distinct because:** it *represents and governs* the developing design — the structural bookkeeping of the design itself, separate from the design content and from process observation.
- **Authority · lifecycle · visibility:** D2-managed under the governance rules; the detailed model awaits the Phase 7 Design Tree / Design Node architecture; visible to the Designer via inspection ("show me the Design Tree; what changed since my last review?").
- **Candidate home:** `d2/` footprint, e.g. `d2/design-tree/`.

### 4. Shared project data
- **Holds:** rules; standards; D1 design rules; applicable D2 concepts and philosophy; glossary and definitions; communication standards; common design conventions; representative usage examples; test examples; shared evaluation material; common reference notes.
- **Distinct because:** it serves the whole project broadly rather than one Design Node — common context that many nodes may draw on.
- **Authority · lifecycle · visibility:** *central collection, distributed authority* — rules, standards, and definitions within it may each have different creation/modification authorities. Designer-visible and Designer-governable in part.
- **Candidate home:** `design/` (the authored, shared design record), e.g. `design/shared/`.

### 5. Predecessor & reference data
- **Holds:** the original V1 D1 package (source, docs, config, tests, usage material, historical design material), revision proposals, supplementary Designer documents, and the **Predecessor Reference Roadmap** (from Item 2).
- **Distinct because:** it is *evidence, not authority* (Phase 1 §3.3) — read-first source material the project refers to but does not author.
- **Authority · lifecycle · visibility:** read-only source; the original material and D2-created notes about it **must remain distinguishable** (principle 4). Large; entered efficiently via the Roadmap.
- **Candidate home:** `ref/` (the read-first evidence bucket), with D2's roadmap/notes kept separate (e.g. `d2/` or `design/`, not intermixed with the originals in `ref/`).

### 6. Project working area
- **Holds:** work that is not yet accepted design, not local to one node, possibly multi-node, exploratory, being consolidated, or temporarily needed during project-level activity.
- **Distinct because:** it is *project-level scratch* — must be separable from persistent accepted design so that intermediate artifacts are not mistaken for design.
- **Authority · lifecycle · visibility:** ephemeral; not authoritative; promote settled results into accepted design (classes 3/4).
- **Candidate home:** `workspace/` (project-level scratch).

### 7. Node-local working areas
- **Holds:** per-node local notes, temporary analysis, candidate designs, local test material, evaluation results, temporary copies/extracts of relevant reference material.
- **Distinct because:** modularization (Phase 5) — each Design Node needs a **local sandbox** so it can investigate, design, and evaluate without treating the shared area as undifferentiated scratch. *Shared data gives common context; the node area gives local freedom.*
- **Authority · lifecycle · visibility:** node-scoped; local autonomy under the node's governing contract; detailed sandbox model deferred to the Phase 7 Design Node architecture.
- **Candidate home:** `workspace/` sub-areas per node, e.g. `workspace/nodes/<node>/`.

### 8. Shared Designer-relevant artifacts
- **Holds:** D0 prototypes; representative D0 package structures; sample health reports; monitoring examples; interface mockups; algorithm demonstrations; comparison results — byproducts useful beyond the node that made them and especially relevant to Designer inspection.
- **Distinct because:** these are *promoted* artifacts — once identified as broadly Designer-relevant, they must not stay hidden inside one node's local area.
- **Authority · lifecycle · visibility:** promoted from node-local (class 7) by a mechanism deferred to Phase 7; **high Designer visibility**.
- **Candidate home:** `product/`-adjacent or a dedicated `design/artifacts/` surfacing area.

## How the classes relate (cross-cutting design)

- **Half-level separations.** Planning (1) sits above the design; design metadata (3) governs the design; both are distinct from the design *content* and from observation (2). Keeping these apart is what lets the Designer ask process questions and design questions separately.
- **Shared vs. local (4 vs. 7).** The modularization spine: common context vs. bounded local freedom. Getting this boundary right is what keeps nodes autonomous without fragmenting the project.
- **Evidence vs. authored (5 vs. 3/4).** Provenance made physical: reference stays read-first and separable from D2's notes and the authored design.
- **Ephemeral vs. accepted (6/7 vs. 3/4).** Working areas must never be silently mistaken for accepted design; promotion is deliberate.
- **Observation underpins interaction.** Class 2 is the data behind the unified Designer inspection capability — the monitoring queries have nowhere to read from without it.

## Relationship to the repository's own layout

This repository already instantiates a form of this environment at the **D2** layer (`ref/design/workspace/product` + `d2/`), and the copyable `product/` skeleton hands the same shape to each D1 project. The candidate homes above show the eight classes mapping cleanly onto that shape — which is strong evidence the fractal layout is a viable architecture for the data environment. **Phase 7 confirms or refines this**; Phase 6 only commits to the eight functional distinctions.

## Deferred to Phase 7 (architecture)

Exact directory structure; file formats; storage technology; ownership/authority mechanisms; the detailed Design-Node sandbox model; the promotion mechanism (class 7 → 8); and whether the eight classes map onto the fractal quad exactly as above or with refinement.

## Registry pointer

To be re-indexed: capability **C-19** currently collapses this whole document into one line. Under the rebuild it should become **eight capabilities** (one per data class) plus the environment-level governance, each pointing back to the matching section here. (Deferred until the substance approach is confirmed, to avoid ID churn.)
