# Role–Action Catalog (DEGRADED FIXTURE — negative test)

*Deliberately broken to prove the harness makes deviation visible. Faults injected:
missing role R-07; duplicate action ID A-034; retired ID A-003 reused; one action with
no Source; one thin description; one action renamed (paraphrased) to test lexical match;
one spurious extra action.*

## Roles

| ID | Role | Relationship | Description | Source |
|------|------|--------------|-------------|--------|
| R-00 | D2 Designer | builds D2 | Builds the D2 product. | Phase 5 (ref) |
| R-01 | D1 Designer | uses D2 → builds D1 | Primary and only user of D2. | Phase 1 §2 |
| R-02 | Design Node Builder | internal to D2 | Builds a Design Node under direction. | Phase 5 §Item 3 |
| R-03 | D1 Programmer | implements code | Changes product code per spec. | Phase 5 §Item 3 |
| R-04 | D1 Technical Manager | operates the D1 wrapper | Runs the D1 wrapper. | Phase 5 §Item 3 |
| R-05 | D0 Operator | operates D0 | Runs the deployed D0 in production. | Phase 5 §Item 3 |
| R-06 | D0 Technical Manager | supports D0 | Front-line support for a D0 deployment. | Phase 5 §Item 3 |

## Actions

### R-00 — D2 Designer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-010 | Complete / clarify / expand D2's living working sets | Phase 5 §Item 2 | |
| A-003 | Revive a retired id on purpose | Phase 5 | retired-id reuse fault |

### R-01 — D1 Designer

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-012 | Confirm the Designer–D2 Operating Contract | Phase 3 §Item 1 | |
| A-013 | Give the starting design materials — the prior D1 build plus the change the Designer wants | | paraphrase of A-013 + missing Source |
| A-015 | Pick | Phase 6 Item 1 §2 | thin description |

### R-04 — D1 Technical Manager

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-034 | Adjust a governed product parameter without changing code | Phase 5 §Item 3 | duplicate id (belongs to R-05) |
| A-999 | Reboot the universe nightly | Phase 5 §Item 3 | spurious / untraceable extra |

### R-05 — D0 Operator

| ID | Action | Source | Notes |
|-------|--------|--------|-------|
| A-034 | Perform routine operation — start, run, stop, schedule D0 jobs | Phase 5 §Item 3 | duplicate id |
