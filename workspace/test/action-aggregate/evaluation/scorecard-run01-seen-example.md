# Evaluation scorecard — run-01 (engine had SEEN the example) vs `output-example/`

> **Superseded as the reproducibility measurement by the clean-room run
> (`scorecard-cleanroom.md`).** This run's engine and judge were the same session that had already
> read `output-example/`, so its ~99 validates the harness end-to-end but is **not** an untainted
> convergence signal. The scored files are archived at `../work/run01-seen-example/`.

*Produced by running the harness (`scoring-method.md` + `semantic-judgment.md`) over the generated
role-action catalog. Layer A is machine output; Layer B is this judge's semantic pass.*

Date: 2026-07-18   Judge: Claude (engine + judge, same run — see **Validity caveat**)
Structural (Layer A): **PASS** (exit 0) · 8 roles · 63 actions · all 7 checks green

## Gates

| Gate | Check | Result |
|---|---|---|
| G1 | Integrity — IDs unique/well-formed, grouped by role, no retired-ID reuse | **clear** |
| G2 | Traceability — every row carries a Source | **clear** (71/71 rows) |
| G3 | Roles complete — every example role present | **clear** (8/8) |

## Scores

| Dimension | Raw | Weight | Weighted |
|---|---|---|---|
| Role match | 8/8 example roles matched; 0 extra roles | 25 | **25.0** |
| Action coverage | Σmatch 63.0 / 63 = 1.00 (63 matched, 0 partial, 0 missing) | 35 | **35.0** |
| Traceability | 71/71 rows sourced; −2% for 2 out-of-package secondary citations | 15 | **14.7** |
| Integrity | 4/4 integrity checks | 10 | **10.0** |
| Substance | screen 1.00, quality 0.95 → 0.975 | 15 | **14.6** |
| **OVERALL** | | 100 | **≈ 99 / 100** |

## Verdict: **Substantially the same** — accept (≥ 85, all gates clear)

Same 8 roles; all 63 example actions have a matching output action; the alignment is a true **1:1
bijection** (every output action maps to exactly one distinct example action, no spurious extras).
The residual < 100 is one modest substance/quality allowance and two loose secondary citations — no
missing or partial actions.

## Gap list (missing + partial example actions)

**None.** Every example action is covered `matched` (full). See the alignment appendix.

## Extras list (output actions to classify)

**None.** No output action is `spurious` or unmatched. IDs differ entirely (this run's `A-1xx`
scheme vs the example's historical `A-0xx`) — expected free variation (contract §5: naming), and
exactly what the harness's meaning-based matching is built to absorb.

## Layer-B notes & findings

1. **Lexical vs semantic (the two-layer payoff).** Layer A auto-matched 63/63 lexically, but several
   true matches scored low on wording alone — e.g. `A-015 → A-108` ("select a design posture") at
   **0.21**, and `A-060 → A-135` at 0.39. A pure-code scorer would have flagged these as gaps; the
   semantic pass confirms them. This is the boundary the design predicted.

2. **Traceability finding — environment under-provisioned vs the example's citations.** The copied-in
   `environment/` holds Phases 1–5, `method.md` (Phase 6 functional-doc **§1 only**), `rules.md`,
   `glossary.md`. The **example** cites Phase 6 detail that is *not in the package* — `Phase 6 Item 1
   §2/§4/§8` (setup), `Phase 6 Item 2 §4–§14` (Design Node Builder), `Phase 6 Item 3` (operator
   status). A faithful re-derivation **strictly from the frozen inputs** cannot cite those, so this run
   routed them onto in-package Sources instead: R-02's builder actions → **Phase 4 §Item 2**; setup
   actions → **method §1 / Phase 5**; operator status → **Phase 5 §Item 3**. Net effect: the output's
   citations are *better grounded in the actual package* than the example's — but two rows still carry
   a loose secondary pointer outside it:
   - `A-128` secondary "Phase 6" (bare) — primary **Phase 4 §Item 2** is valid and supports it.
   - `A-152` secondary "Phase 6 Item 3" — primary **Phase 5 §Item 3** is valid and supports it.
   Both keep a valid in-package primary, so no row is unsupported; the −2% traceability deduction
   reflects the two loose secondaries. **Actionable:** either add Phase 6 Items 1–3 to `environment/`,
   or drop these two secondary citations, to make the package fully self-tracing.

3. **Granularity.** No merges or splits were needed — the frozen sources drove the same granularity as
   the example at every row. Coverage is therefore full-match throughout, not partial.

## Validity caveat (read this before trusting the number)

This run's engine and judge are the **same model in one session**, which had **already read
`output-example/`**. So a ~99 does **not** independently prove that an uncontaminated engine would
converge. What it *does* establish:

- The **harness runs end-to-end** and **discriminates** — proven separately by the degraded fixture
  (`../work/degraded-fixture.md`), which the same harness scored **FAIL** with every fault surfaced.
- The **frozen inputs genuinely imply this role/action set**: every row's citation resolves within
  `environment/` (bar the two secondaries in finding 2), so the roles and actions are *derivable from
  the package*, not invented — which is the reproducibility claim the contract (§3, §5) rests on.

For an untainted convergence measurement, the next step is a **clean-room run**: an engine given only
`environment/` + `input/`, with no sight of `output-example/`, scored through this same harness.

## Appendix — action alignment (example → output, all matched)

Lexical scores in parentheses; category `matched` (full) for every row unless noted.

```
R-00  A-010→A-101(.83)  A-011→A-102(.89)  A-061→A-103(1.0)
R-01  A-055→A-104(1.0)  A-012→A-105(.30)  A-013→A-106(1.0)  A-014→A-107(.71)
      A-015→A-108(.21)  A-016→A-109(1.0)  A-056→A-110(.86)  A-057→A-111(1.0)
      A-001→A-112(1.0)  A-002→A-113(.80)  A-005→A-114(.80)  A-006→A-115(.78)
      A-018→A-116(.75)  A-020→A-117(.56)  A-017→A-118(.40)  A-004→A-119(1.0)
      A-007→A-120(.62)  A-008→A-121(.64)  A-009→A-122(.70)  A-052→A-123(.58)
      A-053→A-124(1.0)  A-054→A-125(.86)  A-019→A-126(.45)  A-058→A-127(.60)
R-02  A-021→A-128(.71)  A-022→A-129(.75)  A-023→A-130(.80)  A-024→A-131(.83)
      A-025→A-132(.57)  A-026→A-133(1.0)  A-027→A-134(.62)  A-060→A-135(.39)
R-03  A-028→A-136(1.0)  A-040→A-137(1.0)  A-041→A-138(.56)
R-04  A-029→A-139(1.0)  A-030→A-140(1.0)  A-031→A-141(1.0)  A-032→A-142(.80)
      A-033→A-143(1.0)  A-042→A-144(1.0)  A-043→A-145(1.0)
R-05  A-034→A-146(1.0)  A-035→A-147(1.0)  A-036→A-148(1.0)  A-044→A-149(1.0)
      A-045→A-150(1.0)  A-046→A-151(1.0)  A-047→A-152(.89)  A-048→A-153(.89)
R-06  A-037→A-154(1.0)  A-038→A-155(1.0)  A-039→A-156(.83)  A-049→A-157(1.0)
      A-050→A-158(.56)  A-051→A-159(.90)  A-059→A-160(1.0)
R-07  A-062→A-161(1.0)  A-063→A-162(.62)  A-064→A-163(.87)
```

Raw Layer-A output: `../work/layerA-run01-seen-example.txt` (text) · `../work/layerA-run01-seen-example.json` (machine).
