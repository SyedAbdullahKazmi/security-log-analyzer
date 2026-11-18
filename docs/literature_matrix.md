
# Literature Review Matrix

## Project Title
Security Log Analyzer and Automated Alert System

## 1. Introduction

This literature review covers existing documentation, security guidelines, and technical resources related to Windows Security Logs, log monitoring, suspicious login detection, and automated security alerts.

The purpose is to understand how existing security technologies collect and analyze logs and how these concepts can be applied to our project.

## 2. Literature Review Matrix

| No. | Source | Main Concept | Application in Our Project |
|---|---|---|---|
| 1 | Microsoft - Audit Logon Events | Windows records successful and failed login attempts. | Understanding login activities. |
| 2 | Microsoft - Event ID 4624 | Records successful account logins. | Identifying successful login events. |
| 3 | Microsoft - Event ID 4625 | Records failed account login attempts. | Detecting repeated failed logins. |
| 4 | Microsoft - Advanced Audit Policy | Explains different Windows security auditing categories. | Identifying useful security events. |
5	Australian Signals Directorate (ASD) / Australian Cyber Security Centre (ACSC) – Priority logs for SIEM ingestion: Practitioner guidance (27 May 2025)	Explains which logs should be prioritized for security monitoring and SIEM ingestion.	Helps us select important Windows Security Events for analysis.
| 6 | NIST SP 800-92 | Provides guidance about computer security log management. | Understanding log collection, storage and management. |

## 3. Existing System Analysis

Existing security monitoring solutions use logs to identify suspicious activities and investigate security incidents.

Examples include:

- SIEM (Security Information and Event Management) systems.
- Windows Event Viewer.
- Centralized log management systems.
- Automated security monitoring solutions.

These systems help security professionals monitor activities and investigate possible threats.

## 4. Identified Project Scope

Based on the reviewed documentation, our project will focus on:

1. Collecting Windows Security Logs.
2. Identifying successful and failed login events.
3. Extracting useful information from log records.
4. Detecting suspicious login patterns.
5. Generating automated security alerts.
6. Presenting analyzed security information.

## 5. Proposed Approach

Our proposed system will use Python to read and analyze Windows Security Logs.

The system will identify selected security events, apply detection rules, and generate alerts when suspicious activity is detected.

## 6. References

1. Microsoft - Audit Logon Events
   https://learn.microsoft.com/windows/security/threat-protection/auditing/basic-audit-logon-events

2. Microsoft - Event ID 4624
   https://learn.microsoft.com/windows/security/threat-protection/auditing/event-4624

3. Microsoft - Event ID 4625
   https://learn.microsoft.com/windows/security/threat-protection/auditing/event-4625

4. Microsoft - Advanced Audit Policy Configuration
   https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

5. Australian Signals Directorate (ASD) / Australian Cyber Security Centre (ACSC) - Priority Logs for SIEM Ingestion
   https://www.cyber.gov.au/publication/priority-logs-for-siem-ingestion-practitioner-guidance

6. NIST - SP 800-92: Guide to Computer Security Log Management
   https://csrc.nist.gov/pubs/sp/800/92/final
