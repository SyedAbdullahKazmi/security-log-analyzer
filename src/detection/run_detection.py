
from pathlib import Path

from src.parser.csv_parser import load_csv
from src.detection.rules import (
    detect_repeated_failed_logins,
    detect_unusual_activity_volume
)


def main():
    project_root = Path(__file__).resolve().parents[2]
    csv_file = project_root / "data" / "test" / "dataset_v1.csv"

    events, rejected = load_csv(csv_file)

    print("\n===== SECURITY LOG ANALYZER =====")
    print("Total accepted events:", len(events))
    print("Rejected events:", len(rejected))

    r1_findings = detect_repeated_failed_logins(events)
    r4_findings = detect_unusual_activity_volume(events)

    print("\n===== R1: REPEATED FAILED LOGINS =====")

    for finding in r1_findings:
        print("Rule:", finding["rule_name"])
        print("Username:", finding["affected_entity"])
        print("Source IP:", finding["source_ip"])
        print("Event count:", finding["event_count"])
        print("Severity:", finding["severity"])

    print("\n===== R4: UNUSUAL ACTIVITY VOLUME =====")

    for finding in r4_findings:
        print("Rule:", finding["rule_name"])
        print("Username:", finding["affected_entity"])
        print("Computer:", finding["computer"])
        print("Event count:", finding["event_count"])
        print("Severity:", finding["severity"])

    print("\n===== DETECTION SUMMARY =====")
    print("R1 findings:", len(r1_findings))
    print("R4 findings:", len(r4_findings))
    print("Total findings:", len(r1_findings) + len(r4_findings))


if __name__ == "__main__":
    main()
