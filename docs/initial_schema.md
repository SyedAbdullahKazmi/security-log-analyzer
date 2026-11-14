
# Initial Data Schema

## Project
Security Log Analyzer and Automated Alert System

## Data Source
Authorized Windows Security Event Logs

## Selected Event IDs
- 4624: Successful Login
- 4625: Failed Login

## Initial Event Fields

| Field Name | Description | Data Type |
|---|---|---|
| timestamp | Event occurrence time | DateTime |
| event_id | Windows event identifier | Integer |
| source | Event source/computer | String |
| event_type | Successful or failed login | String |
| username | Target account name | String |
| source_ip | Source IP address, if available | String |
| logon_type | Type of login | Integer/String |
| message | Event description | String |

## Missing Values
Some fields, especially source IP, may be unavailable.
Missing values will be handled safely during parsing.

## Data Limitations
- Only selected Windows Security Events are initially considered.
- Available fields may differ between event types.
- Real logs may contain sensitive information.
- Sensitive information will be protected or redacted.

## Future Processing
Raw events will be parsed, validated and
normalized into a common event structure.
