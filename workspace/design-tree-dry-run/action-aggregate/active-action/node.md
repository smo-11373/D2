# Node: active-action

- **Authors / owns:** the **active [A]** pieces of the D1 Designer's (R-01) actions — the actions he
  takes *on his own initiative*. Merged up into the parent's aggregate `A-` table.
- **Owns these rows** (full text in `../role-action-table.md`):
  - **Inspect / investigate / direct:** `A-007` (inquiry/inspection), `A-008` (investigation),
    `A-009` (directive)
  - **Monitor:** `A-052` (progress), `A-053` (resource & cost spend), `A-054` (health & anomalies)
  - **Evaluate a change:** `A-058` (impact dry-run, before proposing) — *initiator-driven, placed
    here as a self-started command; borderline, noted below*
  - **Check afterward:** `A-020` (request / review a D2 audit)
- **Contract received (from the action aggregate):** produce the active-action pieces for merge.
- **Contract to children:** none — leaf node (authors its own pieces; no descendants in this run).
- **Justification (`RU-02`):** the `[A]` sections of the functional doc (§9 inspecting/monitoring/
  intervening; checking how D2 served) and their "Why" arguments.
- **Finding (dry run).** A few actions are **borderline** between passive and active — e.g. `A-058`
  (evaluate), placed here, and reserve-authority (kept in passive). The split is a useful *first*
  partition, not a crisp one; the aggregate is unaffected (every row lands in the merge exactly once).
