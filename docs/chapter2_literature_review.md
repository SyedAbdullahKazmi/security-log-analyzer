# Chapter 2: Literature Review

## 2.1 Introduction

Security log analysis is an important activity in cybersecurity because system logs provide information about events occurring within computer systems. Security analysts use these records to investigate login activities, account changes, access failures, and other potentially suspicious behavior.

This chapter reviews relevant concepts and documentation related to Windows Security Logs, event identification, security auditing, log analysis, and centralized security monitoring.

## 2.2 Security Logs and Event Analysis

Security logs contain records of activities performed on or against a computer system. These records can help administrators and security analysts understand what happened, when it happened, and which account or computer was involved.

Windows Security Logs provide information about authentication events and other security-related activities.

For this project, Windows Event IDs 4624 and 4625 are particularly relevant:

- Event ID 4624: Records a successful logon.
- Event ID 4625: Records a failed logon.

These events can be useful when investigating repeated failed logins or successful logins that occur after multiple failures. However, a single failed login does not automatically indicate an attack. Events must be analyzed in context.

[References: 2, 3]

## 2.3 Windows Security Auditing

Windows auditing provides administrators with information about selected system and security activities.

Audit Logon Events and Advanced Audit Policy settings help determine which activities are recorded in the Windows Security Log.

The availability and detail of event records depend on the system's audit configuration. Therefore, the analyzer must handle missing fields and variations in available log information.

[References: 1, 4]

## 2.4 Log Analysis and SIEM Concepts

Security Information and Event Management (SIEM) systems collect and analyze security-related information from different sources.

A typical SIEM workflow includes:

1. Collecting security events.
2. Parsing and normalizing records.
3. Correlating related activities.
4. Detecting suspicious patterns.
5. Generating alerts for investigation.
6. Producing reports for security monitoring.

The proposed project uses a simplified version of this workflow. It will apply documented detection rules to authorized log data and generate alerts with supporting evidence.

The project is not intended to replace a commercial enterprise SIEM platform.

[References: 5, 6]

## 2.5 Detection Rules

Detection rules are conditions used to identify activities that may require security investigation.

The project plans to implement the following rules:

- R1: Repeated failed login attempts.
- R2: Successful login after multiple failed login attempts.
- R3: Changes to privileged account or group membership.
- R4: Unusual activity volume within a defined time window.

Each rule will have documented conditions and thresholds. The analyzer will attach relevant event records to alerts so that an analyst can understand why an alert was generated.

## 2.6 Centralized Monitoring and Multi-Computer Architecture

Monitoring multiple authorized computers can provide a broader view of security activities.

In a centralized architecture, configured agents collect permitted security events from registered computers and forward them to a central system for analysis.

The central system can associate each event with its originating computer, apply detection rules, and generate consolidated alerts.

This project plans to explore this architecture as an approved extension. The implementation will consider authorization, secure communication, device identification, and protection of collected information.

## 2.7 Research Gap and Project Motivation

Windows provides security event logging, while SIEM platforms offer broader event collection and analysis capabilities. However, learning how to process logs, create transparent detection rules, and understand evidence behind alerts is valuable for cybersecurity students.

This project aims to develop a smaller, understandable Python-based solution that demonstrates the core stages of log analysis and alert generation.

Its extended design will also explore how authorized computers can contribute security events to a central analyzer.

## 2.8 Chapter Summary

This chapter reviewed Windows Security Logs, relevant Event IDs, security auditing, SIEM concepts, detection rules, and centralized monitoring.

These concepts provide the foundation for the system requirements, architecture, and implementation discussed in the following chapters.