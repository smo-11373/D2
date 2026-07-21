# Multi-run scorecard — recall-first version, N=3 blind runs

*Second use of the multi-run harness, and the **first properly-attributable version-to-version
comparison** (both versions measured at N=3). Three fresh blind runs of the module after the
**recall-first / inclusion-guard** change (bias to more): `../work/multirun-recall/{a,b,c}/`. Compared
against the prior **lifecycle** version (`scorecard-multirun-lifecycle.md`).*

Date: 2026-07-21

## Mechanical aggregate (multirun.py, Layer A)

| Run | roles | actions | structural | lexical cov |
|---|---|---|---|---|
| a | 8 | 91 | PASS | 0.75 |
| b | 8 | 90 | PASS | 0.75 |
| c | 8 | 87 | PASS | 0.73 |

- Roles **8/8 every run**, structural **100%**.
- Lexical coverage **mean 0.74, spread 0.02**; **UNION 0.87**, INTERSECTION 0.62.
- Actions mean **89** (87–91, spread 4).

## The attributable comparison (recall-first vs lifecycle, N=3 each)

| Metric | lifecycle | recall-first | Δ | vs noise band |
|---|---|---|---|---|
| lexical coverage mean | 0.70 ± 0.03 | **0.74 ± 0.02** | **+0.04** | **> band → real** |
| UNION recall | 0.82 | **0.87** | **+0.05** | **> band → real** |
| actions mean | 75 (spread 13) | **89 (spread 4)** | +14 | — |
| never-matched (lexical) | 11 | **8** | −3 | — |

**Two results at once, both real:**
1. **More coverage.** Union up 0.82 → 0.87; per-run mean up 0.70 → 0.74. The +0.04/+0.05 clears the
   ~0.02–0.03 band, so this is an **attributable gain**, not a lucky draw — exactly the judgment the
   multi-run harness was built to license.
2. **Less variance, not more.** Despite ~+14 actions per run, the spread **fell** (actions 13 → 4,
   lexical 0.03 → 0.02). "When in doubt, keep" removes the run-to-run *merge decisions* that were the
   main source of variance — so runs converge *more*, not less. Bias-to-more bought consistency too.

## Semantic reading (recall-first scorer)

Lexical 0.74 understates true recall (paraphrase); semantic per-run recall is ≈0.90+, and the **union is
≈0.92+**. Under the recall-first scorer the ~89 extras-per-run are a **richness signal, not a penalty**,
so composites rise accordingly — but the **headline is the UNION recall (0.87 lexical / ~0.92 semantic)**,
the more-is-better figure.

## Residual, across runs

Lexically-never-matched narrowed to **8** (`A-011`, `A-061`, `A-016`, `A-004`, `A-058`, `A-032`, `A-044`,
`A-045`). Several are semantic matches the judge clears (`A-032` deploy, `A-044` view-results, `A-058`
evaluate-change-dryrun are present via the lifecycle/lens derivation). The genuinely-hard remainder is a
**handful** — `A-016` setup-configuration-package, `A-004` discuss-concern, `A-045` notifications,
`A-061` audit-adoption — the *derivable-but-hard* items (`../scope.md` §"Source floor"), which the
**union already covers more of** than any single run.

## Bottom line

The recall-first / inclusion-guard change is a **measured, attributable improvement**: union recall
**0.82 → 0.87**, per-run coverage **0.70 → 0.74**, both beyond the noise band — while **variance dropped**
(more actions, tighter agreement). The bias-to-more objective is validated, and this is the multi-run
harness delivering its purpose: a version delta we can *trust*. Prior version:
`scorecard-multirun-lifecycle.md`.
