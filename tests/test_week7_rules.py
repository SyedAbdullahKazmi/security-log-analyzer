import unittest

from src.detection.rules import (
    detect_success_after_failures,
    detect_privileged_account_change
)


class TestWeek7Rules(unittest.TestCase):

    def setUp(self):
        self.base_events = [
            {
                "event_id": "4625",
                "timestamp": "2026-11-20T10:00:00",
                "username": "test_user",
                "source_ip": "192.0.2.10",
                "computer": "LAB-PC",
                "message": "Failed login"
            },
            {
                "event_id": "4625",
                "timestamp": "2026-11-20T10:03:00",
                "username": "test_user",
                "source_ip": "192.0.2.10",
                "computer": "LAB-PC",
                "message": "Failed login"
            },
            {
                "event_id": "4624",
                "timestamp": "2026-11-20T10:05:00",
                "username": "test_user",
                "source_ip": "192.0.2.10",
                "computer": "LAB-PC",
                "message": "Successful login"
            }
        ]

    def test_r2_positive(self):
        findings = detect_success_after_failures(self.base_events)

        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["rule_id"], "R2")
        self.assertEqual(findings[0]["severity"], "High")

    def test_r2_negative_only_one_failure(self):
        events = [self.base_events[0], self.base_events[2]]

        findings = detect_success_after_failures(events)

        self.assertEqual(len(findings), 0)

    def test_r3_positive_administrator_group(self):
        events = [{
            "event_id": "4732",
            "timestamp": "2026-11-20T11:00:00",
            "username": "demo_admin",
            "computer": "LAB-PC",
            "message": "Added test_user to local Administrators group"
        }]

        findings = detect_privileged_account_change(events)

        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["rule_id"], "R3")
        self.assertEqual(findings[0]["severity"], "High")

    def test_r3_negative_other_group(self):
        events = [{
            "event_id": "4732",
            "timestamp": "2026-11-20T11:00:00",
            "username": "demo_admin",
            "computer": "LAB-PC",
            "message": "Added test_user to local Guests group"
        }]

        findings = detect_privileged_account_change(events)

        self.assertEqual(len(findings), 0)


if __name__ == "__main__":
    unittest.main()