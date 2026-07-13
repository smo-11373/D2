# Phase 6 — What D2 Does for the D1 Designer

*Phase 6 translates the constitution (Phases 1–5) into something actionable — for each thing the **D1 Designer** does, the **D2 support** he needs to do it. Section 1 sets out the method; the sections that follow apply it to his work, step by step.*

---

## 1. Methodology

**What this phase is for.** Phases 1–5 are the constitution — they establish, with argument, what the D2 ecosystem is and the principles it must honour. Phase 6 does something different: it **translates that constitution into something actionable**. Its product is a link, built step by step, between **what the D1 Designer needs to do** and **what the D2 product must provide** so he can do it. This document is that translation — it does not re-narrate the constitution, it puts it to work.

**The subject.** This project produces a **D2 product**: the design system the D1 Designer uses to build his **D1** system, which in turn produces the distributable **D0** product (**D2 → D1 → D0**). We describe that product by walking **what the D1 Designer does** with it. One test governs throughout: **write only what the D1 Designer cares about** — how anything is stored or built stays out of scope until it earns its place.

**The method, at each step.** For every step of his work we do three things:

1. **Identify the actions** — what the Designer is required or wants to do, and, where the work is D2's own, the internal *agent* actions that carry it out.
2. **Abstract the common element** — from the unbounded space of possible projects, extract the recurring *form* of that action and argue it from the foundations. We cannot know the content of a Designer's project; the *shape* of his involvement recurs, and that shape is what D2 can support.
3. **Define the D2 support** — the capability the product must provide to satisfy the action.

**This is an open list.** We do not know what project the Designer will bring, so no catalogue of actions or capabilities is ever complete. We aim not for 100% coverage of every project but for the **common, anticipable elements** most projects share — the skeleton the foundations already give us — and let D2 interpret the remainder rather than pretend to pre-enumerate it.

**Two classes of action — and why one is harder.** Everything the Designer does is either **passive** or **active**, and the two differ not only in who initiates but in how anticipable they are:

- **Passive** [P] — he responds to something D2 brings him (a proposed result, a decision, a report). These take a few *static, near-universal forms* — the review / stopping point, the clarification point — so they abstract cleanly and recur in nearly every project. *(Phase 4, Item 2.)*
- **Active** [A] — he acts on his own initiative (monitor progress, monitor spend, inspect, redirect, lay down a rule). These are *fluid and project-dependent*, so they resist anticipation — which makes the abstraction **more** important, not less: the job is to find the common likely elements of active involvement and support those, knowing the list stays open. *(Phase 4, Item 3.)*

**The D0 user is always in view.** Cutting across both classes is the Designer's own purpose: he designs D1 to **serve the D0 users** — the operators and users of the distributable product. So he designs with **D0-user optimization in mind**, a standing consideration that shapes what the D1 system must do; D2's functionality exists to let him hold it and act on it. *(Phase 5, Item 3 — Human Position First.)*

**The bookkeeping.** The abstractions this writing produces are recorded in the living **catalogs** — the role table, the role–action table, the capability catalog, the action↔capability map, and the query catalog. Those catalogs are not the substance; they are the **ledger**. Their value is that they can be *matched* — a relational coverage check that every Designer action has a supporting capability, that no capability is orphaned, that nothing is silently missed. The substance lives in this writing; the catalogs keep it honest.

**What the rest of this document covers.** The sections follow his work in order, each tagged by the class of action it primarily serves — **[P]** passive, **[A]** active.

2. **The entry point — deciding whether to use D2** [P] — his first decision; D2 backs it by orienting him with the concepts it needs.
3. **Building the initial setup — the roles table and the posture** [P] — establish the cast of roles (each intrinsic or a Designer-changeable default) and the run's default design choices, in one setup step.

Beyond setup the coverage stays **fluid** — a list of likely topics, not yet fixed to sections or order:

- giving D2 the starting point — the predecessor plus an informal intended change [P]
- understanding the proposed direction before committing [P]
- setting the design in motion — the operating framework [P]
- overseeing the work without drowning in it [P]
- **inspecting, monitoring, and intervening** — active involvement [A] *(drafted ahead as the register reference)*
- being asked only when it's worth it [P]
- checking how well D2 served him [A]

