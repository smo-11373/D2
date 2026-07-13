# Open Questions

*Living. Unresolved design questions awaiting resolution, each with enough context to pick up later.*

### D2-internal working-agent taxonomy

*(opened 2026-07-13)* — D2 performs the design work through **internal agents**. **R-02 Design Node Builder** is only *one kind*; there will likely be others (e.g. a standard-enforcing agent, an integration agent) alongside **R-03 D1 Programmer**. Unresolved: **how many agents, how many types, and how (if at all) the Designer specifies them.** Deliberately left open at this stage rather than fixing a taxonomy prematurely (*Top-to-Bottom*). These are D2's own design-time labor, not positions the Designer configures. Context: `../phase-6/functional/d2-functionality-for-the-d1-designer.md` §2.

---

### Resolved

- **Action overlap: A-003 vs A-008** *(resolved 2026-07-12, coverage/dedup pass)* — genuine duplicate. **A-003 (Request investigation) merged into A-008**, which now reads "request D2 critically examine a matter or suspected problem and recommend action." A-003 retired; id not reused.

- **A-012 vs A-016** *(resolved 2026-07-12, coverage/dedup pass)* — *not* duplicates. A-012 confirms the **operating-contract terms** (one item within the setup package); A-016 reviews the **full setup package**. Boundary recorded in both rows.

- **Capability boundary clarifications** *(2026-07-12, coverage/dedup pass)* — C-14 (D2-initiated) vs C-20 (Designer-initiated); C-01 posture vs C-22 tuning knob; C-05 setup-item authority vs C-17 design-result authority; C-23 establishes the contract that C-02 carries. A-004 remapped C-14 → C-20.

- **Designer role layering** *(resolved 2026-07-12)* — **D2 Designer** (R-00) builds D2; **D1 Designer** (R-01) is D2's primary & only user and builds the D1 product (= Phase 1's "Designer"). Captured in glossary.

- **D0 User** *(resolved 2026-07-12)* — folded into **D0 Operator** (R-05). Reopen if a distinct D0 end-user emerges.

- **D1 / D0 product boundary** *(resolved 2026-07-12)* — **D0** is the core distributable; **D1** is a thin wrapper (monitoring, upgrade smoke-tests, upgrade records — "half a level above D0"). Captured in glossary.
