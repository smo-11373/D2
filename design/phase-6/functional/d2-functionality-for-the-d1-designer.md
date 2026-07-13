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

*Revival in progress: §1, §2, and the active-interaction reference are in this register; §3 (setup) is next, and later coverage stays fluid.*

---

## 2. The entry point — deciding whether to use D2  [P]

*Derived from Phase 1 (Designer authority & attention); Phase 2 (progressive disclosure).*

Before any run, the Designer stands at a gate that has nothing to do with his particular project: **should I use the D2 product to carry out this design at all?** It is the first thing he does, and until he decides yes, nothing else happens. It is also the most anticipable step in the whole document — every Designer faces the same question and needs the same *kinds* of information to answer it, whatever he is building.

**The Designer action.** One action, with a decision at its centre: **evaluate D2 and decide whether to adopt it** for this design — adopt, decline, or defer. → Designer action **A-055**.

**The common element — what he needs in order to decide.** The decision is his, but he cannot make it blind, and what he needs is the same across projects. Four things:

- **What D2 is** — a meta-design system he drives, and what using it will and won't ask of him.
- **The layer model** — that D2 helps him build a **D1** system which produces the distributable **D0** product, and where his own authority sits in that chain.
- **The roles in play** — the cast the design will recognize (the roles table, §3), so he sees whom D2 works on behalf of and whom the product ultimately serves.
- **What D2 will do for him** — the shape of the work ahead, in brief (the rest of this document).

**The D2 support.** D2 provides an **orientation**: it surfaces exactly those four things, in the Designer's own terms and at the depth he asks for — a short, honest basis for the decision, never a manual to study. He can probe any point and get more; nothing that matters is hidden, nothing is forced. Only once he decides to proceed does setup begin. → new capability **C-37** (adoption orientation), an application of progressive disclosure.

**Why this shape.** The decision to adopt D2 is the Designer's alone — his authority and his limited attention are the top priorities (Phase 1) — so D2 owes him a compact, honest basis rather than presuming adoption. Orienting *before* configuring is progressive disclosure in its first application: show what this decision needs, and no more (Phase 2).

**The open edge.** What finally moves a given Designer to adopt — his risk tolerance, his existing tools, his deadline — D2 cannot know or support; it supplies the common orientation every such decision needs and leaves the judgement itself to him.

---

## 3. Setting up the run — the roles table

With D2 adopted, the Designer's first setup step is to establish *who is in the ecosystem*: the set of **roles** the design recognizes. D2 sets this up as a **roles table** he can read at a glance and adjust — everything downstream (what gets designed, what controls the product exposes, who is asked what) follows from it.

**The D1 product wraps the D0 product.** What the run ultimately produces is a *distributable D1 package*: the **D0 product** — the actual application — wrapped in a thin **D1** layer that adds health/crash monitoring, an upgrade smoke-test suite, and upgrade records ("half a level above D0"). Delivery is a **human decision**: the package is handed to the **IT Manager** (D1 Technical Manager, R-04), who unpacks it, extracts the D0 within, and deploys D0 into production — keeping the D1 wrapper to monitor and upgrade it. From there the **D0 Operator** (R-05) runs it day to day. This chain is why Section 1's throughline holds: the Designer designs the D1 system, but its *primary beneficiary is the D0 Operator* at the far end.

**The D2 Assistant is a role in its own right.** The design is conducted for the Designer by the **D2 Assistant** (R-07) — a non-human, LLM-based role that is his *single point of contact* with the entire D2 system. He never addresses a Design Node, an authority, or a service directly; he speaks to the D2 Assistant in plain design terms, and it reaches whatever is needed on his behalf. *(Phase 4 — the unified D2 interaction point.)*

**The roles.** Each is marked by provenance — intrinsic to the ecosystem, or a D2-provided default the Designer can change:

| Role | What it is | Provenance |
|---|---|---|
| **D1 Designer** (R-01) | The human the ecosystem serves; sole design authority | **Intrinsic** — fixed |
| **D2 Assistant** (R-07) | Non-human LLM; the Designer's single point of contact; conducts the design on his behalf | **Intrinsic** — fixed |
| **IT Manager / D1 Technical Manager** (R-04) | **A human** who receives the delivered D1 package, unpacks it, extracts D0, deploys it to production, and runs the wrapper (monitoring, upgrades) | **Default** — Designer-changeable |
| **D0 Operator** (R-05) | Runs the deployed D0 in production; D1's primary beneficiary | **Default** — Designer-changeable |
| **D0 Technical Manager** (R-06) | Front-line install and technical support of a D0 deployment | **Default** — Designer-changeable |

