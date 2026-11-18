# Chapter 1: Introduction

## 1.1 Background

Cybersecurity monitoring is an important part of protecting computer systems and information. Computers generate security logs that record activities such as successful logins, failed login attempts, account changes, and other security-related events.

These logs can help security analysts identify unusual activities and investigate potential security incidents. However, manually reviewing large numbers of log records can be time-consuming and difficult.

A Security Log Analyzer can help by reading log files, extracting important information, identifying suspicious patterns, and generating alerts for further investigation.

This project focuses on developing a Python-based Security Log Analyzer and Automated Alert System. It will analyze authorized Windows Security Logs and synthetic test datasets. The planned extended architecture will also support authorized monitoring of multiple computers through configured log collection agents and a central analysis system.

## 1.2 Problem Statement

Security logs contain useful information about computer activities, but manually analyzing them can be difficult, especially when the number of records increases.

Important activities, such as repeated failed login attempts or unexpected changes to privileged accounts, may be overlooked during manual inspection.

There is a need for a system that can process security log records, normalize their information, apply defined detection rules, and generate alerts containing evidence about suspicious activities.

The project aims to address this problem through an automated log analysis and alert generation system.

## 1.3 Project Aim

The main aim of this project is to develop a Python-based Security Log Analyzer and Automated Alert System that processes authorized security logs, detects suspicious activities using transparent detection rules, and generates evidence-based alerts.

An extended objective is to support authorized deployment across multiple computers, allowing their security events to be collected and analyzed centrally.

## 1.4 Project Objectives

The objectives are:

1. Read authorized Windows Security Logs and supported CSV or JSON log files.
2. Validate log records and handle malformed or incomplete data.
3. Normalize important fields, including timestamps, usernames, event types, computer names, and source IP addresses.
4. Implement at least four documented security detection rules.
5. Generate alerts containing severity, rule information, affected entities, and supporting evidence.
6. Store alerts and analysis results in persistent formats such as CSV, JSON, or SQLite.
7. Evaluate the system using normal and suspicious test scenarios.
8. Design an authorized multi-computer monitoring extension using log collection agents and a central analyzer.

## 1.5 Project Scope

The project initially focuses on analyzing authorized and exported Windows Security Logs and synthetic datasets.

The planned extended capability includes:

- Configuring monitoring agents on computers with owner or administrator authorization.
- Collecting permitted security events from registered computers.
- Transmitting events securely to a central analysis system.
- Identifying the source computer associated with each event.
- Generating centralized alerts and reports.

The system will focus on detection, analysis, and reporting. Automated account disabling, unauthorized monitoring, and automatic blocking of users or computers are not project objectives.

The multi-computer extension will be implemented within the resources and approval provided for the project.

## 1.6 Ethical and Legal Considerations

The system will only process logs from computers for which monitoring and data collection are authorized.

Access to security logs will be limited to permitted accounts. Sensitive information will be protected, and test datasets will use synthetic or appropriately anonymized data.

The project will not be used for covert monitoring, unauthorized access, or collecting personal information without permission.

## 1.7 Expected Outcome

The expected outcome is a working security log analysis system capable of processing supported log files, detecting defined suspicious patterns, generating evidence-based alerts, and storing results.

The extended architecture is intended to support authorized monitoring of multiple computers through a centralized analysis system.