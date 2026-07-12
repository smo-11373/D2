# Open Questions

*Living. Unresolved design questions awaiting resolution, each with enough context to pick up later.*

- **Action overlap: A-003 vs A-008.** "Request investigation" (Phase 4 §Item 1, during framework review) and "Investigation / concern" (Phase 4 §Item 3, active intervention) may be the same underlying action expressed in two contexts. Decide whether to consolidate during the Action–Capability coverage review. *(Raised while seeding Phase 4.)*

---

### Resolved

- **Designer role layering** *(resolved 2026-07-12)* — **D2 Designer** (R-00) builds the D2 product (the current human developer); **D1 Designer** (R-01) is D2's primary & only user and builds the D1 product (= Phase 1's "Designer"). Bare "Designer" in the baseline = the D1 Designer; Design Node Builder / D1 Programmer are internal to D2. Captured in glossary (`d2-designer`, `d1-designer`, `designer`, `user`).

- **D0 User** *(resolved 2026-07-12)* — folded into **D0 Operator** (R-05); Phase 6 Item 1's "D0 users" are the D0 Operator (and D0-facing roles). Reopen if a distinct D0 end-user emerges as separate from the operator.

- **D1 / D0 product boundary** *(resolved 2026-07-12)* — **D0** is the core distributable (deployed and run in production). **D1** is a *thin wrapper around D0* — usually thin, sometimes unnecessary, kept by default — holding "half a level above D0" operational concerns: health/performance monitoring (e.g. D0-crash detection), an upgrade smoke-test suite, and upgrade records. On handover, an IT manager may deploy only D0 to production while retaining D1 to manage/upgrade it. Captured in glossary (`d0`, `d1`, `half-level`); role descriptions updated (R-04 operates the wrapper; R-05/R-06 face D0).
