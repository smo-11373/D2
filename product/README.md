# D2 / product  —  D1-project skeleton

This directory is the **shippable D2**: a ready-to-copy skeleton for starting a D1 project.

**To start a D1 project, copy this entire directory** into a new working location, e.g.:

    cp -r  <official>/D2/product/   M:/AIProjects/D1-A/

You then get a conforming project with the D2 tool preinstalled in `d2/` and an empty
`ref/ design/ workspace/ product/` quad ready to fill.

Contents:
- `d2/`        — the D2 tool: engine + master template library + defaults (D2-owned)
- `ref/`       — empty; drop the predecessor V1 package here
- `design/`    — empty; the D1 authored design goes here
- `workspace/` — empty; D1 scratch/temp
- `product/`   — empty; becomes the D0

Copying freezes the D2 version — reproducible and self-contained. Upgrading a project to a
newer D2 is a deliberate re-sync, never silent drift.
