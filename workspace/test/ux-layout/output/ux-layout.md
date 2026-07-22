# UX Layout — the Experience node deliverable (indexed BY ACTION)

*Clean-room derivation. Produced by the **Experience (UX) node**, child of the Action-Aggregate node,
fulfilling `input/contract.md`. Substance is derived from the frozen inputs only — the constitution
(Phases 1–5) + `completions.md`, the method (§1), the rules (`RU-*`), the glossary, and the module
(`framework/`) — and must **cover every one of the 63 inherited actions** in
`environment/action-aggregate/role-action-catalog.md`.*

*Structure (contract §1): **A.** shared pattern vocabulary (the reusable interaction *forms*) → **B.**
one **experience surface per action** (63 surfaces, grouped by role for readability) → **C.** attention
accounting rolled up across the surfaces. A self-check closes.*

---

## 0. Governing frame (the conformance envelope every surface obeys)

Four fundamentals bind every surface below; they are stated once here and not re-argued per surface:

- **Single interaction point (gating).** The D1 Designer (R-01) and D2 Designer (R-00) never address an
  internal node, authority, or service directly. **Every R-00/R-01 surface is presented *through* the
  D2 Assistant (R-07)** — the single unified point of contact (Phase 2 §P3; Phase 4 §Item 3;
  `completions.md C-2026-07-19-1`). "position = D1 Designer, *via the D2 Assistant*" is implied
  throughout.
- **Each position sees only what its responsibility needs** (Phase 5 §Item 3, Human Position First;
  "the same underlying event may be represented differently for different positions"). Every surface's
  *what is presented* is scoped to its position's responsibility, skill level, and authority.
- **Attention economy + leverage-gating** (Phase 1 §2.3, §2.5; Phase 2 §P1, §2.3). The scarce resource
  the layout optimises is **D1-Designer attention**. A surface earns Designer attention only when
  judgment has design value; every Designer-facing surface carries a **low-cost default** and asks at
  the highest practical semantic level.
- **Human-framed + progressively disclosed + observable** (Phase 1 §2.4; Phase 2 §3.2, §3.4; Phase 5
  §Item 1). Presented content is organised for human judgment (issue · rationale · alternatives ·
  consequence · requested action), never raw machine records; detail is available on **drill-down**, not
  pushed; state / health / deviation is **visible**.

**Whose attention a surface costs** (the accounting axis, §C): R-01 D1 Designer (the D2 priority);
R-00 D2 Designer (the meta-builder's separate budget); R-02 Design Node Builder = an **internal D2
agent** (its "experience" is a bounded work sandbox, **zero human/Designer attention** — D2 owns the
work); R-03/R-04/R-06 = D1/D0 **technical** positions (cost their own attention, **zero D1-Designer
attention**); R-05 D0 Operator = **D1's primary beneficiary** (its surfaces minimise the *Operator's*
attention first; still zero D1-Designer attention); R-07 D2 Assistant = the **medium** (it *is* the
interaction, so it adds no incremental Designer cost — it exists to absorb it).

---

## A. Pattern vocabulary (the shared interaction *forms*)

Method §1: passive actions "take a few static, near-universal forms." These are the reusable **forms**
the surfaces draw on — defined once, with the good UX the fundamentals require. They are the
**vocabulary, not the deliverable**; the deliverable is the per-action surface in §B, which *instantiates*
one of these forms but is specified per action.

