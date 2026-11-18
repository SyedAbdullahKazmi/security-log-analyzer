# Detection Rules
## Security Log Analyzer and Automated Alert System

### 1. R1 — Repeated Failed Login Attempts

**Purpose:** Identify repeated failed login attempts that may indicate password guessing or brute-force activity.

- Event ID: 4625
- Condition: At least 5 failed login events.
- Time Window: 5 minutes.
- Grouping: Same username and source IP address.
- Severity: Medium.
- Expected Action: Generate an alert containing the related failed login records.

**Example:** Five failed login attempts for the same user from the same IP within five minutes should trigger R1.

### 2. R2 — Successful Login After Multiple Failures

**Purpose:** Identify a successful login that occurs after multiple failed login attempts.

- Event IDs: 4625 and 4624.
- Condition: At least 2 failed login events followed by a successful login.
- Time Window: 10 minutes.
- Grouping: Same username and source IP address.
- Severity: High.
- Expected Action: Generate an alert containing the failed attempts and subsequent successful login.

**Example:** Two failed logins followed by a successful login for the same user and source IP within ten minutes should trigger R2.

### 3. R3 — Privileged Group Membership Change

**Purpose:** Identify changes that add an account to a privileged local security group.

- Event ID: 4732.
- Condition: A user is added to the local Administrators group.
- Severity: High.
- Expected Action: Generate an alert containing the affected account and group change information.

**Example:** An event showing that test_user was added to the local Administrators group should trigger R3.

### 4. R4 — Unusual Login Activity Volume

**Purpose:** Identify an unusually high number of successful login events within a short period.

- Event ID: 4624.
- Condition: At least 6 successful login events.
- Time Window: 1 minute.
- Grouping: Same username and computer.
- Severity: Medium.
- Expected Action: Generate an alert containing the related successful login records.

**Example:** Six successful login events for the same user on the same computer within one minute should trigger R4.

### 5. General Detection Requirements

1. Detection rules must use event fields and defined conditions, not only keywords in messages.
2. Each generated alert must contain its rule ID and supporting evidence.
3. Thresholds must be configurable or clearly documented.
4. Events with missing required fields must be handled safely.
5. A detection result does not automatically prove that an attack occurred.
6. Normal activity should not generate alerts unless it meets a documented rule condition.

### 6. Threshold Limitations

The thresholds in this document are initial testing values. They will be evaluated using normal and suspicious test cases and may be adjusted to reduce false positives and false negatives.