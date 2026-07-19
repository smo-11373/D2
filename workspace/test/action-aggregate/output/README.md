# output — the node's produced package (clean-room run, run-02)

The Action Aggregate node's **untainted** output: derived by a fresh agent given only `../environment/`
+ `../input/`, with no sight of `../output-example/` (or `../work/`, `../evaluation/`). This is the
run that actually tests reproducibility.

- `role-action-catalog.md` — **Step-2 result**: 7 roles (`R-00…R-06`), 50 actions (`A-001…A-051`,
  `A-003` retired/skipped), grouped by role, Source-cited (in-package namespace per
  `../environment/sources.md`), each row substantially described.
- `algorithm.md` — **Step-1**: the procedure the node ran.
- `declaration.md` — **Step-1**: the node's manifest / downstream interface.

**Scored:** `../evaluation/scorecard-cleanroom.md` → composite **≈ 86/100**, but **gate G3 fails**
(the Design Node Builder role was folded into the D2 Assistant), so the verdict is **"Close — not yet
substantially the same."** Strong convergence on the pinned core (D1 Designer, D2 Assistant, tech-manager
core); divergence on one dropped role and the position-derived open-list tail. See the scorecard's
findings for two recommended contract edits.

*The earlier contaminated run (run-01, engine had seen the example, scored ≈99) is archived at
`../work/run01-seen-example/` with `../evaluation/scorecard-run01-seen-example.md`.*
