
from datetime import datetime, timedelta


# Week 4 design thresholds
R1_THRESHOLD = 5
R1_WINDOW_MINUTES = 5

R4_THRESHOLD = 6
R4_WINDOW_SECONDS = 60


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
