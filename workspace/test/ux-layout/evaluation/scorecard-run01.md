# Experience-node scorecard — run-01 vs the v0 poles

*First blind clean-room run of the Experience node (`../output/ux-layout.md`), scored against the
**exemplar-anchored** benchmark (`../benchmark_verification/` **pair version v0**) per `rubric.md` +
`scoring-method.md`. Judge (Layer B): Claude. Coverage from the run's explicit action→pattern map.*

Date: 2026-07-21   ·   Pair version: **v0**   ·   Generator: fresh blind sub-agent

## Coverage (gating) — CLEAR

**63/63 inherited actions mapped** to a pattern, verified against the run's explicit per-role map; every
pattern owns ≥1 action, **no orphans**. The layout distilled the 63 actions into **~22 patterns across 3
surfaces** (the Designer's experience of D2 via the Assistant; the Designer-invisible builder sandbox; the
product experienced by the downstream cast). Coverage is real, not loose (mappings are sensible —
e.g. A-004 discuss-concern → Investigation, A-019 tune-resolution → Config+Directive, A-045 notifications → P13).

## Quality — near-positive on every dimension

Scored by proximity to `positive/` and distance from `negative/`. **No dimension lands near the floor.**

| Dimension | score | note |
|---|---|---|
| Attention economy | **near-positive** | whole layout is "accept / continue / don't look"; explicit concentration map |
| Leverage-gating | **near-positive** | P1 by node height, P2 by consolidation/governing-level, active forms all pull |
| Human-framing | **near-positive** | X1 (Assistant) renders everything human-framed; never raw records by default |
| Progressive disclosure | **near-positive** | summary→detail + drill-down on every Surface-I form |
| Observability | **near-positive** | P7 (Designer) + P14 (product) make state/health/deviation visible |
| Distinctness | **near-positive** | Review Stop ≠ Clarification ≠ Report; cost ≠ health; Monitoring ≠ Diagnosis — explicit |
| Pull/push discipline | **near-positive** | "all active oversight is pull"; push confined to P1/P2/P3 + anomaly alerts |
| Consolidation | **near-positive** | P2 consolidated; one archetype reused across positions |

**The three pole-anchored patterns** (Review Stop, Monitoring, Clarification) each land **near-positive** —
Monitoring and Clarification essentially match the positive (distinct cost/health; pull-default/push-on-anomaly;
investigate-first, consolidate, decision-frame). The one **minor gap**: the run's **Review Stop** doesn't
*explicitly* promise "what changed since last look + the 1–3 leverage-ranked items" as vividly as the
positive pole (it defers that to drill-down) — a small shortfall, not a floor.

## The finding: run-01 reached the v0 ceiling — so raise the bar

This is the expected motion. **The v0 positive was deliberately modest, and a blind run cleared it** — even
*exceeded* it on several axes the pair didn't have:
- **Surface separation** (D2-experience vs product-experience vs invisible builder) — a structural insight.
- **An attention-concentration map** (33/63 actions cost the Designer *zero*; the whole budget lives in
  Surface I) — makes *total* attention legible, which is the D2 priority. The v0 positive only budgeted per-pattern.
- **Cross-position archetype reuse** (one Monitoring form → four position-shaped views; "same event, different
  position") — a consolidation insight.
- **The RU-11 hand-off note** — every pattern must get a capability downstream — anticipating the successor.

Because the run hit the ceiling, the benchmark can no longer discriminate module quality **until the bar is
raised.** That is the exemplar-anchored method working as designed.

## Recommended bar-raise → v1 positive

Author a richer **v1 positive** that folds in what run-01 taught, so the ceiling is above what a blind run
reaches by default:
1. Require the **attention-concentration map** (total budget legible, not just per-pattern).
2. Require **surface separation** + **cross-position archetype reuse** as explicit qualities.
3. **Tighten the Review Stop** to the positive's "what-changed + leverage-ranked 1–3 items" (close run-01's
   one minor gap).
4. Consider adding **dimensions**: cross-pattern *consistency*, and the **D0-operator experience** as its own
   pole (the throughline), which v0 left implicit.

Then future runs measure against v1, and the multi-run harness gives attributable deltas within it.

## Bottom line

Run-01 **clears the v0 bar comprehensively** — full coverage, near-positive quality throughout, with genuine
insight beyond the pair. The Experience node *works* blind. The actionable result is not a module change but a
**bar-raise to v1**, seeded by this run's strengths.
