# Alert Design

## 1. Introduction

The Alert Manager converts detection findings into standardized security alerts. Each alert contains an identifier, timestamp, rule information, severity, affected entity, reason, and supporting evidence.

## 2. Alert Structure

Each generated alert contains:

| Field | Description |
|---|---|
| alert_id | Unique identifier within the current execution |
| timestamp | Timestamp of the latest supporting event |
| event_category | Type of monitored event |
| rule_id | Detection rule identifier |
| rule_name | Name of the matched rule |
| severity | Alert severity |
| affected_entity | User or affected entity |
| reason | Explanation of the detection |
| supporting_evidence | Events that triggered the alert |
| source_ip | Source IP when available |
| computer | Computer name when available |

## 3. Alert Identification

Alert IDs use the following format:

ALT-000001

The identifier increases for each alert generated during the current execution. Persistent global uniqueness will be addressed with alert storage.

## 4. Severity Levels

- High: Activities such as successful login after repeated failures and privileged account changes.
- Medium: Repeated failed logins and unusual login volume.

## 5. Event Categories

### SecurityLog
Used for Windows Security Log events and, in the approved extension, authorized security events received from registered computers.

### FileIntegrity
Reserved for File Integrity Monitoring events such as file creation, modification, deletion, and permission changes.

## 6. Supporting Evidence

Each alert includes the original event records that triggered the detection. Evidence may include event ID, timestamp, username, source IP, computer, and message.

## 7. Approved Project Extensions

### Multi-Computer Monitoring
Transparent agents will be installed and registered only on authorized computers with owner or administrator permission. Permitted security events will be securely forwarded to the central analyzer.

### File Integrity Monitoring
The system will monitor selected authorized files and folders for creation, modification, deletion, and optionally permission changes. SHA-256 hashes and metadata will be used for integrity comparison. File contents will not be uploaded by default.

## 8. Current Implementation Status

The current Alert Manager generates standardized SecurityLog alerts in memory. Persistent alert storage and the approved multi-computer and File Integrity Monitoring extensions remain future implementation work.
