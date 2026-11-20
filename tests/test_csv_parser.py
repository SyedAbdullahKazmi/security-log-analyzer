
import csv
import unittest
import tempfile
from pathlib import Path

from src.parser.csv_parser import load_csv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = PROJECT_ROOT / "data" / "test" / "dataset_v1.csv"


class TestCSVParser(unittest.TestCase):

    def test_original_dataset(self):
        accepted, rejected = load_csv(DATASET_PATH)

        self.assertEqual(len(accepted), 17)
        self.assertEqual(len(rejected), 0)


    def test_normalized_event_fields(self):
        accepted, rejected = load_csv(DATASET_PATH)

        self.assertEqual(len(rejected), 0)

        event = accepted[0]

        expected_fields = {
            "event_id",
            "timestamp",
            "computer",
            "username",
            "source_ip",
            "event_type",
            "status",
            "logon_type",
            "message",
            "source"
        }

        self.assertEqual(set(event.keys()), expected_fields)
        self.assertEqual(event["event_id"], "4624")
        self.assertEqual(event["computer"], "LAB-PC")
        self.assertEqual(event["status"], "Success")
        self.assertEqual(event["source"], "CSV")


    def create_test_csv(self, row):
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)

        file_path = Path(temp_dir.name) / "test.csv"

        columns = [
            "event_id",
            "timestamp",
            "computer",
            "event_type"
        ]

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerow(row)

        return file_path

    def test_invalid_timestamp(self):
        file_path = self.create_test_csv({
            "event_id": "4625",
            "timestamp": "not-a-date",
            "computer": "LAB-PC",
            "event_type": "Failed Login"
        })

        accepted, rejected = load_csv(file_path)

        self.assertEqual(len(accepted), 0)
        self.assertEqual(len(rejected), 1)

    def test_missing_computer(self):
        file_path = self.create_test_csv({
            "event_id": "4625",
            "timestamp": "2026-11-18T10:00:00",
            "computer": "",
            "event_type": "Failed Login"
        })

        accepted, rejected = load_csv(file_path)

        self.assertEqual(len(accepted), 0)
        self.assertEqual(len(rejected), 1)

    def test_extra_value_in_row(self):
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)

        file_path = Path(temp_dir.name) / "test.csv"

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            file.write(
                "event_id,timestamp,computer,event_type\n"
                "4625,2026-11-18T10:00:00,LAB-PC,Failed Login,EXTRA\n"
            )

        accepted, rejected = load_csv(file_path)

        self.assertEqual(len(accepted), 0)
        self.assertEqual(len(rejected), 1)

    def test_missing_required_column(self):
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)

        file_path = Path(temp_dir.name) / "test.csv"

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            file.write(
                "event_id,timestamp,computer\n"
                "4625,2026-11-18T10:00:00,LAB-PC\n"
            )

        with self.assertRaises(ValueError):
            load_csv(file_path)

    def test_blank_row_is_skipped(self):
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)

        file_path = Path(temp_dir.name) / "test.csv"

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            file.write(
                "event_id,timestamp,computer,event_type\n"
                "4625,2026-11-18T10:00:00,LAB-PC,Failed Login\n"
                "\n"
                "4624,2026-11-18T10:05:00,LAB-PC,Successful Login\n"
            )

        accepted, rejected = load_csv(file_path)

        self.assertEqual(len(accepted), 2)
        self.assertEqual(len(rejected), 0)

if __name__ == "__main__":
    unittest.main()
