# Design Decisions
## Security Log Analyzer and Automated Alert System

### 1. Programming Language

**Decision:** Python 3.

**Reason:** Python provides useful libraries for file handling, log parsing, data processing, and automated testing.

### 2. Input Formats

**Decision:** CSV and JSON, with authorized Windows Security Log exports as supported input sources.

**Reason:** These formats make it easier to import and test security event records.

### 3. Modular Architecture

**Decision:** Separate modules for ingestion, parsing, normalization, detection, alerts, and storage.

**Reason:** Modular design makes the system easier to maintain, test, and extend.

### 4. Detection Approach

**Decision:** Use at least four transparent rule-based detection conditions.

**Reason:** Clearly documented rules make alerts understandable and allow repeatable testing.

### 5. Storage

**Decision:** Support persistent storage using CSV, JSON, or SQLite.

**Reason:** Persistent storage allows analysts to review previous alerts and analysis results.

### 6. Multi-Computer Monitoring

**Decision:** Use authorized collection agents and a central analysis system as an extended architecture.

**Reason:** This allows permitted security events from multiple registered computers to be analyzed centrally.

### 7. Agent Authentication and Communication

**Decision:** Agents will be registered with the central system and communicate through authenticated, encrypted channels.

**Reason:** This helps prevent unauthorized devices from submitting events and protects log information during transmission.

### 8. Device Identification

**Decision:** Each registered computer will have a unique device identifier in addition to its computer name.

**Reason:** Computer names alone may not always uniquely identify a device.

### 9. Error Handling

**Decision:** Invalid records will be counted and reported instead of silently discarded.

**Reason:** This improves reliability and makes testing more transparent.

### 10. Project Limitations

**Decision:** The system will focus on security event collection, analysis, alerting, and reporting.

**Reason:** Automated blocking, account disabling, and covert monitoring are not project objectives.