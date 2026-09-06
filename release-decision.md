## Release Communication to Product Management & Development

Hi Product & Development,

Based on the QA pass, my recommendation is **not to release the current build tomorrow** until the Must Fix issues below have been addressed and verified.

### Must Fix Before Release

- **#12 – Core Services "Outdated" filter incorrectly returns devices that are "Unavailable"**
  - Direct filter correctness issue and acceptance-criteria failure.

- **#13 – Core Services "Unavailable" is missing from the Core Service filter**
  - A valid device value cannot be selected through the filter.

- **#14 – Square orientation is missing from the Devices Orientation filter**
  - A valid orientation present in the device data cannot be selected, so the feature does not fully meet the acceptance criteria.

- **#17 – Offline device command returns 500 Internal Server Error and exposes stack trace**
  - An expected offline-device condition results in a server error and exposes internal implementation details.

- **#18 – Devices Command API returns 200 OK for non-existent device ID**
  - The API reports a successful response for an invalid device identifier.

- **#19 – Devices Command API does not validate required command_version**
  - Missing, whitespace-only, and unexpected command_version values are accepted.

### Should Fix / Can Be Planned Separately

- **#16 – Metadata field and value filters have a significant delay when applied**
  - Should Fix. This affects responsiveness, but no performance threshold is defined in the acceptance criteria, so I would not independently block tomorrow's release on this issue.

- **#20 – User is logged out when refreshing the browser page**
  - Should Fix. This disrupts the authenticated user experience, but I would not treat it as an independent release blocker.

### Requires Clarification

- **#21 – Asset content remains accessible after logout via direct URL**
  - Product/Engineering should confirm whether direct asset URLs are intentionally public.
  - If assets are expected to require authentication, this becomes a **Must Fix before release**.
  - If public CDN access is intentional, the behavior should be documented and the issue can be closed or reclassified.

### Deferred Enhancement

- **#15 – Display selected metadata fields and values in the Devices table**
  - Can Defer. This would improve visibility/usability but is not required for the current release.

### Next Steps

Development should prioritize the Must Fix issues above. Once fixes are available, QA will perform targeted retesting of the affected functionality and run the relevant automated regression tests.

If the Must Fix issues cannot be resolved and verified before tomorrow's release, my recommendation remains **NO-GO**.

Thanks,
Neha
