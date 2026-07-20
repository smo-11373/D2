# Multi-run scorecard — lifecycle+intention version, N=3 blind runs

*First use of the multi-run harness (`multirun.py` + `multi-run-method.md`). Three fresh blind
clean-room runs of the **current** module version (conformance + completeness + depth + harness bias +
calibrated distinctness + D2-Assistant completion + lifecycle/intention lenses), aggregated against the
fixed 63-action / 8-role example. Runs: `../work/multirun-lifecycle/{a,b,c}/` (a = run-08).*

Date: 2026-07-20

## Mechanical aggregate (multirun.py, Layer A)

| Run | roles | actions | structural | lexical cov |
|---|---|---|---|---|
| a (=run-08) | 8 | 73 | PASS | 0.68 |
| b | 8 | 82 | PASS | 0.70 |
| c | 8 | 69 | PASS | 0.71 |

- **Roles: 8/8 in every run · structural PASS 100%.** The version *reliably* reaches full role coverage.
- **Lexical coverage: mean 0.70, spread (max−min) 0.03** — a **tight noise band** on coverage.
- **UNION 0.82 · INTERSECTION 0.59** (lexical).

## What the aggregate shows that no single run could

1. **The version is consistent where it matters.** Coverage varies only **0.03** lexically and roles are
   **8/8 every run** — run-08's result was *not* a lucky draw. The big-looking variance is in **action
   count (69–82) and the D1-Designer split (20–24)** — i.e. **granularity**, not *which* example actions
   are hit. The noise is in how finely a run elaborates, not in what it covers.
2. **UNION ≫ single-run — aggregation recovers coverage.** Any one run reaches ~0.70 lexically; across
   three, the **union reaches 0.82**. Different runs surface different subtle-but-derivable items — the
   exact effect the harness was built to capture. The *semantic* union is higher still (several
   lexical-never-matched rows — `A-032` deploy, `A-044` view-results, `A-046` handle-errors — are in fact
   produced via the lifecycle/depth-frame lenses; they miss only on wording).
3. **The attributability tool now exists.** With a quantified band (~0.03 lexical; ≈1–2 composite
   points), a future version's delta is **real only if it exceeds the band** — no more reading a +1 as a
   win. This retroactively confirms the earlier reads: run-05's +4 was signal; run-04's +1 was noise.

## Semantic composite (Layer-B estimate, per the method)

Judging Σmatch per run (a fully, b/c from their catalogs): recall ≈ 0.87 / ≈0.88 / ≈0.83 → composites
**≈ 94 / ≈93 / ≈92**, **mean ≈ 93 ± ~1**. So the version reliably scores **~92–94** — run-08's ≈94 sits
at the top of a narrow band, not above it.

## The residual, seen across runs

The lexically-never-matched set is 11, but semantic judgment clears most (deploy / view / handle-errors
are present). The **genuinely-hard residual** narrows to a handful — chiefly the **setup family**
(`A-015` posture, `A-016` setup-configuration-package, `A-056` roles-table review) and `A-004`
discuss-concern — all **derivable-but-hard** (in-package basis: `method §1` / Phase 5 §Item 2 / Phase 4;
see `../scope.md` §"Source floor"), not out-of-package. Across N runs the **union already covers most of
them** — which is the point: the ceiling is reached *cumulatively* even when a single run misses.

## Bottom line

The current version is **stable (8/8 roles, coverage spread 0.03), scores ~93 mean, and reaches a ~0.82+
derivable union** across three blind runs. The multi-run harness now makes every future module change
**attributable** against a measured noise band, and its **union** metric closes the subtle-but-derivable
tail that confounded single runs — the last methodological gap is filled.
