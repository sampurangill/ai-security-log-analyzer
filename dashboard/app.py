import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd

from parser.log_parser import parse_logs
from detector.rule_engine import detect_brute_force, detect_ip_spike
from ai.analyzer import analyze_threat

st.set_page_config(page_title="AI Security Log Analyzer", layout="wide")

st.title("AI Security Log Analyzer")
st.write("A cybersecurity dashboard for detecting suspicious log activity and explaining threats.")
uploaded_file = st.file_uploader("Upload a log file", type=["txt"])

# Load and parse logs
if uploaded_file is not None:
    # Read uploaded file
    df = parse_logs(uploaded_file)
else:
    # Default sample file
    df = parse_logs("data/sample_logs.txt")

# Run detections
brute_force_threats = detect_brute_force(df)
spike_threats = detect_ip_spike(df)
all_threats = brute_force_threats + spike_threats

# Top metrics
st.subheader("Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total Log Events", len(df))
col2.metric("Failed Logins", len(df[df["status"] == "Failed"]))
col3.metric("Threats Detected", len(all_threats))

# Visual chart
import matplotlib.pyplot as plt

st.subheader("Failed Logins by IP")

failed_df = df[df["status"] == "Failed"]
ip_counts = failed_df["ip"].value_counts()

fig, ax = plt.subplots(figsize=(5, 2))

# Create bar chart
ax.bar(ip_counts.index, ip_counts.values, color="#ff4b4b", width=0.7)

# Labels
ax.set_xlabel("IP Address")
ax.set_ylabel("Failed Login Attempts")
ax.set_title("Failed Logins by IP")

# Rotate labels so they don't overlap
plt.xticks(rotation=45)

st.pyplot(fig)

# Raw logs
st.subheader("Parsed Log Data")
st.dataframe(df, width='stretch')

# Threat detections
st.subheader("Detected Threats")

if not all_threats:
    st.success("No suspicious activity detected.")
else:
    threats_df = pd.DataFrame(all_threats)
    st.dataframe(threats_df, width='stretch')

    st.subheader("Threat Analysis")

    for i, threat in enumerate(all_threats, start=1):
        color = "red" if threat["severity"] == "High" else "orange"

        st.markdown(f"### 🚨 Threat {i}")
        st.markdown(f"**IP:** `{threat['ip']}`")
        st.markdown(f"**Type:** {threat['type']}")
        st.markdown(f"**Severity:** :{color}[{threat['severity']}]")

        if "attempts" in threat:
            st.markdown(f"**Attempts:** {threat['attempts']}")
        if "activity_count" in threat:
            st.markdown(f"**Activity Count:** {threat['activity_count']}")

        st.markdown("**Analysis:**")
        st.write(analyze_threat(threat))

        st.markdown("---")