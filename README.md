# AI Security Log Analyzer

A cybersecurity-focused Python application that detects suspicious activity in authentication and web logs, and provides automated threat analysis through an interactive dashboard.

## 🔍 Overview

This project simulates real-world security monitoring by analyzing log data to identify potential threats such as brute-force attacks, abnormal login patterns, and suspicious IP behavior.

It features a modular pipeline for:
- Log ingestion and parsing
- Threat detection using rule-based logic
- Automated analysis and severity classification
- Visualization through an interactive dashboard

## 🤖 AI Implementation Note

This project was originally designed to integrate with an AI model for dynamic threat analysis.

However, due to API usage costs and the need for a fully reproducible, local environment, the current implementation uses a **rule-based analysis engine that simulates AI-style responses**.

The system:
- Classifies threats based on behavior patterns (e.g., repeated failed logins, IP spikes)
- Assigns severity levels
- Generates structured, explainable analysis outputs

### Why this approach:
- No external API costs  
- Fully local and portable  
- Deterministic and explainable logic  
- Easier to test and validate  

The architecture is intentionally designed to support future integration with real AI/ML models.

## ⚙️ Features

- Multi-format log parsing (custom, Linux SSH, Apache)
- Automatic log type detection
- Brute-force attack detection
- Suspicious IP activity detection
- Automated threat classification and severity labeling
- Interactive dashboard built with Streamlit
- File upload support for custom log analysis
- Data visualization using matplotlib

## 🧱 Supported Log Formats

The parser currently supports:

- Custom authentication logs  
- Linux SSH authentication logs  
- Apache access logs  

Users can:
- Select log type manually  
- Or use automatic format detection  

## 🛠️ Technologies Used

- Python  
- Pandas  
- Streamlit  
- Matplotlib  

## 🚀 How to Run

### 1. Clone the repository:
      
      git clone https://github.com/sampurangill/ai-security-log-analyzer.git

      cd ai-security-log-analyzer

### 2. Install dependencies:
      
      pip install -r requirements.txt

### 3. Run the dashboard:
   
      streamlit run dashboard/app.py

## 📊 Example Use Cases
- Detect brute-force attacks from repeated failed login attempts
- Identify suspicious IP behavior across log sources
- Analyze authentication logs for anomalies
- Simulate basic SIEM-style monitoring workflows

## 📌 Future Improvements
- Real-time log ingestion (stream processing)
- Integration with SIEM platforms (e.g., Splunk)
- Machine learning-based anomaly detection
- Support for additional log formats (e.g., Windows Event Logs)
- Deployment as a hosted web application

## 👤 Author
Sampuran Gill

## 📸 Dashboard Preview
<img width="1595" height="918" alt="Screenshot 2026-04-21 at 5 33 24 PM" src="https://github.com/user-attachments/assets/7cd6ac92-c52f-42c4-a73e-0ac53ebcc1eb" />
<img width="1597" height="565" alt="Screenshot 2026-04-21 at 5 33 53 PM" src="https://github.com/user-attachments/assets/cd1fc3d5-0815-44b9-a4c4-a8dcf5f5d019" />
<img width="1595" height="641" alt="Screenshot 2026-04-21 at 5 34 15 PM" src="https://github.com/user-attachments/assets/a41159f5-1efc-43ec-b620-23792fdb5a5e" />
