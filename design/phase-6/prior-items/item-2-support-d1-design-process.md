# Phase 6 — Item 2: Support the D1 Design Process

## Primary Function

D2 should provide the functional support required for the D1 Designer to move through the D1 design plan from higher-level design toward implementation-ready design.

The governing perspective is:

> The Designer should be able to advance through the D1 design plan while D2 prepares the context, harness, references, evaluation, reporting, and advancement choices required for each design step.

D2 should not require the Designer to manually reconstruct the working environment for every phase or design responsibility.

The preferred sequence is:

> Establish the provisional D1 design route → prepare the current design work → build and evaluate the design result → present Designer-relevant results and decisions → advance the design.

The exact Design Tree and Design Node architecture remains a later design question.

Phase 6 specifies the required D1 design-process functionality.

## 1. Establish the Provisional D1 Design Plan

The Setup Package should include a recommended initial D1 design plan.

The first substantive phase should normally be sufficiently defined to begin work.

Later phases should normally remain provisional.

Conceptually:

> Current phase: defined
> Likely following phases: provisional

This reflects the top-to-bottom design philosophy.

D2 should not pretend to know the complete lower-level design route before the higher-level design has been completed.

At the same time, the Designer benefits from seeing the likely shape of the design process.

A provisional plan may therefore contain:

- the current phase;
- candidate following phases;
- known major design subjects;
- likely Designer Review Stops;
- and known dependencies.

For an upgrade project, the early plan should normally include study of the Predecessor D1 before substantial new design begins.

A typical initial direction may resemble:

> Study Predecessor D1 → Establish D1 Constitution → Provisional later design phases

The exact later phases should be proposed and revised as higher-level design becomes available.

## 2. Study the Predecessor D1 and Build a Reference Roadmap

D2 should study the available Predecessor D1 package early.

The purpose is not merely to produce one general summary.

D2 should also prepare the predecessor material for efficient use throughout later D1 design.

The Predecessor D1 package may be large and may contain:

- source code;
- design documents;
- tests;
- configuration;
- monitoring material;
- usage examples;
- implementation notes;
- operating instructions;
- historical decisions;
- and other reference material.

Later design work should not normally be required to search the entire package from the beginning.

D2 should therefore establish a Predecessor Reference Roadmap.

The roadmap should connect likely D1 design subjects with relevant areas of the Predecessor D1 reference material.

For example:

> **Testing design**
> Review: V1 regression tests, representative input sets, failure examples, test-run documentation.
>
> **Monitoring design**
> Review: V1 health reports, logging implementation, alert behavior, known operational failures.
>
> **LLM interaction design**
> Review: V1 model-call wrappers, prompt material, retry handling, usage accounting.
>
> **D0 Operator design**
> Review: V1 operating instructions, routine workflows, user-facing configuration, common operator errors.

The roadmap should contain pointers to the relevant reference locations rather than reproducing the entire predecessor material.

The functional objective is:

> Investigate broadly once, then preserve a roadmap that allows later design work to investigate deeply where relevant.

The roadmap should remain open to revision.

Later D1 work may discover additional predecessor references or identify that an earlier reference classification was incomplete.

## 3. Prepare Each Design Work Unit

Before a D1 design work unit begins, D2 should prepare the information and constraints relevant to that work.

At the functional level, the work unit may later be implemented as a Design Node or another modular design structure.

The prepared context should, where applicable, include:

- the design responsibility;
- higher-level design intent;
- inherited governing material;
- applicable rules and standards;
- relevant Designer decisions;
- applicable harness;
- relevant Predecessor Reference Roadmap entries;
- expected outputs;
- available working resources;
- evaluation expectations;
- authority and revision boundaries;
- and known unresolved issues.

The governing tendency is:

> Prepare the boundary before beginning the work.

The design worker should not normally be expected to reconstruct the entire D1 project context.

## 4. Perform Relevant Predecessor Investigation Before Design

