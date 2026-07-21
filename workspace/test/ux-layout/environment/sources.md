# Source namespace — what a derivation may cite (traceability contract)

*Fixes the "environment under-provisioned" finding (`../evaluation/scorecard.md` §2). Defines the
**authoritative, in-package Sources** a derivation may cite so the package is **fully self-tracing**,
and maps the stray `Phase 6 Item 1/2/3` provenance references (which appear in the reference catalog
but are **not** in this package) onto their in-package basis. Nothing here supplies new derivation
content — it pins the namespace.*

## Why this exists

`input/contract.md` §2 declares the derivation source-of-truth as **the constitution (Phases 1–5) +
the method (functional doc §1) + the rules (`RU-*`)**. Everything in the role-action table must trace
to that set. Two kinds of citation broke self-tracing:

1. **`Phase 6 Item 1/2/3` references** — the reference catalog cites Phase 6 setup / node-building /
   planning detail that lives in the fuller D2 project and was **not copied into this package**.
2. **`Designer <date>` references** — historical "Designer-stated" provenance stamps, not documents.

Neither is a derivation input here. This file resolves both **without** bundling the Phase 6 detail —
deliberately, because bundling e.g. Phase 6 Item 2 would pre-enumerate the Design Node Builder's
actions and let the node **transcribe instead of derive**, defeating the test. The node must derive
those actions from the frozen constitution (chiefly Phase 4 Item 2), as the algorithm requires.

## The authoritative Source namespace (cite only these)

A row's `Source` must resolve to one of:

| Namespace | Form | In-package file |
|---|---|---|
| Constitution | `Phase 1…5 §<Item/section>` | `constitution/phase-1…5-*.md` |
| Completions | `completions.md C-<id>` (Designer-originated; govern alongside the baseline) | `constitution/completions.md` |
| Method | `method §1` (functional doc §1) | `method.md` |
| Rules | `RU-01 … RU-11` | `rules.md` |
| Glossary | `glossary \`<term-slug>\`` | `glossary.md` |
| Framework | `design-tree` · `design-node-algorithm` | `framework/*.md` |

`position-derived` remains a valid tag for an action elaborated from a role's Phase 5 Item 3 job
function (it still names Phase 5 Item 3 as the anchoring Source).

## Provenance map — resolve out-of-package references to in-package Sources

References below may appear in the reference catalog; a **clean derivation cites the in-package basis
on the right**, not the Phase 6 pointer.

| Out-of-package reference | Covers | In-package basis to cite instead |
|---|---|---|
| `Phase 6 Item 1` (§2/§4/§8) | setup: design posture, setup configuration package, later governed revision | `method §1` (setup = roles table + posture) + `Phase 3 §Item 1–3` (operating contract, initial input, understanding) + `Phase 5 §Item 2` (governed revision) |
| `Phase 6 Item 2` (§4–§14) | Design Node building: investigate, develop candidates, produce spec, internal eval, submit, clarification, spawning | `Phase 4 §Item 2` (Build the Current Design Node) + `Phase 2 §P4` (verification/harness) + `RU-02/RU-04/RU-05/RU-10` |
| `Phase 6 Item 3` | operator status / usage / planning ("half a level above") | `Phase 5 §Item 3` (position-oriented monitoring & config) + `glossary \`half-level\`` |
| Phase 6 governing hierarchy | Role → Action → Capability → Architecture → Implementation | `method §1` (states the layering) + `framework/design-tree.md` |
| `Designer <YYYY-MM-DD>` | a Designer-stated action/decision in the fuller project | cite the frozen doc that grounds it (e.g. `glossary \`d1\`` for deploy-just-D0; `Phase 5 §Item 3` for D0 support) |

## Effect

After this fix, every legal citation resolves inside `environment/`, and the harness's traceability
dimension (`../evaluation/scoring-method.md`) can be checked end-to-end against the package alone —
no external document required. The clean-room run cites only the namespace above.
