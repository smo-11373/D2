# D2 Project

**D2 is a meta-design system:** a system that designs the evolution of a **D1** system into a
revised successor, in service of a human **Designer** whose authority and limited attention are
the top priorities. The layers stack: **D2** designs **D1**, which produces **D0** (the
distributable product).

This repository is the **D2 layer** — the canonical design record for D2. Plain Markdown + PDFs
under git. Phone-primary; desktop stays in sync via GitHub (see *Sync*).

## The fractal layout (one template, every layer)

Every layer/project has the same four-part shape, read top-to-bottom as its lifecycle
(evidence in → decisions → work → product out):

    <layer>/
    ├── ref/          # read-first SOURCE & EVIDENCE — refer to it, don't author it here
    │                 #   frozen baselines, external material, and (for an evolving project) the predecessor
    ├── design/       # the LIVING design record authored at this layer
    ├── workspace/    # intermediate work: temp, scratch, derived evidence, verification harness
    └── product/      # the finished output of this layer

**Ownership rule:** a directory is organized by *which layer owns it*. D2-authored material
inside a D1 project lives in that project's `d2/` footprint; D1-authored material stays in the
quad. This keeps provenance (Phase 1 §4.6) legible at the filesystem level.

## This repo (the D2 layer)

    D2/
    ├── ref/          # frozen Phase 1–5 baseline (PDFs) + superseded Phase 6 + handoff note;
    │                 #   also holds 1–2 sample D1 V1 systems used as evidence while designing D2
    ├── design/       # living record: Phase 6 Role–Action & Capability catalogs, glossary, mappings, decisions
    ├── workspace/    # scratch, derived evidence, the verification harness over test D1 projects
    └── product/      # the shippable D2 — a copy-and-go D1-project skeleton (see product/README.md)

## The product is a copyable skeleton

`product/` ships as a ready-to-copy D1 project: `d2/` (the tool — engine + template library +
defaults) plus an empty `ref/ design/ workspace/ product/` quad. A D1 designer copies `product/`
into a new location and starts immediately. Copying **freezes** the D2 version (reproducible;
upgrading a project to a newer D2 is a deliberate re-sync, never silent drift).

D1/D0 projects are **separate roots** that instantiate this same template — not folders nested
inside this repo.

## Design status

- **Phases 1–5:** frozen governing baseline (in `ref/`). Do not edit; refer to them.
- **Phase 6:** ACTIVE — *Role–Action and Capability Model*. Governing hierarchy:
  Role/Position → Action → Capability → Architecture → Implementation. Phase 6 establishes
  *what D2 must be capable of*, not how it is built.
- **Phase 7:** architecture — begins only after the capability model is complete.

Living Phase 6 artifacts (in `design/`): Role–Action Catalog, Capability Catalog,
Action–Capability Mapping, Designer Query Catalog, Glossary, Working Notes, Open Questions,
Deferred Decisions.

## Working conventions

- **The repository is the canonical design record.** Keep it authoritative and current.
- **Preserve provenance** (Phase 1 §4.6): never blur Designer intent, observed predecessor
  behavior, external reference, D2-derived evidence, and inference. The layout enforces this —
  keep material in the bucket that matches its origin/ownership.
- **Top-to-Bottom:** don't scaffold lower-level structure before it is justified.

## Sync (phone ↔ desktop)

- Remote: private repo `github.com/smo-11373/D2` (origin), branch `main`. Auth via Git
  Credential Manager (already configured on desktop).
- Desktop: `git pull --rebase` at the start of a session; commit + `git push` when done.
- Phone (Claude Code web/mobile) works against the GitHub repo; git is the sync mechanism.
