# Contract — the Experience (UX) node

*The contract its parent (the **Action-Aggregate node**) issues. An **instantiation of the standard contract
template** — the same shape the action-aggregate contract used (`design-node-algorithm.md` Q1:
*fill the template → attach owned data → hand down*), not authored freehand. The parent fills it with the
Experience node's specifics.*

## 1. Deliverable (binding)

A **UX layout** for the inherited action aggregate: for **every action**, the **interaction pattern** it is
experienced through (e.g. Review Stop, Monitoring view, Clarification Request, directive, report), **per
position**, with the **attention cost** made explicit. Common experience **forms are abstracted** (method §1:
passive actions take "a few static, near-universal forms") — the layout is *patterns + the mapping of
actions onto them*, not a bespoke screen per action. Delivered across the **two-step submission** (§5).

## 2. Derivation inputs — the source of truth (binding, read-only)

- **The inherited action aggregate** — `../environment/action-aggregate/role-action-catalog.md`
  (**parent-owned, read-only**; `RU-04`/`RU-08`). This is what the layout must **cover**.
- **The fundamentals** — the constitution (Phases 1–5), method §1, rules `RU-*`, glossary, and
  `constitution/completions.md` (the D2 Assistant is the interaction surface — `C-2026-07-19-1`).
- **The module** — `framework/` (the design-node method the node runs).

## 3. Acceptance criteria (binding)

- **Coverage (gating).** Every inherited action maps to an experience pattern — no action left without an
  experience (`RU-11`-style: the layout drives the capability design, so an un-experienced action is an
  un-served need). A pattern with no owning action, or an action with no pattern, is a miss / a propose-up.
- **Conformance.** The layout contradicts no governing statement of the fundamentals.
- **Quality (exemplar-anchored).** Judged against the **rubric** (`../evaluation/rubric.md`), scored by
  **proximity to the positive pole / distance from the negative** (`../benchmark_verification/`): attention
  economy, leverage-gating, human-framing, progressive disclosure, observability, distinctness, pull/push,
  consolidation.
- **Attention accounting.** The layout makes the **total Designer attention cost** legible (the D2 priority),
  so it can be optimised — not just per-action, but across the whole surface.

## 4. What the module supplies (built later, not the contract)

The design-node method decomposes the layout freely (`RU-10`) — e.g. by interaction form, or by position —
and returns the **aggregate layout** at its boundary. Its acceptance self-check runs conformance →
coverage/quality (against the poles) → the inclusion guard.

## 5. Submission — two steps (defined; NOT exercised by this test)

Consistent with the fundamentals: **Step 1 — activation** (submit the *approach* + declaration to the parent
Action node for approval before spawning children); **Step 2 — result** (submit the UX layout for
acceptance). On acceptance the layout **cascades to the Capability node** (`RU-11`). This test **defines** the
structure but **isolates the derivation** — spawning/submission is exercised in a later test (`scope.md` §2).
