# Negative pole (floor) — bad Designer/operator experience, **v1**

*Paired with positive **v1**. The failure modes to avoid — a run landing near any of these on a rubric
dimension is a strong negative signal. Sections mirror the positive's A / B / C.*

## A. The three Designer interaction forms — done badly

- **Review Stop.** Dumps the **full raw node output** — internal/technical, **no summary, no ranking, no
  "what changed"** (he reconstructs it himself); **no default**; **all-or-nothing**; stops him for
  low-leverage nodes.
- **Monitoring.** Status **buried** (he must ask) *or* **pushed** as routine interruptions; progress/cost/health
  **conflated** into one vague number or **raw logs**; **no at-a-glance health** (anomalies not visible).
- **Clarification Request.** Asks **often, for things it could resolve**, **one at a time**, **raw/open-ended**
  ("what should I do?") with no options/recommendation/consequences, and at the **wrong altitude** (many small
  questions instead of the one governing decision).

## B. Whole-layout failure modes — *new in v1*

1. **Attention unaccounted.** No budget map — attention cost is **implicit and unoptimisable**; the layout can't
   even say where the Designer's cost concentrates.
2. **Surfaces conflated.** The Designer is shown **internal node structures / services directly** (no single
   interaction point), **or** the operator is shown **technical internals** — the wrong surface for the position.
3. **Bespoke per-position.** The same event is **designed differently everywhere** (63 disjoint screens; no
   archetype reuse) — no consolidation.
4. **Inconsistent patterns.** A given form **behaves differently in different places** — the Designer must
   **relearn** the surface repeatedly.

## C. The product experience — done badly

- **D0-Operator Console.** A **technical, complex** console for a low-tech operator: raw config, credentials, and
  deployment internals exposed; **no simple default**, **no "healthy?" indicator**, **no escape hatch** — the
  operator must understand the deployment to run the product. (Violates D0-user-first + Human Position First.)
