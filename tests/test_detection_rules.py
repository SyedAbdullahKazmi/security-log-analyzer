
import unittest
from pathlib import Path
from datetime import datetime, timedelta

from src.detection.rules import (
    detect_repeated_failed_logins,
    detect_unusual_activity_volume
)

from src.parser.csv_parser import load_csv


class TestDetectionRules(unittest.TestCase):

    def make_event(
        self, event_id, timestamp, username="test_user",
        source_ip="192.0.2.10", computer="PC-01"
    ):
        return {
            "event_id": str(event_id),
            "timestamp": timestamp.isoformat(),
            "username": username,
            "source_ip": source_ip,
            "computer": computer,
            "event_type": "Logon",
            "status": "Failure" if str(event_id) == "4625" else "Success"
        }

    def test_r1_positive(self):
        start = datetime(2026, 1, 1, 10, 0, 0)

        events = [
            self.make_event(
                4625, start + timedelta(minutes=i)
            )
            for i in range(5)
        ]

        alerts = detect_repeated_failed_logins(events)

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["rule_id"], "R1")

    def test_r1_negative_below_threshold(self):
        start = datetime(2026, 1, 1, 10, 0, 0)

        events = [
            self.make_event(
                4625, start + timedelta(minutes=i)
            )
            for i in range(4)
        ]

        alerts = detect_repeated_failed_logins(events)

        self.assertEqual(len(alerts), 0)

    def test_r1_negative_outside_time_window(self):
        start = datetime(2026, 1, 1, 10, 0, 0)

        events = [
            self.make_event(
                4625, start + timedelta(minutes=2 * i)
            )
            for i in range(5)
        ]

        alerts = detect_repeated_failed_logins(events)

        self.assertEqual(len(alerts), 0)

    def test_r4_positive(self):
        start = datetime(2026, 1, 1, 11, 0, 0)

        events = [
            self.make_event(
                4624, start + timedelta(seconds=8 * i)
            )
            for i in range(6)
        ]

        alerts = detect_unusual_activity_volume(events)

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["rule_id"], "R4")

    def test_r4_negative_below_threshold(self):
        start = datetime(2026, 1, 1, 11, 0, 0)

        events = [
            self.make_event(
                4624, start + timedelta(seconds=8 * i)
            )
            for i in range(5)
        ]

        alerts = detect_unusual_activity_volume(events)

        self.assertEqual(len(alerts), 0)

    def test_r4_negative_outside_time_window(self):
        start = datetime(2026, 1, 1, 11, 0, 0)

        events = [
            self.make_event(
                4624, start + timedelta(seconds=20 * i)
            )
            for i in range(6)
        ]

        alerts = detect_unusual_activity_volume(events)

        self.assertEqual(len(alerts), 0)

    def test_original_dataset_detection(self):
        project_root = Path(__file__).resolve().parents[1]
        csv_file = project_root / "data" / "test" / "dataset_v1.csv"

        events, rejected = load_csv(csv_file)

        self.assertEqual(len(rejected), 0)

        r1_alerts = detect_repeated_failed_logins(events)
        r4_alerts = detect_unusual_activity_volume(events)

        self.assertTrue(
            any(alert["rule_id"] == "R1" for alert in r1_alerts)
        )
        self.assertTrue(
            any(alert["rule_id"] == "R4" for alert in r4_alerts)
        )


if __name__ == "__main__":
    unittest.main()
