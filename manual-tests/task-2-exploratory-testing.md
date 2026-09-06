# Task 2 – Exploratory Testing & Release Triage

## Scope

Exploratory testing was performed outside the two feature tickets,
with particular focus on authentication, session behavior and asset access.

## Issues Identified

| Issue ID | Issue | Severity | Frequency | Impact | Release Decision | 
|---|---|---|---|---|---|
| #20 | User is logged out when refreshing the browser page | Medium | Always | Normal browser refresh terminates the user's active session and requires re-authentication | Should Fix |
| #21 | Asset content remains accessible after logout via direct URL | High* | Always | Potential access-control issue: asset content remains accessible after the authenticated session has ended | Must Fix / Clarify |

\* Severity assumes asset content is intended to require authentication. The expected access model for direct CDN asset URLs should be confirmed with Product/Engineering.

## Triage Criteria

### Must Fix
Issues that violate critical functionality, acceptance criteria,
data/security expectations, or create unacceptable release risk.

### Should Fix
Important issues that affect usability or reliability but do not
necessarily prevent the release.

### Can Defer
Low-risk issues or improvements that can reasonably be addressed
after the release.

## Task 2 Release Assessment

The page-refresh logout issue should be fixed, but I would not block
the release solely because of this issue.

The direct asset URL behavior requires clarification before release.
If asset content is expected to be accessible only to authenticated
users, this should be treated as a release blocker because the content
remains accessible after logout.
