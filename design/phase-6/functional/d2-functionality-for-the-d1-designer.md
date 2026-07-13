# Phase 6 — What D2 Does for the D1 Designer

*Phase 6 describes the functionality of the **D2 product**, organized by **what the D1 Designer does** with it. Section 1 sets out the method; the sections that follow walk his work step by step.*

---

## 1. Methodology

This project produces a **D2 product**: the design system the D1 Designer will use. He uses the D2 product to design his **D1** system, which in turn produces the distributable **D0** product (**D2 → D1 → D0**). Phase 6 describes that product's functionality by matching it to **what the D1 Designer does** with it. We take his work step by step; at each step we state the functionality D2 gives him to make that step easy, and we justify it from the constitution (Phases 1–5). One test governs throughout: **write only what the D1 Designer cares about.** How anything is stored or built is out of scope — it matters only insofar as it lets him do his work.

**Two classes of Designer action.** Everything the D1 Designer does is one of two kinds, and the constitution already treats them separately (Phase 4):

- **Passive actions — he responds to D2.** D2, driving the design as his assistant, brings him something: a proposed direction, a decision that needs his judgment, a finished report. He reacts — accepts, adjusts, or redirects. D2's job here is to bring him the *right* thing at the *right* moment, already worked through, so his response is cheap. *(Phase 4, Item 2 — passive intervention.)*
- **Active actions — he acts on his own initiative.** Unprompted, he reaches into the project: monitor the progress of the design, monitor the system being designed, inspect any part, drill down, or lay down a rule. D2's job here is to keep the whole project open to him — to let him look wherever he wants and act whenever he wants, through one place, without needing to know how D2 is organized inside. *(Phase 4, Item 3 — active inspection and intervention.)*

**The D0 user is always in view.** Cutting across both classes is the D1 Designer's own purpose: he designs the D1 system in order to **serve the D0 users** — the operators and users of the distributable product that D1 produces. So he designs with **D0-user optimization in mind**: the product should be as convenient and well-optimized for the D0 roles as it can be. This gives him a standing set of **key considerations for the D1 design** — what he weighs when deciding what the D1 system must do for its users. D2's functionality, in turn, exists to let him hold those considerations and act on them; the sections below surface them where each step of his work brings them into play. *(Phase 5, Item 3 — Human Position First.)*

**What the rest of this document covers.** The sections follow his work in order. Each is tagged by the class of action it primarily serves — **[P]** passive, **[A]** active.

2. **The entry point — deciding whether to use D2** [P] — his first decision (adopt the D2 product for this design?); D2 backs it by orienting him with the concepts the decision needs. *(Phase 1; Phase 2.)*
3. **Setting up the run — the roles table** [P] — D2 establishes the cast of roles the design recognizes, each marked by provenance (intrinsic to the ecosystem vs. a Designer-changeable default). *(Phase 5, Item 3.)*
4. **Setting up the run — default design choices** [P] — D2 offers a high-level **posture** (e.g. Standard / High Harness / Lean); one choice settles the run's many low-level knobs, and he can inspect, compare, or override any of it. *(Phase 3, Item 1.)*
5. **Giving D2 the starting point** [P] — he hands over the existing system and says, however roughly, what he wants changed; D2 makes sense of incomplete, informal input so he never writes a full specification. *(Phase 1 §4; Phase 3, Item 2.)*
6. **Understanding the proposed direction before he commits** [P] — D2 studies the system and his intent, resolves what it can, and hands back a clear understanding and a proposed direction to react to — not a pile of open questions. *(Phase 3, Item 3.)*
7. **Setting the design in motion** [P] — D2 proposes how it means to conduct the design — the shape of the work and the rules it will follow — as one thing he can accept, adjust, or push back on. *(Phase 4, Item 1.)*
8. **Overseeing the work without drowning in it** [P] — D2 carries the design forward and brings him only the high-leverage decisions, stopping for review where it matters and proceeding on its own where it doesn't. *(Phase 2; Phase 4, Item 2.)*
9. **Inspecting, monitoring, and intervening** [A] — on his own initiative he watches progress and the emerging system's health, asks in plain terms, drills down, redirects, or lays down a rule — all through one place. *(Phase 4, Item 3; Phase 5, Item 1.)*
10. **Being asked only when it's worth it** [P] — when D2 needs his judgment it gathers its questions and asks once; when work is done it reports in his terms, not machine records. *(Phase 2.)*
11. **Checking how well D2 served him** [A] — afterward, D2 shows him what the process cost him — his time, his attention, where it went — and where it could serve better next time. *(Phase 3, Item 5.)*

*Sections 6–11 are to be written in the same style as Sections 2–5 below.*

---

## 2. The entry point — deciding whether to use D2

Before any run, the D1 Designer faces one prior decision: **shall I use the D2 product at all to carry out this design?** Nothing else happens until he says yes, so this is where his journey with D2 begins.

That decision needs backing — so D2's first job is not to configure anything but to **orient him**, giving him just enough to decide well:

- **what D2 is** — a meta-design system he drives, and what using it will (and won't) ask of him;
- **the layer model** — that the D2 product helps him build a **D1** system which produces the distributable **D0** product, and where his own authority sits in that chain;
- **the roles in play** — the cast the design will recognize (the roles table, §3), so he can see whom D2 works on behalf of and whom the product ultimately serves;
- **what D2 will do for him** — the shape of the work ahead (the rest of this document, in brief).

He is never handed a manual to study; D2 surfaces only what this decision needs, in his terms, and he can ask for more on any point. Only once he decides to proceed does setup begin.

**Why D2 works this way.** The decision to adopt D2 is the Designer's alone — his authority and his limited attention are the top priorities (Phase 1) — so D2 owes him an honest, compact basis for the choice rather than presuming adoption. Orienting *before* configuring also follows progressive disclosure: show what the current decision needs and no more (Phase 2), keeping his first encounter with D2 a single clear judgment, not a study exercise.

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
