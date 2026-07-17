# D2 Design — Phase 4: Designer D1 Action Model

*Status: Persistent working set. This document defines the Designer-facing D1 action model and guides later D2 architecture and governance design unless explicitly revised.*

## Phase Purpose

Define, from the Designer's perspective, how D1 design is initially framed, how Design Nodes are built with appropriate passive Designer intervention, and how the Designer may inspect and actively intervene in the emerging D0 design and the ongoing D1 design process.

Phase 4 deliberately avoids prematurely specifying the internal architecture of Design Nodes, the exact Design Tree relationship model, or the ownership of monitoring services.

## Item 1 — Establish the D1 Design Operating Framework

Upon entering D1 design mode, D2 shall prepare a proposed D1 Design Operating Framework for low-cost Designer review and confirmation. The framework establishes the initial design skeleton, relevant D1-specific design rules and inherited constraints, and material D1-specific Designer control points.

The Designer should see one consolidated prepared package that says, in effect: 'Here is how I propose to conduct this D1 design.'

**Initial design skeleton**

D2 provides a provisional high-level plan. The current starting point may be firm enough to initiate, while later subjects remain provisional. For example, D2 may recommend that the first Design Node establish the D1 Constitution and identify likely later subjects without committing to a fixed 10- or 15-phase sequence.

**D1 design rules and inherited constraints**

D2 inspects available Predecessor D1 rule material and proposes what should be inherited, revised, rejected, or left unresolved. The framework may also identify D1-specific design rules derived from the persistent D2 working principles.

**D1-specific Designer control points**

The existing Designer–D2 Operating Contract is inherited by default. D2 identifies only material D1-specific exceptions or high-value areas that may warrant special visibility, Review Stops, or D2-initiated intervention treatment.

The normal Designer action should remain low-cost: accept the proposed framework, modify selected parts, request investigation, or discuss a material concern.

## Item 2 — Build the Current Design Node

D2 builds the current Design Node through autonomous investigation, internal design and governance processes, and consolidated Designer clarification when necessary. Upon reaching a proposed node design, D2 produces a Designer-oriented node report and proposed spawning strategy. Designer review is provided according to the operating framework and the node's significance. Each node has an explicit revision-authority status determining whether later material changes may be governed autonomously by D2 or require Designer approval.

**Designer-facing node-building flow**

- D2 receives the task of building the current Design Node.
- D2 investigates, designs, checks, tests, submits, enforces, and revises internally as required by the node's governing process.
- When material Designer clarification remains necessary, D2 accumulates and prepares high-leverage questions into a consolidated Clarification Request where practical.
- D2 resolves the consequences of Designer answers and continues internal convergence.
- D2 produces the proposed Node Design Specification or equivalent node result.
- D2 prepares a Designer-oriented node report.
- Where the node-building action includes decomposition, D2 also proposes a spawning strategy. Spawning and general design-process advancement are distinct concepts.
- The Designer receives the review opportunity appropriate to the node's significance and the operating framework.

**Designer attention should generally increase with node height**

As a rule of thumb, higher Design Nodes should normally receive more Designer attention because their decisions govern larger descendant regions of the design. A Constitution Node is a natural candidate for a Review Stop. Lower implementation-related nodes may normally proceed with much greater D2 autonomy.

**Designer review and revision authority are distinct**

Designer review is an event. Designer revision authority is a continuing governance property.

A Designer may review a node and say 'continue' without reserving personal authority over every future revision. Therefore review history and revision authority should be represented separately.

Provisional revision-authority states:

- **D2-governed node** — D2 may resolve later material revision proposals through the D1 governance process unless the operating contract independently requires Designer intervention.
- **Designer-governed node** — material revision requires Designer approval. The Constitution is the obvious example.

The D1 Design Operating Framework should provide defaults by node level or class so that the Designer is not asked to choose revision authority after every node. D2 should call attention mainly to recommended exceptions.

**Upward revision proposals**

