# benchmark_verification — the harness's own validity check

*The **primary harness tool**: it validates the scorer before we trust any real measurement. A harness
is only as good as its ability to **discriminate** — to score a good answer high and a bad answer low.
This directory proves that discrimination by bracketing the shared harness with a **positive example**
(a ceiling) and **negative examples** (floors).*

## Why this exists

When the real clean-room run scores 84 or 86, that number only means something if the harness can be
*trusted* to recognize good and bad outputs. If a perfect-information output didn't score ~100, or a
broken output didn't score low, the harness would be miscalibrated and every real number would be
noise. So we validate the instrument first — with controls whose correct scores we already know.

**The harness itself is NOT here** — it lives in `../evaluation/` (`structural_check.py`,
`scoring-method.md`, `semantic-judgment.md`). That is deliberate: we must validate *the same
instrument we use on the real run*, not a fork. This directory holds only the **controls** and their
expected results.

## The controls

| Control | Input | Must score | Validates |
|---|---|---|---|
| **positive/** (ceiling) | `role-action-catalog.md` — a **cheat** run given sight of `output-example/` | **~100, all gates clear** | no false-negative at the top; the target is achievable & self-consistent; the harness runs end-to-end |
| **negative/structural/** (floor) | `degraded-fixture.md` — deliberately broken (dup ID, retired-ID reuse, missing Source, thin text, missing role, spurious extra) | **Layer A FAIL (exit 1)** | the harness rejects broken structure |
| **negative/conformance/** (floor) | `role-action-catalog.md` — the run-02 **fold** (a named position collapsed into another role) | **rejected as non-conformant** | the harness rejects a structurally-clean but non-conformant output |

### Measured results (this harness)

- **positive** → Layer A **PASS**, 8 roles, 63 actions, **100%** provisional coverage vs the example. ✔ ceiling holds.
- **negative/structural** → Layer A **FAIL** (exit 1); `action_ids`, `retired-id-reuse`, `traceability`, `substance` all trip. ✔ floor holds.
- **negative/conformance** → Layer A **PASS** (exit 0, 7 roles, 50 actions) — **and this is the point**: Layer A does **not** auto-catch the fold. Its role-alignment silently aliases the reused id (example R-02 *and* R-07 both map to the output's single R-02), so it reports **no missing role**. The fold is caught only by **Layer B** (the semantic judge) / the module's conformance gate. This is a **recorded fact about where discrimination lives**, not a defect to code around (improving the evaluation is not the goal).

## How to run the validation

```bash
# from action-aggregate/
# positive — expect PASS, ~100 coverage
python evaluation/structural_check.py benchmark_verification/positive/role-action-catalog.md \
    --compare output-example/role-action-catalog.md

# negative / structural — expect FAIL (exit 1)
python evaluation/structural_check.py benchmark_verification/negative/structural/degraded-fixture.md

# negative / conformance — Layer A PASSes (exit 0); the fold is a Layer-B / conformance-gate reject
python evaluation/structural_check.py benchmark_verification/negative/conformance/role-action-catalog.md \
    --compare output-example/role-action-catalog.md
```

## Two disciplines

1. **Standing calibration, not one-time.** The positive must keep scoring ~100 and the negatives must
   keep failing **whenever the harness or the target changes**. If an edit lets the positive drop or a
   negative pass, the edit **broke the instrument** — fix that before trusting any real score.
2. **This validates the scorer, not the target.** A wrong `output-example/` plus a matching cheat
   output would still score 100 here. Whether the target itself is **fundamentals-faithful** is a
   *separate* check ("does the example conform to the constitution?") — not part of this pos/neg pair.

## Relationship to the real measurement

This directory answers *"is the benchmark trustworthy?"* Once it passes, the **real, blind clean-room
measurement** of the module lives separately in `../output/` (the clean output) and
`../evaluation/scorecard-run03-conformant.md` (the real scorecard). Never mix the two: a contaminated
control must never be read as a real measurement.
