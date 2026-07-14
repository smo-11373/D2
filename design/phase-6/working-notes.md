# Phase 6 — Working Notes

*In-progress reasoning for Phase 6 (Role–Action & Capability Model). Messy by design; settled results graduate into `../catalogs/`.*

## Reconciling the prior Phase 6 items with the handoff rewrite

*(Recorded after converting the three prior items into `prior-items/` and re-reading the handoff note.)*

**The reframe.** The handoff replaces Phase 6's *organizing principle*, not its substance. The
prior items were a **list of functionality**; the new Phase 6 is a **model**:
Role → Action → Capability (→ Architecture → Implementation, both deferred to Phase 7). The prior
items' content survives — it becomes the **raw material for the Capability Catalog**.

**Naming hazard.** "Phase 6 Item 1/2/3" now means two different things. Old items = Template
Library / Support D1 Process / Data & Working Areas. New items = Role–Action Catalog / Capability
Catalog / Action–Capability Coverage. Always disambiguate.

**The prior items map onto capability clusters** (candidate `C-` entries to derive):

- **Item 1 (Template Library)** → a *setup / default-design-choice* capability cluster:
  template library, simple posture choice (Standard / High Harness / Lean), Selected Setup
  Configuration Package, progressive-disclosure review, authority-follows-meaning, later revision.
- **Item 2 (Support D1 Process)** → the largest cluster: ~16 process functions — provisional
  plan, Predecessor Reference Roadmap, per-work-unit context prep, submission vs acceptance,
  local vs integration evaluation, posture-scaled harness depth, result reports, review stops,
  advancement vs spawning, revision authority, design lineage.
- **Item 3 (Data & Working Areas)** → a *data-environment provisioning* capability: the eight
  functional data classes.

**Observation — Item 3 is where our own layout work came from.** Item 3 says "the exact directory
structure … remain later design questions," then lists eight data classes (planning, observation,
metadata, shared, reference, project working, node-local working, Designer-relevant artifacts).
Our fractal `ref/design/workspace/product` + `d2/` footprint is effectively an early answer to
that deferred question *at the D2 layer*. Worth deciding later whether the eight classes map onto
our quad or refine it.

**Recurring themes reinforce decisions already made:**

- *Authority follows meaning; central collection ≠ central authority* (Item 1 §6–7, Item 3 §4) →
  matches our **ownership rule** and the `d2/` footprint.
- *Original reference vs D2-created notes must stay distinguishable* (Item 3 §5) → matches
  Phase 1 §4.6 provenance and our `ref/` vs `design/` split.
- *Prefer human-readable, transparent material over opaque parameter tables* (Item 1 §1) →
  matches our choice to keep catalogs in Markdown, not JSON.

**Open reconciliation questions** (candidates for `../decisions/`):

1. Do capabilities attach to **actions** (handoff model) or can a capability be a standing D2
   *function* with no single Designer action? Item 2's functions are mostly D2-internal — they
   *support* Designer/D1-Designer actions rather than *being* Designer actions. Likely need
   capabilities that reference *supported roles* even where no `A-` maps 1:1.
2. Are the prior items' "Selected Setup Configuration Package" and "Setup Package" the same object
   referenced across Items 1–3? (They read as the same thing.) Consolidate in the glossary.
3. Roles beyond the Designer (D1 Designer, D1 Programmer, Technical Managers, D0 Operator) are
   *referenced* by the prior items but defined in Phase 5 — seed them from Phase 5, not here.

**Recommended next step.** Derive an initial `C-` capability list from Item 2 (richest source),
then Items 1 and 3; wire each to its supporting role(s)/action(s) via `action-capability-map.md`;
log the open questions above in `../decisions/`.

## D2 ↔ D1 self-similarity — what carries forward, what differs

*(Recorded 2026-07-13, Designer direction, while reviving §4–§5 of the functional doc.)*

**Stable core.** Phases 1–5 read as largely **fixed across the layers** — the same governing
constitution is expected to hold for D2 and D1, and possibly D0, with only modest layer-specific
adaptation. As we revive later sections, keep testing whether the Phase-1–5 frame keeps carrying
forward.

**The similarity — shared structural concepts.** Both D2 and D1 designs should be built on the
same two concepts: the **design graph** (the Design Tree / design-graph structure) and the
**design node** (a bounded design responsibility). These are common elements worth abstracting.
The *implementation* of each may differ by layer — D1's is expected to be **significantly more
sophisticated**, D2's **relatively simple** — but the concepts are shared.

**The primary difference — the existing-system harness.** D1, by necessity, **upgrades an
existing (V1) system**, and that system is a huge factor in D1 design. In particular it is a
**strong harness**: one of the strongest motivations for upgrading rather than building from
scratch is that the predecessor supplies behavioural examples, expected input–output pairs, and
constraints (Phase 5, Item 1 — Harness First). D1 design steps should **exploit it to the
maximum** — constructing test examples and so on — and this shapes those steps. **At the D2 level
there is no such predecessor**, so this harness is absent. This is the **primary difference
between D2 and D1 design steps.**

**Forward intent.** To the extent possible, arrange **D2's own design** on the same design-graph /
design-node concepts — deferred to **later, likely after this phase** (Phase 7 architecture
territory). Note the Design-Tree-vs-graph relationship model is itself still open (Phase 4,
Item 2).
