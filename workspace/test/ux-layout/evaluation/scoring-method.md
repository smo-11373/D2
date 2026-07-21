# Scoring method — position between the poles (exemplar-anchored)

*How `evaluation/` scores a UX layout when there is **no answer key**. Not recall-against-a-set — instead,
**proximity to the positive pole and distance from the negative**, per the rubric.*

## What is scored

The Experience node's output: a **UX layout** that, for the inherited action aggregate
(`../environment/action-aggregate/role-action-catalog.md`), gives the **interaction pattern each action maps
to** and how it is experienced, per position, attention-budgeted.

## Two things it must satisfy

1. **Coverage (RU-11-style).** Every inherited action maps to an experience pattern — an action with **no**
   experience is a miss (the analogue of un-covered coverage; a downstream capability would have nothing to
   serve). This is the objective, checkable part.
2. **Quality (rubric, exemplar-anchored).** For each interaction pattern the layout produces, judge each
   **rubric dimension** (`rubric.md`) on a 3-point proximity scale:
   - **near-positive (1.0)** — matches the positive pole's treatment,
   - **mid (0.5)** — neither pole clearly,
   - **near-negative (0.0)** — exhibits the negative pole's failure mode.

`quality = mean over (patterns × dimensions)`. Report the **per-dimension breakdown** and the **near-floor
list** (dimensions landing at/near negative) — the number without that list is not usable.

## Layers

- **Layer B (judge), rubric-driven** is primary here — UX quality is inherently semantic, and the poles are
  the calibration that makes two judges converge.
- **Layer A (structural)** is **deferred** until the layout's *format* is pinned (it is fluid in v0). When
  pinned, a light structural check (every action mapped; every pattern well-formed) joins as the mechanical
  screen.

## Recall-first still applies

Consistent with the action-aggregate scorer: **more** (extra patterns, richer treatment) is welcome if
traceable to the fundamentals; only **missing** coverage and **near-negative** quality cost. The positive is
a **floor of quality to clear**, not a ceiling to stop at.

## Bar versioning

A score is only comparable **within a positive/negative version**. Record the pair version with every
scorecard; a bar-raise starts a new version (see `../benchmark_verification/README.md`).
