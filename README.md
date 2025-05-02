# Secure Todo App

This is a Flask-based web application designed to demonstrate secure development practices within a DevSecOps workflow. The app allows users to manage a simple to-do list while integrating static analysis, container security scanning, CI/CD automation, and basic logging.

---

## Features

- Simple Flask web interface for task management  
- Docker containerization for consistent deployment  
- Static code analysis using Bandit and ESLint  
- Vulnerability scanning using Trivy  
- CI/CD pipeline automation with GitHub Actions  
- Basic logging for user activity  

---

## DevSecOps Workflow Overview

This project showcases an end-to-end DevSecOps pipeline:

### 1. Static Code Analysis
- **Tools:** Bandit (Python), ESLint (JavaScript)  
- **Purpose:** Detect insecure coding practices  
- **Execution:** Integrated into CI pipeline  
- **Results:** No high-severity issues found in application code  

### 2. Docker Image Creation
- **Tool:** Docker  
- **Image Name:** `todo-app:latest`  
- **Base Image:** Debian 12.10  
- **Purpose:** Encapsulate the Flask app and its environment  

### 3. Vulnerability Scanning
- **Tool:** Trivy by Aqua Security  
- **Scope:** Scans Docker image for known CVEs  
- **Mode:** Fail pipeline on CRITICAL or HIGH vulnerabilities  
- **Findings:**  
  - 2 vulnerabilities detected (1 HIGH, 1 CRITICAL)  
  - Both originate from the Debian base image  
  - Neither is exploitable in the current application context  
- **Details available in:** `vulnerability_report.md`  

### 4. CI/CD Pipeline
- **Platform:** GitHub Actions  
- **Workflow Includes:**  
  - Code checkout  
  - Static analysis (Bandit, ESLint)  
  - Docker image build  
  - Trivy vulnerability scan  
- **Outcome:** Fails if critical/high severity issues are found  

### 5. Logging
- **Implementation:** Python `logging` module  
- **Purpose:** Track user logins and task creation  
- **Security:** No passwords or sensitive data are stored in logs  
- **Log File:** `app.log`  

---

## Logging Configuration

Configured in `app.py`:

```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s'
)
```

Used as:

```python
logging.info(f"User '{username}' successfully logged in.")
logging.info(f"Task added by user: '{task}'.")
```

---

## File Structure

```
todo-app/
├── app.py
├── Dockerfile
├── requirements.txt
├── trivy_report_latest.txt
├── vulnerability_report.md
├── .github/
│   └── workflows/
│       └── main.yml
└── README.md
```

---

## Summary

The Secure Todo App demonstrates how to integrate core security practices into a modern DevSecOps pipeline. It includes static code scanning, secure containerization, automated vulnerability assessments, and secure logging — all built and tested through GitHub Actions.

---

**Prepared by:**  
Rachid Dwyer  
Intern, Refonte Cybersecurity Program  
[GitHub Repository](https://github.com/Rachid1026/todo-app)