*Revival in progress: §1–§3 and the active-interaction reference (§9) are in this register. §4–§6 (giving the starting point, understanding the direction, setting in motion) are pre-revival drafts awaiting rework; later coverage stays fluid.*

---

## 2. The entry point — deciding whether to use D2  [P]

*Derived from Phase 1 (Designer authority & attention); Phase 2 (progressive disclosure).*

Before any run, the Designer stands at a gate that has nothing to do with his particular project: **should I use the D2 product to carry out this design at all?** It is the first thing he does, and until he decides yes, nothing else happens. It is also the most anticipable step in the whole document — every Designer faces the same question and needs the same *kinds* of information to answer it, whatever he is building.

**The Designer action.** One action, with a decision at its centre: **evaluate D2 and decide whether to adopt it** for this design — adopt, decline, or defer. → Designer action **A-055**.

**The common element.** This gate is the same in every project: whatever he is building, the Designer needs the same *kinds* of information to decide, so D2 can prepare them once, generically.

**The D2 support — an orientation summary.** What D2 provides at this gate is a single **orientation summary**: a short, top-level document that answers, *in summary and not in detail*, the questions behind the decision, and in doing so makes each role's responsibility plain. We cannot write that document fully here — its final content depends on D2's later design — but we can already fix the **key elements it must contain**:

- **What D2 is and does** — the meta-design system, and what it offers him.
- **The layer model and his place in it** — D2 → D1 → D0, with the Designer as the top authority the whole ecosystem serves.
- **Who is responsible for what** — the roles and their responsibility boundaries: he holds design authority; the D2 Assistant is his single point of contact and conducts the design; internal agents do the work; downstream, the IT Manager deploys and the D0 Operator runs the product. (The full cast is §3.)
- **What using D2 will ask of him** — the shape of his involvement (a few review and clarification points; inspection whenever he wants) and what it will and won't cost his attention.
- **What he gets out** — a delivered D1 product wrapping D0, built for the D0 users.

It is a summary he can act on, not a manual he must study; he can probe any element for more, and nothing that matters is hidden. Only once he decides to proceed does setup begin. → new capability **C-37** (adoption orientation), an application of progressive disclosure.

**Why this shape.** The decision to adopt D2 is the Designer's alone — his authority and his limited attention are the top priorities (Phase 1) — so D2 owes him a compact, honest basis rather than presuming adoption. Orienting *before* configuring is progressive disclosure in its first application: show what this decision needs, and no more (Phase 2).

**The open edge.** What finally moves a given Designer to adopt — his risk tolerance, his existing tools, his deadline — D2 cannot know or support; it supplies the common orientation every such decision needs and leaves the judgement itself to him. The element list above is itself open: these are the anticipable pieces of the summary, not its finished content.

---

## 3. Building the initial setup — the roles table and the posture  [P]

*Derived from Phase 5 Item 3 (Human Position First); Phase 3 Item 1 & Phase 6 Item 1 (setup package, postures).*

With D2 adopted, the Designer builds the run's **initial setup**. It has two parts — *who is in the ecosystem* (the roles) and *how the run will be conducted* (the posture) — and they share one shape: D2 supplies a good default and keeps his action to a light review. Both land in a single reviewable **setup package** he can inspect, revise, and return to later.

### 3a — The roles table

**The Designer action.** Review and adjust the cast of **roles** the design will recognize — accept the defaults or tailor them. → new action **A-056**.

**The common element.** Every project recognizes the same *kinds* of role, differing only in the product-side cast: the ecosystem's core roles are fixed, while the downstream, product-facing roles are project-dependent but seedable with sensible defaults. The role set matters because — *Human Position First* — controls, monitoring, and behaviour are all shaped by which role they serve, so it frames everything the design will do.

**The D2 support.** D2 provides a **default roles table**, each role marked **intrinsic** (fixed) or a **Designer-changeable default**, which he accepts or tailors. → new capability **C-38**.

