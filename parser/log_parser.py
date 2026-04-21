import pandas as pd

from parser.custom_parser import parse_custom_line
from parser.linux_auth_parser import parse_linux_auth_line
from parser.apache_parser import parse_apache_line


def read_lines(file_input):
    """
    Reads lines from either:
    - an uploaded Streamlit file object
    - a local file path
    """
    if hasattr(file_input, "read"):
        content = file_input.read()

        if isinstance(content, bytes):
            content = content.decode("utf-8")

        return content.splitlines()
    else:
        with open(file_input, "r") as file:
            return file.readlines()


def detect_log_type(lines):
    """
    Attempts to detect log type from the first few lines.
    """
    for line in lines[:10]:
        stripped = line.strip()

        if "Failed login user=" in stripped or "Successful login user=" in stripped:
            return "custom"

        if "sshd" in stripped and ("Failed password" in stripped or "Accepted password" in stripped):
            return "linux_auth"

        if '"' in stripped and "[" in stripped and "]" in stripped:
            return "apache"

    return "custom"


def parse_logs(file_input, log_type="auto"):
    """
    Parses logs into a pandas DataFrame.
    Supported log_type values:
    - auto
    - custom
    - linux_auth
    - apache
    """
    lines = read_lines(file_input)

    if log_type == "auto":
        log_type = detect_log_type(lines)

    data = []

    for line in lines:
        parsed = None

        if log_type == "custom":
            parsed = parse_custom_line(line)
        elif log_type == "linux_auth":
            parsed = parse_linux_auth_line(line)
        elif log_type == "apache":
            parsed = parse_apache_line(line)

        if parsed:
            data.append(parsed)

    return pd.DataFrame(data)