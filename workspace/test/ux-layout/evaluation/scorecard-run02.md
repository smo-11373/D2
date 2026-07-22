# Experience-node scorecard — run-02 (by-action) vs the v1 poles

*Blind re-derivation after the contract §1 change to **by-action** (`../output/ux-layout.md`), scored at
**pair version v1** per `rubric.md` (11 dimensions). Judge (Layer B): Claude. Prior run (pattern-indexed,
scored at v0) archived at `../work/run01-pattern-indexed/`.*

Date: 2026-07-22   ·   Pair version: **v1**   ·   Structure: **by-action**

## The structural result — by-action, driven by the contract

**Confirmed: the deliverable is now indexed by action.** 18 patterns as a shared **vocabulary** (§A), then
**one experience surface per action** (§B, 63 surfaces grouped by role), each with its own interaction spec
(position · pattern · trigger · presented · default · drill-down · attention · direction · derivable/slot),
then the attention accounting rolled up (§C). Actions that **share a pattern still get distinct surfaces** —
A-035 health-monitor vs A-047 usage/cost-monitor; A-034 operate vs A-044 results; reactive A-049 vs proactive
A-059; A-001 accept vs A-002 modify. **This came entirely from the contract change** — the surfaces are
derivations; nothing was hand-authored. The discipline worked.

## Coverage (gating) — CLEAR

**63/63 actions have their own surface**, no orphan; every surface names a position, a pattern, and its
interaction spec, with product-specific content as an explicit `‹slot›`.

## Quality at v1 — near-positive on 10 of 11 dimensions

| # | Dimension | score | note |
|---|---|---|---|
| 1 | Attention economy | near-positive | low-cost defaults throughout; 39/63 cost the Designer nothing |
| 2 | Leverage-gating | near-positive | A-057 high *by leverage*; A-018 batched + leverage-pitched; node-height scaling; active = pull |
| 3 | Human-framing | near-positive | consumer-framed, never machine dump |
| 4 | Progressive disclosure | near-positive | drill-down on every surface |
| 5 | Observability | near-positive | P6 monitoring; deviation visible; push on anomaly |
| 6 | Distinctness | near-positive | health ≠ usage/cost; operate ≠ results; reactive ≠ proactive — explicit |
| 7 | Pull/push discipline | near-positive | §C direction split; push confined to gates + operator prompts + anomaly alerts |
| 8 | Consolidation | near-positive | Clarification batched + governing-level; pattern reuse |
| **9** | **Attention legibility** *(v1)* | **near-positive** | §0 "whose attention each surface costs" + §C accounting (peak = A-057 + A-018) |
| **10** | **Surface separation** *(v1)* | **near-positive** | single interaction point; operator sees no endpoints/credentials (those are R-06's) |
| **11** | **Cross-position reuse** *(v1)* | **near-positive** | 18-pattern vocabulary reused per-position (P6, P10 scoped by position) |
| **—** | **Review Stop (v1 tightening)** | **partial** | see below |

**The D0-operator pole (v1 §C) is excellent:** simple non-technical console, plain "working / needs
attention" (not telemetry), operator-scoped controls, consumer-framed results, a context-carrying escape
hatch — matches the v1 positive closely.

## The one gap — the v1 bar discriminated

The **Review Stop tightening** (v1's specific raise) is only **partial**. The run's Review Stops (A-014,
A-057) are strong on the *general* form — low-cost "continue" default, drill-down, attention scaled to node
height — but they do **not lead with "what changed since last look + the 1–3 leverage-ranked items"** the way
the v1 positive requires; they present a full report and leave ranking to drill-down. This is exactly the
raise v1 introduced, and **v1 caught it where v0 could not.** The bar-raise did its job.

## What this means (and the disciplined next move)

- **By-action, via the contract: done.** The main objective of this run is met, cleanly.
- **The module clears the raised v1 bar nearly completely** — including the new whole-layout dimensions and
  the operator pole — with the **tightened Review Stop** as the single shortfall.
- **To close that gap, the lever is the contract, not the output.** Either (a) it is run-variance (a
  multi-run at v1 would tell), or (b) if we want it reliably, the contract's acceptance should require review
  surfaces to *lead with what-changed + leverage-ranked items* — then re-derive. We never hand-edit the surface.

## Bottom line

The by-action re-derivation **succeeded structurally** (contract-driven, 63/63 own surfaces) and **held
quality at the higher v1 bar** (near-positive on 10/11 dimensions, excellent operator pole). The lone gap —
the tightened Review Stop — is the discrimination v1 was raised to provide. Prior run:
`../work/run01-pattern-indexed/` (v0).
