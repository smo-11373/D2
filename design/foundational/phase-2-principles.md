# D2 Design — Phase 2: D2 Design Principles

## 1. Purpose of Phase 2

Phase 1 establishes the primary user, initial use case, and initial information available to D2.

Phase 2 establishes the high-level principles that shall govern the design of D2.

These principles are intentionally defined before D2 architecture, workflow, agent roles, design structures, or implementation mechanisms are selected.

Phase 2 answers the question:

> What principles should a good D2 system follow?

The principles in this phase are intended to guide and constrain later D2 design.

## 2. Principle 1 — D2-Initiated Designer Intervention

**Primary Declaration**

D2 shall minimize Designer Attention Cost by actively investigating available evidence and seeking to resolve material design uncertainty as early and at as high a semantic level as practical.

D2 should seek Designer intervention when Designer judgment has sufficient design value to justify its attention cost.

**Supporting Declarations**

### 2.1 D2 Shall Investigate Before Escalating

D2 should actively investigate the Predecessor D1, Designer-provided material, reference resources, and available behavior before transferring investigative work to the Designer.

The natural D2 bias is to dig more deeply into available evidence when doing so may materially resolve an important uncertainty.

### 2.2 Material Uncertainty Should Be Resolved Early

D2 should seek early resolution of uncertainty that may materially affect downstream design.

An unresolved high-level issue should not be allowed to propagate through substantial downstream design merely because D2 can temporarily proceed by assumption.

### 2.3 Designer Intervention Should Maximize Design Leverage

When Designer input is necessary, D2 should preferentially request a high-level principle, invariant, tradeoff, or direction capable of governing multiple lower-level decisions.

Designer intervention should occur as early as practical when an early decision can prevent downstream ambiguity, inconsistent assumptions, or extensive redesign.

### 2.4 Justified Inference Is Permitted

D2 may resolve an uncertainty through inference when available evidence provides sufficient justification and the consequence of an incorrect inference is limited, detectable, or reasonably reversible.

The inference and its basis must remain distinguishable from Designer-stated intent.

### 2.5 Deferral Requires Justification

Material uncertainty should not be deferred merely because it is currently unresolved.

Deferral should normally identify a meaningful constraint on further useful investigation.

Such constraints may include:

- an unavailable smoke-test or evaluation environment;
- unavailable reference data;
- inability to execute or observe relevant predecessor behavior;
- a logically prior unresolved decision; or
- investigation cost that is presently disproportionate to the expected design impact.

Where practical, a deferred issue should identify the condition or resource that may allow future resolution.

### 2.6 Resolution Depth May Be Tunable

D2 may provide a Designer-controlled parameter or equivalent mechanism influencing the balance among:

- deeper investigation;
- justified inference;
- Designer intervention; and
- explicit deferral.

The baseline D2 bias remains toward early investigation and early resolution of material uncertainty.

The tuning mechanism should alter investigation depth and Designer Attention Cost without removing D2's obligation to identify material uncertainty and justify unresolved assumptions.

## 3. Principle 2 — Designer-Initiated Intervention

**Primary Declaration**

The Designer shall have sufficient visibility into the progress, evolution, and behavioral health of D2 to independently determine when intervention is warranted and shall have practical means to initiate such intervention.

D2-initiated Designer intervention and Designer-initiated intervention are complementary mechanisms.

**Supporting Declarations**

### 3.1 D2 Shall Be Observable to the Designer

The Designer should be able to understand how the D2 process is progressing and whether its behavior appears consistent with the Designer's expectations.

Observability is required so that the Designer is not dependent solely on D2's own ability to recognize when Designer attention is needed.

### 3.2 Observability Shall Be Designer-Oriented

D2 should provide human-readable reports, summaries, indicators, and investigative views suitable for design judgment.

The Designer should not normally be required to inspect raw machine records, internal execution details, or agent interactions in order to monitor D2.

### 3.3 The Designer May Initiate Intervention Independently of D2

The Designer's ability to intervene shall not depend on D2 first detecting a problem, identifying uncertainty, or requesting assistance.

The Designer may independently determine that an area requires review, criticism, redirection, or further investigation.

### 3.4 D2 Shall Support Investigation Before Intervention

When the Designer identifies a possible concern, D2 should allow the Designer to obtain progressively deeper information.

The Designer should be able to move from high-level observation toward more detailed investigation before deciding whether intervention is necessary and what form that intervention should take.

Observability is therefore not merely passive reporting. It is a means of enabling informed Designer-initiated intervention.

## 4. Principle 3 — Unified Designer Interaction

**Primary Declaration**

