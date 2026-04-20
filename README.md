# AI Security Log Analyzer

A cybersecurity-focused Python project that detects suspicious activity in authentication logs and provides automated threat analysis through an interactive dashboard.

## 🔍 Overview
This project simulates real-world security monitoring by analyzing login activity to identify potential threats such as brute-force attacks and abnormal login patterns.

It includes a modular pipeline for parsing logs, detecting threats, and visualizing results through a dashboard.

## ⚙️ Features
- Log parsing and structured data extraction
- Detection of brute force login attempts
- Suspicious IP identification
- Automated threat classification and severity labeling
- Interactive dashboard built with Streamlit
- File upload support for custom log analysis
- Data visualization with matplotlib

## 🛠️ Technologies Used
- Python
- Pandas
- Streamlit
- Matplotlib

## 🚀 How to Run

1. Clone the repository:
   
git clone https://github.com/sampurangill/ai-security-log-analyzer.git
cd ai-security-log-analyzer

2. Install dependencies:
   
pip install -r requirements.txt

3. Run the dashboard:
   
streamlit run dashboard/app.py

## 📊 Example Use Cases
- Detect brute force attacks from repeated failed login attempts
- Identify suspicious IP activity
- Analyze authentication logs for anomalies

## 📌 Future Improvements
- Real-time log ingestion
- Integration with SIEM tools
- Machine learning-based anomaly detection
- Deployment as a web app

## 👤 Author
Sampuran Gill
