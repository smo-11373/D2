# Output product 2 — the algorithm · submitted at **Step 1 (activation)**

*Submitted with the declaration for the parent's approval. The node is **activated** (may spawn its
children) only once this is accepted. This is the concrete procedure the node commits to; it is
written to be **re-run** and to yield the role-action table substantially the same each time.*

## 0. Inputs I read (from `environment/`)

- `constitution/phase-5-…` **Item 3 (Human Position First)** — the **positions** (roles).
- `constitution/phase-3-…` and `phase-4-…` — the **Designer's action model** (Phase 3 = his D2
  actions; Phase 4 = his D1 actions), the source of the D1 Designer's actions.
- `constitution/phase-1-…`, `phase-2-…` — authority, attention, the principles that shape actions.
- `method.md` (§1) — the derivation discipline: **identify actions → abstract the common element →
  split passive / active → open-list → keep the D0-user throughline**.
- `rules.md`, `glossary.md` — governance and terms.

## 1. Decomposition — the children I spawn, with their sub-contracts

1. **Roles node.** Sub-contract: *"Derive the role table from Phase 5 Item 3 + the layer model
   (D2→D1→D0). For each position give: stable ID, name, relationship, a **substantial description**,
   and an **intrinsic / default** tag, each Source-cited. Deliver the role table."*
2. **Per-role action nodes** (one per role the Roles node returns). Sub-contract: *"For role R,
   derive the actions R performs from its **job function** (Phase 5) and the relevant phase items.
   For each action: stable ID, a **substantial description**, Source. For the **D1 Designer**,
   sub-split **passive / active**. Deliver R's action pieces."*

## 2. Derivation method (how each child extracts — not invents)

- **Roles:** take the positions listed in Phase 5 Item 3; add the **D2 Assistant** (the unified
  interaction point, Phase 4 Item 3). Tag **intrinsic** (ecosystem-fixed: D1 Designer, D2 Assistant,
  internal agents) vs **default** (product-side: the D0 roles, the IT Manager).
- **D1 Designer actions:** walk the method's journey — *entry → setup → input → direction → framework
  → oversee → inspect/monitor → asked → check* — lifting each action; classify **passive** (he
  *responds to* D2) vs **active** (he acts *on his own initiative*).
- **Downstream-role actions:** lift from each position's job function in Phase 5 — D0 Operator
  (run / monitor / configure / view / notify / support-request), D0 Technical Manager (install /
  maintain / diagnose / patch / escalate), D1 Technical Manager (deploy / upgrade / rollback /
  records), D1 Programmer (implement / test / fix).

## 3. Aggregate

Merge all per-role pieces into one table, **grouped by role**, stable IDs, deduplicated.

## 4. Acceptance / stop condition (coverage — this is what makes it terminate & reproduce)

- Every action a competent re-derivation from the inputs would surface is **present** (open-list
  target — not claimed exhaustive).
- Every action and role is **Source-cited** and **substantially described**.
- IDs **stable** and **deduplicated**.
- If a gap is found, return to step 2 for the affected role; otherwise stop.

## 5. Package

Emit the three products. **Step 1:** this algorithm + the declaration (now). **Step 2:** the
role-action table with descriptions (after the work). Submission/approval is out of this test's scope.
