# Handoff — Action Aggregate: evaluation harness + node output

*For the D2 developer. This note defines exactly what is being handed back, what it means, and how to
reproduce it. Everything lives inside `action-aggregate/`; paths below are relative to this folder.*

> **Structure note (updated after this handoff):** the controls were reorganized into
> `benchmark_verification/` (positive = cheat/ceiling; negative = structural + conformance floors), and
> a conformant re-run produced a new `output/` scored in `evaluation/scorecard-run03-conformant.md`.
> Paths below that point into `work/` or `evaluation/scorecard-cleanroom.md` reflect the *original*
> layout — see `benchmark_verification/README.md` for the current map.

## What was asked, and what this delivers

The node test shipped with an **empty** `output/` and `evaluation/`. This handoff fills both:

1. **An evaluation harness** that scores a generated `output/` against `output-example/` for
   "substantially the same" (contract §3).
2. **A node output** produced by running the design-node algorithm — delivered as **two runs**: an
   untainted **clean-room** run (the real measurement) and an earlier **contaminated** control.
3. **One environment fix** (`environment/sources.md`) that makes the package fully self-tracing.

## The package (what to take)

**In scope — the deliverable:**

| Path | What it is |
|---|---|
| `output/` | **Clean-room node output** (run-02): `role-action-catalog.md` (7 roles, 50 actions), `algorithm.md`, `declaration.md`, `README.md`. The legitimate result. |
| `evaluation/` | The harness: `structural_check.py` (runnable Layer A), `scoring-method.md`, `semantic-judgment.md`, `README.md`, and **two scorecards** (clean-room + the superseded control). |
| `environment/sources.md` | The fix: the Source-namespace / traceability contract (see "Environment fix" below). Referenced from `environment/README.md`. |

**Out of scope — kept as a control, not part of the handoff:** everything in `work/` (scratch),
including the contaminated run and raw Layer-A dumps. See "Two runs" for why it's kept.

*(Unchanged inputs `input/`, `output-example/`, and the rest of `environment/` are the pre-existing
test fixture; the harness reads them but this handoff did not alter them, apart from adding
`sources.md` and a pointer line in `environment/README.md`.)*

## TL;DR result

- **Clean-room run scored ≈ 86/100, verdict "Close — not yet substantially the same."** Gate **G3
  fails**: the run **folded the Design Node Builder into the D2 Assistant**, dropping a Phase-5 Item 3
  position. It also left ~13 `position-derived` downstream actions implicit.
- **Convergence is strong where the contract pins hardest** — the D1 Designer's full passive/active
  set (22/24), the D2 Assistant (3/3), the technical-manager core — reproduced independently from the
  frozen inputs, with different wording and IDs.
- **The harness earned its two layers:** lexical pre-alignment scored only 41%; the semantic pass
  lifted true coverage to 71%. A code-only scorer would have badly under-counted.

Full detail and the per-role coverage table: `evaluation/scorecard-cleanroom.md`.

## How to reproduce / verify (Python 3.7+, stdlib only)

```bash
# from action-aggregate/
# 1. structural check on the clean-room output (expect PASS, exit 0)
python evaluation/structural_check.py output/role-action-catalog.md

# 2. structural check + lexical pre-alignment vs the target
python evaluation/structural_check.py output/role-action-catalog.md \
    --compare output-example/role-action-catalog.md

# 3. machine-readable
python evaluation/structural_check.py output/role-action-catalog.md \
    --compare output-example/role-action-catalog.md --json
```

Layer A is deterministic (same input → same report). Layer B is the semantic/judge pass defined in
`evaluation/semantic-judgment.md`; the scorecards are its filled-in output. Harness self-tests: the
reference catalog passes its own checks; a deliberately-broken fixture (`work/degraded-fixture.md`)
**FAILs** with every injected fault surfaced (proves the harness makes deviation visible).

## Reading order

1. `evaluation/README.md` — the harness in one page (two-layer design, how to run).
2. `evaluation/scorecard-cleanroom.md` — **the result**: score, gates, per-role coverage, gap/extras
   lists, and findings with recommended contract edits.
3. `evaluation/scoring-method.md` + `semantic-judgment.md` — the scoring spec and judge rubric.
4. `output/role-action-catalog.md` — the node's actual re-derived table.
5. `environment/sources.md` — the traceability fix.

## Environment fix (what changed and why)

The scorecard's traceability finding was that the reference catalog cites `Phase 6 Item 1/2/3` detail
**not in the package**. Rather than paste in Phase 6 docs — which would (a) require authoring
constitution-level content and (b) hand the node its Design Node Builder actions pre-enumerated,
defeating the test — I added **`environment/sources.md`**: it pins the authoritative in-package Source
namespace (Phases 1–5, `method §1`, `RU-*`, glossary, framework) and maps each out-of-package
`Phase 6 Item N` reference onto its in-package basis. After the fix, every legal citation resolves
inside `environment/`, so the harness's traceability dimension is checkable against the package alone.
The clean-room run cited only this namespace and passed traceability 57/57.

## Two runs — and why the contaminated one is kept, separated

| | Clean-room (run-02) — **the measurement** | "Cheat" (run-01) — **control only** |
|---|---|---|
| Engine saw `output-example/`? | **No** (fresh agent, blind) | **Yes** (same session) |
| Output package | `output/` | `work/run01-seen-example/` |
| Roles / actions | 7 / 50 | 8 / 63 |
| Score / verdict | ≈86, "Close" (G3 fail) | ≈99 (**superseded** — banner in its scorecard) |
| Scorecard | `evaluation/scorecard-cleanroom.md` | `evaluation/scorecard-run01-seen-example.md` |
| Raw Layer-A dump | `work/layerA-cleanroom.{txt,json}` | `work/layerA-run01-seen-example.{txt,json}` |

The contaminated run is retained as a documented baseline (it proves the harness runs end-to-end and
that the inputs *do* imply the full set), but it is **not** an untainted convergence signal and is kept
out of `output/`. Its scorecard carries a "superseded" banner. If you don't want the control at all,
delete `work/run01-seen-example/`, `evaluation/scorecard-run01-seen-example.md`, and
`work/layerA-run01-seen-example.*`.

## Recommended next steps (from the clean-room findings)

Prioritized; the first is the fix for the missing role and the only reason G3 failed.

1. **Make the role table an input, not a re-derived output.** Per `RU-04`/`RU-08`/`RU-09`, roles are
   owned by a Roles node and passed **down** to the Role-Action node as read-only contract data — the
   action-aggregate node should not invent roles. Reclassify the role table into `contract.md` §2
   (binding inputs); the node's deliverable narrows to actions-per-role + aggregate, and it may only
   **propose** a role change upward. This eliminates the role-folding failure mode.
2. **Harden the harness against role-folding.** `structural_check.py` currently aligns roles by
   id-then-name, so a reused id can silently satisfy two example roles (it did — clean-room `R-02`
   matched both example R-02 and R-07). Change to meaning-based alignment and flag any many-to-one
   role mapping so **G3 trips automatically** instead of needing a human correction.
3. **Add a position-derived depth cue** to the per-role action sub-contract (e.g. "for each downstream
   position, elaborate the operate / monitor / configure / view / handle-error / escalate actions its
   job function implies") to recover the open-list tail.
4. **Settle the substance:** confirm the Design Node Builder is genuinely distinct from the D2
   Assistant (the glossary says a design node "may internally consist of … a builder …", so it is —
   meaning the fold is an error, not a modelling choice). If you decide otherwise, the **example**
   changes rather than the run.

---
*Prepared 2026-07-18. Harness and both runs are reproducible from the files above.*
