# Contract — the Experience (UX) node

*The contract its parent (the **Action-Aggregate node**) issues. An **instantiation of the standard contract
template** — the same shape the action-aggregate contract used (`design-node-algorithm.md` Q1:
*fill the template → attach owned data → hand down*), not authored freehand. The parent fills it with the
Experience node's specifics.*

## 1. Deliverable (binding) — indexed **by action**

A UX layout **indexed by action**: for **each** inherited action, **its own experience surface** — how that
action is experienced by its position, specified as far as the fundamentals allow. **One surface per action**
(not patterns-with-a-mapping — the *surface* is the deliverable, per action, because `RU-11` runs per action:
each action's surface drives that action's capabilities). Each surface names:

- the **position** whose experience it is;
- the **interaction pattern** it instantiates — patterns are the reusable **vocabulary** (Review Stop,
  Monitoring view, Clarification Request, Console, Report, …) so surfaces **share forms** rather than being
  bespoke, yet the surface is still specified **per action**;
- its **interaction spec**: *trigger · what is presented · low-cost default · drill-down · attention cost ·
  direction (pull/push)*.

Because the **D1/D0 project is unknown**, each surface specifies the **derivable form + qualities now** and
leaves **product-specific content as a named slot** (e.g. *what* the results are, *what* a job is). The
deliverable is thus **one surface per action** + the shared **pattern definitions** (the vocabulary) + the
**attention accounting** rolled up across the per-action surfaces. Delivered across the **two-step
submission** (§5).

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
