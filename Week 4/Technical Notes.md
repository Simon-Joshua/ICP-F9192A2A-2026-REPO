# Week 4 Technical Notes: SIEM Engine Initialization
**Project 2: Automated SIEM Log Analysis Engine**
## 1. Engineering Framework & Core Concepts
This week focused on designing and building a Python-based parsing pipeline to ingest and analyze flat text-based computer system authentication logs. In enterprise network defense, tracking high-volume access logs manually is impossible. The core utility of an automated Security Information and Event Management (SIEM) pipeline is to ingest raw metadata, map key-value attributes, and match them against alert detection rules to reveal active network threats.

## 2. Ingestion Architecture & Metadata Extraction
The analysis core applies regular expressions (RegEx) with named capture groups to map unstructured log data into a structured dictionary layout:
* **Temporal Tracking:** Extracts timestamps (`YYYY-MM-DD HH:MM:SS`) to record when an anomaly occurs.
* **Network Actor Resolution:** Isolates the source IPv4 address to map the identity of unique malicious machines.
* **Access Vector Mapping:** Evaluates authorization outcome states (`SUCCESS` vs. `FAILED`) to index threat spikes.

## 3. Threshold Configuration & Alert Rule Logic
* **Rule Reference ID:** SIG-001 (Authentication Brute Force Mapping)
* **Detection Threshold:** Alarm triggers immediately if a single unique source IP generates $\ge 5$ cumulative authentication failures.
* **Functional Logic:** The script uses an associative dictionary counter. During validation, the external IP address `203.0.113.5` was found to have generated 6 distinct login failures, crossing the security policy boundary and successfully triggering the high-priority automated response alarm.
