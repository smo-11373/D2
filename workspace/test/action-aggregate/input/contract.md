# Contract — the Action Aggregate node

*The contract its parent (Fundamentals / the D2 Designer) issues. Written to be **generative**: an
automated engine running the **design-node algorithm** (to be developed) over this contract should
spawn the Roles node and the per-role action nodes and re-derive a role-action table that is
**substantially the same** — not identical, but the same roles and substantially the same actions.
What makes that possible is that the contract **pins the inputs and the acceptance test**; the
algorithm supplies the general decomposition.*

## 1. Deliverable (binding) — an output package of three products

The node produces an **output package** with three products, all products of this contract. They
are delivered across a **two-step submission** (§6):

1. **The role-action aggregate table — with substantial descriptions.** The actions each recognized
   role performs, **merged**, **grouped by role**, stable IDs, each row **Source**-cited — and each
   **action carrying a substantial description** (what it *is*), each **role a substantial
   description**. Target = the **common, anticipable** set (open-list). *(Step 2 — the result.)*
2. **The algorithm** — the procedure to derive the table (seek roles → per-role actions → aggregate →
   coverage-check), written so the table can be **re-derived / reproduced**. *(Step 1 — activation.)*
3. **The declaration** — the node's **manifest / plan / downstream interface**: its identity, what it
   will deliver, and the interface it offers the capability branch. *(Step 1 — activation. First-cut
   meaning of "declaration" — to confirm.)*

## 2. Derivation inputs — the source of truth (binding, read-only)

Roles and actions are **derived from these**, not invented; every row cites where it came from.

- **The constitution — Phases 1–5** (frozen). The positions live in **Phase 5 Item 3 (Human Position
  First)**; the actions are implied by each position's job function and the phase items.
- **The method — functional doc §1.** The translation discipline: identify the Designer's actions,
  **abstract the common element**, split **passive / active**, keep the **D0-user throughline**, treat
  the list as **open**.
- **The rules — `RU-01…RU-11`.** Design-tree governance (author owns its table; aggregate at the
  boundary; propose-up; coverage; …).

## 3. Acceptance criteria (binding — this is what makes it reproducible)

- **Coverage.** Every action a competent re-derivation from the inputs would surface is present
  (open-list target).
- **Traceability.** Every row cites a `Source` in the inputs. *(This is why we record Sources: the
  Source **is** the derivation trace that lets the table be reproduced.)*
- **Integrity.** Stable IDs, grouped by role, deduplicated; the action↔capability map resolves.
- **Substantial reproducibility.** Contract + same inputs + the design-node algorithm ⇒ a
  **substantially matching** table: the **same roles**, and substantially the **same actions** modulo
  naming, granularity, and open-list judgment.

## 4. What the design-node algorithm supplies (not the contract — the engine, built later)

The contract does **not** hard-code the decomposition (`RU-10` leaves internal shape to the child).
The general algorithm applies its standard pattern to this contract:

1. **Seek the roles.** Spawn a **Roles** child, sub-contract: *derive the role table from Phase 5
   Item 3 + the layer model (D2→D1→D0), each role tagged intrinsic/default, Source-cited.*
2. **Actions per role.** For each role, spawn an **action** child, sub-contract: *derive this role's
   actions from its job function and the relevant phase items, Source-cited; for the D1 Designer,
   sub-split passive / active.*
3. **Aggregate.** Merge the per-role pieces into the table; run the coverage check.
4. **Submit** with justification (`RU-02`) for the parent's approval.

## 5. Why "substantially the same," not identical

**Pinned** → convergence: the inputs are *frozen* (Phases 1–5), the method is fixed, and acceptance
is *coverage against those inputs*. Two competent runs over the same frozen source land on the same
roles and substantially the same actions. **Free** → variation: naming, granularity, which
*position-derived* actions get elaborated, and the open-list tail. That residual is the "not 100%."

## 6. Submission — two steps (structure defined; NOT exercised by this test)

Submission is **two steps**, consistent with the fundamentals — approve the **approach**, then the
**result**:

- **Step 1 — activation (before spawning children).** The node submits its **algorithm** and
  **declaration** to the parent (Fundamentals) for approval (`RU-02`). Only on acceptance is the node
  **activated**; it may *then* spawn its child nodes (roles → per-role actions) and do the work.
- **Step 2 — result.** After the work, the node submits its **result**: the role-action table **with
  substantial descriptions** — a substantial description of **each action** and of **each role**. On
  acceptance, the deliverable is final.

**Then (later, out of scope):** the node calls out its successor branch — **capability → architecture
→ implementation** — a cascade (`RU-11`).

This test **defines** the two-step structure but does **not exercise** submission, approval, or
cascade; it isolates the **contract** and the **shape of the output**.
