# D2 Design — Phase 3: Designer D2 Action Model

*Status: Persistent working set. This document guides later D2 design unless explicitly revised through the D2 design process.*

## Phase Purpose

Define, from the Designer's perspective, how the Designer enters, observes, and interacts with D2 before D1 design begins, and how D2 may later be audited after a completed D1 design run.

Phase 3 is Designer-oriented. It does not specify D2's internal architecture. The Designer experience drives later D2 architecture.

## Phase-Wide Designer Interaction Rule

Every Phase 3 item produces a Designer-oriented completion report. D2 may request required Designer clarification when necessary. At selected high-value review points, D2 should stop and offer the Designer an optional review opportunity before continuing.

Three interaction classes are distinguished:

- **Clarification Request** — D2 requires material Designer judgment that it cannot reasonably resolve through further investigation.
- **Review Stop** — D2 has completed a meaningful body of work and offers an optional opportunity to review or intervene; no unresolved question is necessarily present.
- **Completion Report** — D2 records and presents the result of an item. Designer response is optional unless a Clarification Request is also made.

Reporting boundaries and intervention boundaries are distinct. Every item is observable; only some items require Designer attention.

## Item 1 — Establish the Designer–D2 Operating Contract

At the beginning of a D2 design process, the Designer should be given a low-cost opportunity to review and confirm how D2 will seek Designer intervention and how the Designer intends to observe and actively intervene in the D2 process. D2 shall provide reasonable defaults so that extensive configuration is not normally required.

**Key declarations**

- D2 provides the default operating posture. The Designer is not asked to design the intervention policy; the normal action should often be to accept the defaults.
- The operating contract covers both D2-initiated Designer intervention and Designer-initiated intervention.
- Confirmation should be compact and human-oriented, such as a short checklist or selection table rather than a configuration document.
- Designer preferences guide D2 but do not silently override the Phase 1 and Phase 2 working principles. A preference for minimal intervention does not authorize unsupported material decisions.

The first meaningful D2 interaction is therefore about establishing the Designer–D2 operating relationship for the design run.

## Item 2 — Establish the Initial Design Input

D2 and the Designer shall establish the initial design input consisting of the available Predecessor D1 package and the available expression of intended D1 change. D2 shall not require the intended change to be fully specified before this item begins and should actively assist the Designer in developing a sufficiently clear initial upgrade direction when necessary.

**Key declarations**

- Establish the available Predecessor D1 package and the material D2 can study. This may include the executable system, source material, documentation, tests, environments, datasets, usage examples, and other relevant resources.
- The intended change may be supplied in any reasonably useful initial form: a formal revision document, rough notes, known problems, bug lists, user complaints, desired features, prior discussions, prototype ideas, undesirable-behavior examples, or general direction.
- D2 evaluates whether the upgrade direction is sufficiently established for governed D1 design to begin without creating excessive downstream ambiguity; completeness of a formal specification is not required.
- D2 should investigate the available package deeply and bias toward resolving material ambiguity early. Designer clarification is used when necessary after investigation.
- If substantial early discussion prevents much larger downstream Designer Attention Cost, that early discussion is desirable.
- The output is an initial upgrade direction, not a final D1 design specification. Explicit open questions may remain.

## Item 3 — Establish the Initial Design Understanding and Direction

D2 studies the Predecessor D1, the initial upgrade direction, and available reference material; resolves as much uncertainty as practical through investigation; and forms a consolidated initial understanding of the design problem together with a proposed high-level design direction.

The Designer-oriented report should normally cover:

- D2's understanding of the existing D1 system, limited to major characteristics relevant to the intended upgrade.
- D2's understanding of what should be preserved, changed, corrected, added, or reconsidered.
- Likely invariants, protected areas, or areas requiring special caution.
- Material uncertainties or contradictions that D2 could not reasonably resolve through further investigation.
- D2's recommended initial design direction.

Items previously framed as 'initial understanding' and 'initial direction' are intentionally consolidated into one normal passive-intervention round. D2 should try to converge internally before approaching the Designer. Multiple rounds are permitted when genuinely necessary.

**Default Review Stop**

> Initial design understanding and direction are documented in XXX. I have stopped here to give you an opportunity to review. Review now, or continue?

This Review Stop is separate from a Clarification Request. It is a courtesy and control boundary for Designer-initiated intervention, not an assertion that D2 has unresolved questions.

## Item 4 — Enter D1 Design Mode

D2 notifies the Designer that the initial D2 setup process is complete and that D2 is entering D1 design mode.

The normal interaction may be as simple as:

> Initial D2 setup is complete. Entering D1 design mode.

No D1 Constitution, phase sequence, Design Tree structure, node architecture, or D1 governance mechanics are specified here. Those questions belong to D1 design.

## Item 5 — Optionally Audit the D2 Design Process

After completion of the D1 design process, D2 should offer the Designer an optional D2-level audit of the completed design process to evaluate process cost, time consumption, Designer Attention Cost, and potential D2 improvement points.

The distinction is:

- D1 review asks whether the D1 design is good.
- D2 audit asks whether D2 designed D1 well.

Candidate audit subjects include:

- Total elapsed time and major time-consuming areas.
- Designer Attention Cost, including the number, timing, and burden of interventions.
- Clarification rounds, repeated questions, and late discoveries that could have been resolved earlier.
- Unnecessary investigation, repeated deferral, expensive redesign, or reversal points.
- Other meaningful process costs and abnormal resource consumption.
- Candidate improvements to D2 principles, defaults, process, or operating contract.

The audit may identify and propose D2 improvements, but it must not silently modify the persistent D2 working sets. Proposed changes require explicit D2 revision and Designer review.

## Phase 3 Summary

- Item 1 — Establish the Designer–D2 Operating Contract
- Item 2 — Establish the Initial Design Input
- Item 3 — Establish the Initial Design Understanding and Direction
- Item 4 — Enter D1 Design Mode
- Item 5 — Optionally Audit the D2 Design Process
