# UX Layout — how each action is *experienced*, per position

*The Experience (UX) node's deliverable. Derived from the inherited action aggregate
(`../environment/action-aggregate/role-action-catalog.md`, read-only) and the fundamentals
(constitution Phases 1–5 + `completions.md`, `method §1`, `RU-*`, `framework/`). Format is v0/fluid.
Structure: **the two experience surfaces → the pattern catalog → the full action→pattern coverage map →
the attention accounting → the self-check.***

---

## 0. Orientation — two surfaces, one interaction point

The 63 actions are experienced across **two distinct surfaces**, and keeping them distinct is itself a
conformance requirement (Phase 2 §Principle 3; `completions.md C-2026-07-19-1`):

- **Surface I — the Designer's experience *of D2*.** Everything the **D1 Designer (R-01)** does, he does
  through **one medium: the D2 Assistant (R-07)** — the single, unified point of contact. He never
  addresses a Design Node, a governing authority, or a service directly (Phase 4 §Item 3). The
  **D2 Designer (R-00)** touches a narrow meta-authoring variant of the same surface (he *builds* D2's
  living sets; he is not a D2 user). **This is where the Designer's scarce attention is spent, so this is
  where the design works hardest** (Phase 1 §2.3).

- **Surface II — the product's experience by the downstream cast.** The **D1 Programmer, D1/D0 Technical
  Managers, and D0 Operator** experience the **D1/D0 product**, not D2's Assistant. Human Position First:
  each position gets *exactly* the information and controls its responsibility needs, and no more
  (Phase 5 §Item 3). **None of this costs the D1 Designer any attention** — it is a different human at a
  different position (see §4, the accounting).

Between them sits an **internal, Designer-invisible layer**: the **Design Node Builder (R-02)** doing D2's
own design work inside a bounded sandbox. Its only Designer-visible *projection* is Surface I's passive
forms (a Review Stop, a Clarification Request, a report) — never a direct interface.

### The experience archetypes (the "handful of forms")

Method §1 says passive actions take *"a few static, near-universal forms"* and active involvement its own
few forms. The whole 63-action space collapses onto **~10 recurring archetypes** that *reappear across
surfaces and positions at different altitudes* — e.g. the single **Monitoring** archetype serves the
Designer's progress view, the operator's health light, and the technical manager's wrapper dashboard
(Phase 5 §Item 3: *"the same underlying event represented differently for different positions"*). That
recurrence is the abstraction doing its job — one well-designed form, many instantiations, rather than 63
bespoke screens.

| # | Archetype | Class | Default direction |
|---|---|---|---|
| **X1** | Unified Assistant Surface (the medium) | structural | — |
| **X2** | Internal Work Sandbox (Designer-invisible) | structural | — |
| **P1** | Review Stop | passive | push, optional |
| **P2** | Clarification Request | passive | push, required |
| **P3** | Report / Notification | passive | push→pull, ambient |
| **P4** | Prepared-Choice / Configuration | passive-choice | push package, pull to revise |
| **P5** | Orientation / Decision Support | passive-choice | pull |
| **P6** | Intake / Input Provision | active-input | pull (Designer supplies) |
| **P7** | Monitoring View | active | pull; push only on anomaly |
| **P8** | Inspection / Drill-down | active | pull |
| **P9** | Investigation / Concern | active | pull |
| **P10** | Directive / Authority Action | active | pull |
| **P11–P20** | Product-side operational forms (Human Position First) | product | mixed |

---

## 1. Surface I — the Designer's experience of D2 (via the Assistant)

### X1 — The Unified Assistant Surface *(the medium, not a screen)*

**Covers R-07:** A-062 (conduct design + answer queries), A-063 (interpret & route input, preserve
context), A-064 (present Designer-oriented output with drill-down).

The Assistant is not one more pattern the Designer chooses among — it is the **conversational fabric that
renders every other Surface-I pattern**. The Designer expresses any request in natural language; the
Assistant bears the burden of locating the design state, interpreting, routing to the right internal
function, and returning a human-framed result (Phase 2 §4.1–4.3; Phase 4 §Item 3). A-064 is literally the
rendering engine behind P1/P2/P3/P7/P8 — Review Stops, Clarification Requests, reports, monitoring views,
and drill-downs are all *presented through it*.

