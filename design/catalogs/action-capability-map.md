# Action ↔ Capability Mapping

*Living. The Action ↔ Capability join — traceability that surfaces unsupported actions, orphan capabilities, and coverage gaps. Grouped by role for a per-role coverage view. See `README.md` for ID conventions; capabilities and their layers are in `capabilities.md`.*

## R-00 — D2 Designer

| Action | Capability | Notes |
|--------|------------|-------|
| A-010 | — | Meta: designing D2 itself; no operational capability |
| A-011 | — | Meta |

## R-01 — D1 Designer  *(served by D2 capabilities)*

| Action | Capability | Notes |
|--------|------------|-------|
| A-001 | C-06 | Accept the operating framework/plan |
| A-002 | C-06 | Modify the framework/plan |
| A-004 | C-20 | Discuss a concern (Designer-initiated) |
| A-005 | C-15 | Review a node (a Review Stop) |
| A-006 | C-17 | Reserve/assign revision authority |
| A-007 | C-20 | Inquiry / inspection |
| A-008 | C-20 | Investigation / concern (absorbs former A-003) |
| A-009 | C-20 | Directive |
| A-012 | C-23 | Review operating contract (part of intake) |
| A-013 | C-23 | Provide initial design input |
| A-014 | C-13, C-15 | Review understanding: a report + a review stop |
| A-015 | C-01, C-22 | Select posture: choice + posture tuning |
| A-016 | C-02, C-03 | Review/revise the setup package |
| A-017 | C-05 | Revise setup later (governed) |
| A-018 | C-14 | Answer a Clarification Request |
| A-019 | C-22 | Tune resolution depth / posture |
| A-020 | C-21 | Request/review a D2 audit |
| A-052 | C-34 | Monitor design progress |
| A-053 | C-35 | Monitor resource & cost spend |
| A-054 | C-36 | Monitor design-process health & anomalies |
| A-055 | C-37 | Decide whether to adopt D2 (orientation-backed) |
| A-056 | C-38 | Review/adjust the roles table |
| A-057 | C-15, C-39 | Confirm the D1 foundational documents (key Review Stop) |

## R-02 — Design Node Builder  *(served by D2 capabilities)*

| Action | Capability | Notes |
|--------|------------|-------|
| A-021 | C-09 | Investigate predecessor material |
| A-022 | C-10 | Develop/compare/critique choices |
| A-023 | C-10 | Produce the node design spec |
| A-024 | C-11 | Internal evaluation |
| A-025 | C-12 | Submit for acceptance |
| A-026 | C-16 | Propose spawning strategy |
| A-027 | C-17 | Propose upward revision |

## R-03 — D1 Programmer  *(D1-product)*

| Action | Capability | Notes |
|--------|------------|-------|
| A-028 | C-27 | Implement from spec |
| A-040 | C-27 | Implementation-level tests |
| A-041 | C-27 | Fix implementation defects |

## R-04 — D1 Technical Manager  *(D1-product)*

| Action | Capability | Notes |
|--------|------------|-------|
| A-029 | C-24 | Adjust a governed parameter (RU-01) |
| A-030 | C-25 | Run the upgrade smoke-test harness |
| A-031 | C-25 | Repackage & distribute |
| A-032 | C-26 | Deploy D0 |
| A-033 | C-26 | Monitor D0 health |
| A-042 | C-25 | Roll back a release |
| A-043 | C-25 | Review upgrade records |

## R-05 — D0 Operator  *(D0-product)*

| Action | Capability | Notes |
|--------|------------|-------|
| A-034 | C-28 | Routine operation |
| A-035 | C-30 | User-level monitoring |
| A-036 | C-29 | Operator-level controls |
| A-044 | C-30 | View results/reports |
| A-045 | C-31 | Notifications / approvals |
| A-046 | C-31 | Routine error handling |
| A-047 | C-30 | Activity/usage/cost status |
| A-048 | C-33 | Request support / escalate |

## R-06 — D0 Technical Manager  *(D0-product)*

| Action | Capability | Notes |
|--------|------------|-------|
| A-037 | C-32 | Install a deployment |
| A-038 | C-32 | Maintain a deployment |
| A-039 | C-33 | Provide front-line support |
| A-049 | C-32 | Diagnose a deployment issue |
| A-050 | C-32 | Apply a fix/patch |
| A-051 | C-33 | Escalate to D1 Technical Manager |
