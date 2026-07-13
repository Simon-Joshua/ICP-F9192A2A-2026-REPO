# Cybersecurity Engineering Portfolio
**Internship ID:** ICP-F9192A2A-2026 | **Duration:** 6 Weeks Self-Learning Program

---

## 🧑‍💻 Portfolio Overview
Welcome to my final cybersecurity portfolio project repository. Over the last 6 weeks, I have engineered and thoroughly tested two distinct security utilities aimed at resolving real-world infrastructure defense vulnerabilities.

---

## 🛠️ Project 1: Desktop Password Strength Analyzer (Weeks 2-3)
* **Real-World Problem:** Standard corporate complex password complexity rules create human patterns easily broken by dictionary attacks.
* **Solution Engineered:** A standalone Python desktop GUI application deploying a dual-engine validation framework.
* **Key Components:** * Shannon Entropy Math Engine ($E = L \times \log_2(R)$) checking theoretical randomness space.
  * Behavioral Heuristic Processing via the `zxcvbn` architecture to instantly flag keyboard sequences, predictable character modifications, and pre-compiled data leak wordlists.

## 🛡️ Project 2: Automated SIEM Log Analysis Engine (Weeks 4-5)
* **Real-World Problem:** Enterprise event monitoring produces vast metadata arrays that human analysts cannot trace manually.
* **Solution Engineered:** A high-speed, programmatic backend event correlation engine built in Python.
* **Key Components:**
  * Regex structural parsing mapping raw unstructured `auth.log` metadata into tokenized variables.
  * Multi-Vector Correlation Alert Rules processing Brute-Force indicators ($\ge 5$ failures), Off-Hours system access, and critical Post-Failure Account Takeovers.
  * Automatic generation of permanent structural `siem_alert_report.json` data logs for incident retention teams.

---

## 📊 Final Internship Verification Matrix
* [x] Week 1: Target environment tooling and project path alignment configured.
* [x] Week 2-3: Core cryptographic math verified and GUI application completed.
* [x] Week 4-5: Multi-vector logging analysis rules defined and verified with JSON reporting.
* [x] Week 6: Full repository optimization and formal portfolio release.
