# AI & Agentic QA Approach

## Where I Would Use AI in QA

I would use AI to support QA activities where it can reduce repetitive
work while keeping human review for release-critical decisions.

Potential uses include:

- Generating initial test scenarios from requirements and acceptance criteria
- Identifying missing or ambiguous requirements
- Suggesting edge cases and negative tests
- Generating initial API/UI automation test skeletons
- Analyzing failed automated tests and logs
- Summarizing regression results
- Detecting patterns across recurring defects
- Assisting with exploratory testing ideas


## Worked Example – AI-Assisted Requirement and Test Coverage Review

Before testing a new feature, an AI agent could analyze:

- Ticket description
- Acceptance criteria
- API contract
- Existing regression tests
- Related historical defects

The agent could produce:

1. Requirements ambiguities that need clarification
2. Positive test scenarios
3. Negative and boundary scenarios
4. Existing tests that already provide coverage
5. Missing regression coverage
6. Suggested automation candidates


### Example

For the Devices Command API, the ticket defines:

`POST /api/devices/command`

An AI-assisted requirements review could identify additional scenarios such as:

- Missing authentication
- Invalid authentication
- Unsupported command
- Empty devices array
- Non-existent device
- Missing command_version
- Invalid command_version
- Mixed online/offline device batch

The output would be reviewed by QA before execution rather than automatically
being treated as correct test coverage.


## Agentic Extension

This could later be extended into an agent integrated with the development
workflow.

When a ticket moves to `Ready for Test`, the agent could:

1. Read the ticket and acceptance criteria.
2. Compare the change with existing tests.
3. Suggest missing test scenarios.
4. Identify potentially affected regression areas.
5. Generate draft automated tests.
6. Present the proposed coverage to QA for approval.

QA would remain responsible for approving the test strategy and release decision.


## AI Limitations

AI should assist QA rather than replace QA judgement.

Important limitations include:

- AI can misunderstand incomplete requirements.
- Generated test cases may contain incorrect assumptions.
- AI may generate tests that appear valid but do not test the intended behavior.
- AI cannot reliably determine business priority without product context.
- Generated automation can contain incorrect selectors, assertions, or test data.
- Sensitive credentials, production data, tokens, or customer information should
  not be provided to external AI systems without appropriate controls.
- AI-generated findings should be verified before bugs are reported.
- Release decisions should remain human-owned.

The goal is to use AI to increase QA speed and coverage while maintaining
human validation for correctness, risk assessment, and release decisions.
