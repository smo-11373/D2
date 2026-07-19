# Negative control (conformance floor) — the fold vs `output-example/`

> **This is a benchmark-validity control, not the current measurement.** Originally the pre-conformance
> clean-room run (run-02), it is retained here as the **conformance floor**: a structurally-clean,
> fully-traceable output that **folds a named Phase-5 position** (Design Node Builder) into another
> role. The harness must **reject** it as non-conformant. Note the mechanical Layer A *passes* it
> (exit 0) and its role-alignment silently aliases the reused id (example `R-02` and `R-07` both map to
> the output's single `R-02`) — the fold is caught only by Layer B below and the module's conformance
> gate. That is precisely why it is kept. The real measurement of the conformant module is
> `../../../output/` + `../../../evaluation/scorecard-run03-conformant.md`. See `../README.md`.

*The blind derivation behind this control: a fresh agent given only `environment/` + `input/`,
forbidden the example, scored through this harness.*

Date: 2026-07-18   Engine: fresh sub-agent (clean context)   Judge: Claude (Layer B)
Structural (Layer A): **PASS** (exit 0) · **7 roles · 50 actions** · all 7 checks green

## Headline

The clean-room run **converged strongly on the pinned core** (roles by layer, the D1 Designer's whole
passive/active action set, the D2 Assistant, the technical-manager core) but **diverged in two
systematic ways**: it (1) **folded the Design Node Builder role into the D2 Assistant** — dropping a
Phase-5-listed position — and (2) **under-elaborated the open-list tail** of `position-derived`
downstream actions (tests, rollback, notifications, escalation, standing monitoring). Result: a
composite of **~86/100**, but **gate G3 fails** (a pinned role is missing), so the verdict is
**"Close — not yet substantially the same."**

## Gates

| Gate | Check | Result |
|---|---|---|
| G1 | Integrity — IDs unique/well-formed, grouped, no retired-ID reuse | **clear** |
| G2 | Traceability — every row Source-cited (57/57), all within the `sources.md` namespace | **clear** |
| G3 | **Roles complete** — every example role present | **FAIL** — Design Node Builder (example R-02) absent (folded into the D2 Assistant) |

*Note a Layer-A role-matching artifact the judge corrected: the clean-room reused id `R-02` for
**D2 Assistant**, so the code matched example R-02 (Design Node Builder) to it **by id** and example
R-07 (D2 Assistant) to it **by name**. By meaning, D2 Assistant maps across and **Design Node Builder
is genuinely missing** — this is what trips G3.*

## Scores

| Dimension | Raw | Weight | Weighted |
|---|---|---|---|
| Role match | 7/8 example roles present by meaning; 0 unjustified extra roles | 25 | **21.9** |
| Action coverage | Σmatch **44.5 / 63 = 0.71** (see per-role table) | 35 | **24.7** |
| Traceability | 57/57 rows sourced, all in-namespace | 15 | **15.0** |
| Integrity | 4/4 checks | 10 | **10.0** |
| Substance | screen 1.00, quality ~0.98 | 15 | **14.7** |
| **COMPOSITE** | | 100 | **≈ 86** |

**Verdict: Close — NOT yet "substantially the same"** (G3 failed: a pinned role is missing).
The composite would clear the ≥85 bar, but a missing Phase-5 position is a structural miss, not
open-list slack (contract §5). Restore the Design Node Builder role (and elaborate the flagged tail)
and this run would land in the "substantially the same" band.

### Action coverage, per role

| Role | Σmatch / n | Notes |
|---|---|---|
| R-00 D2 Designer | 2.5 / 3 | audit-adoption action (ex A-061) only partially present |
| R-01 D1 Designer | 22 / 24 | strong — missing only "revise setup later" (A-017) and "tune resolution depth" (A-019) |
| R-02 Design Node Builder | 4.5 / 8 | **collapsed** — the 8-action decomposition folded into one D2-Assistant action (A-033) plus scattered pieces |
| R-03 D1 Programmer | 1 / 3 | missing "write/run tests" (A-040) and "diagnose/fix defects" (A-041) |
| R-04 D1 Technical Manager | 4 / 7 | missing D0-wrapper health monitoring (A-033), rollback (A-042), review records (A-043) |
| R-05 D0 Operator | 4 / 8 | missing notifications (A-045), handle-errors (A-046), support-request (A-048); results/usage partial |
| R-06 D0 Technical Manager | 3.5 / 7 | missing diagnose (A-049), escalate (A-051), standing health monitoring (A-059) |
| R-07 D2 Assistant | 3 / 3 | full — mapped onto the clean-room's R-02 D2 Assistant |

## Gap list (missing / partial example actions)

**Missing role (G3):** Design Node Builder — present in Phase 5 Item 3 as a distinct position; the
clean-room folded its function into the D2 Assistant (its A-033 absorbs node-building), so it has no
distinct role or action block.

**Missing actions (12 full misses):** A-017 revise-setup-later · A-019 tune-resolution-depth ·
A-060 harness-before-committing · A-040 impl-tests · A-041 fix-defects · A-033(ex) D0-health-via-wrapper ·
A-042 rollback · A-043 review-records · A-045 ack-notifications · A-046 handle-routine-errors ·
A-048 request-support · A-049 diagnose-deployment · A-051 escalate · A-059 standing-deployment-monitoring.
**Partial (subsumed/merged):** A-061 audit-adoption; A-022/023/024/025/027 (builder decomposition
collapsed into A-033); A-044/A-047 operator view; A-050 apply-fix.

*(Merges that fully cover — not penalized: the D1 Designer's setup A-012 absorbs ex A-015/A-016/A-056;
framework A-011 absorbs ex A-001/A-002/A-004; monitoring A-017 absorbs ex A-052/A-054.)*

## Extras list (clean-room actions with no example counterpart — open-list, all traceable)

`extra-justified` (traceable, plausible; **not** penalized): A-001 build-D2, A-004 approve-submissions
(R-00); A-010 enter-D1-mode-ack, A-016 receive-completion-reports, A-023 lay-down-rule,
A-025 D0-user-optimization (R-01); A-028/A-029/A-030/A-031/A-032/A-034/A-035 (D2-Assistant investigate/
escalate-leverage/report/observe/context/route/provenance); A-037/A-038/A-039 (Programmer principles/
propose-up); A-043 tech-controls (R-04). **`spurious` (untraceable): none.**

## Findings — what this run teaches about the contract

1. **Convergence is real where the contract pins hardest.** The D1 Designer's action set — the passive
   journey and the active inspection/monitoring/intervention actions — reproduced almost completely
   (22/24) from Phases 3–4 + method §1, independently, with different wording and IDs. Same for the
   D2 Assistant (3/3) and the tech-manager core. The frozen inputs genuinely drive this.

2. **Divergence #1 — role granularity is under-pinned.** The contract's role-seeding sub-contract
   ("derive the role table from Phase 5 Item 3 + the layer model") let a competent run **fold the
   Design Node Builder into the D2 Assistant**. Both are defensible readings of Phase 5, but the
   example treats them as two positions. **Recommended contract tightening:** require each Phase 5
   Item 3 position to appear as its **own distinct role** (fold/alias only with explicit justification).
   This is the highest-leverage fix — it is the sole reason G3 failed.

3. **Divergence #2 — the open-list tail is where runs vary most.** Nearly all remaining misses are
   `position-derived` downstream actions (tests, rollback, notifications, escalation, standing
   monitoring). The example elaborates them; the clean-room stopped at the near-explicit set. This is
   exactly the "which position-derived actions get elaborated" variation the contract predicts (§5) —
   but its size (≈13 actions) suggests the contract could set a **depth cue** for position-derived
   elaboration (e.g. "for each downstream position, elaborate the routine operate / monitor / configure
   / view / handle-error / escalate actions its job function implies").

4. **The harness earned its two layers.** Lexical pre-alignment scored only **41%** because the
   clean-room's wording and IDs differ heavily; the semantic pass lifted true coverage to **71%**.
   A code-only scorer would have badly under-counted. The negative-test fixture separately proved the
   harness fails dirty input, so this 86 is a real discrimination, not a rubber stamp.

## Bottom line

The current contract + output shape **drive substantial — but not yet "substantially the same" —
reproduction** on an untainted run: **86/100, one pinned role folded away, a ~13-action open-list tail
left implicit.** Two concrete, cheap contract edits (pin one-role-per-Phase-5-position; add a
position-derived depth cue) would very likely push a clean-room run over the ≥85 / G3-clear bar. That
is a directly actionable answer to the test's core question.

Raw Layer-A output: `../work/layerA-cleanroom.txt` · `../work/layerA-cleanroom.json`.
Full example→clean-room alignment worked out in this judge pass; per-role summary above.