- **Pull or push:** neither — it is the channel; it carries push (P1/P2/P3) and pull (P6–P10) alike.
- **Attention cost:** the Assistant's *purpose* is to drive total attention cost down (routing,
  context-preservation, and consolidation are D2's burden, never the Designer's — he never re-states
  context for different recipients, Phase 2 §4.3).
- **Fundamentals honored:** Unified interaction (P3); D2 owns routing (§4.2); human-oriented output (Phase 1
  §2.4). **Provenance:** whatever the Assistant presents keeps the Phase 1 §4.6 distinctions visible
  (Designer intent vs observed predecessor behavior vs D2-derived evidence vs inference) — the surface must
  never silently launder inference into intent.

### P1 — Review Stop *(passive, push, optional)*

> "*I have completed [X] and stopped to give you an opportunity to review. Review now, or continue?*"

**Covers:** A-014 (review initial understanding — *"A Review Stop"*), A-005 (review a node / "continue"),
A-057 (confirm the D1 Constitution — *a key, strongly-encouraged Review Stop*), A-001 (accept the proposed
framework — the low-cost accept-and-continue), A-061 (R-00: adopt/reject post-run audit proposals).

- **Low-cost default:** *continue / accept* — a single gesture, no obligation to look. D2 has already
  converged internally before stopping (Phase 3 §Item 3; Phase 4 §Item 2).
- **Drill-down:** on request, expand into the underlying report (→ P3) and inspection (→ P8).
- **Attention cost:** near-zero by default; **weighted to node height** — higher/governing nodes (the
  Constitution) earn a stop; low implementation nodes proceed with autonomy and don't stop the Designer
  (Phase 4 §Item 2, *"attention should generally increase with node height"*). This is the primary
  leverage-gating lever on passive review.
- **Fundamentals:** Phase 3 phase-wide rule (Review Stop as a control boundary, distinct from a
  Clarification Request); Phase 4 §Item 2.

### P2 — Clarification Request *(passive, push, required)*

> "*I need your judgment on [material issue]; here are the alternatives, consequences, and my
> recommendation.*"

