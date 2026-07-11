# Week 5 Project Completion Report
**Project 2: Advanced SIEM Log Analysis & Incident Alerting Engine**
**Course Module: Security Event Correlation, Detection Rules, & Log Automation**
## 1. Executive Summary
Modern enterprise environments generate vast pools of network log metadata across production boundaries. Relying on manual oversight is a critical security vulnerability. This project successfully engineered an automated, scriptable Security Information and Event Management (SIEM) ingestion pipeline to address this issue.

[cite_start]The finished software reads raw text logs, structures data using named regular expression capture groups, validates time ranges against organizational policy, and automatically triggers indicators of compromise (IOCs) . It exports event data to a JSON tracking schema, ensuring seamless documentation retention for blue-team operations.

## 2. Multi-Vector Correlation Rules Framework
[cite_start]The analysis engine was expanded to validate traffic against three core correlation alert configurations[cite: 69]:

### A. SIG-001: Alphanumeric Brute-Force Defenses
* **Objective:** Detect automated credential-guessing software.
* **Logic Boundary:** Alarms when a single source IP address registers $\ge 5$ distinct authorization failures.

### B. SIG-002: Off-Hours Activity Detection
* **Objective:** Identify potential malicious operations or compromised user profiles active outside corporate business hours.
* **Logic Boundary:** Inspects valid logins (`SUCCESS`) occurring exclusively between the hours of 00:00 AM and 05:00 AM.

### C. SIG-003: Post-Failure Successful Entry Verification
* **Objective:** Capture successful account takeover patterns where an attacker successfully guesses a password after several failed attempts.
* **Logic Boundary:** Evaluates if a successful login event stems from an IP that previously registered authentication failures.

## 3. Empirical Test Log Matrix (Thorough Testing Validation)
[cite_start]The completed tool was executed against a highly complex validation dataset (`expanded_auth.log`)[cite: 110]:

| Test Case ID | Target Vector Sample | Detected Trigger Condition | Engine Alert Output | Verification Outcome / Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-201** | `203.0.113.5` | $\ge 5$ Failed Logins | `SIG-001 (High)` | **PASS** — Successfully isolated rapid credential-stuffing attempts. |
| **TC-202** | `198.51.100.44` | Success login at 02:15 AM | `SIG-002 (Medium)` | **PASS** — Correctly flagged unauthorized off-hours system usage. |
| **TC-203** | `45.33.22.112` | Failure followed by Success | `SIG-003 (Critical)`| **PASS** — Flagged a critical account compromise verification event. |


## 4. Final Security Conclusions & Architectural Impact
[cite_start]Automating log parsing removes human error and drastically decreases mean time to detect (MTTD) unauthorized operations . This prototype demonstrates a highly effective, low-overhead solution for indexing enterprise logs, managing detection rules, and formatting automated security warnings.

