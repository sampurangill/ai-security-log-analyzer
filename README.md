# AI Security Log Analyzer

A cybersecurity-focused Python project that detects suspicious activity in authentication logs and provides automated threat analysis through rule-based, AI-style detection.

## 🔍 Overview
This project simulates real-world security monitoring workflows by analyzing login activity to identify potential threats such as brute-force attacks and abnormal login patterns.

It includes a modular pipeline for parsing logs, detecting threats, and visualizing results through a dashboard.

## 🤖 AI Implementation Note

This project was originally designed to integrate with an AI model for dynamic threat analysis. However, due to API usage costs, the current version uses a rule-based analysis engine that simulates AI-style responses.

The system classifies threats and assigns severity levels based on detected patterns (e.g., repeated failed logins, suspicious IP activity), providing structured and explainable outputs.

This approach ensures:
- No external API costs
- Fully local and reproducible analysis
- Clear, deterministic threat detection logic

The architecture is designed to support future integration with real AI models if needed.

## ⚙️ Features
- Log parsing and structured data extraction
- Detection of brute force login attempts
- Suspicious IP identification
- Rule-based threat classification with AI-style analysis output
- Interactive dashboard built with Streamlit
- File upload support for custom log analysis
- Data visualization with matplotlib

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
- Detect brute force attacks from repeated failed login attempts
- Identify suspicious IP activity
- Analyze authentication logs for anomalies

## 📌 Future Improvements
- Real-time log ingestion
- Integration with LLM-based threat analysis (cost-optimized implementation)
- Machine learning-based anomaly detection
- Deployment as a web app

## 👤 Author
Sampuran Gill

## 📸 Dashboard Preview
<img width="1641" height="459" alt="Screenshot 2026-04-20 at 4 15 41 PM" src="https://github.com/user-attachments/assets/f28d700f-779b-485a-b499-1f6c5b8ebcc7" />
<img width="1464" height="930" alt="Screenshot 2026-04-20 at 4 16 48 PM" src="https://github.com/user-attachments/assets/55a1d59f-8a9d-4190-8ae5-130b29197398" />
<img width="1599" height="866" alt="Screenshot 2026-04-20 at 4 17 16 PM" src="https://github.com/user-attachments/assets/b0fd2028-8e75-4b1e-99bf-9690f6213a7c" />
