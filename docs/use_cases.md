# Use Cases
## Security Log Analyzer and Automated Alert System

### UC-01: Import Security Log File

**Actor:** Security Analyst

**Description:** The analyst selects an authorized CSV or JSON security log file for analysis.

**Expected Result:** The system reads the file and sends valid records to the parser.

### UC-02: Validate and Normalize Events

**Actor:** System

**Description:** The system validates incoming records and converts supported events into the normalized event format.

**Expected Result:** Valid records are normalized, while malformed records are counted and reported.

### UC-03: Detect Suspicious Activities

**Actor:** Detection Engine

**Description:** The system applies the configured detection rules R1, R2, R3, and R4.

**Expected Result:** Matching activities generate alerts with supporting evidence.

### UC-04: Review Security Alerts

**Actor:** Security Analyst

**Description:** The analyst reviews generated alerts and their associated event evidence.

**Expected Result:** The analyst can understand why an alert was generated.

### UC-05: Register an Authorized Computer

**Actor:** System Administrator

**Description:** An administrator authorizes and registers a computer for monitoring and configures its approved log collection agent.

**Expected Result:** The computer is recognized as an authorized monitoring source.

### UC-06: Collect Events from Registered Computers

**Actor:** Authorized Collection Agent

**Description:** The configured agent collects permitted security events and securely transmits them to the central system.

**Expected Result:** The central system receives events associated with the correct registered computer.

### UC-07: Centralized Monitoring

**Actor:** Security Analyst

**Description:** The analyst reviews security events and alerts received from multiple registered computers.

**Expected Result:** The system provides centralized visibility of authorized computers.

### UC-08: Generate Reports

**Actor:** Security Analyst

**Description:** The analyst generates summaries of processed events, detection alerts, and severity counts.

**Expected Result:** The system produces reports for review and evaluation.