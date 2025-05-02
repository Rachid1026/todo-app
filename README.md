# Secure TODO App – DevSecOps Integration

This project is a simple Flask-based TODO web application with integrated DevSecOps tooling to demonstrate secure development practices. It forms part of a cybersecurity internship project focusing on containerized security scanning using Trivy.

## 🔐 Security Tools Used

### Trivy
Trivy was integrated into the CI/CD pipeline to scan for vulnerabilities in:

- **Operating system packages** (Debian 12)
- **Application dependencies** (Flask, Jinja2, etc.)
- **Docker image layers**

### Key Findings (from Trivy scan)

- **Total vulnerabilities in container image**: 104
  - LOW: 72
  - MEDIUM: 30
  - HIGH: 1
  - CRITICAL: 1
- **Notable CVEs:**
  - `CVE-2023-31484` – TLS verification issue in Perl’s CPAN module (HIGH)
  - `CVE-2023-45853` – zlib heap-based buffer overflow (CRITICAL)

> 🔎 These findings were documented in `vulnerability_report.md`.

## 🧪 How to Run the App Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Rachid1026/todo-app.git
   cd todo-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

##  Docker Support

You can also run the app in a container:
```bash
docker build -t secure-todo-app .
docker run -p 5000:5000 secure-todo-app
```

##  Trivy Scan

To run a Trivy scan manually:
```bash
trivy image secure-todo-app
```

##  Author

**Rachid Dwyer**  
Cybersecurity Intern, Refonte  
GitHub: [@Rachid1026](https://github.com/Rachid1026)

---
*This repository is part of a hands-on DevSecOps internship project to demonstrate secure application deployment using Docker and Trivy.*
