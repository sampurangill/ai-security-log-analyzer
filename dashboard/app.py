import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from parser.log_parser import parse_logs
from detector.rule_engine import detect_brute_force, detect_ip_spike
from ai.analyzer import analyze_threat

st.set_page_config(page_title="AI Security Log Analyzer", layout="wide")

st.title("AI Security Log Analyzer")
st.write("A cybersecurity dashboard for detecting suspicious log activity and explaining threats.")

uploaded_file = st.file_uploader("Upload a log file", type=["txt", "log"])

log_type = st.selectbox(
    "Select log type",
    ["auto", "custom", "linux_auth", "apache"]
)

# Load and parse logs
if uploaded_file is not None:
    df = parse_logs(uploaded_file, log_type=log_type)
else:
    df = parse_logs("data/sample_logs.txt", log_type=log_type)

# Handle empty or failed parsing
if df.empty:
    st.warning("No valid log entries were parsed. Try another file or log type.")
    st.stop()

# Run detections
brute_force_threats = detect_brute_force(df)
spike_threats = detect_ip_spike(df)
all_threats = brute_force_threats + spike_threats

# Overview metrics
st.subheader("Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total Log Events", len(df))
col2.metric("Failed Logins", len(df[df["status"] == "Failed"]))
col3.metric("Threats Detected", len(all_threats))

# Bar chart
st.subheader("Failed Logins by IP")

failed_df = df[df["status"] == "Failed"]
ip_counts = failed_df["ip"].value_counts()

if not ip_counts.empty:
    fig, ax = plt.subplots(figsize=(6, 3))

    ax.bar(ip_counts.index, ip_counts.values, color="#ff4b4b", width=0.4)
    ax.set_xlabel("IP Address")
    ax.set_ylabel("Failed Login Attempts")
    ax.set_title("Failed Logins by IP")

    plt.xticks(rotation=45)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()

    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        st.pyplot(fig)
else:
    st.info("No failed login events found for charting.")

# Parsed log data
st.subheader("Parsed Log Data")
st.dataframe(df, use_container_width=True)

# Detected threats
st.subheader("Detected Threats")

if not all_threats:
    st.success("No suspicious activity detected.")
else:
    threats_df = pd.DataFrame(all_threats)
    st.dataframe(threats_df, use_container_width=True)

    st.subheader("Threat Analysis")

    for i, threat in enumerate(all_threats, start=1):
        with st.expander(f"Threat {i}: {threat['type']} from {threat['ip']}"):
            st.write(f"**IP:** {threat['ip']}")
            st.write(f"**Type:** {threat['type']}")
            st.write(f"**Severity:** {threat['severity']}")

            if "attempts" in threat:
                st.write(f"**Attempts:** {threat['attempts']}")
            if "activity_count" in threat:
                st.write(f"**Activity Count:** {threat['activity_count']}")

            analysis = analyze_threat(threat)
            st.write("**Analysis:**")
            st.write(analysis)