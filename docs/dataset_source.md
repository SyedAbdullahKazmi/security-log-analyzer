
# Dataset and Source Documentation

## 1. Project
Security Log Analyzer and Automated Alert System

## 2. Selected Data Source
Windows Security Event Logs

## 3. Data Collection Method
Security events will be obtained from an authorized
Windows computer using Windows Event Viewer.

## 4. Selected Event IDs

| Event ID | Description |
|---|---|
| 4624 | Successful Logon |
| 4625 | Failed Logon |

## 5. Dataset Format
Initial source format: Windows EVTX event logs.

For analysis and testing, records may be converted
into a normalized CSV or JSON format.

## 6. Important Data Fields
- Timestamp
- Event ID
- Computer
- Username
- Source IP
- Logon Type
- Event Message

## 7. Data Privacy
Only authorized logs will be used.
Sensitive usernames and IP addresses will be
redacted when sharing project evidence.

## 8. Dataset Limitations
- Some events may contain missing fields.
- Local login events may not provide a source IP.
- Selected events do not represent every possible
  security activity.
- A limited dataset cannot represent all real-world
  attack scenarios.

## 9. Future Dataset Preparation
A labelled dataset containing normal and suspicious
events will be prepared in Week 3.

Expected outcomes will be documented for testing
detection rules.
