# Ticket #1 — Devices Page Filters

## Scope

Validation of Status, Core Services, Orientation and Metadata filters,
including individual filtering and combined AND behavior.

## Test Execution

| ID | Scenario | Expected Result | Result | Related Issue |
|---|---|---|---|---|
| 01 | Filter by Status = Online | Only Online devices are returned | PASS | — |
| 02 | Filter by Status = Offline | Only Offline devices are returned | PASS | — |
| 03 | Filter by Core Services = Up-To-Date | Only Up-To-Date devices are returned | PASS | — |
| 04 | Filter by Core Services = Outdated | Only Outdated devices are returned | FAIL | #12 |
| 05 | Filter by Core Services = Unavailable | Unavailable is selectable and only Unavailable devices are returned | FAIL | #13 |
| 06 | Filter by Orientation = Portrait | Only Portrait devices are returned | PASS | — |
| 07 | Filter by Orientation = Landscape | Only Landscape devices are returned | PASS | — |
| 08 | Filter by Orientation = Square | Square is selectable and only Square devices are returned | FAIL | #14 |
| 09 | Select Metadata field and value | Matching devices are returned | PASS | — |
| 10 | Apply multiple filters | Returned devices satisfy every selected filter (AND) | PASS | — |
| 11 | Change/clear filters | Results update according to remaining filters | PASS | — |
| 12 | Apply Metadata field/value | Results update without significant unexplained delay | IMPROVEMENT | #16 |