| Role | What it is | Provenance |
|---|---|---|
| **D1 Designer** (R-01) | The human the ecosystem serves; sole design authority | **Intrinsic** — fixed |
| **D2 Assistant** (R-07) | Non-human LLM; his single point of contact; conducts the design on his behalf | **Intrinsic** — fixed |
| **IT Manager / D1 Technical Manager** (R-04) | A human who receives the delivered D1 package, extracts D0, deploys it, and runs the wrapper | **Default** — Designer-changeable |
| **D0 Operator** (R-05) | Runs the deployed D0 in production; D1's primary beneficiary | **Default** — Designer-changeable |
| **D0 Technical Manager** (R-06) | Front-line install and technical support of a D0 deployment | **Default** — Designer-changeable |

*The product boundary this encodes:* what the run produces is a distributable **D1 package** wrapping the **D0 product**; delivery is a human decision — the IT Manager (R-04) unpacks it, extracts D0, and deploys it, while the D0 Operator (R-05) runs it. That chain is why Section 1's throughline holds — the Designer designs D1, but its primary beneficiary is the D0 Operator at the far end.

*Not roles he configures:* D2 does the design work through **internal agents** — the Design Node Builder (R-02), the D1 Programmer (R-03), and likely others (a standard-enforcer, an integrator). How many, and of what types, is deliberately **left open** (*Top-to-Bottom*) and recorded as an open question; these are D2's own labour, not part of the roles table he sets.

### 3b — The posture (default design choices)

**The Designer action.** Select a **posture** — *Standard*, *High Harness*, or *Lean* — or accept the one D2 recommends; optionally tune it. → action **A-015** (tuning **A-019**).

**The common element.** A run has many low-level knobs — how much harness and monitoring, how deeply to investigate, how much to report, when to stop for review, how much resource to spend — and across projects they **co-vary** into a few coherent stances. So one high-level choice can settle them all.

**The D2 support.** D2 offers **default design choices**: a few postures, one choice resolving into many settings, each inspectable, comparable, and overridable. → **C-01** (default design choices), **C-22** (tunable resolution depth & posture).

### The setup package

Both parts land in one **Selected Setup Configuration Package** — a centralized, versioned, reviewable record he can inspect, compare, revise, and return to later, with his own changes visible. → **A-016** / **C-02**, **C-03**; later governed revision **A-017** / **C-05**.

**How much he can change — and what he can always see.** How far the Designer may revise or add to the roles and the posture is itself a **D2 design question**; D2 may start simple and relatively rigid and widen later. But one thing is the **guaranteed floor, whatever that choice**: he can always *look inside*. For the roles, that means seeing each role's definition and its intrinsic/default status; for the posture, drilling from any chosen value into **what that setting means and what it entails** — a next-level view of each knob's definition and consequence, so a choice is never opaque. He may not always be free to change a thing, but he is always free to understand it. → **C-03** (inspect / explain the setup); the posture's next-level definition-and-consequence view is part of **C-01**. *(How much change/add flexibility to allow is logged as an open question.)*

**Why this shape.** Human Position First (Phase 5, Item 3) makes the role set the natural first thing to fix — it frames the design. And the Designer's attention belongs on high-level choices, not low-level configuration (Phase 1): *"the normal action should often be to accept the defaults"* (Phase 3, Item 1). So both parts of setup reduce to a good default plus a light review.

**The open edge.** Default roles and postures cover the common shape; a project may need a role the defaults don't name or a setting no posture captures — D2 lets him add or override. The defaults are a starting point, not a ceiling. *(Whether he may change the setup mid-run is itself an open question — see the decisions log.)*

---

## 4. Giving D2 the starting point

With the run set up, the Designer gives D2 what it needs to begin: **the existing system, and — however roughly — what he wants changed.** This is the one moment he must supply something of his own, so D2's whole job here is to make that as light as possible: to take incomplete, informal input and do the work of making sense of it, so he never has to write a full specification.

He hands over two things, neither required to be complete:

- **The predecessor system** — whatever exists and can be studied: the running system, source, documentation, tests, environments, datasets, usage examples. He points D2 at the material; he does not curate or explain it.
- **His intended change** — in any form that is useful *to him*: a revision note, rough jottings, a bug list, user complaints, desired features, a prior discussion, a prototype idea, examples of behavior he dislikes, or just a general direction.