| # | Pattern | The form (one line) | Good-UX qualities it must carry | Grounding |
|---|---------|---------------------|--------------------------------|-----------|
| **P1** | **Orientation** | Present just enough concept/tradeoff to support a Designer *decision*; commits nothing. | High-level, human-framed, no configuration; the choice stays the Designer's. | Phase 3 §Item; Phase 1 §2.4 |
| **P2** | **Review Stop** | D2 has completed a meaningful body of work and offers an *optional* review; no unresolved question. | Low-cost default = "continue"; drill-down into what was done; attention scales with node height. | Phase 3 §Phase-wide; Phase 4 §Item 2 |
| **P3** | **Confirmation Gate** | A *prepared proposal* offered for **accept / modify / discuss**; the default is accept. | One consolidated package; defaults pre-filled; modify touches only selected parts. | Phase 4 §Item 1; Phase 3 §Item 1 |
| **P4** | **Clarification Request** | A material judgment D2 **cannot** self-resolve, raised as a consolidated, high-leverage question. | Accumulated & batched; one high-level question governing many low-level ones; blocks the affected branch, not the Designer's whole world. | Phase 3; Phase 4 §Item 2; Phase 2 §2.3 |
| **P5** | **Completion Report / Notification** | A **pushed** record that an item finished; response optional. | Human-readable summary; skimmable; drill-down on request; never demands action by itself. | Phase 3 §Phase-wide; Phase 1 §2.4 |
| **P6** | **Monitoring View** | A **standing, pull** view of live state — progress, spend, health, deviation. | Observable without asking D2 to notice first; deviation/anomaly surfaced; drill-down from indicator → detail. | Phase 2 §P2, §3.1–3.4; Phase 5 §Item 1 |
| **P7** | **Inquiry / Inspection** | Natural-language *ask* → human-framed answer (explain/report/trace/show/compare); drill down if desired. | D2 owns locating the state & routing; no need to name the node; progressive depth. | Phase 4 §Item 3 |
| **P8** | **Investigation / Concern** | Request D2 *critically examine* a suspected matter and **recommend action**. | Returns diagnosis + material alternatives + recommendation; initiates investigation, does not silently mutate. | Phase 4 §Item 3; Phase 2 §4.4 |
| **P9** | **Directive / Authority Action** | The Designer *imposes / reserves / suspends / exercises* authority (stop a branch, reserve approval). | Recognised as an authority action and applied **promptly**; effect made visible. | Phase 4 §Item 3 |
| **P10** | **Configuration** | A **position-oriented** settings surface of *governed* parameters, with safe defaults. | Per-position scope; no hard-coded values (RU-01); impact preview + history; a change runs its harness. | Phase 5 §Item 3; RU-01 |
| **P11** | **Operate Console** | Issue an operational command (run / start / stop / schedule / deploy) and see its immediate effect. | Simple, action-first, status-confirmed; scoped to the operating position; reversible where practical. | Phase 5 §Item 3 |
| **P12** | **Results View** | View the outputs / results / reports that are *the point of running*. | Consumer-framed (not machine dump); organised for the viewing position; drill-down to detail. | Phase 5 §Item 3; Phase 1 §2.4 |
| **P13** | **Approval Prompt** | A **pushed**, simple decision — acknowledge / approve / retry — at the operator's competence level. | Non-technical, single-decision, low-cost; escalation offered if beyond competence. | Phase 5 §Item 3 |
| **P14** | **Support / Escalation** | Request help or hand a problem to a higher position; produces a routed hand-off. | Low-friction escape hatch; carries context so the receiver need not reconstruct it; hand-off is a verified produce/receive pair. | Phase 5 §Item 3; framework lifecycle lens |
| **P15** | **Diagnosis** | *Reactive* examine-a-fault → root cause + recommended fix (a technical position's investigation). | Evidence-organised; distinguishes cause from symptom; proposes a fix within the established design. | Phase 5 §Item 3; `design-node-algorithm` depth-frame |
| **P16** | **Deploy / Release** | Package / deploy / distribute / roll back — **harness-gated**, with upgrade records. | Cannot ship past a failed harness; records the change; rollback uses the record; "no code change ≠ no harness." | Phase 5 §Item 3; glossary `d1`; RU-01 harness-note |
| **P17** | **Harness / Validation Run** | Run the test / smoke / regression suite and see **pass/fail + failure visibility**. | Results made visible before proceeding; failures localised; gates the step it protects (Verification Before Realization). | Phase 2 §P4; Phase 5 §Item 1 |
| **P18** | **Internal Work Sandbox** | An **internal D2 agent's** bounded working surface — investigate, build candidates, self-evaluate, submit, propose-up. | Not Designer-facing; strong boundary / local autonomy; its *outputs* surface to the Designer only via P2/P4/P5. | Phase 5 §Item 3, §Item 5; Phase 4 §Item 2; `design-node-algorithm` |

*18 patterns. Two actions that share a pattern still receive **distinct surfaces** in §B (e.g. A-034
Operate and A-044 Results View are both operator-facing but different surfaces; A-053 spend-monitor and
A-054 health-monitor are both P6 but different surfaces). The surface is per action.*

---

## B. The deliverable — one experience surface per action

*Format per surface: **position** · **pattern** · then the interaction spec —
**Trigger · Presented · Low-cost default · Drill-down · Attention (whose, how much) · Direction** — and
**Derivable/Slot** (the form+qualities fixed now; product-specific content left as a named `‹slot›`
because the D1/D0 project is unknown).*

### R-00 — D2 Designer *(meta-builder of D2; surfaces via the D2 Assistant; attention is the D2-Designer's own budget, not the D1-Designer priority)*

**A-010 — Complete / clarify / expand D2's living working sets** · D2 Designer, via D2 Assistant · **P3 Confirmation Gate** (low-hurdle variant)
- *Trigger*: D2 Designer initiates a completion of an intentionally-open set (glossary, query catalog, philosophy).
- *Presented*: the target set item, the proposed addition/clarification pre-drafted, and a consistency check against established design.
- *Default*: accept the drafted completion (low hurdle, Phase 5 §Item 2).
- *Drill-down*: show the governing statements the completion must stay consistent with.
- *Attention*: D2-Designer, **low** (deliberately low-hurdle).
- *Direction*: **pull** (Designer-initiated).
- *Derivable/Slot*: form = low-hurdle append-with-consistency-check; slot = `‹which living set, what entry›`.

**A-011 — Revise D2's persistent working sets through the explicit process** · D2 Designer, via D2 Assistant · **P8 Investigation/Concern → P3 Confirmation Gate**
- *Trigger*: a change to a *persistent* (non-open) set is proposed — requires explicit revision, higher hurdle than A-010.
- *Presented*: the proposed revision, an **impact evaluation** (probe up/down, RU-06), material alternatives, consequences.
- *Default*: none forced — a persistent set changes only via deliberate confirmation (no silent default-accept).
- *Drill-down*: the full dry-run report; what descendants the change touches.
- *Attention*: D2-Designer, **medium** (explicit-revision hurdle).
- *Direction*: **pull**, ending in a push decision.
- *Derivable/Slot*: form = evaluate-then-confirm explicit revision; slot = `‹which persistent set, the revision›`.

**A-061 — Review and adopt/reject D2 improvements proposed by the optional post-run audit** · D2 Designer, via D2 Assistant · **P2 Review Stop** (adopt/reject variant)
- *Trigger*: the optional post-run D2 audit has produced candidate improvements.
- *Presented*: a human-framed list of proposed improvements, each with its evidence and expected benefit; **must not** be pre-applied (Phase 3 §Item 5).
- *Default*: adopt none (status quo holds until explicit adoption).
- *Drill-down*: the audit finding behind each proposal (cost/time/attention data).
- *Attention*: D2-Designer, **low–medium** (batched, optional).
- *Direction*: **push** (audit-offered), Designer disposes.
- *Derivable/Slot*: form = adopt/reject list over audit proposals; slot = `‹the proposed improvements›`.

### R-01 — D1 Designer *(the D2 priority user; every surface via the single D2 Assistant point)*

**A-012 — Confirm the Designer–D2 Operating Contract** · D1 Designer, via D2 Assistant · **P3 Confirmation Gate**
- *Trigger*: start of a design run; D2 presents the default operating posture.
- *Presented*: a **compact human-oriented checklist/selection table** (not a config document) of how D2 will seek intervention and how the Designer will observe/intervene — one item within the setup package (A-016).
- *Default*: **accept the defaults** (Phase 3 §Item 1: "the normal action should often be to accept").
- *Drill-down*: what each default means and the principle it protects.
- *Attention*: D1-Designer, **low**.
- *Direction*: **push** (offered at entry), low-cost accept.
- *Derivable/Slot*: form = compact accept-defaults checklist; slot = `‹the specific posture defaults›`.

**A-013 — Provide the initial design input (Predecessor D1 + intended change)** · D1 Designer, via D2 Assistant · **P7 Inquiry/Inspection** (intake variant)
- *Trigger*: Designer supplies predecessor package + intended change, in **any useful initial form** (notes, bug lists, direction).
- *Presented*: an intake surface that **accepts loose, incomplete, human-oriented material** (Phase 1 §4.3) and reflects back D2's structured reading for confirmation; D2 bears the translation burden.
- *Default*: submit what exists; completeness not required.
- *Drill-down*: D2's provisional structuring of the input, with provenance kept distinct (Phase 1 §4.6).
- *Attention*: D1-Designer, **low–medium** (front-loaded; early discussion that saves later cost is welcome, Phase 3 §Item 2).
- *Direction*: **pull** (Designer-initiated supply).
- *Derivable/Slot*: form = tolerant incremental intake + reflect-back; slot = `‹the predecessor package, the intended change›`.

**A-014 — Review the initial design understanding & direction** · D1 Designer, via D2 Assistant · **P2 Review Stop**
- *Trigger*: D2 has consolidated its understanding + recommended direction and stops (the Phase 3 §Item 3 default Review Stop).
- *Presented*: a report covering existing-system understanding, what to preserve/change, likely invariants, unresolved uncertainties, recommended direction.
- *Default*: **continue** ("Review now, or continue?").
- *Drill-down*: the evidence behind each understanding; open questions.
- *Attention*: D1-Designer, **medium** (high-value early stop).
- *Direction*: **push** (courtesy stop), optional engagement.
- *Derivable/Slot*: form = consolidated understanding+direction stop; slot = `‹the actual understanding & direction›`.

**A-015 — Select a design posture (Standard / High Harness / Lean)** · D1 Designer, via D2 Assistant · **P3 Confirmation Gate** (single-choice, high-leverage)
- *Trigger*: setup; **one choice → many detailed settings** (leverage-gating in its purest form, Phase 1 §2.5).
- *Presented*: 2–3 named postures with a one-line consequence each; recommended default marked.
- *Default*: the recommended posture.
- *Drill-down*: the detailed settings each posture implies.
- *Attention*: D1-Designer, **low** (one high-level pick).
- *Direction*: **push**, low-cost.
- *Derivable/Slot*: form = single high-leverage posture pick; slot = `‹the posture→settings expansions›`.

**A-016 — Review / revise the Selected Setup Configuration Package** · D1 Designer, via D2 Assistant · **P3 Confirmation Gate** + **P10 Configuration** (progressive-disclosure)
- *Trigger*: D2 presents the assembled setup package derived from the posture.
- *Presented*: one **consolidated package** with defaults filled; **progressive disclosure** — accept whole, compare options, or revise selected parts.
- *Default*: accept the package as assembled.
- *Drill-down*: expand any section to its governed settings and rationale.
- *Attention*: D1-Designer, **low–medium** (only if revising).
- *Direction*: **push**, low-cost accept.
- *Derivable/Slot*: form = consolidated accept/compare/revise package; slot = `‹the setup settings›`.

**A-017 — Revise setup material later (governed)** · D1 Designer, via D2 Assistant · **P10 Configuration** (governed later-edit)
- *Trigger*: Designer returns to change setup after the run has started.
- *Presented*: the current setup with a required **impact analysis** and preserved **history** (Phase 5 §Item 2 governed revision).
- *Default*: no change (view-only until a change is chosen).
- *Drill-down*: the impact dry-run; prior versions.
- *Attention*: D1-Designer, **low** unless a material change is made.
- *Direction*: **pull** (Designer-initiated).
- *Derivable/Slot*: form = governed later-edit with impact+history; slot = `‹the setting being revised›`.

**A-001 — Accept the proposed D1 Design Operating Framework** · D1 Designer, via D2 Assistant · **P3 Confirmation Gate**
- *Trigger*: entering D1 design mode, D2 presents one consolidated framework: "here is how I propose to conduct this D1 design."
- *Presented*: the design skeleton, inherited/derived rules, and material control points — **one prepared package** for low-cost review.
- *Default*: **accept** (Phase 4 §Item 1 "low-cost default response").
- *Drill-down*: any framework element and why it is proposed.
- *Attention*: D1-Designer, **low–medium** (governs a large region → some attention warranted).
- *Direction*: **push**, low-cost accept.
- *Derivable/Slot*: form = consolidated framework acceptance; slot = `‹the proposed framework contents›`.

**A-002 — Modify selected parts of the framework** · D1 Designer, via D2 Assistant · **P3 Confirmation Gate** (partial-edit branch of A-001)
- *Trigger*: Designer chooses to change parts rather than accept whole.
- *Presented*: editable framework parts with defaults intact; only the touched parts change (a **distinct surface** from A-001's accept).
- *Default*: leave a part unchanged.
- *Drill-down*: consequence of a modification.
- *Attention*: D1-Designer, **medium** (proportional to what is edited).
- *Direction*: **pull** within the framework gate.
- *Derivable/Slot*: form = selective part-modification; slot = `‹the modifiable framework parts›`.

**A-004 — Discuss a material concern** · D1 Designer, via D2 Assistant · **P8 Investigation/Concern** (dialogue variant)
- *Trigger*: Designer raises a material concern about the framework or design (Designer-initiated).
- *Presented*: a conversational surface where D2 interprets the concern, investigates, and returns findings + options — context preserved across turns (Phase 2 §4.3).
- *Default*: n/a (open dialogue); no forced disposition.
- *Drill-down*: the investigation D2 ran to answer.
- *Attention*: D1-Designer, **medium** (chosen dialogue).
- *Direction*: **pull**.
- *Derivable/Slot*: form = context-preserving concern dialogue; slot = `‹the concern's subject›`.

**A-005 — Review a Design Node (approve / "continue")** · D1 Designer, via D2 Assistant · **P2 Review Stop**
- *Trigger*: D2 reaches a proposed node design and offers review per the framework and **node height** (higher nodes → more attention, Phase 4 §Item 2).
- *Presented*: a Designer-oriented **node report** (result + rationale + proposed spawning strategy), sized to significance.
- *Default*: **continue** (review is an event, not a duty).
- *Drill-down*: the node's design detail and its justification (RU-02).
- *Attention*: D1-Designer, **low→high by node height** (a Constitution node warrants a real stop).
- *Direction*: **push**, optional.
- *Derivable/Slot*: form = height-scaled node Review Stop; slot = `‹the node & its result›`.

**A-006 — Reserve or assign revision authority over a design object** · D1 Designer, via D2 Assistant · **P9 Directive/Authority Action**
- *Trigger*: Designer sets whether later changes to an object are D2-governed or Designer-governed (a *continuing governance property*, distinct from the review event A-005).
- *Presented*: the object's current authority state and the toggle, with the framework's default-by-node-class shown.
- *Default*: inherit the framework default (Designer asked mainly about **recommended exceptions**, Phase 4 §Item 2).
- *Drill-down*: what a governed vs reserved state changes downstream.
- *Attention*: D1-Designer, **low**.
- *Direction*: **pull** (authority action), applied promptly.
- *Derivable/Slot*: form = per-object authority toggle with class defaults; slot = `‹the design object›`.

**A-007 — Inquiry / inspection (explain, report, trace, show, compare)** · D1 Designer, via D2 Assistant · **P7 Inquiry/Inspection**
- *Trigger*: Designer asks a natural-language design/process question ("show the proposed D0 structure", "explain Algorithm A vs V1").
- *Presented*: a human-framed answer; **D2 owns locating the state and routing** — the Designer never names the node.
- *Default*: n/a (answer-on-ask).
- *Drill-down*: progressively deeper detail on request (Phase 2 §3.4).
- *Attention*: D1-Designer, **low, self-chosen** (zero unless he asks).
- *Direction*: **pull**.
- *Derivable/Slot*: form = NL ask → human answer + drill-down; slot = `‹the design object queried›`.

**A-008 — Investigation / concern (critically examine a suspected problem, recommend action)** · D1 Designer, via D2 Assistant · **P8 Investigation/Concern**
- *Trigger*: Designer suspects a problem and asks D2 to examine it (absorbs former "request investigation").
- *Presented*: D2 **initiates investigation** (does not directly mutate the tree), returns findings, affected objects, options, and a recommendation.
- *Default*: act on the recommendation, or not — Designer disposes.
- *Drill-down*: the evidence chain behind the recommendation.
- *Attention*: D1-Designer, **low–medium, self-chosen**.
- *Direction*: **pull**.
- *Derivable/Slot*: form = examine → recommend (no silent mutation); slot = `‹the suspected matter›`.

**A-009 — Designer directive (impose, revise, reserve, suspend, exercise authority)** · D1 Designer, via D2 Assistant · **P9 Directive/Authority Action**
- *Trigger*: Designer issues an authority action ("stop the implementation branch", "reserve approval on Algorithm A").
- *Presented*: recognition that the input is an **authority action**, its scope, and **prompt application**; the effect made visible.
- *Default*: n/a (explicit command).
- *Drill-down*: what the directive halted/reserved and where it now stands.
- *Attention*: D1-Designer, **low** (issuing is cheap; leverage is high).
- *Direction*: **pull**, applied promptly.
- *Derivable/Slot*: form = recognised-and-applied directive; slot = `‹the authority target & verb›`.

**A-018 — Answer a Clarification Request** · D1 Designer, via D2 Assistant · **P4 Clarification Request**
- *Trigger*: D2 has hit a material judgment it **cannot** resolve by further investigation and has **accumulated** it into a consolidated, high-leverage question (Phase 4 §Item 2).
- *Presented*: the issue, why D2 cannot self-resolve it, material alternatives + consequences, and the specific decision requested — human-framed.
- *Default*: none forced; but the question is pitched so a **high-level answer governs many low-level ones** (Phase 2 §2.3).
- *Drill-down*: the investigation D2 already did.
- *Attention*: D1-Designer, **medium–high** (this is the genuine cost — minimised by batching + leverage).
- *Direction*: **push** (blocks the affected branch, per RU-05-style stop, not the Designer's whole world).
- *Derivable/Slot*: form = consolidated high-leverage question; slot = `‹the unresolved judgment›`.

**A-019 — Tune resolution depth / intervention posture** · D1 Designer, via D2 Assistant · **P10 Configuration** (single tunable)
- *Trigger*: Designer adjusts the investigate-vs-infer-vs-ask-vs-defer balance (Phase 2 §2.6).
- *Presented*: a governed tuning control with its current setting and the attention/depth tradeoff it moves; baseline bias toward early investigation shown.
- *Default*: the baseline posture (from A-015).
- *Drill-down*: what the setting changes in D2 behaviour; the obligation it **cannot** remove (identify material uncertainty).
- *Attention*: D1-Designer, **low**.
- *Direction*: **pull**.
- *Derivable/Slot*: form = single governed depth tunable; slot = `‹the tuning range›`.

**A-020 — Request / review an optional D2 audit after completion** · D1 Designer, via D2 Assistant · **P8 Investigation/Concern** (retrospective) + **P5 Report**
- *Trigger*: after a completed run, Designer requests "did D2 design D1 well?" (distinct from A-061, which is R-00 disposing of the audit's D2-improvements).
- *Presented*: a process audit — total time, Designer attention cost, clarification rounds, redesigns, anomalies — human-framed, with candidate improvements (not applied).
- *Default*: don't request (optional).
- *Drill-down*: per-node cost/time/revision detail.
- *Attention*: D1-Designer, **low, self-chosen**.
- *Direction*: **pull** (request) → **push** (report).
- *Derivable/Slot*: form = optional retrospective process audit; slot = `‹the run's process data›`.

**A-052 — Monitor design progress** · D1 Designer, via D2 Assistant · **P6 Monitoring View**
- *Trigger*: standing; Designer looks at advancement / changes-since-last-review / revision counts.
- *Presented*: a live, human-oriented progress view (Design Tree state, "what changed since my last review").
- *Default*: passive glance; nothing demanded.
- *Drill-down*: from an indicator into the node/change behind it.
- *Attention*: D1-Designer, **low, self-chosen** (pull observability, Phase 2 §3.1).
- *Direction*: **pull**.
- *Derivable/Slot*: form = standing progress monitor; slot = `‹the design's progress metrics›`.

**A-053 — Monitor resource & cost spend** · D1 Designer, via D2 Assistant · **P6 Monitoring View** (distinct subject from A-052/A-054)
- *Trigger*: standing; Designer inspects time & cost, cumulative and per-node.
- *Presented*: spend indicators with per-node breakdown ("which nodes consumed the most").
- *Default*: passive glance.
- *Drill-down*: node-level cost/time detail.
- *Attention*: D1-Designer, **low, self-chosen**.
- *Direction*: **pull**.
- *Derivable/Slot*: form = standing spend monitor; slot = `‹the cost/time metrics›`.

**A-054 — Monitor design-process health & anomalies** · D1 Designer, via D2 Assistant · **P6 Monitoring View** (health/deviation subject)
- *Trigger*: standing; Designer watches for abnormal behaviour, rejection loops, high-impact open issues.
- *Presented*: a **health/deviation** view that surfaces anomalies proactively (Phase 5 §Item 1 make-deviation-visible); investigation escalates via A-008.
- *Default*: passive glance; anomalies flagged when present.
- *Drill-down*: from a flagged anomaly into its cause; hand-off to A-008.
- *Attention*: D1-Designer, **low, self-chosen**.
- *Direction*: **pull**, with **push** alerts on material deviation.
- *Derivable/Slot*: form = standing health/anomaly monitor; slot = `‹the health signals›`.

**A-055 — Evaluate D2 and decide whether to adopt it** · D1 Designer, via D2 Assistant · **P1 Orientation**
- *Trigger*: the entry-point decision (adopt / decline / defer); the choice is the Designer's, D2 supports by orienting.
- *Presented*: just enough of what D2 is and offers to inform the decision — no configuration, no commitment.
- *Default*: defer (no adoption implied by looking).
- *Drill-down*: deeper explanation of D2's model on request.
- *Attention*: D1-Designer, **low** (one framed decision).
- *Direction*: **pull**.
- *Derivable/Slot*: form = decision-support orientation; slot = `‹the D2 value framing›`.

**A-056 — Review and adjust the roles table** · D1 Designer, via D2 Assistant · **P10 Configuration** (roster) + **P2 Review Stop**
- *Trigger*: setup; Designer accepts or tailors the cast of roles (intrinsic roles fixed; default product-side roles changeable).
- *Presented*: the roles table with intrinsic/default marking; edit only the changeable ones.
- *Default*: accept the default roster.
- *Drill-down*: what each role implies for the design.
- *Attention*: D1-Designer, **low**.
- *Direction*: **push** (offered in setup), low-cost accept.
- *Derivable/Slot*: form = roster review with intrinsic/default guard; slot = `‹the product-side roles›`.

**A-057 — Review and confirm the D1 foundational documents (the D1 Constitution)** · D1 Designer, via D2 Assistant · **P2 Review Stop** (key, strongly-encouraged)
- *Trigger*: D2 has assembled the D1 Constitution — the **highest-leverage** Review Stop (a Constitution node warrants real attention, Phase 4 §Item 2).
- *Presented*: the foundational set, human-framed, with what it governs and where it came from; Designer-governed (revision reserved).
- *Default*: continue — but the stop is **strongly encouraged**, not a bare courtesy.
- *Drill-down*: each foundational document and its basis.
- *Attention*: D1-Designer, **high** (deliberately — the leverage justifies it).
- *Direction*: **push**, strongly-encouraged engagement.
- *Derivable/Slot*: form = strongly-encouraged Constitution Review Stop; slot = `‹the D1 foundational docs›`.

**A-058 — Evaluate a proposed change before formalizing it (impact dry-run)** · D1 Designer, via D2 Assistant · **P8 Investigation/Concern** (dry-run; commits nothing)
- *Trigger*: Designer wants to see a change's impact **before** any official proposal (RU-06; separate command that commits nothing).
- *Presented*: an **evaluation report** — probe up (lands on ancestor?) and down (child contract effect) — with a formalize-or-revise choice.
- *Default*: neither formalize nor revise until chosen (commits nothing).
- *Drill-down*: the up/down probe detail.
- *Attention*: D1-Designer, **low–medium, self-chosen**.
- *Direction*: **pull**.
- *Derivable/Slot*: form = commit-nothing impact dry-run; slot = `‹the proposed change›`.

### R-02 — Design Node Builder *(internal D2 agent; surfaces are the P18 work sandbox — **zero Designer attention**; outputs reach the Designer only via R-01's P2/P4/P5)*

**A-021 — Investigate relevant predecessor & reference material** · Design Node Builder · **P18 Internal Work Sandbox** (study)
- *Trigger*: node building begins; the builder enters via the Predecessor Reference Roadmap.
- *Presented*: (agent-facing) curated read-context — the ancestor/sibling links its contract supplies (RU-08); provenance kept distinct (Phase 1 §4.6).
- *Default*: n/a (autonomous work).
- *Drill-down*: n/a (internal).
- *Attention*: **zero Designer** — D2 owns it.
- *Direction*: internal.
- *Derivable/Slot*: form = bounded study sandbox over curated context; slot = `‹the predecessor/reference material›`.

**A-022 — Develop, compare, and critique candidate design choices** · Design Node Builder · **P18 Internal Work Sandbox** (candidate exploration)
- *Trigger*: after study; bounded local autonomy under the harness.
- *Presented*: (agent-facing) a candidate-comparison workspace within the node's harness (strong boundary; local autonomy, Phase 5 §Item 5).
- *Attention*: **zero Designer**.
- *Direction*: internal.
- *Derivable/Slot*: form = harnessed candidate-exploration sandbox; slot = `‹the candidate space›`.

**A-023 — Produce the Node Design Specification / result** · Design Node Builder · **P18 Internal Work Sandbox** (author)
- *Trigger*: candidates converge.
- *Presented*: (agent-facing) authoring surface producing the node result the contract demands.
- *Attention*: **zero Designer** (surfaces later as A-005's node report).
- *Direction*: internal.
- *Derivable/Slot*: form = spec-authoring sandbox; slot = `‹the node's deliverable›`.

**A-024 — Internally evaluate the result before submission** · Design Node Builder · **P17 Harness/Validation Run** (internal self-check)
- *Trigger*: result ready; "submission is not the first evaluation" (Phase 6 Item 2 §6 → derived from Phase 2 §P4).
- *Presented*: (agent-facing) the acceptance self-check (conformance → coverage/quality) run **before** submitting.
- *Attention*: **zero Designer**.
- *Direction*: internal (Verification Before Realization).
- *Derivable/Slot*: form = pre-submission self-evaluation harness; slot = `‹the node's acceptance criteria›`.

**A-025 — Submit the design result for acceptance** · Design Node Builder · **P18 Internal Work Sandbox** (submission hand-off)
- *Trigger*: self-check passed; submission ≠ acceptance (RU-02).
- *Presented*: (agent-facing) the submission package = result + its **justification**, handed to the parent as enforcer.
- *Attention*: **zero Designer** (parent-node hand-off, not Designer-facing).
- *Direction*: internal, upward (adjacency, RU-07).
- *Derivable/Slot*: form = justify-and-submit hand-off; slot = `‹the result & its justification›`.

**A-026 — Propose a spawning strategy (descendant responsibilities)** · Design Node Builder · **P18 Internal Work Sandbox** (spawning proposal)
- *Trigger*: node includes decomposition; spawning ≠ advancement.
- *Presented*: (agent-facing) proposed child responsibilities/contracts; may surface to the Designer only as part of A-005's node report.
- *Attention*: **zero Designer** directly.
- *Direction*: internal.
- *Derivable/Slot*: form = spawning-strategy proposal; slot = `‹the descendant responsibilities›`.

**A-027 — Propose upward revision of governing design** · Design Node Builder · **P18 Internal Work Sandbox** (propose-up + stop)
- *Trigger*: the builder finds a defect in inherited/governing design.
- *Presented*: (agent-facing) an upward proposal routed by the affected node's revision authority; the builder **stops** until resolved (RU-05, no drift).
- *Attention*: **zero Designer** unless the affected node is Designer-governed — then it surfaces as a prepared high-level A-018/A-008 decision.
- *Direction*: internal, upward.
- *Derivable/Slot*: form = propose-up-and-halt; slot = `‹the proposed upward revision›`.

**A-060 — Establish the node's verification harness & derive design evidence *before* committing** · Design Node Builder · **P17 Harness/Validation Run** (harness-first)
- *Trigger*: node building — **before** committing the design (Harness First, Phase 5 §Item 1; Verification Before Realization, Phase 2 §P4).
- *Presented*: (agent-facing) construction of observation/monitoring/health-visibility, representative inputs, expected outputs, evaluation cases — distinct from passive study A-021.
- *Attention*: **zero Designer**.
- *Direction*: internal (monitoring before usage).
- *Derivable/Slot*: form = harness-first evidence construction; slot = `‹the node's harness & evidence›`.

### R-03 — D1 Programmer *(implements D0 code from spec; a D1-world technical position — **zero D1-Designer attention**; should not reconstruct the design)*

**A-028 — Implement product (D0) code from the implementation specification** · D1 Programmer · **P11 Operate Console** (implementation workspace)
- *Trigger*: an implementation spec is handed off, complete enough to implement **without reconstructing the design** (Phase 5 §Item 3 handoff).
- *Presented*: the spec as a self-sufficient work boundary — inputs, constraints, expected output — not the upstream design process.
- *Default*: implement to spec.
- *Drill-down*: from spec item to its governing requirement (not the whole history).
- *Attention*: **Programmer's own**; zero D1-Designer.
- *Direction*: pull (Programmer works the spec).
- *Derivable/Slot*: form = self-sufficient spec-to-code boundary; slot = `‹the implementation spec›`.

**A-040 — Write and run implementation-level tests against the code** · D1 Programmer · **P17 Harness/Validation Run**
- *Trigger*: code produced; implementation-level verification.
- *Presented*: a test-authoring/running surface with pass/fail + failure localisation (Harness First at the code level).
- *Default*: run the suite.
- *Drill-down*: a failing test → the code path.
- *Attention*: Programmer's own; zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = code-level test harness; slot = `‹the tests & code under test›`.

**A-041 — Diagnose and fix implementation defects (within the spec)** · D1 Programmer · **P15 Diagnosis**
- *Trigger*: a defect appears at the code level.
- *Presented*: evidence organised for root-cause; fix stays **within the spec** (no product redesign).
- *Default*: propose a within-spec fix.
- *Drill-down*: cause vs symptom; the spec boundary the fix must respect.
- *Attention*: Programmer's own; zero D1-Designer.
- *Direction*: reactive/pull.
- *Derivable/Slot*: form = within-spec code diagnosis+fix; slot = `‹the defect›`.

### R-04 — D1 Technical Manager *(operates the D1 wrapper — governed params, upgrade, deploy, monitor; **zero D1-Designer attention**; drives RU-01)*

**A-029 — Adjust a governed product parameter without changing code** · D1 Technical Manager · **P10 Configuration** (governed params)
- *Trigger*: a product-level value legitimately needs adjustment without redesign (RU-01: no hard-coded numbers).
- *Presented*: the **explicitly governed** parameters exposed to this position (product defaults, provider defaults, retry within ranges, resource profiles) — with valid ranges; **not** code.
- *Default*: the current governed value.
- *Drill-down*: what the parameter affects; the harness that a change triggers.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = governed-parameter config exposed to R-04; slot = `‹the governed parameters›`.

**A-030 — Run the upgrade validation / regression (smoke-test) harness** · D1 Technical Manager · **P17 Harness/Validation Run**
- *Trigger*: any upgrade or parameter change ("no code change ≠ no harness").
- *Presented*: the D1-wrapper smoke-test suite with pass/fail + failure visibility; **gates** repackage/distribute.
- *Default*: run before shipping.
- *Drill-down*: a failing check → the affected behaviour.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull (gate).
- *Derivable/Slot*: form = wrapper smoke-test run; slot = `‹the smoke-test suite›`.

**A-031 — Update release state, repackage, and distribute the product** · D1 Technical Manager · **P16 Deploy/Release**
- *Trigger*: harness green; ship the upgraded package.
- *Presented*: release-state update, repackage, distribute — with an **upgrade record** written.
- *Default*: proceed only past a green harness (A-030).
- *Drill-down*: the release contents & record.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = harness-gated release with record; slot = `‹the release artifact›`.

**A-032 — Deploy D0 into production (optionally retaining D1)** · D1 Technical Manager · **P16 Deploy/Release** (production deploy — distinct from A-031 distribute)
- *Trigger*: a validated package is deployed to production; D1 may be retained to manage/upgrade D0 (glossary `d1`).
- *Presented*: a deploy surface with the retain-D1 choice and post-deploy status.
- *Default*: deploy the validated package with D1 retained (the default).
- *Drill-down*: deployment target & what D1 continues to manage.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = production deploy with retain-D1 option; slot = `‹the deployment target›`.

**A-033 — Monitor D0 health & performance via the D1 wrapper** · D1 Technical Manager · **P6 Monitoring View** (half-level-above-D0)
- *Trigger*: standing; watch D0 health/performance from the wrapper (~half a level above D0, glossary `half-level`).
- *Presented*: health/performance indicators (e.g. crash detection) framed for the technical manager; deviation surfaced.
- *Default*: passive glance; alert on deviation.
- *Drill-down*: an indicator → the underlying signal.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull, with push alerts.
- *Derivable/Slot*: form = wrapper health monitor; slot = `‹the D0 health signals›`.

**A-042 — Roll back to a previous release on a failed upgrade** · D1 Technical Manager · **P16 Deploy/Release** (rollback)
- *Trigger*: an upgrade fails; recover using the D1-wrapper **upgrade record**.
- *Presented*: the recorded prior releases and a one-action rollback; the record makes recovery reliable.
- *Default*: roll back to the last known-good release.
- *Drill-down*: what changed between releases.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull (recovery).
- *Derivable/Slot*: form = record-driven rollback; slot = `‹the release history›`.

**A-043 — Review upgrade records / release history** · D1 Technical Manager · **P12 Results View** (audit trail)
- *Trigger*: the manager inspects the wrapper's upgrade records.
- *Presented*: a human-readable history of upgrades/releases and their outcomes.
- *Default*: view-only.
- *Drill-down*: a record → its harness result and changes.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = upgrade-record history view; slot = `‹the release records›`.

### R-05 — D0 Operator *(**D1's primary beneficiary**; low technical understanding — surfaces minimise the **Operator's** attention first; zero D1-Designer attention)*

**A-034 — Perform routine operation (start/run/stop/schedule/pause/cancel jobs)** · D0 Operator · **P11 Operate Console**
- *Trigger*: routine operation of the deployed D0.
- *Presented*: a **simple, non-technical** action console — start/run/stop/schedule/pause/cancel — with immediate status; scoped to the Operator (Phase 5 §Item 3).
- *Default*: the safe/common operation; reversible where practical.
- *Drill-down*: current job status.
- *Attention*: **Operator's — minimised** (primary-beneficiary principle); zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = non-technical operate console; slot = `‹what a job is›`.

**A-035 — Perform routine user-level monitoring (is D0 working & healthy?)** · D0 Operator · **P6 Monitoring View** (user-level)
- *Trigger*: standing; the Operator glances at whether D0 is working.
- *Presented*: a **user-level** health indicator — plain "working / needs attention", not technical telemetry.
- *Default*: passive glance.
- *Drill-down*: a simple "what's wrong" summary (escalates via A-048 if beyond competence).
- *Attention*: Operator's — minimised; zero D1-Designer.
- *Direction*: pull, with plain push alerts.
- *Derivable/Slot*: form = plain-language health glance; slot = `‹the user-level health signal›`.

**A-036 — Set operator-level controls (spending limits, scheduling, scope, approved choices)** · D0 Operator · **P10 Configuration** (operator-scoped)
- *Trigger*: the Operator sets position-oriented controls (Phase 5 §Item 3 examples: daily spend limits, scheduling, collection scope).
- *Presented*: only the **operator-level** governed controls — nothing technical (no endpoints/credentials — those are R-06's).
- *Default*: sensible defaults; safe ranges.
- *Drill-down*: what a control affects, in operator terms.
- *Attention*: Operator's — minimised; zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = operator-scoped controls; slot = `‹the operator controls›`.

**A-044 — View D0 results, outputs, and reports** · D0 Operator · **P12 Results View**
- *Trigger*: the Operator views outputs — **the point of running D0**.
- *Presented*: results organised for the Operator (consumer-framed, not machine dump).
- *Default*: view the latest results.
- *Drill-down*: from summary → detailed result.
- *Attention*: Operator's — minimised; zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = consumer-framed results view; slot = `‹what the results are›`.

**A-045 — Acknowledge and respond to notifications/prompts/routine approvals** · D0 Operator · **P13 Approval Prompt**
- *Trigger*: D0 pushes a simple, non-technical decision (prompt / routine approval).
- *Presented*: a single low-cost decision at operator competence (ack / approve); escalation offered if beyond competence.
- *Default*: the safe response, or defer.
- *Drill-down*: plain context for the decision.
- *Attention*: Operator's — minimised (pushed but cheap); zero D1-Designer.
- *Direction*: **push**.
- *Derivable/Slot*: form = non-technical approval prompt; slot = `‹the routine decision›`.

**A-046 — Handle routine, non-technical error conditions (retry/restart within competence)** · D0 Operator · **P13 Approval Prompt** + **P14 Support/Escalation** (escape hatch)
- *Trigger*: a routine error the Operator can handle (retry/restart).
- *Presented*: a plain error with a within-competence action (retry/restart) **and** a one-tap escalation (A-048) when beyond competence.
- *Default*: the safe within-competence action.
- *Drill-down*: plain "what happened".
- *Attention*: Operator's — minimised; zero D1-Designer.
- *Direction*: **push** (error) → pull (action/escalate).
- *Derivable/Slot*: form = routine-error handling with escape hatch; slot = `‹the routine error class›`.

**A-047 — View routine activity, usage, and cost-to-date (operator status)** · D0 Operator · **P6 Monitoring View** (usage/cost, distinct from A-035 health)
- *Trigger*: standing; the Operator checks usage & cost-to-date (uses observation data; Phase 5 §Item 3, "half a level above" planning data).
- *Presented*: operator-level activity/usage/spend, plainly framed.
- *Default*: passive glance.
- *Drill-down*: usage over time.
- *Attention*: Operator's — minimised; zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = operator usage/cost status; slot = `‹the usage & cost metrics›`.

**A-048 — Request front-line support / escalate to the D0 Technical Manager** · D0 Operator · **P14 Support/Escalation**
- *Trigger*: a problem beyond the Operator's competence — the low-technical operator's **escape hatch**.
- *Presented*: a low-friction request that **carries context** (so R-06 need not reconstruct it) and routes to the D0 Technical Manager (A-039).
- *Default*: send with auto-attached context.
- *Drill-down*: what context is being sent.
- *Attention*: Operator's — minimised; zero D1-Designer.
- *Direction*: pull → hand-off (a verified produce/receive pair).
- *Derivable/Slot*: form = context-carrying escalation; slot = `‹the problem being escalated›`.

### R-06 — D0 Technical Manager *(front-line support/install/maintain a D0 deployment; **zero D1-Designer attention**; walks diagnose→fix→escalate)*

**A-037 — Install a D0 deployment** · D0 Technical Manager · **P16 Deploy/Release** (install)
- *Trigger*: a D0 deployment must be installed (lifecycle: package → install → smoke-test → hand-over).
- *Presented*: an install surface with the deployment's technical prerequisites and a post-install check.
- *Default*: install with validated defaults.
- *Drill-down*: install steps & their verification.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = deployment install with post-check; slot = `‹the deployment package›`.

**A-038 — Technically maintain a D0 deployment (paths, endpoints, service config, limits, credentials, health settings)** · D0 Technical Manager · **P10 Configuration** (deployment-scoped, technical)
- *Trigger*: technical maintenance of a specific deployment.
- *Presented*: the **technical** deployment controls (deployment paths, storage endpoints, service config, resource limits, credentials, health settings) — the R-06 scope, distinct from R-05's operator controls.
- *Default*: current validated config.
- *Drill-down*: what each setting affects; the health settings feed A-059.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = deployment-scoped technical config; slot = `‹the deployment settings›`.

**A-039 — Provide front-line technical support** · D0 Technical Manager · **P14 Support/Escalation** (receiving end)
- *Trigger*: an A-048 escalation arrives from the D0 Operator.
- *Presented*: the incoming request **with the Operator's context attached**; a workspace to respond/resolve; onward escalation to R-04 (A-051) if it exceeds front-line.
- *Default*: respond to the operator.
- *Drill-down*: the deployment state relevant to the request.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: **push** in (received) → pull (resolve).
- *Derivable/Slot*: form = front-line support queue with context; slot = `‹the support request›`.

**A-049 — Diagnose a D0 deployment issue** · D0 Technical Manager · **P15 Diagnosis** (reactive, distinct from standing A-059)
- *Trigger*: a deployment fault to be diagnosed (reactive, vs A-059's proactive monitoring).
- *Presented*: deployment evidence organised for root-cause; cause vs symptom.
- *Default*: propose a diagnosis.
- *Drill-down*: the signals behind the diagnosis.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: reactive/pull.
- *Derivable/Slot*: form = deployment diagnosis; slot = `‹the deployment issue›`.

**A-050 — Apply a fix, patch, or config change to a deployment** · D0 Technical Manager · **P11 Operate Console** (apply within design)
- *Trigger*: a diagnosed issue gets a fix **within the established design** (no product redesign).
- *Presented*: an apply surface bounded to deployment-level changes; records the change.
- *Default*: apply the diagnosed fix.
- *Drill-down*: the change scope & its boundary.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull.
- *Derivable/Slot*: form = within-design deployment fix; slot = `‹the fix/patch›`.

**A-051 — Escalate to the D1 Technical Manager when a problem exceeds front-line support** · D0 Technical Manager · **P14 Support/Escalation** (up the hierarchy)
- *Trigger*: a problem exceeds front-line competence/authority (position hierarchy, Phase 5 §Item 3 — escalate only when the lower position lacks authority).
- *Presented*: a context-carrying escalation to R-04; the reason it exceeds front-line.
- *Default*: escalate with attached diagnosis.
- *Drill-down*: the diagnosis being handed up.
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull → hand-off.
- *Derivable/Slot*: form = upward escalation with diagnosis; slot = `‹the exceeding problem›`.

**A-059 — Monitor / observe D0 deployment health & status (standing, proactive)** · D0 Technical Manager · **P6 Monitoring View** (proactive, distinct from reactive A-049 and from A-038's health *settings*)
- *Trigger*: standing; proactive observation of deployment health/status.
- *Presented*: deployment health/status indicators (the operational counterpart to A-038's health *settings*); deviation surfaced proactively (monitoring before usage, Phase 5 §Item 1).
- *Default*: passive glance; alert on deviation.
- *Drill-down*: an indicator → its signal → diagnosis (A-049).
- *Attention*: Technical-Manager's own; zero D1-Designer.
- *Direction*: pull, with push alerts.
- *Derivable/Slot*: form = standing deployment health monitor; slot = `‹the deployment health signals›`.

### R-07 — D2 Assistant *(the single interaction point itself — the **medium** through which every R-00/R-01 surface is delivered; adds **no incremental Designer attention**, it exists to absorb it)*

**A-062 — Conduct the design on the Designer's behalf and answer his queries through the single interaction point** · D2 Assistant · **P18 Internal Work Sandbox** (the interaction front's own work) *(realises P1–P9 for R-01)*
- *Trigger*: any Designer interaction; the Assistant's **core function** (Phase 2 §P3; Phase 4 §Item 3; `C-2026-07-19-1`).
- *Presented*: from the Designer's side, **one system** — he never selects a component or channel; the Assistant conducts the design and answers behind that single surface.
- *Default*: n/a (it is the medium).
- *Drill-down*: it *provides* others' drill-down; owns none of its own toward the Designer.
- *Attention*: **absorbs** Designer attention cost (does not add it) — this is the consolidation the fundamentals demand.
- *Direction*: two-way; the single point.
- *Derivable/Slot*: form = unified conduct-and-answer front; slot = `‹the design being conducted›`.

**A-063 — Interpret and route the Designer's input; preserve interaction context** · D2 Assistant · **P18 Internal Work Sandbox** (routing)
- *Trigger*: any Designer input (direction / clarification / investigation / monitoring / intervention).
- *Presented*: (Designer-invisible) D2 **owns the routing burden** — the Designer does not decide which internal function receives the input; **context is preserved** across interactions (Phase 2 §4.1–4.3).
- *Default*: route by interpreted intent.
- *Drill-down*: n/a to the Designer (internal).
- *Attention*: **removes** Designer attention (he need not route or re-supply context).
- *Direction*: internal, invisible.
- *Derivable/Slot*: form = intent-routing + context preservation; slot = `‹the input to route›`.

**A-064 — Present Designer-oriented output (completion reports, Review Stops, Clarification Requests, summaries) with drill-down** · D2 Assistant · **P5 Completion Report / Notification** *(the presentation engine behind P2/P4/P5)*
- *Trigger*: any item produces output for the Designer (the reporting side of every item).
- *Presented*: **human-readable**, judgment-oriented output — completion reports, Review Stops, Clarification Requests, summaries — never raw machine records; **drill-down on request** (Phase 1 §2.4; Phase 2 §3.2, §3.4).
- *Default*: skimmable summary; detail only on request.
- *Drill-down*: progressive depth into any presented item.
- *Attention*: the **presentation** that keeps every other surface's cost low; itself minimal.
- *Direction*: **push** (present) with **pull** drill-down.
- *Derivable/Slot*: form = human-framed presentation + drill-down engine; slot = `‹the output being presented›`.

---

## C. Attention accounting (rolled up across the 63 surfaces)

**The axis that matters (the D2 priority):** total **D1-Designer** attention. The layout concentrates it
deliberately and keeps the rest at or near zero.

**By whose budget:**

| Bearer | Actions | D1-Designer attention |
|---|---|---|
| **R-01 D1 Designer** (via the D2 Assistant) | 24 (A-012–A-020, A-001/002/004/005/006/007/008/009, A-052/053/054/055/056/057/058) | the **entire** D1-Designer budget |
| **R-00 D2 Designer** (meta-builder) | 3 (A-010, A-011, A-061) | **zero** — separate D2-Designer budget |
| **R-02 Design Node Builder** (internal D2 agent) | 8 (A-021–A-027, A-060) | **zero** — D2 owns the work |
| **R-03 D1 Programmer** | 3 (A-028, A-040, A-041) | **zero** — Programmer's own budget |
| **R-04 D1 Technical Manager** | 7 (A-029–A-033, A-042, A-043) | **zero** — Technical-Manager's budget |
| **R-05 D0 Operator** | 8 (A-034–A-036, A-044–A-048) | **zero** — Operator's own (itself minimised, primary-beneficiary) |
| **R-06 D0 Technical Manager** | 7 (A-037–A-039, A-049–A-051, A-059) | **zero** — Technical-Manager's budget |
| **R-07 D2 Assistant** | 3 (A-062, A-063, A-064) | **negative** — the medium that *absorbs* Designer cost |
| **Total** | **63** | — |

**How many actions cost the D1 Designer nothing: 39 of 63** (all of R-00, R-02–R-07). The Designer's
attention is spent **only** on the 24 R-01 surfaces — and most of those are optional pull.

**Within the 24 R-01 surfaces (where the cost concentrates):**

- **Push, worth-it interventions (the genuine cost, ~8):** A-057 Constitution Review Stop **(high —
  deliberately, highest leverage)**; A-018 Clarification Request **(medium–high, the only hard-blocking
  cost, batched + leverage-pitched)**; A-014 initial understanding Review Stop (medium); A-001 framework
  acceptance, A-016 setup package, A-012 operating contract, A-015 posture, A-056 roles (each **low**,
  low-cost-default accept); A-005 node Review Stops (**scale with node height** — low for deep nodes,
  high for a Constitution-class node).
- **Pull, self-chosen (zero unless the Designer chooses to spend, ~16):** monitoring (A-052/053/054),
  inquiry (A-007), investigation (A-008, A-058, A-020, A-004), directives/authority (A-009, A-006),
  edits (A-002, A-017, A-019), entry decision (A-055), plus intake (A-013, front-loaded).

**Direction split (63):** **push** demanding-or-offered ≈ 10 (8 R-01 gates + A-045/A-046 to the
Operator + A-039 into R-06 as received); **pull** self-initiated ≈ most of the rest; **internal / zero-
Designer** = 14 (R-02's 8 + R-07's 3 + R-03's pull-only work, etc.). Standing **monitoring** surfaces
(A-052/053/054/033/035/047/059) are pull with push-on-deviation alerts.

**Where attention concentrates — one line:** on the **high-leverage passive gates for the D1
Designer** — chiefly the **Constitution Review Stop (A-057)** and consolidated **Clarification Requests
(A-018)**, with everything else either a low-cost accept-the-default gate or Designer-initiated pull;
**39 of 63 actions cost the Designer nothing**, and the D2 Assistant (R-07) is the single surface that
absorbs, rather than adds, interaction cost.

---

## Self-check (contract §3)

- **Coverage (gating) — PASS.** All **63** inherited actions have their **own** surface, by action (not a
  pattern-with-a-mapping): R-00 (3) + R-01 (24) + R-02 (8) + R-03 (3) + R-04 (7) + R-05 (8) + R-06 (7) +
  R-07 (3) = **63**. Every pattern P1–P18 owns ≥1 action; no orphan action, no orphan pattern.
  Actions sharing a pattern keep **distinct** surfaces (e.g. A-052/053/054 all P6; A-001 vs A-002;
  A-034 vs A-044; A-049 vs A-059).
- **Conformance — PASS (checked first, gating).** No governing statement is contradicted:
  **single interaction point** — every R-00/R-01 surface is delivered *through* the D2 Assistant; no
  Designer surface addresses an internal node (Phase 2 §P3, Phase 4 §Item 3, `C-2026-07-19-1`).
  **Each position sees only what it needs** — operator vs technical-manager configuration surfaces are
  scoped apart (A-036 vs A-038), machine records never pushed to the Designer (Phase 1 §2.4, Phase 5
  §Item 3). **Attention priority** — every Designer surface carries a low-cost default and is
  leverage-gated; the accounting makes total Designer cost legible (Phase 1 §2.3/§2.5, Phase 2 §P1).
  **Observability / harness / verification-before-realization** — monitoring surfaces (P6), harness runs
  (P17, A-024/A-060 before commit), deploy gates (P16) all honoured. Provenance kept distinct (Phase 1
  §4.6). No surface deviates-and-flags.
- **Quality (derived from the fundamentals, not a scorer) — PASS.** Each surface minimises attention
  (low-cost default + leverage), is human-framed (issue/rationale/alternatives/consequence/action),
  progressively disclosed (drill-down not push), observable (state/health/deviation visible), and
  distinct. Bias-to-more honoured: distinct surfaces kept wherever plausibly distinct (18 patterns; the
  three monitoring subjects and the reactive/proactive diagnosis pair kept separate).
- **Derivable-vs-slot — PASS.** Every surface fixes the **form + qualities** now and leaves
  **product-specific content** as a named `‹slot›` (results, jobs, parameters, deployment, …), since the
  D1/D0 project is unknown.
