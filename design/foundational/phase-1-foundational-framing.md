# D2 Design — Phase 1: Foundational Framing

## 1. Purpose of Phase 1

Phase 1 establishes the foundational framing for D2.

D2 is a system for designing a D1 system. The initial D2 scope is deliberately constrained to the upgrade of an existing D1 system or a sufficiently functional D1 prototype into a materially revised successor D1 system.

Phase 1 does not define the architecture, internal agents, workflow, data structures, or implementation of D2. Its purpose is to establish:

1. the primary user of D2;
2. the initial D1 use case; and
3. the initial information and resources available to D2.

These declarations provide the governing context for subsequent D2 design.

## 2. Primary User of D2

**Primary Declaration**

The primary user of D2 is the Designer responsible for directing the evolution of an existing D1 system into an upgraded D1 system.

D2 exists primarily for the benefit of the Designer.

**Supporting Declarations**

### 2.1 Designer Benefit Has Priority

The convenience of D2, its internal processes, its agents, implementation organization, or computational efficiency is subordinate when it materially conflicts with the Designer's ability to direct, understand, and control the D1 design process.

### 2.2 The Designer Retains Effective Design Authority

D2 may autonomously investigate, perform design work, form proposals, evaluate alternatives, and resolve routine design questions.

The Designer nevertheless retains effective authority over the material direction of D1.

Effective authority requires comprehensible and practical control. Merely requiring the Designer to approve a large number of machine-generated decisions does not constitute effective Designer authority.

### 2.3 Designer Attention Is a Primary Resource

The Designer's time and cognitive effort are scarce resources.

D2 should reduce the attention burden imposed on the Designer while preserving sufficient Designer influence over material D1 design decisions.

The objective is not merely to reduce the number of interactions. D2 should reduce the total cognitive burden associated with Designer participation.

### 2.4 Designer Interaction Must Be Human-Oriented

Information presented to the Designer should be organized for human design judgment.

When Designer review or decision is required, D2 should present the relevant issue, rationale, material alternatives, consequences, and requested action in a comprehensible form.

The Designer should not normally be required to inspect machine-oriented records, agent transcripts, or extensive internal reasoning in order to reconstruct the issue.

### 2.5 Designer Attention Should Be Concentrated at High Levels of Abstraction

To the extent practical, Designer attention should be applied to principles, invariants, material tradeoffs, system direction, and other high-leverage decisions.

D2 should resolve lower-level design questions autonomously when justified.

Repeated local questions that derive from a common higher-level issue should, where practical, be elevated into a higher-level Designer decision.

## 3. Initial D1 Use Case

**Primary Declaration**

The initial D2 system is designed to support the evolution of an existing D1 system, or a sufficiently functional D1 prototype, into a materially revised successor D1 system.

The initial D2 scope is system evolution rather than unrestricted greenfield design.

**Supporting Declarations**

### 3.1 The Initial D2 Scope Is D1 Evolution

The first D2 design shall focus on the upgrade of an existing D1 system.

D2 may later be generalized to support greenfield D1 design. The initial D2 design should not incur the complexity required to design an arbitrary D1 system from an empty specification unless that complexity is independently justified.

### 3.2 A Predecessor D1 Is a Primary Design Input

The Predecessor D1 may be a released system or a sufficiently functional prototype.

It should expose enough actual structure or behavior to provide meaningful evidence about the existing D1 system.

### 3.3 The Predecessor D1 Is Evidence, Not Authority

The Predecessor D1 may contain:

- intended behavior;
- important invariants;
- successful design decisions;
- historical compromises;
- accidental behavior;
- obsolete constraints; and
- known or unknown defects.

D2 shall not automatically treat existing D1 behavior as a requirement for the successor D1.

### 3.4 The Successor D1 Is Primarily Described Incrementally

The Designer should normally describe desired changes relative to the Predecessor D1.

Designer input may identify:

