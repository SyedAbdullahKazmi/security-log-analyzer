# File Integrity Monitoring (FIM) Design
## Security Log Analyzer and Automated Alert System

### 1. Introduction

File Integrity Monitoring (FIM) is an additional feature of the Security Log Analyzer and Automated Alert System.

Its purpose is to monitor selected authorized files and folders and detect changes that may affect their integrity or security.

The system will identify file creation, modification, deletion, and optionally permission changes.

### 2. Objectives

- Monitor administrator-selected files and folders.
- Detect file creation.
- Detect file modification.
- Detect file deletion.
- Detect file permission changes where supported.
- Calculate SHA-256 hashes to identify content changes.
- Generate evidence-based security alerts.
- Associate file events with their originating computer.
- Support centralized monitoring through authorized collection agents.

### 3. Monitored File Events

| Event | Description |
|---|---|
| File Created | A new file appears in a monitored folder. |
| File Modified | Existing file contents or relevant metadata change. |
| File Deleted | A monitored file is removed. |
| Permission Changed | File access permissions are modified, where supported. |

### 4. File Integrity Verification

The system will calculate the SHA-256 hash of selected files.

A baseline hash will be recorded when monitoring begins or when an administrator approves the initial baseline.

When a file is modified, the system will calculate its hash again and compare it with the baseline.

If the hashes differ, the system will record a file modification event and generate an alert according to the configured policy.

### 5. File Event Information

Each detected file event will contain:

- Event ID
- Timestamp
- Computer name
- Device identifier, where available
- File path
- File name
- Event type
- Previous SHA-256 hash, where available
- Current SHA-256 hash, where available
- Event description

### 6. Multi-Computer Integration

The FIM component will operate through the authorized collection agent installed on registered computers.

The agent will monitor only administrator-selected files and folders.

Detected events will be transmitted through authenticated and encrypted communication to the central analysis system.

The central system will associate each event with its registered computer and generate centralized alerts.

### 7. Security and Privacy Considerations

- Monitoring requires computer owner or administrator authorization.
- Only explicitly selected files and folders will be monitored.
- File contents will not be uploaded to the central system by default.
- Hashes and relevant metadata will be used for integrity verification.
- Access to monitoring records will be restricted.
- Sensitive directories will be excluded unless explicitly approved.
- The agent will provide transparent monitoring and configuration.

### 8. Limitations

- SHA-256 detects content changes but does not identify who made the change by itself.
- Some temporary files may change frequently.
- Large files may require additional processing time.
- Permission monitoring depends on operating system capabilities and permissions.
- A trusted baseline is required for reliable integrity comparisons.

### 9. Expected Outcome

The FIM component will extend the project beyond security log analysis by detecting changes to selected files and folders.

It will provide evidence-based alerts and support centralized monitoring of authorized computers.