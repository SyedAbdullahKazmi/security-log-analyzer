# System Architecture
## Security Log Analyzer and Automated Alert System

### 1. Architecture Overview

The system will use a modular architecture. Its main purpose is to process security events, normalize their information, detect suspicious activities, and generate alerts.

The basic analyzer will support offline CSV and JSON log files. An approved multi-computer extension will allow registered computers to send permitted security events to a central analysis system.

### 2. Main Components

**1. Log Sources**

- Authorized Windows Security Log exports.
- Synthetic security datasets.
- Security events from approved computers through configured collection agents.

**2. Log Collection Agent — Multi-PC Extension**

- Runs on an authorized and registered computer.
- Collects only configured security events.
- Associates events with the originating computer.
- Sends events to the central system through authenticated, encrypted communication.

**3. Log Ingestion Module**

- Receives supported log files or events from registered agents.
- Checks input format.
- Handles invalid or incomplete records.
- Tracks accepted and rejected records.

**4. Parser**

- Reads CSV and JSON records.
- Extracts relevant security fields.
- Converts supported input records into a common structure.

**5. Normalization Module**

- Standardizes timestamps, computer identifiers, usernames, event types, and other fields.
- Handles missing or unavailable values consistently.

**6. Detection Engine**

Applies at least four documented detection rules:

- R1: Repeated failed login attempts.
- R2: Successful login after multiple failed attempts.
- R3: Privileged account or group membership change.
- R4: Unusual activity volume.

**7. File Integrity Monitoring Component**

The system will include a File Integrity Monitoring component that monitors administrator-selected files and folders on authorized computers. It will use SHA-256 hashes and file metadata to identify file creation, modification, and deletion. Detected file events will be forwarded to the central analysis system and processed by the unified alert generator.

**8. Alert Generator**

Creates alerts containing an alert ID, timestamp, rule name, severity, affected entity, and supporting evidence.

**9. Storage and Reporting**

- Stores normalized events and alerts.
- Supports CSV, JSON, or SQLite storage.
- Produces summaries and reports.

### 3. System Workflow

Log Sources → Collection or File Import → Log Ingestion → Parser → Normalization → Detection Engine → Alert Generator → Storage and Reporting

### 4. Multi-Computer Extension

For authorized multi-computer monitoring, registered agents will send permitted security events to the central system.

The central system will identify the originating computer and analyze the received events using the same normalization and detection pipeline.

### 5. Security Considerations

- Only authorized computers will be registered.
- Agent-to-server communication will use authentication and encryption.
- Access to collected logs will be restricted.
- Sensitive information will be protected.
- The system will not perform automatic blocking or account disabling.

### 6. Design Approach

The architecture will be modular so that file-based analysis can work independently of the multi-computer extension. This will make testing easier and allow additional authorized log sources to be integrated later.