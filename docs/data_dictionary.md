# Data Dictionary — Security Log Analyzer and Automated Alert System

## Dataset Information

- Dataset Name: Dataset v1
- File: `data/test/dataset_v1.csv`
- Dataset Type: Synthetic test dataset
- Purpose: To test security log parsing and detection rules.
- Data Source: Manually created synthetic security events.
- IP Addresses: Documentation-only example IP ranges; not real monitoring targets.

## Field Definitions

| Field | Description |
|---|---|
| case_id | Unique identifier for a test scenario. Multiple events can belong to one case. |
| event_id | Windows Event ID, such as 4624, 4625, or 4732. |
| timestamp | Date and time when the event supposedly occurred. |
| computer | Name of the computer that generated the event. |
| username | Account associated with the event. |
| source_ip | IP address associated with the event, if available. |
| event_type | General category of the event, such as Login or AccountChange. |
| status | Outcome or status of the event, such as Success or Failed. |
| logon_type | Windows logon type, when applicable. |
| message | Human-readable description of the event. |
| label | Expected classification: Normal or Suspicious. |
| expected_rule | Detection rule expected to identify the scenario, if applicable. |
| expected_result | Expected analyzer outcome, such as Alert or No Alert. |

## Dataset Labels

- Normal: An event or scenario that should not trigger a security alert.
- Suspicious: An event or scenario designed to test a detection rule.

## Planned Detection Rules

- R1: Repeated failed login attempts.
- R2: Successful login after multiple failed attempts.
- R3: Privileged account or group membership change.
- R4: Unusual activity volume.

## Dataset Limitations

- This is a synthetic dataset, not a live monitoring feed.
- Events are manually created for testing.
- Detection thresholds will be finalized and documented during system design.
- Synthetic events do not prove that an actual attack occurred.
