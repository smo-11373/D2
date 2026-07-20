# Multi-run method — measuring a module version through N blind runs

*The measurement harness for the **real** (clean-room) runs. Distinct from
`../benchmark_verification/`, which validates the **scorer**; this makes a module version's score
**attributable** by averaging out run-to-run noise.*

## Why

Every composite so far (86 → 94) is a **single blind run**, and blind runs vary a lot on the parts the
fundamentals leave open — the D1-Designer count alone has been 21 → 15.5 → 20 → 14 → 18 → 24 across
versions. That variance **confounds attribution**: a +1 composite between two versions can be pure
noise, and a subtle-but-derivable action (e.g. `revise-setup-later`, basis Phase 5 §Item 2) is present in
one run and absent in the next. A single number can neither confirm a gain nor reveal the true ceiling.

## Method

For a module version V:

1. **Run N blind clean-room runs** — same `environment/` + `input/`, N fresh agents, each forbidden
   `output-example/` / `evaluation/` / `work/` / `benchmark_verification/`. Write each to its own dir
   (e.g. `work/multirun-V/{a,b,c}/role-action-catalog.md`).
2. **Aggregate Layer A** — `python evaluation/multirun.py output-example/role-action-catalog.md
   work/multirun-V/*/role-action-catalog.md`. It reports the count distributions, structural pass rate,
   and the coverage aggregates below.
3. **Judge Layer B once, over the aggregate** — the semantic Σmatch still needs a judge, but run it over
   the **union / never-matched** sets multirun.py surfaces, not each run separately.

## The metrics that matter (and why single-run can't give them)

| Metric | Meaning | Use |
|---|---|---|
| **mean ± spread** | central coverage and its run-to-run band | the **noise band** |
| **UNION coverage** | example actions reached by **≥1** run | the version's **derivable ceiling** — closes subtle-but-derivable items that only *some* runs get |
| **INTERSECTION** | reached by **every** run | the **stable core** the version reliably produces |
| **NEVER matched** | reached by **no** run | candidate **true hard-misses** — hand to the judge |

## The attributability rule

> A version-to-version delta is **real** only if `mean(B) − mean(A) > spread`. Report every delta **with
> the band**; a gain inside the noise is *not yet* a gain — add runs or treat it as flat.

This is why run-04's "+1" and run-05's "+4" read so differently: the first was inside the band, the second
well outside it.

## N guidance

- **N = 3** — minimum for a first spread (what we run by default).
- **N = 5+** — tighter band when a delta is close to the noise, or to trust a UNION ceiling claim.
- Lexical coverage (Layer A) **under-states** true coverage; use it for **spread, union, and never** (the
  structural/relative signals), and the Layer-B judge for the absolute Σmatch.

## Relationship to the other harnesses

- `benchmark_verification/` — validates the **scorer** (positive/negative controls). Run once per scorer
  or target change.
- `multirun.py` + this method — measures a **module version** (the output side). Run N per version you
  want an attributable number for.
- `structural_check.py` — the per-catalog Layer-A engine both reuse.