From there D2 does the making-sense. It **investigates the predecessor deeply** and biases toward resolving ambiguity on its own, returning to him for clarification only where investigation genuinely cannot settle a material point — and then batching that into a few worthwhile questions rather than a stream of small ones. The existing system is not merely a starting point but an **unusually strong source of harness** (Phase 5, Item 1): D2 mines it for representative behavior, expected input–output pairs, and constraints the successor should keep. What this step produces is a *sufficient initial direction* to begin governed design — not a finished specification, and explicit open questions may remain.

Because his intended change so often speaks *for the D0 users* — their complaints, the features they want, the behavior that fails them — this is also where the **D0-user considerations of Section 1 first enter the design**, carried in his own words rather than a form.

**Why D2 works this way.** The constitution forbids demanding a complete spec up front: "D2 shall not require the intended change to be fully specified" and "should actively assist the Designer in developing a sufficiently clear initial upgrade direction" (Phase 3, Item 2). His scarce resource is attention (Phase 1), so D2 investigates first and asks second — spending its own effort to spare his — and accepts his input in whatever form costs him least. Early discussion is welcome precisely when it prevents far larger downstream Designer Attention Cost (Phase 3, Item 2).

---

## 5. Understanding the proposed direction before he commits

Before the real design work begins, the Designer gets to see what D2 made of his input — and to react to it. This is his first substantial **passive** step: D2 has done the studying, and now hands him back a clear picture and a proposed way forward to accept, adjust, or redirect — not a pile of open questions to resolve.

D2 reaches this point by **converging on its own first**. It studies the predecessor, his intended change, and the reference material, resolves as much uncertainty as it practically can through investigation, and only then consolidates everything into a single, Designer-oriented account that normally covers:

- **its understanding of the existing system** — just the major characteristics that bear on the intended upgrade;
- **what it reads as to-be-preserved, changed, corrected, added, or reconsidered**;
- **likely invariants, protected areas, and places needing special caution**;
- **the material uncertainties or contradictions it could not reasonably resolve** — surfaced honestly, not hidden;
- **its recommended initial design direction.**

He is not handed this as a to-do list. D2 presents it at a **Review Stop** — *"understanding and direction are documented; I've stopped so you can review — review now, or continue?"* The stop is a *courtesy and a control boundary*, not a claim that D2 is stuck: he may read deeply and steer, skim, or simply wave it on. That differs from a **Clarification Request**, which D2 raises only when it genuinely needs his judgment on something investigation could not settle. Here the default is the gentler Review Stop; the residual uncertainties above are reported for his awareness, not dumped on him as questions.

What he commits to at this step is a *direction*, not a finished design — and only if he chooses to engage at all. If the picture is wrong or the direction off, this is the cheap moment to say so, before work is built on it.

**Why D2 works this way.** The constitution consolidates "initial understanding" and "initial direction" into *one* normal passive-intervention round and tells D2 to "converge internally before approaching the Designer" (Phase 3, Item 3) — so his attention meets a finished thought, not D2's working-out. It also draws a firm line between three interaction classes — Completion Report, Review Stop, and Clarification Request — insisting that "every item is observable; only some items require Designer attention" (Phase 3, Phase-Wide Interaction Rule). Offering an *optional* review here rather than demanding sign-off is that principle in action: everything is open to him, but nothing is forced on him.

---

## 6. Setting the design in motion

With the direction agreed, the Designer settles one more thing before work proceeds: **how D2 will actually conduct the design.** D2 prepares this as a single package that says, in effect, *"here is how I propose to run this D1 design"* — and, as with every setup-shaped step, his normal action is simply to accept it, with adjusting or pushing back kept cheap.

The proposed **operating framework** gathers three things:

- **A design skeleton** — a provisional high-level plan of the work. What comes first is firm enough to start on; later subjects are named but left provisional. D2 might, for instance, propose that the first piece of work establish the D1 Constitution and merely *flag* likely later subjects, rather than committing up front to a fixed sequence of phases.
- **The design rules and inherited constraints** — D2 inspects the predecessor's own rule material and proposes what to **inherit, revise, reject, or leave unresolved**, and it names any D1-specific rules that follow from D2's standing principles. He sees what will govern the work before the work starts.
- **His control points** — the operating relationship settled earlier carries over by default; here D2 flags only the *material exceptions* — the specific places in this design that warrant extra visibility, a Review Stop, or D2 pausing for his judgment.

