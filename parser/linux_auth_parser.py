import re


def parse_linux_auth_line(line: str):
    failed_pattern = r"([A-Z][a-z]{2}\s+\d+\s+\d{2}:\d{2}:\d{2}).*Failed password for (\w+) from ([\d\.]+)"
    success_pattern = r"([A-Z][a-z]{2}\s+\d+\s+\d{2}:\d{2}:\d{2}).*Accepted password for (\w+) from ([\d\.]+)"

    failed_match = re.match(failed_pattern, line.strip())
    if failed_match:
        timestamp, user, ip = failed_match.groups()
        return {
            "timestamp": timestamp,
            "status": "Failed",
            "user": user,
            "ip": ip,
            "source_type": "linux_auth"
        }

    success_match = re.match(success_pattern, line.strip())
    if success_match:
        timestamp, user, ip = success_match.groups()
        return {
            "timestamp": timestamp,
            "status": "Successful",
            "user": user,
            "ip": ip,
            "source_type": "linux_auth"
        }

    return None