Every Design Node may propose revision to governing design above it. The treatment of the proposal depends on the revision authority of the affected node.

- If the affected node is D2-governed, D2 may investigate and resolve the proposal autonomously through the applicable governance process.
- If the affected node is Designer-governed, D2 first investigates, evaluates alternatives and consequences, and prepares a high-level Designer decision if a material revision remains recommended.
- Lower nodes retain the right to challenge higher design; Designer control prevents silent revision, not upward feedback.

**Provisional rule and sandbox model relevant to node building**

The current provisional model separates D1 rules, which govern the process of designing and producing D0, from D0 rules, which govern the distributable product and user-visible result.

- Designer rules require Designer permission for material creation, revision, supersession, or retirement.
- Design Nodes may own rules within the authority granted by their governing contracts.
- Rules may be collected in a central, versioned registry without implying centralized ownership of every rule.
- When a node is spawned, rules above it in the Design Tree are candidates for inclusion in the child contract.
- Non-applicable rules may be filtered out, with traceable justification, to keep the child contract lean.
- The child may then work primarily in a sandboxed node environment under a compiled governing contract.

The exact authority model for rules and standards remains deferred. The exact Design Tree relationship model also remains open: strict single-parent authority, one spawning parent plus non-spawning governing parents or references, and broader multi-parent structures remain candidates.

## Item 3 — Support Active Designer Inspection and Intervention

The Designer shall be able to inspect the emerging D0 design and the ongoing D1 design process through the unified D2 interaction point, using natural design-oriented requests. The Designer may inspect, investigate, or intervene without identifying the internal Design Node, governing authority, data location, or service responsible for the requested information.

From the Designer's perspective, the interaction model is: ask, inspect, drill down if desired, and intervene if desired. The internal question of whether a monitoring capability belongs to D1, D2, a shared service, or another governed object is intentionally deferred.

**Illustrative Designer queries**

- "Show me the current proposed D0 directory structure."
- "Show me the major files in the distributed package and what each one is for."
- "What will the D0 health report look like to the user?"
- "Show me the current D0 monitoring design."
- "Explain the current design of Algorithm A and how it differs from V1."
- "Which parts of the D0 design are still highly uncertain?"
- "How much time has D1 design consumed so far?"
- "How much has the D1 design process cost so far?"
- "Which Design Nodes have consumed the most time or cost?"
- "Which nodes have required the most revisions?"
- "Are any parts of the design process behaving abnormally?"
- "Show me the current D1 design health report."
- "Why has the configuration branch been rejected so many times?"
- "Which unresolved issues are most likely to affect major parts of the design?"
- "Show me the Design Tree."
- "Show me what changed in the Design Tree since my last review."
- "Investigate whether the D0 directory structure is becoming unnecessarily complicated."
- "Do not allow Algorithm A to be materially changed without my approval."
- "Stop work on the implementation-related branches until I review the verification design."

These examples are illustrative, not a command vocabulary. If the Designer can express a reasonable design inspection or intervention request in natural language, D2 bears the burden of locating the relevant design state, interpreting the request, and routing any resulting action through the appropriate governance process.

**Active intervention behavior**

- **Inquiry or inspection** — explain, report, trace, show, or compare current design or process state.
- **Investigation or concern** — critically examine a suspected design or process problem and recommend action.
- **Designer directive** — impose, revise, reserve, suspend, or otherwise exercise Designer authority.

Designer intervention should normally initiate investigation rather than directly mutate the Design Tree. D2 should interpret the concern, identify affected design objects and authority, investigate, and then act autonomously or prepare a Designer decision as required. Explicit Designer directives such as stopping a branch or reserving approval authority should be recognized as authority actions and applied promptly.

## Phase 4 Summary

- Item 1 — Establish the D1 Design Operating Framework
- Item 2 — Build the Current Design Node
- Item 3 — Support Active Designer Inspection and Intervention

Phase 4 closes with these three items. It defines the Designer-facing D1 action model without forcing unresolved internal D2 architecture decisions.
