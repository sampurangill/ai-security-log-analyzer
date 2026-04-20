def analyze_threat(threat):
    threat_type = threat.get("type", "Unknown")
    ip = threat.get("ip", "Unknown")
    severity = threat.get("severity", "Unknown")
    attempts = threat.get("attempts", threat.get("activity_count", "Unknown"))

    if threat_type == "Brute Force":
        return f"""
        This activity suggests a brute force attack from IP {ip}.
        The system detected {attempts} failed login attempts, indicating possible credential guessing.

        Risk:
        Unauthorized access could be gained if successful.

        Recommended Actions:
        - Block or rate-limit the IP
        - Enable multi-factor authentication
        - Monitor authentication logs
        """

    elif threat_type == "Traffic Spike":
        return f"""
        This activity indicates abnormal traffic from IP {ip}.
        The system recorded {attempts} requests, which may suggest scanning or automated probing.

        Risk:
        Could indicate reconnaissance activity.

        Recommended Actions:
        - Investigate traffic patterns
        - Apply rate limiting
        - Monitor for escalation
        """

    return f"""
    Suspicious activity detected from IP {ip}.
    Severity level: {severity}.

    Recommended Actions:
    - Investigate logs
    - Monitor activity
    """