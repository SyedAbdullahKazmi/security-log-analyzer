
import csv
from pathlib import Path


def load_test_metadata(file_path):
    metadata = []

    with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        required_columns = [
            "case_id",
            "label",
            "expected_rule",
            "expected_result"
        ]

        if not reader.fieldnames:
            raise ValueError("CSV file has no header.")

        missing_columns = [
            column for column in required_columns
            if column not in reader.fieldnames
        ]

        if missing_columns:
            raise ValueError(
                f"Missing testing metadata columns: {missing_columns}"
            )

        for row in reader:
            if not row or all(
                not value or not value.strip()
                for value in row.values()
                if value is not None
            ):
                continue

            metadata.append({
                "case_id": row["case_id"].strip(),
                "label": row["label"].strip(),
                "expected_rule": row["expected_rule"].strip(),
                "expected_result": row["expected_result"].strip()
            })

    return metadata


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]
    dataset = project_root / "data" / "test" / "dataset_v1.csv"

    records = load_test_metadata(dataset)

    print("Testing metadata records:", len(records))
    print("First metadata record:", records[0])