- behavior to preserve;
- known problems or defects;
- desired corrections;
- desired simplifications;
- new capabilities;
- areas of dissatisfaction;
- important constraints;
- areas requiring reconsideration; and
- general directions of improvement.

The Designer should not normally be required to completely restate unchanged portions of the Predecessor D1.

### 3.5 D2 May Derive Candidate Design Evidence from the Predecessor D1

D2 may study the Predecessor D1 and derive candidate evidence such as:

- observed workflows;
- environment assumptions;
- representative inputs;
- observed outputs;
- input-output relationships;
- behavioral comparisons;
- candidate invariants; and
- candidate evaluation cases.

Derived evidence remains provisional until interpreted through the D2 design process.

### 3.6 Unspecified Predecessor Behavior Is Initially Unresolved

Behavior observed in the Predecessor D1 but not addressed by the Designer is not automatically preserved and is not automatically discarded.

Such behavior is initially unresolved.

D2 should determine its relevance when it becomes material to the design process. The Designer should not be required to classify every observed predecessor behavior before D2 design can begin.

## 4. Initial Information and Resources Provided to D2

**Primary Declaration**

D2 begins with a Predecessor D1, incremental Designer intent, and available reference resources.

D2 is responsible for converting these incomplete inputs into structured design evidence rather than requiring the Designer to provide a complete system specification.

**Supporting Declarations**

### 4.1 The Predecessor D1 Is the Primary Reference Resource

To the extent technically available, D2 should be permitted to inspect, execute, and otherwise study the Predecessor D1.

The purpose is to learn about the existing D1 system through available evidence rather than requiring the Designer to describe the entire system.

### 4.2 Designer Intent Is Primarily Incremental

Designer input may consist of changes, problems, defects, dissatisfaction, additions, constraints, and directions of improvement.

The Designer is not normally responsible for restating unchanged portions of the Predecessor D1.

### 4.3 Initial Designer Input May Be Incomplete and Loosely Structured

D2 should accept human-oriented commentary, notes, examples, concerns, and other incomplete material.

The initial burden of translating this material into structured candidate design meaning belongs primarily to D2.

### 4.4 Reference Resources May Supplement the Predecessor D1

Available resources may include:

- existing documentation;
- prior design material;
- known test cases;
- user examples;
- datasets;
- existing environments;
- evaluation material; and
- other relevant reference resources.

The existence, completeness, and reliability of these resources may vary.

### 4.5 D2 May Actively Derive New Design Evidence

D2 may use available resources to conduct further investigation.

This may include executing or probing the Predecessor D1, constructing representative inputs, capturing outputs, comparing behavior, identifying apparent boundaries, and constructing candidate evaluation material.

These derived artifacts constitute design evidence. They do not automatically become accepted design requirements.

### 4.6 Provenance and Uncertainty Must Be Preserved

D2 must preserve the semantic distinction among:

- Designer-stated intent;
- directly observed Predecessor D1 behavior;
- externally provided reference material;
- D2-derived evidence; and
- D2 inference.

D2 must not silently convert inference into Designer intent.

D2 must not silently convert observed predecessor behavior into an approved successor requirement.

The origin, interpretation, and uncertainty of material design information must remain distinguishable throughout the D2 process.

## 5. Phase 1 Result

Phase 1 establishes the following foundation:

- D2 is primarily designed for the Designer.
- D2 should preserve effective Designer authority while reducing Designer Attention Cost.
- The initial D2 use case is the evolution of a Predecessor D1 into a successor D1.
- The Predecessor D1 is a major source of evidence but is not design authority.
- The Designer primarily supplies incremental intent rather than a complete system specification.
- D2 is expected to actively study available resources and derive additional design evidence.
- Provenance, inference, observation, and Designer intent must remain semantically distinguishable.

Phase 1 intentionally does not prescribe D2 architecture or internal mechanisms.

Those decisions must be governed by subsequent D2 design principles.
