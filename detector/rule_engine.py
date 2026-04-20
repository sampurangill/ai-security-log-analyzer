# Brute Force Detection
def detect_brute_force(df, threshold=2):
    results = []

    # Filter failed logins
    failed_logins = df[df["status"] == "Failed"]

    # Count attempts per IP
    counts = failed_logins["ip"].value_counts()

    # Detect suspicious IPs
    for ip, count in counts.items():
        if count > threshold:
            results.append({
                "ip": ip,
                "attempts": count,
                "type": "Brute Force",
                "severity": "High"
            })

    return results

# Traffic Analysis
def detect_ip_spike(df, threshold=5):
    results = []

    counts = df["ip"].value_counts()

    for ip, count in counts.items():
        if count > threshold:
            results.append({
                "ip": ip,
                "activity_count": count,
                "type": "Traffic Spike",
                "severity": "Medium"
            })

    return results