The Predecessor Reference Roadmap is a starting point rather than a substitute for investigation.

Before substantial design begins, the current design work should inspect the predecessor material identified as relevant.

The depth of investigation may vary according to:

- the importance of the design subject;
- the selected harness posture;
- the degree of intended V1 preservation;
- known uncertainty;
- the level of the design;
- and available evidence.

The work may also follow references beyond the initial roadmap when investigation reveals that additional material is relevant.

The preferred tendency is:

> Use the roadmap to enter the predecessor system efficiently, then investigate deeply enough to establish the appropriate harness for the current design responsibility.

## 5. Build the Design Result

D2 should support bounded design work within the prepared context.

The work should be allowed appropriate local autonomy while remaining constrained by higher-level design and the applicable harness.

The design process may include:

- investigation;
- development of candidate design choices;
- comparison;
- internal critique;
- revision;
- construction of design specifications;
- production of Designer-relevant byproducts;
- and preparation of advancement recommendations.

The exact internal agentic mechanism remains a later design question.

The functional requirement is that D2 can carry a bounded design responsibility from prepared input to an evaluated design result.

## 6. Provide Internal Evaluation before Submission

A design result should normally be evaluated before it is submitted as complete.

The evaluation should be appropriate to the design responsibility and selected harness posture.

Possible evaluation may include:

- conformance with higher-level design;
- conformance with applicable rules and standards;
- predecessor-behavior comparison;
- representative usage examples;
- semantic review;
- internal consistency checks;
- design-specific tests;
- monitoring or observability review;
- interface or boundary checks;
- and other relevant harness.

The governing tendency is:

> Do not use submission as the first serious evaluation of the work.

The design work should first perform its own applicable internal evaluation.

## 7. Support Submission and Acceptance as Distinct Steps

D2 should distinguish between:

> Submission: the work unit presents a claimed completed result.

and:

> Acceptance: the governing design process determines that the result is acceptable for use in the continuing D1 design.

Submission and acceptance should not be treated as the same event merely because the same technical system can perform both functions.

The acceptance process may consider:

- completeness;
- applicable harness results;
- higher-level conformance;
- unresolved issues;
- required Designer authority;
- impact on existing design;
- and readiness for design advancement.

A submitted result may be:

- accepted;
- returned for revision;
- conditionally accepted;
- escalated for Designer intervention;
- or handled through another later-defined status.

The exact acceptance mechanism remains a later design question.

## 8. Distinguish Local Evaluation from Broader Integration Evaluation

D2 should support different evaluation scopes.

A design work unit may first be evaluated within its own bounded context.

Later, its result may need evaluation against a broader design context.

Conceptually:

> Local evaluation asks whether the work is internally sound and satisfies its local contract.
>
> Integration evaluation asks whether the accepted result works coherently with the surrounding D1 design.

The exact timing and depth of integration evaluation may vary.

Not every small design result requires a large integration process.

However, D2 should preserve the functional distinction so that local success is not automatically treated as evidence of broader design coherence.

## 9. Scale Harness and Evaluation Depth

The selected setup posture should influence the depth of design evaluation.

For example, a stronger harness posture may result in:

- deeper predecessor investigation;
- more representative examples;
- stronger internal critique;
- more evaluation rounds;
- greater integration testing;
- stronger evidence requirements;
- or larger resource allowance.

A leaner posture may reduce some of these expectations where appropriate.

The Designer should normally choose the higher-level posture rather than configure every evaluation mechanism independently.

D2 should translate the selected posture into the appropriate design-process consequences.

The depth may also vary by design importance.

Higher-level or semantically critical design work may justify stronger evaluation than routine lower-level work.

## 10. Produce a Designer-Oriented Result Report

After a major design work unit is completed and accepted, D2 should produce a concise Designer-oriented report.

The report should focus on information the Designer may reasonably care about.

Depending on the work, this may include:

