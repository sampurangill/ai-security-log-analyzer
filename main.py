from parser.log_parser import parse_logs
from detector.rule_engine import detect_brute_force, detect_ip_spike
from ai.analyzer import analyze_threat

# Parse logs
df = parse_logs("data/sample_logs.txt")

# Run detections
brute_force_threats = detect_brute_force(df)
spike_threats = detect_ip_spike(df)

# Combine all threats
all_threats = brute_force_threats + spike_threats

print("Detected Threats with Analysis:\n")

if not all_threats:
    print("No suspicious activity detected.")
else:
    for threat in all_threats:
        print(f"⚠️ IP: {threat['ip']}")
        print(f"   Type: {threat['type']}")
        print(f"   Severity: {threat['severity']}")

        if "attempts" in threat:
            print(f"   Attempts: {threat['attempts']}")
        if "activity_count" in threat:
            print(f"   Activity Count: {threat['activity_count']}")

        analysis = analyze_threat(threat)

        print("\n🧠 Analysis:")
        print(analysis)
        print("\n" + "=" * 50 + "\n")