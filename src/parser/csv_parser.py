
import csv
import json
from datetime import datetime
from pathlib import Path


REQUIRED_COLUMNS = [
    "event_id",
    "timestamp",
    "computer",
    "event_type"
]


def parse_timestamp(value):
    """Convert timestamp text into a Python datetime object."""
    value = value.strip().replace("Z", "+00:00")
    return datetime.fromisoformat(value)


def load_csv(file_path):
    accepted_records = []
    rejected_records = []

    # Open CSV file
    with open(file_path, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        # Check whether required CSV columns exist
        if not reader.fieldnames:
            raise ValueError("CSV file is empty or has no header.")

        missing_columns = [
            column for column in REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        # Read CSV rows while the file is still open
        for row_number, row in enumerate(reader, start=2):

            # Skip completely blank rows
            if not row or all(
                not value or not value.strip()
                for value in row.values()
                if value is not None
            ):
                continue

            try:
                # Detect extra values in a CSV row
                if None in row:
                    raise ValueError("Extra values found in row.")

                # Check required fields
                for column in REQUIRED_COLUMNS:
                    if not row.get(column) or not row[column].strip():
                        raise ValueError(
                            f"Missing required field: {column}"
                        )

                # Validate timestamp
                timestamp = parse_timestamp(row["timestamp"])

                # Create normalized event
                event = {
                    "event_id": row["event_id"].strip(),
                    "timestamp": timestamp.isoformat(),
                    "computer": row["computer"].strip(),
                    "username": row.get("username", "").strip(),
                    "source_ip": row.get("source_ip", "").strip(),
                    "event_type": row["event_type"].strip(),
                    "status": row.get("status", "").strip(),
                    "logon_type": row.get("logon_type", "").strip(),
                    "message": row.get("message", "").strip(),
                    "source": "CSV"
                }

                accepted_records.append(event)

            except (ValueError, TypeError) as error:
                rejected_records.append({
                    "row": row_number,
                    "reason": str(error)
                })

    return accepted_records, rejected_records


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]
    csv_file = project_root / "data" / "test" / "dataset_v1.csv"

    accepted, rejected = load_csv(csv_file)

    print("\n===== CSV PARSER SUMMARY =====")
    print("Accepted records:", len(accepted))
    print("First accepted record:", accepted[0])
    print("Rejected records:", len(rejected))
    report_file = project_root / "data" / "processed" / "rejected_records.json"

    with open(report_file, "w", encoding="utf-8") as file:
        json.dump(rejected, file, indent=4)

    print("Rejected records report saved:", report_file)
    for error in rejected:
        print(f"Row {error['row']}: {error['reason']}")
