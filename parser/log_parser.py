import pandas as pd
import re

def parse_logs(file_input):
    data = []

    # Handle uploaded file OR file path
    if hasattr(file_input, "read"):
        lines = file_input.read().decode("utf-8").splitlines()
    else:
        with open(file_input, "r") as file:
            lines = file.readlines()

    for line in lines:
        pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (Failed|Successful) login user=(\w+) ip=([\d\.]+)"
        match = re.match(pattern, line)

        if match:
            timestamp, status, user, ip = match.groups()

            data.append({
                "timestamp": timestamp,
                "status": status,
                "user": user,
                "ip": ip
            })

    df = pd.DataFrame(data)
    return df