He is meant to move through this quickly: accept the framework as proposed, change selected parts, ask D2 to investigate something first, or raise a concern to discuss. Nothing here demands a heavy sit-down; the point is that the *shape and rules of the work are visible and his to shape* before momentum builds.

**Why D2 works this way.** The constitution has D2 "prepare a proposed D1 Design Operating Framework for low-cost Designer review and confirmation" — one consolidated package, not a scattering of decisions — and keeps his normal action to "accept the proposed framework, modify selected parts, request investigation, or discuss a material concern" (Phase 4, Item 1). Deciding *how* the design will run is exactly the high-leverage, low-frequency choice his attention is for: settle the frame once, cheaply, then let D2 carry it out (Phase 2).

---

## 9. Inspecting, monitoring, and intervening  [A]

*Active involvement — derived from Phase 4 Item 3; the single interaction point is Phase 2, Principle 3. **This section is written in the target register; §1–§8 will be revived to match.***

Everything before this is **passive**: the Designer reacting to what D2 brings him. This is the **active** counterpart — what he does on his own initiative, unprompted, whenever he wants. It is the harder side to pin down. Passive involvement takes a few static, near-universal forms (a review, a clarification); active involvement is fluid and varies with the project, so we cannot pre-enumerate it. What we *can* do — and what the foundation's own query examples let us do — is abstract the **common likely elements** and support those, accepting that the list stays open.

**The invariant — one channel.** However he reaches in, the model is fixed: *ask, inspect, drill down, intervene*, in natural language through the single D2 interaction point (the D2 Assistant, R-07). He never names the Design Node, authority, data location, or service behind his question; D2 carries the burden of locating the relevant state, interpreting the request, and routing any resulting action through governance. This channel is the static, always-present part of the active side. → Designer action **A-007**, D2 support **C-20**.

**What he watches — the monitoring subjects.** The foundation's illustrative queries, though explicitly "not a command vocabulary," cluster into a small set of recurring subjects — and the clustering *is* the abstraction. Across projects he will want to watch:

- **The design itself** — the emerging D0 design and the D1 structure: *"show me the proposed D0 directory structure," "explain Algorithm A and how it differs from V1," "show me the Design Tree."* Ordinary inspection, already carried by the channel. → A-007 / C-20.
- **Progress** — how far the work has advanced and how it is moving: *"how far has the work advanced," "which nodes required the most revisions," "what changed since my last review."* → new **A-052** / **C-34**.
- **Resource and cost spend** — *"how much time has design consumed so far," "how much has it cost," "which nodes have consumed the most time or cost."* → new **A-053** / **C-35**.
- **Health and risk** — *"are any parts of the process behaving abnormally," "why has this branch been rejected so many times," "which unresolved issues are most likely to affect major parts."* → new **A-054** / **C-36**.

Progress, spend, and health are exactly the active elements the coverage check found *unabstracted* — real, recurring, named in the foundation, yet previously folded into generic inspection. They rest on the observation-data D2 provisions at setup (**C-19**). Naming them as first-class subjects is the substance of this section.

**What he does about it — the intervention modes.** Having looked, he may act, in one of three forms the foundation names:

- **Inquiry / inspection** — explain, report, trace, show, compare. → A-007.
- **Investigation / concern** — have D2 critically examine a suspected problem and recommend action: *"investigate whether the D0 directory structure is becoming unnecessarily complicated."* → A-008.
- **Directive** — exercise authority: *"do not allow Algorithm A to change without my approval," "stop the implementation branches until I review the verification design."* → A-009.

One rule governs D2's handling: an intervention **normally initiates investigation rather than directly mutating the design** — D2 interprets the concern, finds the affected objects and their authority, investigates, then either acts on its own or prepares a decision for him. Explicit authority directives (stop a branch, reserve approval) are recognized as authority actions and applied promptly. All of this flows through the one channel, **C-20**.

**The open edge.** This is deliberately an open list. The specific things a Designer asks are unbounded and project-dependent; D2 supports the recurring *subjects* (design, progress, spend, health) and *modes* (inquire, investigate, direct) the foundation lets us anticipate, and interprets any novel natural-language request against them. It does not pretend to pre-enumerate every project's active concern — which is exactly why the channel is natural-language and D2, not the Designer, carries the interpretive burden.
