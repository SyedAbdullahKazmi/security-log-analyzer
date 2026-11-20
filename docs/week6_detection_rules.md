
# Week 6 - Detection Rules Implementation

## 1. Introduction

This week implements two baseline detection rules for
the Security Log Analyzer and Automated Alert System.

The rules analyze normalized Windows security events
and identify selected patterns that may require
further investigation.

## 2. Rule R1 - Repeated Failed Logins

**Purpose:**
Detect repeated failed authentication attempts for
the same user account from the same source IP.

**Input Event:**
- Windows Event ID: 4625

**Detection Logic:**
- Group events by username and source IP.
- Count failed login events within a rolling time window.
- Generate a detection finding when the threshold is met.

**Threshold:**
- Minimum events: 5
- Time window: 5 minutes
- Severity: Medium

**Rationale:**
Repeated failed logins may indicate password guessing
or another authentication problem. The threshold helps
identify repeated activity without treating one failed
login as suspicious by itself.

**Positive Test:**
Five failed login events for the same username and
source IP within five minutes.

**Negative Tests:**
- Four failed login events.
- Five failed login events spread over more than
  five minutes.

## 3. Rule R4 - Unusual Activity Volume

**Purpose:**
Detect an unusually high number of successful logins
for the same user account on the same computer.

**Input Event:**
- Windows Event ID: 4624

**Detection Logic:**
- Group events by username and computer.
- Count successful login events within a rolling
  time window.
- Generate a detection finding when the threshold
  is met.

**Threshold:**
- Minimum events: 6
- Time window: 1 minute
- Severity: Medium

**Rationale:**
An unusually high login event volume may indicate
repeated account activity that requires investigation.
A high event count alone does not prove malicious
behavior.

**Positive Test:**
Six successful login events for the same username
and computer within one minute.

**Negative Tests:**
- Five successful login events.
- Six successful login events spread over more than
  one minute.

## 4. Testing Approach

Automated unit tests are used to verify:
- Positive detection cases.
- Negative detection cases.
- Time-window boundaries.
- Detection against the labelled synthetic dataset.

The test suite is executed using:

python -m unittest discover -s tests -v

## 5. Limitations

- The rules depend on the availability and accuracy
  of normalized event fields.
- Missing usernames, source IP addresses, or computer
  names may prevent grouping.
- A detection finding is an indicator for investigation,
  not proof of an attack.
- Thresholds are baseline values and may require
  tuning for different environments.

## 6. Future Integration

The detection engine is designed to support the
project's approved extensions:

- Authorized monitoring agents on registered computers
  will forward permitted security events to the central
  analyzer.
- File Integrity Monitoring will provide file creation,
  modification, and deletion events for selected
  authorized paths.

These event sources will be integrated with the
appropriate detection and alert workflows in later
implementation stages.

## 7. Implementation and Test Results

Both baseline detection rules were implemented
successfully in Python.

Automated test results:
- Total tests: 16
- Passed: 16
- Failed: 0

The original synthetic dataset contains 17 accepted
records and was used to verify R1 and R4 detection.

Sample detection output was generated using the
run_detection.py module.

Screenshots are available in docs/evidence/.