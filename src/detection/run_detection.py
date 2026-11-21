from pathlib import Path

from src.parser.csv_parser import load_csv
from src.detection.rules import (
    detect_repeated_failed_logins,
    detect_success_after_failures,
    detect_privileged_account_change,
    detect_unusual_activity_volume
)
from src.detection.alert_manager import generate_alerts


def main():
    project_root = Path(__file__).resolve().parents[2]
    csv_file = project_root / "data" / "test" / "dataset_v1.csv"

    events, rejected = load_csv(csv_file)

    print("\n===== SECURITY LOG ANALYZER =====")
    print("Total accepted events:", len(events))
    print("Rejected events:", len(rejected))

    r1_findings = detect_repeated_failed_logins(events)
    r2_findings = detect_success_after_failures(events)
    r3_findings = detect_privileged_account_change(events)
    r4_findings = detect_unusual_activity_volume(events)

    all_findings = (
        r1_findings
        + r2_findings
        + r3_findings
        + r4_findings
    )
    alerts = generate_alerts(all_findings)

    print("\n===== GENERATED SECURITY ALERTS =====")

    for alert in alerts:
        print("\n--------------------------------")
        print("Alert ID:", alert["alert_id"])
        print("Timestamp:", alert["timestamp"])
        print("Category:", alert["event_category"])
        print("Rule ID:", alert["rule_id"])
        print("Rule:", alert["rule_name"])
        print("Severity:", alert["severity"])
        print("Affected Entity:", alert["affected_entity"])
        print("Reason:", alert["reason"])

        if "source_ip" in alert:
            print("Source IP:", alert["source_ip"])

        if "computer" in alert:
            print("Computer:", alert["computer"])

        print("Supporting Evidence:")

        for evidence in alert["supporting_evidence"]:
            print("  Event ID:", evidence.get("event_id"))
            print("  Timestamp:", evidence.get("timestamp"))
            print("  Username:", evidence.get("username"))
            print("  Message:", evidence.get("message"))

    print("\n===== DETECTION SUMMARY =====")
    print("R1 findings:", len(r1_findings))
    print("R2 findings:", len(r2_findings))
    print("R3 findings:", len(r3_findings))
    print("R4 findings:", len(r4_findings))
    print("Total findings:", len(all_findings))
    print("Generated alerts:", len(alerts))


if __name__ == "__main__":
    main()