# evaluation — the Experience-node scorer

Scores a UX layout with **no answer key**: **coverage** (every inherited action → an experience pattern)
+ **quality** (proximity to the positive pole / distance from the negative), per the rubric.

- `rubric.md` — the scoring dimensions, each anchored to a fundamental; calibrated by the pos/neg pair.
- `scoring-method.md` — position-between-poles scoring; coverage + quality; layers; bar versioning.
- The poles live in `../benchmark_verification/` (positive = ceiling, negative = floor).

**Status:** Layer-B (rubric-driven judgment) is primary; Layer A (structural) deferred until the layout
format is pinned. Scores are comparable only **within a pair version**.
