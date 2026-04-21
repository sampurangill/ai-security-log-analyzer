import re


def parse_apache_line(line: str):
    pattern = r'([\d\.]+)\s+-\s+-\s+\[([^\]]+)\]\s+"([A-Z]+)\s+([^"]+)\s+HTTP/[0-9.]+"\s+(\d{3})'
    match = re.match(pattern, line.strip())

    if not match:
        return None

    ip, timestamp, method, path, status_code = match.groups()

    if status_code == "401":
        status = "Failed"
    elif status_code in ["200", "302"]:
        status = "Successful"
    else:
        status = "Unknown"

    return {
        "timestamp": timestamp,
        "status": status,
        "user": "web_user",
        "ip": ip,
        "source_type": "apache",
        "method": method,
        "path": path,
        "http_status": status_code
    }