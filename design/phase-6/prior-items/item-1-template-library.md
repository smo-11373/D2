# Phase 6 — Item 1: Provide Default Design Choices through a Template Library

## Primary Function

D2 should provide prepared default design choices through a Template Library and allow the Designer to select a high-level design posture with minimal effort.

The Designer's choice should produce a centralized, reviewable setup configuration package. D2 may then use that package to establish the corresponding effective design material in the appropriate D2, D1, and D0 contexts.

The governing functional sequence is:

> Template Library → Designer choice → Selected Setup Configuration Package → Designer review or revision → Effective configuration in the appropriate design contexts

## 1. Template Library

The Template Library is a reusable collection of prepared design material.

It is not expected to be a single file.

A template choice may draw from a package containing many related files or semantic design artifacts.

Most template material should, where practical, be human-readable and semantically expressive because it ultimately serves the Designer and supports later inspection, explanation, and revision.

Candidate forms may include:

- plain text;
- Markdown;
- structured text;
- declarative configuration;
- human-readable rule or policy files;
- position descriptions;
- design-posture descriptions;
- contract material;
- report templates;
- or other semantically transparent forms.

The exact formats remain a later design question.

The functional preference is:

> Use transparent, retrievable, human-readable design material where practical rather than hiding consequential choices inside opaque parameter tables or executable setup logic.

The Template Library may contain prepared material for:

- the Designer–D2 relationship;
- D1 design operating posture;
- D0 human positions;
- D0 user priorities;
- harness posture;
- monitoring posture;
- evaluation posture;
- investigation depth;
- Design Node defaults;
- resource and budget posture;
- reporting behavior;
- Review Stop behavior;
- authority defaults;
- and other recurring design choices.

The library should remain extensible.

## 2. Simple Designer Choice

D2 should present the Designer with a small number of meaningful high-level choices rather than requiring direct configuration of every underlying file or parameter.

For example:

- Standard;
- High Harness;
- Lean;
- or another project-specific recommended posture.

A single choice may select, combine, or modify many pieces of template material.

For example, selecting High Harness may affect:

- Design Node evaluation expectations;
- investigation depth;
- predecessor-derived usage-example requirements;
- test and evidence expectations;
- monitoring requirements;
- expected resource allowance;
- Review Stop behavior;
- and reporting depth.

The Designer chooses the posture.
D2 resolves the detailed consequences.

## 3. Selected Setup Configuration Package

After the Designer makes or confirms a choice, D2 should create a centralized Selected Setup Configuration Package.

This package represents the actual setup chosen for the current design run.

It is distinct from the reusable Template Library.

The Template Library contains possible defaults.

The Selected Setup Configuration Package contains the specific combination selected, inferred, or modified for the current project.

The package should be:

- centrally available;
- human-readable where practical;
- versioned;
- reviewable;
- traceable to its template sources;
- explicit about Designer modifications;
- and retrievable later.

The Selected Setup Configuration Package should exist before its contents are distributed, referenced, generated, or otherwise made effective in other design contexts.

This creates a clear Designer-facing source of truth:

> These are the setup choices governing this D2 and D1 design run.

## 4. Designer Review before Activation

The normal Designer action may be simply:

> Accept the recommended setup and continue.

However, the Designer should be able to inspect the Selected Setup Configuration Package before D2 activates or distributes its consequences.

The Designer may request:

- a summary of the package;
- the full package;
- only the material affecting D0 users;
- only the harness-related settings;
- a comparison against another template choice;
- explanation of a particular derived setting;
- or direct revision of selected material.

D2 should support progressive disclosure.

The Designer should not be forced to inspect every file, but no consequential setup choice should be inaccessible merely because it originated from a default template.

## 5. Establishing Effective Configuration

After confirmation, D2 should establish the relevant material in the appropriate design contexts.

This may involve:

- copying;
- generating;
- referencing;
- linking;
- materializing;
- registering;
- or another later-defined mechanism.

Phase 6 should not require a specific CLI, file-copying process, or setup technology.

The functional requirement is:

> The confirmed setup package must become effective in the appropriate contexts without losing traceability to the centralized chosen package.

The centralized package remains the reviewable record of what was selected.

The effective configuration may then appear in different places because different parts of the setup govern different levels and responsibilities.

## 6. Distinct Authority over Setup Material

The Selected Setup Configuration Package may contain material governed by different authorities.

The package is centralized for visibility and review, but authority over every item does not necessarily remain centralized.

For example:

**Designer–D2 relationship material**

Once confirmed, some operating-contract material may become governed by D2's established operating process.

Changes may require the modification mechanism defined for the Designer–D2 relationship.

The Designer still retains the right to inspect and initiate modification, but D2 may own the formal maintenance and application of the effective operating contract.

**D1 design material**

Some selected material may become part of the D1 Design Operating Framework.

Its later modification may be governed by D1 design authority, Designer control points, or delegated D2 authority.

**D0 relationship and user-position material**

Material defining D0 positions, D0 user priorities, user experience expectations, or the Designer's intended relationship to D0 may remain more directly under Designer authority.

This material may reasonably be revised later as D1 design reveals more about the emerging D0 product.

For example, the Designer may later decide:

- the D0 Operator requires more control;
- the D0 Technical Manager should receive additional monitoring capability;
- a configuration responsibility belongs to a different position;
- or a previously assumed user skill level was incorrect.

Such revision should remain available without requiring the Designer to reconstruct the original setup process.

## 7. Authority Should Follow Meaning

The authority of a configuration item should derive from what the item governs, not merely from the fact that it was initially selected through one setup package.

Therefore:

> Centralized selection and visibility do not imply centralized modification authority.

A setup package may contain items that later belong to:

- D2 governance;
- D1 governance;
- Designer-reserved authority;
- D0 product design;
- or another later-defined authority boundary.

The exact authority model remains a later design question.

Phase 6 establishes only the functional requirement that D2 must preserve and apply those distinctions.

## 8. Later Revision

The setup should not be treated as immutable.

The Designer may revise relevant setup material later, especially material concerning D0 user positions, user priorities, monitoring expectations, or product relationships.

D2 should support:

- retrieval of the current effective configuration;
- identification of the governing authority;
- proposed revision;
- impact analysis;
- governed application of the change;
- and preservation of revision history.

Later revision should not silently overwrite the original setup record.

The design run should retain a traceable history of how the setup evolved.

## General Functional Philosophy

D2 should make setup easy without making it opaque.

The preferred experience is:

> D2 recommends a small number of high-level choices.
>
> The Designer selects or adjusts the desired posture.
>
> D2 creates a centralized, human-readable setup configuration package.
>
> The Designer may review or revise it.
>
> D2 establishes its contents in the appropriate design contexts.
>
> Authority over individual items follows their meaning and governing level.

This approach reduces Designer effort while preserving transparency, retrievability, reviewability, and later control.
