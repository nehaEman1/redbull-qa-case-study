# QA Case Study
## Manual Testing

Manual testing was performed for Ticket #1 – Devices Filters.

Coverage included:
- Status filter correctness
- Core Services filter correctness
- Orientation filter correctness
- Metadata field/value filtering
- Combined filter AND behavior
- Filter result accuracy
- Basic responsiveness during filtering

Test scenarios, execution results, and related defects are documented here:

`manual-tests/ticket-1-devices-filters.md`

Defects discovered during manual testing were logged individually on the provided GitHub project board.

## Automated Tests
### Automation Setup
The automated UI tests are implemented using:
- Python
- pytest
- Selenium WebDriver
- Google Chrome

## Ticket #1 – Devices Filters
File:
`test_devices_filters.py`

### Automated Scenario
**Core Services – Outdated Filter**

The test verifies that when **Core Services = Outdated** is selected, every device returned in the table has a Core Services value of **Outdated**.

Test flow:

1. Open the QA application.
2. Log in with the test user.
3. Navigate to the Devices page.
4. Select `Core Services = Outdated`.
5. Wait for the device table to refresh.
6. Read the Core Services value of each returned device.
7. Assert that every returned value is `Outdated`.

### Regression Coverage
This test provides regression coverage for **Bug #12 – Core Services "Outdated" filter incorrectly returns devices that are "Unavailable"**.
The test currently fails in the QA environment because devices with `Core Services = Unavailable` are returned when the `Outdated` filter is selected.
Once the defect is fixed, the same test can be used as a regression test to ensure the issue does not reoccur.

## Setup

Install the required packages:
```bash
pip install selenium pytest
```

The test credentials are provided through environment variables rather than being stored in the source code.

### Windows Command Prompt

```cmd
set TEST_EMAIL=<test-email>
set TEST_PASSWORD=<test-password>
```

## Running the Test

Run:

```bash
pytest test_devices_filters.py -v
```

Expected behavior after Bug #12 is fixed:

```text
test_core_services_outdated_filter PASSED
```

Current QA behavior:

```text
test_core_services_outdated_filter FAILED
Expected 'Outdated' but found 'Unavailable'
```