- what was designed;
- important decisions;
- significant changes from V1;
- important preserved behavior;
- unresolved issues;
- material harness results;
- Designer-relevant artifacts produced;
- proposed revision of higher-level design;
- and recommended next design actions.

The Designer should be able to inspect deeper material when desired.

The normal report should not require the Designer to read the full internal work record.

## 11. Support Passive Designer Intervention

D2 should consolidate Designer clarification needs where practical.

The normal tendency is:

> Investigate first → resolve what can be resolved → collect remaining high-leverage questions → ask the Designer together.

The selected Designer-intervention posture may affect the threshold for asking questions.

Designer clarification is distinct from a Review Stop.

Clarification means D2 requires or strongly benefits from Designer input to resolve a design issue.

A Review Stop means the design work has reached a point at which the Designer may wish to inspect the result before continuation.

The two should remain functionally distinct.

## 12. Provide Review Stops at Appropriate Design Points

After important design work, D2 should allow the Designer to review before continuation.

The normal interaction may be:

> Design documents and result report are available in the current design area. Stop for review, or continue?

Higher-level design work should normally have a stronger tendency toward Designer review.

Lower-level design work may normally continue with greater autonomy.

The setup posture and Designer choices should influence Review Stop behavior.

## 13. Propose Design Advancement

At the completion of a design work unit, D2 should determine what design work should follow.

This may include:

- continuing the current phase;
- creating one or more descendant design responsibilities;
- beginning a new design phase;
- performing integration evaluation;
- creating a shared design artifact;
- revisiting an unresolved issue;
- or proposing revision of earlier design.

Design advancement and spawning should remain conceptually distinct.

A design phase may advance without spawning a child design responsibility.

A design work unit may propose multiple descendant responsibilities without implying that the overall D1 design has entered a new phase.

The exact Design Tree mechanics remain a later design question.

## 14. Support Spawning Decisions

When bounded descendant design responsibilities are appropriate, D2 should propose the spawning strategy.

The proposal may include:

- the proposed child responsibilities;
- the reason for separating them;
- the governing parent context;
- relevant inherited harness;
- candidate rules and standards;
- relevant predecessor references;
- Designer authority implications;
- and expected relationships among the resulting work.

The spawning decision may be autonomous or may require Designer review depending on:

- design level;
- Designer-selected posture;
- revision authority;
- semantic importance;
- and other later-defined governance conditions.

The Designer should normally review high-level spawning decisions more often than low-level routine spawning.

## 15. Preserve Revision Authority

D2 should distinguish design material that may be revised autonomously from design material requiring Designer approval for material revision.

A design result may therefore carry a governing revision-authority status.

For example:

- D2-managed;
- Designer-governed;
- or another later-defined authority class.

The Constitution is a likely example of Designer-governed design.

Lower-level implementation-oriented design may often be managed more autonomously.

A descendant design work unit may propose revision of an earlier design result.

D2 should preserve the proposal and route it according to the authority governing the affected design.

A lower-level work unit should not silently revise Designer-governed higher-level design.

## 16. Preserve Design History and Traceability

As D1 design progresses, D2 should preserve enough history to explain:

- what design result is currently effective;
- where it came from;
- what higher-level design governs it;
- what predecessor references materially informed it;
- what harness was applied;
- whether the Designer reviewed or approved it;
- what revisions occurred;
- and why major changes were made.

The objective is not to preserve every internal thought.

The objective is:

> Preserve the design lineage required for governance, investigation, revision, and Designer understanding.

## General Functional Philosophy

D2 should make the D1 design process feel to the Designer like movement through a prepared, progressively developing design route.

For each major design responsibility, D2 should:

> prepare the context;
> identify and apply the relevant harness;
> investigate the relevant predecessor material;
> perform the design;
> evaluate internally;
> submit and accept the result;
> report to the Designer;
> allow review or intervention where appropriate;
> and propose the next design action.

The Designer should primarily spend attention on high-leverage design decisions and important review points.

The internal complexity required to prepare, evaluate, trace, and advance the design should normally be carried by D2.
