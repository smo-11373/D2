# Open Questions

*Living. Unresolved design questions awaiting resolution, each with enough context to pick up later.*

- **D1 / D0 product boundary.** *(High-leverage.)* Phase 5's D1 roles act on "the product" / "product code" and describe D0 as "a deployment" / "the distributable product," while the working model is "a D1 product that wraps D0 inside," with D1 and D0 each having their own operator/technical roles. Clarify what "the product" denotes at each layer and exactly where the D1/D0 boundary sits. *(Raised during role clarification.)*

- **Action overlap: A-003 vs A-008.** "Request investigation" (Phase 4 §Item 1, during framework review) and "Investigation / concern" (Phase 4 §Item 3, active intervention) may be the same underlying action expressed in two contexts. Decide whether to consolidate during the Action–Capability coverage review. *(Raised while seeding Phase 4.)*

---

### Resolved

- **Designer role layering** *(resolved 2026-07-12)* — **D2 Designer** (R-00) builds the D2 product (the current human developer); **D1 Designer** (R-01) is D2's primary & only user and builds the D1 product (= Phase 1's "Designer"). Bare "Designer" in the baseline = the D1 Designer; Design Node Builder / D1 Programmer are internal to D2. Captured in glossary (`d2-designer`, `d1-designer`, `designer`, `user`).

- **D0 User** *(resolved 2026-07-12)* — folded into **D0 Operator** (R-05); Phase 6 Item 1's "D0 users" are the D0 Operator (and D0-facing roles). Reopen if a distinct D0 end-user emerges as separate from the operator.
