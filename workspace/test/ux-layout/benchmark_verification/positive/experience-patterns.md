# Positive pole (ceiling) — good Designer experience, v0

*The **ceiling**: the experience of three canonical interaction forms done *well*, per the fundamentals.
A blind run's UX layout is scored by **proximity to this**. Deliberately modest — this is v0, meant to be
**raised** as we learn (see `../README.md`). Anchored to the inherited action aggregate
(`../../environment/action-aggregate/role-action-catalog.md`); action IDs are that catalog's.*

## Pattern 1 — Review Stop (`A-013` review a node / `A-010` confirm the D1 Constitution)

D2 (through the Assistant) brings **one screen**: a plain-language summary of what was decided, **what
changed since he last looked**, and the **1–3 items most worth his judgment** (leverage-ranked), with a
**default "Continue."** Everything is in *his* terms — no node IDs, no capability refs. Each item
**expands on request** (the "why" — which fundamentals/rules drove it — is one click, never forced). He
approves in **one action**, or drills into exactly the one thing he cares about. He is stopped here only
because it is a **Constitution-level** node (high leverage); low nodes don't interrupt him.

*Anchors: attention cost (P1 §2.3); asked-only-when-worth-it (P2 §Principle 1); human-framing + drill-down (P1 §2.4; P2 §3.2/3.4).*

## Pattern 2 — Monitoring (`A-016/017/018` monitor progress / cost / health)

A **standing, glanceable view** he can pull up anytime: **progress** (phase / where the design is),
**spend** (time + cost, cumulative & per-node), and **health** (normal by default; anomalies flagged) —
**cost and health kept distinct**, not blended. Routine status is **pull** (his initiative); D2 only
**pushes** when something *abnormal* is worth his attention. One click deeper: "which nodes cost most /
what's abnormal."

*Anchors: observability / deviation-visible (P5 Item 1; P2 §Principle 2); pull-vs-push; distinctness (cost ≠ health); attention cost.*

## Pattern 3 — Clarification Request (`A-012` answer a clarification)

D2 asks **only when it genuinely can't resolve by investigation**, and **consolidates** related questions
into **one** high-leverage decision. The ask is **framed for a decision**: the specific judgment needed,
the options, **D2's recommendation + why**, and each option's consequence — so he decides fast, and can
just **accept the recommendation** (cheap default). The investigation D2 already did is there if he wants
to check its work; context is preserved.

*Anchors: asked-only-when-worth-it + consolidation (P2 §Principle 1); decision-framing; attention cost; D2 owns the burden (P2 §Principle 3).*
