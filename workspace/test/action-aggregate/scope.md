# Scope & deliberately-open questions — this test

*What this test fixes now, and what it deliberately leaves open. The contract form is **fluid** — not
fixed at this point; expect it to change down the road.*

## In focus now (the substance we are pinning down)

- The **shape of the output** — what the deliverable looks like (`output-example/`).
- The **shape of the input contract, in narrative terms** (`input/contract.md`).

Everything below is deliberately deferred.

## Deliberately not addressed (open)

1. **How the contract is specified / generated.** Conceptually the contract **comes from the
   fundamentals** (the parent derives it — see `environment/framework/design-node-algorithm.md`).
   We do **not** exercise that generation here. First we want to learn whether the **current shape**
   of the contract can produce the desired outcome at all; contract *generation* comes after.

2. **Why this node — and why first.** We isolate the **action aggregate** node on the assumption that
   **figuring out the user actions is the first thing to do, in any layer (D2 / D1 / D0), and
   especially D1** — before capabilities, architecture, implementation. That ordering is *assumed*
   here, not derived; the isolation reflects the assumption.

3. **The algorithm and the "declaration."** *Resolved (first cut):* they are **not inputs — they are
   output products** of the contract, alongside the table (see `input/contract.md` §1 and the three
   files in `output-example/`). The node *produces* the algorithm and the declaration; `input/` holds
   only the contract. *("Declaration" meaning is a first cut, to confirm.)*

4. **Submission — two-step structure defined, not exercised.** Submission is **two steps** (§6):
   Step 1 submits the **algorithm + declaration** for **activation** (children spawn only after
   approval); Step 2 submits the **result** — the table with substantial descriptions of each action
   and each role. On approval the node cascades into the successor branch (capability → architecture →
   implementation). This test **defines** the structure but does **not exercise** submission/approval/
   cascade — it isolates the contract and the shape of the output.

## Status of the contract form

**Fluid — not fixed.** The form of the contract is expected to change; nothing about it is frozen at
this point. This test exists to probe whether the *current* output-shape + contract-shape can drive
the desired result — not to lock the contract down.

## Source "floor" — checked, and there is none (2026-07-19, after run-08)

The residual coverage gap was suspected to be an **un-derivable floor**: example rows sourced to Phase 6
material not copied into this sandbox. **Checked — it is not a floor.** All **12** example rows that cite
Phase 6 have an **in-package basis** (per `environment/sources.md`'s provenance map) and are derivable
from the frozen Phases 1–5:

- **Node-building** (`A-021`–`A-026`) → Phase 4 §Item 2 + Phase 2 §P4 + `RU-02/03/04` *(run-08 derived these).*
- **Setup** (`A-015` posture, `A-016` setup package, `A-017` revise-later, `A-056` roles-table) → `method §1`
  (setup = roles table + posture) + Phase 3 §Item 1–3 + **Phase 5 §Item 2** (governed revision).
- **Clarification** (`A-018`) → Phase 3/4. **Operator usage/status** (`A-047`) → Phase 5 §Item 3 + glossary `half-level`.

**Conclusion:** the achievable target is the **full 63** — nothing is out-of-package. The remaining misses
(e.g. `revise-setup-later`, whose in-package basis is Phase 5 §Item 2) are **derivable-but-hard** — subtle
in-package connections a run makes inconsistently — **not** a package limit.

Two options **rejected**:
- *Copy Phase 6 in* — it would let the node **transcribe** the node-building/setup actions instead of
  deriving them, defeating the test's core purpose (`sources.md` §"Why this exists").
- *Accept a package limit* — there is no limit; the content is derivable.

So the last coverage gains are a **derivation-difficulty / run-variance** matter, best addressed by the
**multi-run harness** (average N blind runs so the subtle-but-derivable items surface across runs), not by
any Source change. (This corrects the run-08 scorecard's over-strong "un-derivable floor" wording.)
