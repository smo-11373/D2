# Phase 6 — Item 3: Provide D1 Design Data and Working Areas

D2 should provide, as part of the project setup, the major data and working areas required to conduct, govern, observe, and preserve a D1 design project.

The governing tendency is:

> D1 design work should begin inside a prepared data environment rather than inventing storage, working areas, and shared data locations as the project proceeds.

The exact directory structure, file formats, storage technology, and ownership mechanisms remain later design questions.

## 1. D1 Design Project Planning Data

D2 should provide an area for the current D1 design plan and its history.

This includes:

- the current phase;
- the provisional list of later phases;
- phase advancement decisions;
- completed phases;
- revisions to the plan;
- and sufficient planning history to explain how the current plan developed.

The D1 design plan is conceptually different from the design being produced.

It governs the process used to produce the D1 design.

In this sense, planning data may be viewed as sitting approximately one-half level above the D1 design work itself.

## 2. D1 Design Project Observation Data

D2 should provide project-level data describing the progress and condition of the D1 design project.

Candidate information includes:

- current design activity;
- completed design work;
- pending work;
- project progress;
- resource consumption;
- financial cost;
- elapsed time;
- Designer Attention Cost;
- unresolved issues;
- abnormal process conditions;
- and other project-health information.

This data supports Designer queries such as:

> "Show me the resource consumption so far for D1 design."
>
> "Where are we in the D1 design?"
>
> "What is currently blocking progress?"

The exact monitoring responsibility may later belong to D1, D2, or a combination.

From the Designer's perspective, the functionality should be available.

## 3. D1 Design Metadata

D2 should provide storage for the metadata required to represent and govern the developing D1 design.

This may include:

- Design Tree information;
- Design Node information;
- design relationships;
- node status;
- governing relationships;
- revision authority;
- submission and acceptance status;
- spawning records;
- design lineage;
- and other metadata required by the later Design Tree and Design Node design.

The detailed metadata model should be established during the more detailed design of the Design Tree and Design Node.

Phase 6 establishes the need for a persistent D1 design metadata area.

## 4. Shared D1 Design Project Data

D2 should provide an area for data intended to serve the D1 design project broadly rather than one individual Design Node.

Candidate shared project data includes:

- rules;
- standards;
- D1 design rules;
- applicable D2 concepts and philosophy;
- glossary and definitions;
- communication standards;
- common design conventions;
- representative usage examples;
- test examples;
- shared evaluation material;
- common reference notes;
- and other project-wide design resources.

This area should support information that may be relevant to multiple Design Nodes.

The existence of a central shared area does not determine authority over every item stored there.

Rules, standards, definitions, examples, and other shared data may have different creation and modification authorities.

Central collection should not be confused with centralized authority.

## 5. Predecessor and Reference Data

D2 should provide access to the Predecessor D1 package and other reference material used by the D1 design project.

This may include:

- the original V1 D1 package;
- source code;
- documentation;
- configuration;
- tests;
- usage material;
- historical design material;
- revision proposals;
- supplementary Designer documents;
- and other relevant references.

The reference material may be large.

D2 should therefore also preserve reference aids such as the Predecessor Reference Roadmap described in Item 2.

The original reference material and D2-created descriptions or notes about that material should remain distinguishable.

## 6. D1 Project Working Area

D2 should provide a temporary or working area for the D1 design project as a whole.

This area supports work that:

- is not yet accepted design;
- is not local to one Design Node;
- may involve multiple nodes;
- is exploratory;
- is being consolidated;
- or is temporarily required during project-level design activity.

The project working area should be distinguishable from persistent accepted design data.

D2 should not require every intermediate artifact to become permanent project data.

## 7. Design Node Working Areas

Each Design Node or equivalent bounded design work unit should have an appropriate local working area.

The local working area supports the modularization philosophy established in Phase 5.

A Design Node should be able to perform local investigation, design, evaluation, and revision without using the shared D1 project area as an undifferentiated scratch space.

Conceptually:

> Shared project data provides common context.
>
> The node working area provides local design freedom.

The node working area may contain:

- local notes;
- temporary analysis;
- candidate designs;
- local test material;
- evaluation results;
- temporary copies or extracts of relevant reference material;
- and other node-local working data.

The detailed sandbox model remains a later Design Node design question.

## 8. Shared Designer-Relevant Artifacts

D2 should provide an area for artifacts produced during D1 design that are useful beyond the local work unit that created them and are particularly relevant to Designer inspection.

Examples may include:

- D0 prototypes;
- representative D0 package structures;
- sample health reports;
- monitoring examples;
- interface mockups;
- algorithm demonstrations;
- comparison results;
- and other Designer-relevant design byproducts.

A D0 prototype may originate from work inside a particular Design Node.

Once identified as broadly Designer-relevant, it should not remain hidden only inside that node's local working area.

The exact promotion mechanism remains a later design question.

## 9. Data Areas Should Be Established through Setup

The major D1 design data and working areas should normally be established through the D2 setup process.

The selected Setup Configuration Package may determine:

- which areas are created;
- their default structure;
- their initial contents;
- applicable templates;
- access expectations;
- and other initial properties.

The Designer should not normally need to manually construct the D1 design data environment.

D2 should provide a prepared default environment and allow later modification where appropriate.

## 10. Preserve Functional Distinctions

Different classes of D1 design data may eventually use the same physical storage technology or even reside within one directory hierarchy.

Phase 6 does not require physical separation for every conceptual distinction.

However, D2 should preserve the functional differences among:

- planning data;
- project observation data;
- design metadata;
- shared project data;
- reference data;
- project working data;
- node-local working data;
- and shared Designer-relevant artifacts.

These distinctions affect authority, lifecycle, visibility, retrieval, modification, and later architectural design.

## General Functional Philosophy

D2 should provide a prepared data environment for D1 design.

The Designer and the D1 design process should be able to assume that there are appropriate places for:

- planning the work;
- observing the project;
- representing the developing design;
- maintaining shared design resources;
- preserving predecessor references;
- performing project-level temporary work;
- performing node-local work;
- and surfacing Designer-relevant artifacts.

The detailed structure should be derived later.

Phase 6 establishes that these data functions must be supported.
