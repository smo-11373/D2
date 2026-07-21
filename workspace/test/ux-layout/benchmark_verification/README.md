# benchmark_verification — the exemplar-anchored benchmark (positive + negative UX)

*Unlike the action-aggregate test, the Experience node has **no derivable answer key** — we don't yet
know what a "correct" UX layout is. So the benchmark is **exemplar-anchored**: a **positive** pole
(good, per the fundamentals) and a **negative** pole (the failure modes), and a run is scored by
**proximity** (`../evaluation/rubric.md` + `scoring-method.md`).*

## The two modes of our benchmark method

| | derivable target (action-aggregate) | **exemplar-anchored (this test)** |
|---|---|---|
| target | `output-example` (≈ answer key) | **none** — the positive *is* the reference |
| pos/neg role | *controls* validating the scorer | **the benchmark itself** (anchors + scorer-validation) |
| scoring | recall against the derivable set | **position between the poles** |

Here the pair does **double duty**: it *anchors the rubric* (positive = each dimension satisfied,
negative = failed) **and** validates the scorer (a good layout scores high, a bad one low).

## The poles

- **`positive/`** — the ceiling: three canonical interaction forms (Review Stop, Monitoring, Clarification)
  done *well*. Deliberately **modest (v0)** — room to raise.
- **`negative/`** — the floor: the same three done *badly* (the failure modes to avoid).

## Iterate to raise the bar — with discipline

The positive is a **moving ceiling** we deliberately push up as we learn what better UX is. Two things
stay separate:
- **Raising the bar** = improving the *positive example* (target moves up) — a **versioned, recorded** event.
- **Improving the module** = making blind runs climb toward the *current* bar.

Within a bar version the pair is **fixed**, so the multi-run harness gives **attributable module-deltas**
exactly as in the action-aggregate test. A bar-raise is labelled like a module version. Never conflate the
two — else "we improved" is unfalsifiable.

Anchoring keeps the raise a **convergence, not a wander**: every rubric dimension traces to a fundamental
(attention cost, asked-when-worth-it, observability, human-framing), so the bar rises toward *better
satisfaction of the constitution*, not toward taste.
