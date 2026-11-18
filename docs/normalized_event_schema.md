# Normalized Event Schema

## 1. Purpose

The Normalized Event Schema defines a common structure for security events received from CSV files, JSON files, authorized Windows Security Log exports, and registered monitoring agents.

## 2. Standard Fields

| Field | Data Type | Description |
|---|---|---|
| event_id | String | Original Windows Event ID |
| timestamp | ISO 8601 string | Time when the event occurred |
| computer | String | Computer name that generated the event |
| username | String | Associated user account |
| source_ip | String or null | Source IP address, if available |
| event_type | String | Normalized event category |
| status | String | Success, Failure, or Unknown |
| logon_type | Integer or null | Windows logon type, when applicable |
| message | String | Event description |
| source | String | Origin of the record, such as CSV, JSON, or Windows Agent |

## 3. Example Normalized Event

```json
{
  "event_id": "4625",
  "timestamp": "2026-11-18T10:00:00",
  "computer": "LAB-PC",
  "username": "test_user",
  "source_ip": "198.51.100.20",
  "event_type": "Logon",
  "status": "Failure",
  "logon_type": 3,
  "message": "Repeated failed login attempt",
  "source": "CSV"
}
```

## 4. Normalization Rules

1. Timestamps will be converted into a consistent ISO 8601 format.
2. Event IDs will be stored consistently as strings.
3. Missing usernames will be represented as null or an agreed unknown value.
4. Missing source IP addresses will be represented as null.
5. Event status will use standardized values: Success, Failure, or Unknown.
6. Computer names will be retained to identify the originating system.
7. Original event information will be preserved where practical for investigation.

## 5. Multi-Computer Support

For the authorized agent extension, the system will associate every event with its originating computer. A registered device identifier may also be added during implementation.

## 6. Data Validation

The normalizer will validate required fields, check timestamp formats, and identify incomplete or malformed records.

Invalid records will be counted and reported rather than silently discarded.