The Designer should interact with D2 through a single primary interaction point.

D2 shall internally coordinate the interpretation, routing, investigation, and consequences of Designer interaction rather than requiring the Designer to select among multiple D2 components or interaction channels.

**Supporting Declarations**

### 4.1 The Designer Interacts with D2 as One System

The Designer should not normally need to determine which internal D2 function, process, role, or future agent should receive a question, instruction, criticism, or intervention.

Internal D2 decomposition should not unnecessarily become Designer interaction complexity.

### 4.2 D2 Owns Interaction Routing

Designer interaction may concern:

- design direction;
- clarification;
- criticism;
- investigation;
- monitoring;
- intervention;
- correction; or
- requests for deeper analysis.

D2 is responsible for determining how such input should be handled internally.

### 4.3 Interaction Context Should Be Preserved

The Designer should be able to interact with D2 without repeatedly reconstructing relevant context for different internal recipients.

D2 should preserve sufficient interaction and design context to interpret Designer input within the relevant D2 process.

### 4.4 Multiple Interaction Modes Are a Possible Future Extension

A future D2 design may introduce multiple Designer interaction modes when they provide clear Designer benefit.

One possible extension is a distinction between:

- constructive or positive interaction; and
- explicitly critical or negative investigation.

A critical interaction mode could allow the Designer to request skeptical investigation of potential flaws, hidden assumptions, or failure conditions.

The initial D2 design should nevertheless prefer one unified interaction point for simplicity.

## 5. Principle 4 — Verification Before Realization

**Primary Declaration**

D2 shall prioritize the design of observation, monitoring, testing, and evaluation capabilities before the design of implementation methods and shall prioritize sufficiently explicit implementation design or implementation specification before actual coding or equivalent realization.

The purpose is to move the discovery of uncertainty, deviation, and failure as early as practical in the D1 design and realization process.

**Supporting Declarations**

### 5.1 Observability and Evaluation Should Precede Implementation Choice

Before D2 commits to how a D1 capability should be implemented, D2 should, to the extent practical, establish how the relevant behavior can be observed, monitored, tested, or evaluated.

Implementation choices should preferably be made in an environment where their material consequences can be detected.

### 5.2 Testing and Evaluation Capabilities Are Design Assets

Environments, representative inputs, reference or expected outputs, evaluation methods, smoke tests, comparison methods, and monitoring capabilities should be developed early when they can improve subsequent design decisions.

These capabilities are not merely implementation-stage quality-control mechanisms.

They may be necessary tools for design discovery.

### 5.3 Implementation Design Precedes Realization

D2 should seek a sufficiently explicit implementation design or implementation specification before coding or equivalent realization becomes the primary means of discovering the design.

Actual implementation should primarily realize an understood design rather than serve as the default environment for resolving fundamental design questions.

### 5.4 Earlier Evidence Is Preferred to Later Correction

When D2 can establish an observation, monitoring, smoke-test, comparison, or evaluation capability that may expose material problems earlier, D2 should generally prioritize that capability over proceeding directly toward implementation.

The objective is to detect design deviation and incorrect assumptions before they propagate into detailed implementation.

### 5.5 The Principle Establishes Priority, Not a Rigid Waterfall

Verification Before Realization does not require all monitoring, testing, or evaluation design to be completed before any implementation-related exploration occurs.

A prototype, implementation sketch, or experimental realization may sometimes be necessary to discover what is observable or testable.

The principle establishes the preferred bias and ordering:

> move evidence formation and verification capability earlier whenever practical.

Feedback among design, experimentation, evaluation, and implementation specification remains permitted when justified.

## 6. Phase 2 Result

Phase 2 establishes four initial D2 design principles:

**Principle 1 — D2-Initiated Designer Intervention**

D2 should investigate deeply, resolve material uncertainty early, and request Designer attention at high-leverage points when Designer judgment justifies its attention cost.

**Principle 2 — Designer-Initiated Intervention**

The Designer must have sufficient visibility and investigative access to independently recognize concerns and initiate intervention.

**Principle 3 — Unified Designer Interaction**

The Designer should interact with D2 through one primary interaction point, while D2 owns internal routing and coordination.

**Principle 4 — Verification Before Realization**

D2 should move observation, monitoring, testing, and evaluation capability earlier than implementation-method decisions and should move implementation design ahead of actual realization.

Together, these principles establish a common direction:

> D2 should resolve important design issues early, maximize the leverage of Designer attention, preserve active Designer oversight, hide unnecessary internal interaction complexity, and create the means of detecting design problems before they become implementation problems.

Phase 2 intentionally does not yet determine the architecture by which these principles will be realized.
