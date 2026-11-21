# Detection Engine Design

## 1. Introduction

The Detection Engine is a core component of the Security Log Analyzer and Automated Alert System. It analyzes normalized Windows Security Events and identifies suspicious activities using predefined detection rules.

## 2. Detection Rules

The system currently implements four detection rules.

### R1 – Repeated Failed Logins
- Event ID: 4625
- Threshold: 5 failed login events
- Time Window: 5 minutes
- Grouping: Same username and source IP
- Severity: Medium

### R2 – Successful Login After Failures
- Event IDs: 4625 and 4624
- Threshold: At least 2 failed logins followed by a successful login
- Time Window: 10 minutes
- Grouping: Same username and source IP
- Severity: High

### R3 – Privileged Account Change
- Event ID: 4732
- Condition: User added to the local Administrators group
- Severity: High

### R4 – Unusual Activity Volume
- Event ID: 4624
- Threshold: 6 successful logins
- Time Window: 1 minute
- Grouping: Same username and computer
- Severity: Medium

## 3. Detection Process

1. The CSV Parser loads and validates input events.
2. Normalized events are passed to the Detection Engine.
3. Each detection rule evaluates events according to its threshold and conditions.
4. Matching events generate detection findings.
5. Findings are forwarded to the Alert Manager.

## 4. Testing

The detection rules are tested using positive and negative test cases.

The test suite covers:
- Repeated failed login detection.
- Successful login after repeated failures.
- Privileged account change detection.
- Unusual successful login volume.
- Negative cases where detection conditions are not satisfied.

## 5. Current Limitations

- Detection currently uses the prepared CSV dataset.
- R3 relies on the Administrators group name being available in the event's message or normalized target_group field.
- Multi-computer agent collection and File Integrity Monitoring are approved project extensions and are not claimed as implemented by this detection engine yet.

## 6. Future Extensions

The Detection Engine will be extended to process authorized security events received from multiple registered computers and File Integrity Monitoring events.
