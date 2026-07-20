# Algorithm — deriving the Role–Action Aggregate table

*Product 2 of 3 (contract §1; Step-1 activation product). The procedure this node runs to derive
Product 1 so that a competent re-run over the same frozen inputs reproduces the **same roles and
substantially the same actions**. Substance is **derived** from the frozen inputs
(constitution Phases 1–5 + their completions + method §1 + rules `RU-*`), nothing invented; every
row carries a `Source` that is its derivation trace.*

## Inputs (read-only source of truth)

- The **constitution**, Phases 1–5 (`constitution/phase-1…5-*.md`) — positions in **Phase 5 §Item 3**;
  the passive/active Designer journey in **Phases 3–4**; the philosophies (Harness First, Human
  Position First, Quality over Expediency, Modularization) in **Phase 5**.
- The **completions** (`constitution/completions.md`) — Designer-originated positions/requirements
  that **govern alongside** the frozen baseline (cited `completions.md C-<id>`).
- The **method** — functional doc §1 (`method.md`): identify actions → abstract the common element →
  keep it an open list; split passive/active; hold the D0-user throughline.
- The **rules** — `RU-01…RU-11` (`rules.md`); the **framework** (`framework/*.md`); the **glossary**.
- The **Source namespace** (`sources.md`) — the only citations a row may use.

## Procedure

**Step 1 — Seek roles.** Extract the **named positions** from Phase 5 §Item 3 (D1 Designer, Design
Node Builder, D1 Programmer, D1 Technical Manager, D0 Technical Manager, D0 Operator), **plus any
position a completion names** (the **D2 Assistant**, `completions.md C-2026-07-19-1`), **plus** the
layer-model roles the glossary fixes (the **D2 Designer**, `R-00`, meta/builder). Order by layer
(`R-00…`). Tag each **intrinsic** (fixed) or **default** (D1-Designer-changeable). Cite each role's
Source. All named positions are **gating for conformance** — none may be dropped, collapsed, or
recast.

**Step 2 — Actions per role.**
- **D1 Designer (R-01):** walk the full journey and **sub-split passive `[P]` / active `[A]`**.
  Passive = the review/stop and clarification points of Phases 3–4 (entry → operating contract →
  initial input → understanding/direction → enter-design → operating framework → Constitution
  confirmation → clarification responses → node Review Stops). Active = inspect, investigate,
  monitor progress/cost, monitor health, directives, propose-change, D0-user optimization,
  Designer-level product controls, D2-process audit (Phase 4 §Item 3; Phase 2 §Principle 2; RU-06).
- **Each downstream operational role** (Programmer, D1/D0 Technical Managers, D0 Operator): apply
  the **position-derived depth frame** — elaborate the facets the role's Phase 5 §Item 3 job
  function *genuinely implies*: **operate/perform · monitor · configure/control · view/report ·
  handle routine errors · escalate**; for maintenance/support roles also walk **diagnose → apply-fix
  → recover-from-a-failed-change → record-the-change**. The frame is a completeness prompt, not a
  checklist — elaborate only genuinely-implied facets; never invent a row to fill one.
- **Internal/meta roles** (D2 Designer, Design Node Builder, D2 Assistant): **not** depth-framed;
  derive actions from the stated job function (glossary; Phase 4 §Item 2) and, for a completion-named
  position, from the **responsibility the completion states**.
- **Every role — harness-richness bias** (Harness First, Phase 5 §Item 1; Verification Before
  Realization, Phase 2): preferentially surface what the role **tests / monitors / detects (hidden
  failures) / makes visible**. Bias ≠ padding — do not manufacture a harness the fundamentals don't
  warrant, nor split one responsibility into mechanical steps.

**Step 3 — Aggregate.** Merge the per-role action sets into one table, **grouped by role**, stable
IDs `A-001…` (`A-003` retired/skipped), each row Source-cited.

**Step 4 — Acceptance self-check** (gating order):
1. **Conformance (first, gating).** Contradict **no** governing statement of the fundamentals or
   their completions — no principle, named enumeration (incl. completion-named positions), method
   discipline, or rule. Traceability ≠ conformance: a cited row can still contradict an enumeration.
   On a conflict: **revise to conform** or **propose-up-and-halt** (`RU-04`/`RU-05`) — never
   emit-and-flag (`conformance.md`).
2. **Completeness (active).** Derive the *should-exist* set from the fundamentals + completions and
   check each is present — **gating** for named/specified pieces (the position list, the
   position-oriented control lists, the passive/active journey, the depth-frame facets), strong bias
   for derivable ones. **Work-conservation:** every derivable action must be owned by some concrete
   role; a folded/omitted candidate position's actions must redistribute or the position stays — no
   orphaned work.
3. **Distinctness guard (Quality over Expediency).** Each row is a **distinct responsibility**, not a
   mechanical step or a restatement of a rule the node merely operates under. **Merge only** mechanics
   and rule-restatements; **preserve any distinction the fundamentals themselves make** (distinct
   data/concern/Source — e.g. monitor **cost** vs monitor **health**, Phase 4 §Item 3). Completeness =
   distinct responsibilities covered, not row count.
4. **Traceability & integrity.** Every row cites an in-namespace `Source` (`sources.md`); IDs stable,
   grouped, deduplicated; the aggregate is ready to drive the capability layer (`RU-11`).

Iterate Step 4 until it passes; only then emit the three products. A known deviation is **never**
emitted with a flag — it is resolved or a propose-up-and-halt is recorded in `declaration.md`.

## Why it reproduces

The inputs are **frozen**, the method is fixed, and acceptance is **coverage + conformance against
those inputs**. Two competent runs land on the **same roles** and substantially the **same actions**;
the residual variation (the deliberate "not identical") is naming, granularity, which position-derived
actions get elaborated, and the open-list tail (contract §5).
