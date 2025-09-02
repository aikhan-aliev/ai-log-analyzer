# AI-Powered Log Analyzer

## Project Overview
**AI Log Analyzer** is an advanced Python-based tool that automatically parses, processes, and analyzes system or CI/CD pipeline logs to detect anomalies. By applying **machine learning techniques** (Isolation Forest) to structured log data, it identifies unusual patterns such as failed jobs, long-running tasks, or unexpected errors, enabling faster troubleshooting and improving the reliability of development pipelines.

This project showcases the integration of **AI-driven analytics**, **data engineering**, and **containerization** into a single workflow, making it highly relevant for DevOps, software engineering, and AI-assisted operations roles.

---

## Key Features
- **Log Parsing & Feature Extraction:**  
  Reads CSV-formatted logs and transforms them into structured, numeric, and categorical features suitable for machine learning.
  
- **Anomaly Detection:**  
  Uses **Isolation Forest** to detect abnormal events in the pipeline, such as unusually long durations, failed tests, or deployment errors.

- **Visualization & Reporting:**  
  Automatically generates clear, interpretable visualizations, including:
  - Job status distribution (`success` vs `fail`)
  - Pipeline stage distribution (`build`, `test`, `deploy`)
  - Timeline of anomalies
  - Boxplots comparing normal vs anomalous feature distributions  
  All reports are saved as PNG files in the `reports/` folder for easy review.

- **Containerization with Docker:**  
  Fully Dockerized for portability, reproducibility, and integration into CI/CD pipelines. Runs consistently across different environments without dependency issues.

- **Extensible & CI/CD Ready:**  
  Designed to be integrated into development pipelines to monitor logs in real-time or batch mode, providing actionable insights for software teams.

---

## Technologies & Tools
- **Programming:** Python 3.11  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** scikit-learn (Isolation Forest)  
- **Visualization:** Matplotlib, Seaborn  
- **Containerization:** Docker  
- **Version Control:** Git  

---


## Why This Project Stands Out
1. **AI applied to real-world DevOps problems:** Detects pipeline anomalies automatically, saving engineers’ time and preventing downtime.  
2. **End-to-end pipeline integration:** From parsing logs → feature extraction → ML detection → visualization → Docker deployment.  
3. **Professional-grade deliverables:** Includes automated visual reports, fully containerized environment, and ready-to-run scripts.  
4. **Technical depth & clarity:** Demonstrates Python programming, data engineering, ML modeling, visualization, and containerization skills in one project.  

---

