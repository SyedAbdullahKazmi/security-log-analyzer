def generate_alerts(findings):
    """
    Convert detection findings into standardized security alerts.
    Alert IDs are unique within the current execution.
    """

    alerts = []

    for number, finding in enumerate(findings, start=1):

        evidence = finding.get("evidence", [])

        # Use the latest supporting event timestamp
        if evidence:
            alert_timestamp = max(
                evidence,
                key=lambda event: event["timestamp"]
            )["timestamp"]
        else:
            alert_timestamp = None

        alert = {
            "alert_id": f"ALT-{number:06d}",
            "timestamp": alert_timestamp,
            "event_category": "SecurityLog",
            "rule_id": finding["rule_id"],
            "rule_name": finding["rule_name"],
            "severity": finding["severity"],
            "affected_entity": finding["affected_entity"],
            "reason": finding["rule_name"],
            "supporting_evidence": evidence
        }

        if "source_ip" in finding:
            alert["source_ip"] = finding["source_ip"]

        if "computer" in finding:
            alert["computer"] = finding["computer"]

        alerts.append(alert)

    return alerts