# Rubric — the dimensions the positive/negative pair calibrates

*The scoring axes for a UX layout, each **anchored to a fundamental** (so "good UX" is constitutional, not
taste). The `benchmark_verification/` positive/negative pair is the **calibration** of these axes — the
positive shows each dimension satisfied, the negative shows it failed. A run is scored per dimension by
**proximity to the positive / distance from the negative** (`scoring-method.md`).*

| # | Dimension | Positive | Negative | Fundamental |
|---|---|---|---|---|
| 1 | **Attention economy** | one glance / one-action default | wall-of-text / many actions | Designer attention cost (P1 §2.3) |
| 2 | **Leverage-gating** | surfaced only when worth it, ranked | interrupts low-leverage / pushes routine | asked-when-worth-it (P2 §Principle 1) |
| 3 | **Human-framing** | his terms, decision-framed | internal/technical, raw | human-oriented output (P1 §2.4) |
| 4 | **Progressive disclosure** | summary + opt-in drill-down | all-or-nothing | drill-down (P2 §3.2/3.4) |
| 5 | **Observability** | health/anomaly visible by design | buried | Harness First / observability (P5 Item 1; P2 §Principle 2) |
| 6 | **Distinctness** | cost vs health separate | conflated | matches the action set's own distinctions |
| 7 | **Pull/push discipline** | routine = pull; only anomalies push | pushes routine | asked-when-worth-it; attention cost |
| 8 | **Consolidation** | related asks → one decision | a stream of pings | consolidation (P2 §Principle 1) |

**Bar-raising note.** These eight are the v0 axes; raising the bar may **add** dimensions (e.g. cross-pattern
consistency, error-recovery experience, the D0-user experience) or **tighten** the positive on an existing
one. Each such change is a **versioned** bar-raise (see `../benchmark_verification/README.md`).
