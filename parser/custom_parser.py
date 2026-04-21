import re


def parse_custom_line(line: str):
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*(Failed|Successful).*user=(\w+).*ip=([\d\.]+)"
    match = re.match(pattern, line.strip())

    if not match:
        return None

    timestamp, status, user, ip = match.groups()

    return {
        "timestamp": timestamp,
        "status": status,
        "user": user,
        "ip": ip,
        "source_type": "custom"
    }