**Covers:** A-018 (answer a Clarification Request — the Designer's answering side).

- **Low-cost default:** none by definition (this is the one form that genuinely *requires* the Designer) —
  so the design's whole job is to **make it rare and high-value.** D2 investigates first and only escalates
  when Designer judgment has enough design value to justify the attention cost (Phase 2 §Principle 1,
  §2.1). Questions are **consolidated** into one high-leverage request where practical (Phase 4 §Item 2),
  and pitched at the **highest governing level** — ask for the principle/invariant/tradeoff that settles
  many lower questions, not the many questions (Phase 2 §2.3; Phase 1 §2.5).
- **Drill-down:** each option carries its rationale, consequences, and requested action (Phase 1 §2.4);
  the Designer can expand any into P8 before answering.
- **Attention cost:** the highest per-instance cost of any Surface-I form — therefore the most tightly
  rationed. Distinct from P1: a Review Stop asserts no open question; a Clarification Request does.

### P3 — Report / Notification *(passive, push→pull, ambient)*

> "*[Item] is complete. Result recorded.*" — response optional.

**Covers:** the ambient completion-report layer under every item (Phase 3 phase-wide rule), and the
delivery vehicle for results the Designer *chose* to request — the audit report (A-020's review leg) and
the impact-evaluation report (A-058's report leg).

- **Low-cost default:** *don't read it* — every item is **observable** but only some **demand attention**
  (Phase 3: *"reporting boundaries and intervention boundaries are distinct"*). The report sits ready; the
  Designer pulls it if and when he wants.
- **Drill-down:** a summary that expands to detail on request (Phase 2 §3.2/§3.4) — never raw machine
  records, transcripts, or internal reasoning by default (Phase 1 §2.4).
- **Attention cost:** ~zero unless pulled. This is the low-salience floor that makes the process
  observable without spending attention.

### P4 — Prepared-Choice / Configuration *(passive-choice: push a prepared package, pull to revise)*

> "*Here is the proposed [contract / posture / framework / roles table]. Accept, compare, or adjust.*"

**Covers (R-01):** A-012 (confirm operating contract), A-015 (select posture — *one choice → many
settings*), A-016 (review/revise the setup package), A-017 (revise setup material later, governed),
A-056 (review/adjust the roles table), A-002 (modify parts of the framework), A-019 (tune resolution
depth / intervention posture). **Covers (R-00, meta-authoring variant):** A-010 (complete/clarify/expand
D2's living sets — low hurdle), A-011 (revise persistent sets through the explicit process).

- **Low-cost default:** **accept the prepared defaults.** D2 always supplies reasonable defaults so
  extensive configuration is never *required* (Phase 3 §Item 1). Posture is the key leverage device — a
  single high-level choice (Standard / High-Harness / Lean) expands into many detailed settings the
  Designer needn't touch individually (A-015). A-019 tuning is the same lever moved mid-run.
- **Drill-down:** **progressive disclosure** — the package presents as a short checklist/selection table,
  expandable to any setting; later governed revision (A-017) shows impact analysis and preserves history.
- **Pull/push:** D2 *pushes* the prepared package (so the Designer starts from a good default, not a blank
  form); the Designer *pulls* only the parts he wants to change.
- **Attention cost:** **front-loaded and one-time**, collapsible to a single "accept" gesture. The
  R-00 meta-variant (A-010/A-011) is authoring, not a D2-user cost — it belongs to the builder.
- **Fundamentals:** Phase 3 §Item 1 (compact, human-oriented, defaults-first); Phase 5 §Item 2
  (Designer-originated completion at a low hurdle); §Item 3 (position-oriented configuration).

### P5 — Orientation / Decision Support *(passive-choice, pull)*

**Covers:** A-055 (evaluate D2 and decide whether to adopt it — adopt/decline/defer).

- **Low-cost default:** the **choice stays the Designer's**; D2 only *orients* him with the concepts the
  decision needs — it does not push adoption. Pull: the Designer engages when deciding.
- **Attention cost:** a single entry-point decision, supported not demanded.

### P6 — Intake / Input Provision *(active-input, pull)*

**Covers:** A-013 (provide the initial design input — Predecessor D1 package + intended change).

- **Experience:** the Designer supplies material in *any useful form* — a revision doc, rough notes, a bug
  list, complaints, general direction — and points D2 at the predecessor package. **D2 bears the
  translation burden** (Phase 1 §4.3; Phase 3 §Item 2); the Designer is never asked to restate unchanged
  portions (Phase 1 §3.4) nor to hand over a complete spec.
- **Low-cost default:** loose, incremental, incomplete input is accepted; open questions may remain.
- **Attention cost:** proportional to how much the Designer *wants* to say; the floor is low by design.

### P7 — Monitoring View *(active, pull; push only on anomaly)*

> A standing, at-a-glance view of process state, progress, spend, and health.

**Covers:** A-052 (monitor progress — advancement, changes since last review, revision counts),
A-053 (monitor resource & cost — cumulative & per node), A-054 (monitor process health & anomalies —
abnormal behavior, rejection loops, high-impact open issues).

- **Pull/push:** **pull by default** — the Designer looks when *he* decides oversight is warranted, not
  dependent on D2 first flagging a problem (Phase 2 §Principle 2, §3.3). **Push is reserved for
  anomalies** — A-054's abnormal behavior/rejection-loops surface as an alert that can escalate into an
  Investigation (→ P9 / A-008).
- **Low-cost default:** a compact health/progress indicator; no action implied by a green state.
- **Drill-down:** the view is the *entry* to progressive investigation (Phase 2 §3.4) — from the indicator
  into P8/P9. Observability is *"not merely passive reporting… a means of enabling informed
  Designer-initiated intervention."*
- **Attention cost:** Designer-paced and self-throttled (pull); makes state/health/deviation **visible**
  (Phase 5 §Item 1; Phase 2 §Principle 2) so the Designer is never dependent solely on D2's own judgment
  of when he's needed.

### P8 — Inspection / Drill-down (Inquiry) *(active, pull)*

> "*Show me… / explain… / trace… / compare…*" — against any design or process state.

**Covers:** A-007 (inquiry / inspection — explain, report, trace, show, compare design or process state).

- **Experience:** ask → inspect → drill down, in natural language, without naming the internal node, data
  location, or service that holds the answer (Phase 4 §Item 3 — the Assistant routes). Progressive depth:
  high-level view first, deeper detail on request.
- **Pull/push:** pure pull, Designer-initiated and self-budgeted.
- **Attention cost:** entirely discretionary — the Designer spends exactly as much as he chooses.

### P9 — Investigation / Concern *(active, pull → returns a recommendation)*

> "*Critically examine [suspected problem] and recommend an action.*"

**Covers:** A-008 (investigation / concern), A-058 (evaluate a proposed change — impact dry-run, probe up
& down, get a report), A-020 (request/review the optional D2 audit — *"did D2 design D1 well?"*),
A-004 (discuss a material concern — Designer-initiated).

- **Experience:** the Designer raises a concern; **D2 initiates investigation rather than directly mutating
  the design** (Phase 4 §Item 3) — it interprets the concern, identifies affected objects/authority,
  investigates, and returns a recommendation or a prepared decision (delivered via P3/P1). A-058 is the
  *commits-nothing* dry-run (RU-06); A-020 turns the lens on D2's own process.
- **Pull/push:** pull; the *result* returns as a report (P3) or a decision point (P1).
- **Attention cost:** discretionary to launch; the heavy lifting is D2's, so the Designer's cost is the
  concern in + the recommendation out, not the investigation itself.

### P10 — Directive / Authority Action *(active, pull; applied promptly)*

> "*Do not allow Algorithm A to change without my approval." / "Stop the implementation branch until I
> review the verification design.*"

**Covers:** A-009 (Designer directive — impose, revise, reserve, suspend, exercise authority), A-006
(reserve/assign revision authority over a design object).

- **Experience:** explicit authority actions are **recognized as authority actions and applied promptly**
  (Phase 4 §Item 3) — distinct from an inquiry or a concern, which initiate investigation. A-006 sets a
  *continuing* governance property (which nodes are Designer-governed vs D2-governed), distinct from the
  one-off review event (A-005/P1) — so review history and revision authority are represented separately
  (Phase 4 §Item 2).
- **Pull/push:** pull; the Designer steers on his own initiative (Phase 2 §Principle 2).
- **Attention cost:** small per act; this is the Designer converting attention into *durable* control —
  high-leverage because one reservation governs a whole region without repeated intervention (Phase 1
  §2.5).

---

## 2. Surface II — the internal work sandbox (Designer-invisible)

### X2 — Internal Work Sandbox

**Covers R-02 (Design Node Builder):** A-021 (investigate predecessor/reference), A-022 (develop, compare,
critique candidates), A-023 (produce the node design spec), A-024 (internally evaluate before submission),
A-025 (submit for acceptance), A-026 (propose a spawning strategy), A-027 (propose upward revision),
A-060 (establish the verification harness / derive evidence *before* committing — Harness First).

- **Experience:** this is the Builder's **bounded contract environment** (Phase 5 §Item 5, module as
  conceptual sandbox): contract-in (its inputs, harness, permitted actions, acceptance boundary), local
  autonomy inside, submission-package-out. It is a *work* surface, not a Designer UX.
- **Designer-visible projection:** **none directly** — the invariant is that the Designer never addresses
  the Builder (Phase 2 §4.1; `C-2026-07-19-1`). The Builder's work reaches the Designer *only* re-cast
  through Surface I: a completed submission becomes a **Review Stop** (P1) or **Report** (P3); an
  unresolvable material question becomes a consolidated **Clarification Request** (P2); an upward proposal
  (A-027) is resolved by D2 autonomously if the affected node is D2-governed, or prepared as a
  Designer decision (P1/P9) if Designer-governed (Phase 4 §Item 2).
- **Attention cost to the D1 Designer:** **zero**, except where the Builder's work legitimately surfaces
  as P1/P2/P3 above. A-060's harness-first bias is what *keeps* it near zero — deviation is caught inside
  the sandbox, before it needs the Designer (Phase 2 §Principle 4; Phase 5 §Item 1).

---

## 3. Surface III — the product experienced by the downstream cast (Human Position First)

*Experiences of the delivered **D1/D0 product**, not of D2's Assistant. Each form is designed for the
position that owns it, exposing exactly what that responsibility needs (Phase 5 §Item 3). The **same
archetype recurs** across positions at different altitudes — most visibly Monitoring (P14) and
Configuration (P15). These forms **cost the D1 Designer no attention** (§4).*

### P11 — Operational Console (run the product) *(product-side, active)*
**Covers R-05:** A-034 (routine operation — start, run, stop, schedule, pause/resume, cancel D0 jobs).
- **Experience:** a simple, non-technical control surface for the D0 Operator (*normally low technical
  understanding*). Low-cost default = the common operations one gesture away; advanced options tucked
  behind. Push: none (operator-initiated). **D0-Operator-first** — D1 is built for the operator's
  convenience first (catalog Primary-user principle; Phase 5 §Item 3).

### P12 — Results & Output View *(product-side, passive-pull)*
**Covers R-05:** A-044 (view D0 results, outputs, reports — *the point of running D0*).
- **Experience:** the operator's payoff view; human-framed, drill-down to detail. A specialization of the
  Report archetype (P3) for the product side.

### P13 — Notification & Routine Approval *(product-side, push, simple)*
**Covers R-05:** A-045 (acknowledge/respond to notifications, prompts, routine approvals from D0).
- **Experience:** the product-side sibling of P2 — but for *simple, non-technical* decisions within the
  operator's competence. Low-cost default: a clear ack/approve gesture; anything beyond competence routes
  to Support (→ P16).

### P14 — Health & Status Monitoring *(product-side, pull; per-position views of one event)*
**Covers:** A-035 (R-05: user-level "is it working & healthy?"), A-047 (R-05: routine activity, usage,
cost-to-date), A-033 (R-04: monitor D0 health & performance via the D1 wrapper — *half a level above D0*),
A-059 (R-06: standing, proactive deployment health/status).
- **Experience:** **one underlying health/telemetry stream, four position-shaped views** (Phase 5 §Item 3,
  *"the same underlying event represented differently for different positions"*): the operator sees a
  plain "healthy?" light and a usage/cost tally; the D1 Technical Manager sees wrapper-level
  health/performance; the D0 Technical Manager sees a standing operational-health view. Makes state/health
  **visible** (Phase 5 §Item 1); design health/monitoring *before* the thing monitored (Harness First,
  *monitoring before usage*). Distinct from reactive diagnosis (A-049/P17).
- **Pull/push:** pull; anomalies push to the responsible position.

### P15 — Position-Oriented Configuration & Governed Controls *(product-side, active)*
**Covers:** A-036 (R-05: operator controls — spending limits, scheduling, collection scope, approved
choices), A-038 (R-06: technical maintenance — deployment paths, storage endpoints, service config,
resource limits, credentials, health settings), A-029 (R-04: adjust a governed product parameter *without
touching code*).
- **Experience:** the product-side sibling of P4 — **each position gets the control boundary its
  responsibility warrants and no more** (Phase 5 §Item 3). A-029 is the concrete payoff of RU-01 (no
  hard-coded numbers): the D1 Technical Manager changes a governed value, then runs the harness (→ P19) —
  *"no code change does not mean no harness."*
- **Attention:** each position's own; work sits at the **lowest position** with the needed authority
  (Phase 5 §Item 3, position hierarchy reduces escalation).

### P16 — Support & Escalation Chain *(product-side, mixed)*
**Covers:** A-046 (R-05: handle routine, non-technical errors — retry/restart within competence),
A-048 (R-05: request front-line support / escalate to R-06), A-039 (R-06: provide front-line support),
A-051 (R-06: escalate to the D1 Technical Manager when beyond front-line).
- **Experience:** the **escape-hatch + hand-off ladder** — the low-technical operator handles what he can,
  then a single "get help" action hands off up the position hierarchy (operator → D0 Tech Mgr → D1 Tech
  Mgr). Each rung is a produce/receive hand-off with the context the next position needs. Do not escalate
  what a lower position can safely handle; do not delegate below the authority to judge it (Phase 5
  §Item 3).

### P17 — Diagnosis & Fix *(product-side, active, technical)*
**Covers:** A-049 (R-06: diagnose a deployment issue), A-050 (R-06: apply a fix/patch/config change within
the established design), A-041 (R-03: diagnose & fix implementation defects within the spec).
- **Experience:** the technical remediation surface — reactive, distinct from standing health monitoring
  (P14) and from support triage (P16). Bounded: fixes stay *within the established design / spec*, no
  product redesign.

### P18 — Install / Deploy / Package & Release *(product-side, lifecycle)*
**Covers:** A-037 (R-06: install a deployment), A-032 (R-04: deploy D0 into production, optionally
retaining D1), A-031 (R-04: update release state, repackage, distribute).
- **Experience:** the build-out/lifecycle surface. Deployment can be **D0-only while retaining D1** to
  manage/upgrade it (glossary `d1`). A forced lifecycle hand-off: *package → install → deploy* each has an
  owning position and a verification gate (→ P19).

### P19 — Upgrade Validation & Recovery (the D1 wrapper harness) *(product-side, harness)*
**Covers R-04:** A-030 (run the upgrade validation / regression smoke-test harness), A-042 (roll back to a
previous release on a failed upgrade), A-043 (review upgrade records / release history).
- **Experience:** the **wrapper's Harness-First surface** — the half-level-above-D0 safety apparatus:
  run the smoke-test suite before/after an upgrade, roll back on failure using the upgrade record, review
  release history. This is Verification Before Realization made operational (Phase 2 §Principle 4;
  Phase 5 §Item 1; glossary `d1`). Every parameter change (A-029/P15) and deploy (P18) passes through it.

### P20 — Implementation Work Surface *(product-side, dev)*
**Covers R-03:** A-028 (implement D0 code from the implementation specification), A-040 (write & run
implementation-level tests against the code).
- **Experience:** the Programmer's dev surface. The ideal handoff: the spec is complete enough that the
  Programmer implements **without reconstructing the design** (Phase 5 §Item 3, design-to-programming
  handoff). Tests (A-040) are the position's own harness rung.

---

## 4. Attention accounting — where the Designer's budget goes

*Attention accounting is the D2 priority (Phase 1 §2.3): the layout must make the **total** D1-Designer
attention cost legible so it can be optimised. The single most important fact:*

### 4.1 The concentration map — most actions cost the Designer nothing

| Bucket | Actions | Count | D1-Designer attention |
|---|---|---|---|
| **Surface III — product-side** (P11–P20) | A-028…A-051, A-059 (all R-03/04/05/06) | **25** | **zero** — other positions, other humans |
| **Surface II — internal builder** (X2) | A-021…A-027, A-060 (R-02) | **8** | **zero** — Designer-invisible; surfaces only as P1/P2/P3 |
| **Surface I meta — D2 Designer** (P4/P1 variant) | A-010, A-011, A-061 (R-00) | **3** | **n/a** — the *builder* of D2, not a D2 user |
| **Surface I — the D1 Designer's own actions** (X1, P1–P10) | R-01 + R-07 | **27** | **the entire budget lives here** |

**33 of 63 actions impose no D1-Designer attention at all.** The Designer's whole attention budget is
spent inside Surface I — and even there, most of it is *optional* or *pull*.

### 4.2 The Surface-I ledger — pull vs push, and the low-cost default

| Pattern | Pull / Push | Default cost | What concentrates attention |
|---|---|---|---|
| X1 Assistant | medium | — | none (its job is to *reduce* cost) |
| P1 Review Stop | **push, optional** | ~0 (accept/continue) | only the **high nodes** stop him (Constitution A-057) |
| P2 Clarification Request | **push, required** | the one unavoidable cost | **the peak** — rationed, consolidated, high-leverage |
| P3 Report/Notification | push→**pull** | ~0 (don't read) | none unless pulled |
| P4 Config/Setup | push package, **pull to revise** | ~0 (accept defaults) | **front-loaded, one-time**; posture collapses many settings to one |
| P5 Orientation | **pull** | 1 decision | entry point only |
| P6 Intake | **pull** | as much as he wants to say | floor is low (loose input OK) |
| P7 Monitoring | **pull**; push on anomaly | ~0 (green = no action) | Designer-paced; anomalies escalate |
| P8 Inspection | **pull** | discretionary | self-budgeted |
| P9 Investigation | **pull** | concern in / recommendation out | D2 does the work |
| P10 Directive | **pull** | small per act | converts attention into durable control |

### 4.3 Where total attention concentrates, and the levers to optimise it

- **The single peak is P2 (Clarification Requests).** It is the only form with no low-cost default, so the
  whole design pushes cost *away* from it: investigate-before-escalating (Phase 2 §2.1), consolidate
  questions, and pitch them at the governing level so one answer settles many (Phase 2 §2.3; Phase 1 §2.5).
- **A one-time front-loaded ridge at P4 (Setup).** Real but bounded and defaults-collapsible; the
  **posture** choice (A-015) and its mid-run tuning (A-019) are the master levers — one high-level setting
  governs many detailed ones, and A-019 lets the Designer re-balance investigation-depth vs attention cost
  at any time (Phase 2 §2.6).
- **Everything push-and-optional (P1, P3) or pull (P5–P10) is self-throttled** — the Designer spends
  exactly what his judgment says is worth it, which is the definition of leverage-gated attention
  (Phase 2 §Principle 1). Push is deliberately confined to P1/P2/P3 and P7's anomaly alerts; **all active
  oversight is pull**, so it never *imposes* cost.
- **The default posture of the whole surface is "accept / continue / don't look."** The Designer is
  *observably* in control of everything (P3 makes every item visible, P7 makes state/health/deviation
  visible) while *attending to* almost nothing unless he chooses — the Phase 1 §2.3 objective (reduce total
  cognitive burden, not merely interaction count) and the Phase 2 §2.5 balance (visibility without
  dependence on D2 self-reporting).

---

## 5. Self-check (contract §3)

**Conformance** — contradicts no governing statement:
- *Single interaction point:* the Designer touches only X1; X2 and Surface III are never Designer-facing
  interfaces (Phase 2 §4.1; `C-2026-07-19-1`). ✓
- *Attention is the priority, leverage-gated:* P2 rationed/consolidated/high-level; P1 weighted to node
  height; active forms all pull (Phase 1 §2.3, §2.5; Phase 2 §Principle 1). ✓
- *Human-oriented, progressive disclosure:* P3/P4/P8 summarise-then-expand; never raw records by default
  (Phase 1 §2.4; Phase 2 §3.2/§3.4). ✓
- *Observability:* P7 (Designer), P14 (product) make state/health/deviation visible without forcing
  attention (Phase 5 §Item 1; Phase 2 §Principle 2). ✓
- *Human Position First:* P14/P15 are per-position views/controls of one event; the support ladder respects
  the position hierarchy (Phase 5 §Item 3). ✓
- *Provenance:* Surface-I presentation preserves the Phase 1 §4.6 distinctions (intent / observed / derived
  / inference). ✓
- *Harness First / Verification Before Realization:* X2 (A-060) and P19 place monitoring/validation before
  and around realization (Phase 2 §Principle 4; Phase 5 §Item 1). ✓

**Coverage (gating)** — every one of the 63 inherited actions maps to ≥1 pattern; no orphan action, no
pattern without an owning action. Full map:

| Role | Actions → pattern |
|---|---|
| **R-00** | A-010→P4 · A-011→P4 · A-061→P1 |
| **R-01** | A-012→P4 · A-013→P6 · A-014→P1 · A-015→P4 · A-016→P4 · A-017→P4 · A-001→P1(+P4) · A-002→P4 · A-004→P9 · A-005→P1 · A-006→P10 · A-007→P8 · A-008→P9 · A-009→P10 · A-018→P2 · A-019→P4(+P10) · A-020→P9(+P3) · A-052→P7 · A-053→P7 · A-054→P7 · A-055→P5 · A-056→P4 · A-057→P1 · A-058→P9 |
| **R-02** | A-021…A-027, A-060 → X2 (all 8) |
| **R-03** | A-028→P20 · A-040→P20 · A-041→P17 |
| **R-04** | A-029→P15 · A-030→P19 · A-031→P18 · A-032→P18 · A-033→P14 · A-042→P19 · A-043→P19 |
| **R-05** | A-034→P11 · A-035→P14 · A-036→P15 · A-044→P12 · A-045→P13 · A-046→P16 · A-047→P14 · A-048→P16 |
| **R-06** | A-037→P18 · A-038→P15 · A-039→P16 · A-049→P17 · A-050→P17 · A-051→P16 · A-059→P14 |
| **R-07** | A-062→X1 · A-063→X1 · A-064→X1 |

63/63 mapped. Every pattern X1–P20 owns ≥1 action. ✓

**Quality** — each pattern is derived to minimise attention cost (a low-cost default + drill-down on every
Surface-I form), leverage-gated (P1 by height, P2 by consolidation/level, active forms by pull),
human-framed (X1/A-064 renders everything for design judgment), progressively disclosed (summary→detail),
and observable (P3/P7/P14). Distinctness is preserved (Review Stop ≠ Clarification Request ≠ Report;
Directive ≠ Investigation ≠ Inspection; Monitoring ≠ Diagnosis) while consolidation is real (one archetype
recurs across surfaces — Monitoring P7/P14, Configuration P4/P15, Notification P2/P3/P13). Per the
inclusion bias (contract §3, "when in doubt, keep"), plausible distinct forms were kept rather than merged.

**Note for the successor (Capability) node (RU-11):** coverage here is action→experience. The Capability
node inherits this layout and must supply a capability for **every pattern** (e.g. the routing/context
engine behind X1, the consolidation logic behind P2, the per-position telemetry projection behind P14).
No pattern is left without a capability owner downstream.
