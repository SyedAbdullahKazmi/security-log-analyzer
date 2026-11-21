
from datetime import datetime, timedelta


# Week 4 design thresholds
R1_THRESHOLD = 5
R1_WINDOW_MINUTES = 5

R4_THRESHOLD = 6
R4_WINDOW_SECONDS = 60

R2_THRESHOLD = 2
R2_WINDOW_MINUTES = 10


def parse_event_time(value):
    """Convert an event timestamp into a datetime object."""
    value = value.replace("Z", "+00:00")
    return datetime.fromisoformat(value)


def find_matching_window(events, threshold, window):
    """
    Find the first time window containing at least
    the required number of events.
    """
    sorted_events = sorted(
        events,
        key=lambda event: parse_event_time(event["timestamp"])
    )

    for start in range(len(sorted_events)):
        start_time = parse_event_time(
            sorted_events[start]["timestamp"]
        )

        matching_events = []

        for event in sorted_events[start:]:
            event_time = parse_event_time(event["timestamp"])

            if event_time - start_time <= window:
                matching_events.append(event)
            else:
                break

        if len(matching_events) >= threshold:
            return matching_events

    return []


def detect_repeated_failed_logins(events):
    """R1: Detect repeated failed logins for one account and IP."""
    groups = {}

    for event in events:
        if str(event.get("event_id")) != "4625":
            continue

        username = event.get("username", "").strip()
        source_ip = event.get("source_ip", "").strip()

        if not username or not source_ip:
            continue

        key = (username, source_ip)
        groups.setdefault(key, []).append(event)

    findings = []

    for (username, source_ip), group_events in groups.items():
        matches = find_matching_window(
            group_events,
            R1_THRESHOLD,
            timedelta(minutes=R1_WINDOW_MINUTES)
        )

        if matches:
            findings.append({
                "rule_id": "R1",
                "rule_name": "Repeated Failed Logins",
                "severity": "Medium",
                "affected_entity": username,
                "source_ip": source_ip,
                "event_count": len(matches),
                "threshold": R1_THRESHOLD,
                "time_window": "5 minutes",
                "evidence": matches
            })

    return findings


def detect_unusual_activity_volume(events):
    """R4: Detect unusually high successful login volume."""
    groups = {}

    for event in events:
        if str(event.get("event_id")) != "4624":
            continue

        username = event.get("username", "").strip()
        computer = event.get("computer", "").strip()

        if not username or not computer:
            continue

        key = (username, computer)
        groups.setdefault(key, []).append(event)

    findings = []

    for (username, computer), group_events in groups.items():
        matches = find_matching_window(
            group_events,
            R4_THRESHOLD,
            timedelta(seconds=R4_WINDOW_SECONDS)
        )

        if matches:
            findings.append({
                "rule_id": "R4",
                "rule_name": "Unusual Activity Volume",
                "severity": "Medium",
                "affected_entity": username,
                "computer": computer,
                "event_count": len(matches),
                "threshold": R4_THRESHOLD,
                "time_window": "1 minute",
                "evidence": matches
            })

    return findings

def detect_success_after_failures(events):
    """
    R2: Detect a successful login after at least
    two failed logins for the same user and source IP
    within 10 minutes.
    """
    groups = {}

    for event in events:
        event_id = str(event.get("event_id"))

        if event_id not in ("4624", "4625"):
            continue

        username = event.get("username", "").strip()
        source_ip = event.get("source_ip", "").strip()

        if not username or not source_ip:
            continue

        key = (username, source_ip)
        groups.setdefault(key, []).append(event)

    findings = []

    for (username, source_ip), group_events in groups.items():

        sorted_events = sorted(
            group_events,
            key=lambda event: parse_event_time(event["timestamp"])
        )

        for success_event in sorted_events:

            if str(success_event.get("event_id")) != "4624":
                continue

            success_time = parse_event_time(
                success_event["timestamp"]
            )

            previous_failures = [
                event for event in sorted_events
                if str(event.get("event_id")) == "4625"
                and timedelta(0) < (
                    success_time - parse_event_time(event["timestamp"])
                ) <= timedelta(minutes=R2_WINDOW_MINUTES)
            ]

            if len(previous_failures) >= R2_THRESHOLD:

                findings.append({
                    "rule_id": "R2",
                    "rule_name": "Successful Login After Failures",
                    "severity": "High",
                    "affected_entity": username,
                    "source_ip": source_ip,
                    "event_count": len(previous_failures) + 1,
                    "threshold": R2_THRESHOLD,
                    "time_window": "10 minutes",
                    "evidence": previous_failures + [success_event]
                })

                break

    return findings

def detect_privileged_account_change(events):
    """
    R3: Detect a user being added to the local
    Administrators group.
    """
    findings = []

    for event in events:

        if str(event.get("event_id")) != "4732":
            continue

        # Prefer an explicit normalized target_group field.
        target_group = event.get("target_group", "").strip()

        # Our current synthetic dataset stores this detail
        # in the message field.
        message = event.get("message", "").strip()

        is_admin_group = (
            "administrators" in target_group.lower()
            or "administrators" in message.lower()
        )

        if not is_admin_group:
            continue

        findings.append({
            "rule_id": "R3",
            "rule_name": "Privileged Account Change",
            "severity": "High",
            "affected_entity": event.get("username", "Unknown"),
            "computer": event.get("computer", "Unknown"),
            "event_count": 1,
            "threshold": "Event ID 4732 + Administrators group",
            "time_window": "Single event",
            "evidence": [event]
        })

    return findings