**D2-internal working agents — an open area.** Separately from those roles, D2 does the design work through **internal agents**. The **Design Node Builder** (R-02) that builds one bounded design node is really just *one kind of agent*; there will likely be **others** — an agent that enforces a standard, an agent that does integration, and so on — alongside the **D1 Programmer** (R-03) that writes the D0 code. How many agents, how many *types*, and how the Designer would even specify them, is **left deliberately open at this stage** — we keep an open mind rather than fix a taxonomy before it is justified (*Top-to-Bottom*). These are D2's own labor, not roles the Designer configures.

**Why D2 works this way.** The constitution designs by **human role first** (Phase 5, Item 3 — "Human Position First"): controls, monitoring, and behavior are all shaped by which role they serve — so the role set is the natural first thing to set up, the frame the rest of the design hangs on. Marking provenance keeps intent legible (the provenance principle): the Designer always sees what the ecosystem fixed versus what D2 merely seeded and he can change.

---

## 4. Setting up the run — default design choices (the posture)

With the roles settled, the Designer's next setup step is to choose *how the run will be conducted*. He wants this to be easy: to get going from a good default, not to fill in a configuration document.

So D2 offers him **default design choices**. It presents a small number of high-level **postures** — for example *Standard*, *High Harness*, or *Lean* — and he picks one, or simply accepts the one D2 recommends. That single choice settles the many things a run would otherwise make him configure: how he and D2 will work together, how much harness and monitoring to expect, how deeply to investigate and evaluate, how much to report, when to stop for his review, how much resource to spend. He chooses the posture; D2 works out the detailed consequences.

The choice stays compact and human-oriented — a short selection, not a settings file. He is never forced to look deeper, but nothing that matters is hidden from him: if he wants, he can see what a posture entails, compare it against another, ask why a particular setting came out the way it did, or change any part before continuing. And because he may want to revisit how the run was set up, D2 keeps his setup as one thing he can return to, review, and revise — with his own changes plain to see.

**Why D2 works this way.** His time and attention are the scarce resource (Phase 1 §2.3), and his attention belongs on high-level design, not low-level configuration (Phase 1 §2.5). So D2 supplies the defaults and asks him only for a high-level choice — "the normal action should often be to accept the defaults" (Phase 3, Item 1) — resolving the rest itself (Phase 2, Principle 1). Making setup a single easy choice is D2 serving him exactly as the constitution requires.

---

## 5. Giving D2 the starting point

With the run set up, the Designer gives D2 what it needs to begin: **the existing system, and — however roughly — what he wants changed.** This is the one moment he must supply something of his own, so D2's whole job here is to make that as light as possible: to take incomplete, informal input and do the work of making sense of it, so he never has to write a full specification.

He hands over two things, neither required to be complete:

- **The predecessor system** — whatever exists and can be studied: the running system, source, documentation, tests, environments, datasets, usage examples. He points D2 at the material; he does not curate or explain it.
- **His intended change** — in any form that is useful *to him*: a revision note, rough jottings, a bug list, user complaints, desired features, a prior discussion, a prototype idea, examples of behavior he dislikes, or just a general direction.

From there D2 does the making-sense. It **investigates the predecessor deeply** and biases toward resolving ambiguity on its own, returning to him for clarification only where investigation genuinely cannot settle a material point — and then batching that into a few worthwhile questions rather than a stream of small ones. The existing system is not merely a starting point but an **unusually strong source of harness** (Phase 5, Item 1): D2 mines it for representative behavior, expected input–output pairs, and constraints the successor should keep. What this step produces is a *sufficient initial direction* to begin governed design — not a finished specification, and explicit open questions may remain.

Because his intended change so often speaks *for the D0 users* — their complaints, the features they want, the behavior that fails them — this is also where the **D0-user considerations of Section 1 first enter the design**, carried in his own words rather than a form.

**Why D2 works this way.** The constitution forbids demanding a complete spec up front: "D2 shall not require the intended change to be fully specified" and "should actively assist the Designer in developing a sufficiently clear initial upgrade direction" (Phase 3, Item 2). His scarce resource is attention (Phase 1), so D2 investigates first and asks second — spending its own effort to spare his — and accepts his input in whatever form costs him least. Early discussion is welcome precisely when it prevents far larger downstream Designer Attention Cost (Phase 3, Item 2).

---

## 6. Understanding the proposed direction before he commits

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

## 7. Setting the design in motion

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
