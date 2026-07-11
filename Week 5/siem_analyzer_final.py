import re
import json
from datetime import datetime

def advanced_siem_engine(log_path, output_report_path="siem_alert_report.json"):
    print("=" * 65)
    print("🛡️  RUNNING PRODUCTION SIEM ENGINE - FINAL COMPLETION SUITE")
    print("=" * 65)
    
    # Incident Tracking Data Structures
    ip_failure_counts = {}
    incident_alerts = []
    
    log_pattern = r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - IP: (?P<ip>[\d\.]+) - STATUS: (?P<status>\w+) - USER: (?P<user>\w+)"

    try:
        with open(log_path, 'r') as file:
            for line in file:
                match = re.search(log_pattern, line)
                if not match:
                    continue
                    
                data = match.groupdict()
                timestamp = data['timestamp']
                ip_addr = data['ip']
                status = data['status']
                username = data['user']
                
                # Convert string timestamp to Python datetime object for temporal validation
                log_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                
                # RULE 1: Track Brute-Force Metrics
                if status == 'FAILED':
                    ip_failure_counts[ip_addr] = ip_failure_counts.get(ip_addr, 0) + 1
                    if ip_failure_counts[ip_addr] == 5:
                        incident_alerts.append({
                            "timestamp": timestamp,
                            "rule_triggered": "SIG-001 (Brute-Force Detection)",
                            "severity": "HIGH",
                            "source_ip": ip_addr,
                            "details": f"IP address reached critical threshold of 5 consecutive authentication failures."
                        })
                
                # RULE 2: Detect Off-Hours Access Anomaly (Midnight to 05:00 AM)
                if status == 'SUCCESS' and (0 <= log_time.hour < 5):
                    incident_alerts.append({
                        "timestamp": timestamp,
                        "rule_triggered": "SIG-002 (Off-Hours Active Connection)",
                        "severity": "MEDIUM",
                        "source_ip": ip_addr,
                        "details": f"Successful authentication by User [{username}] during unauthorized off-hours window."
                    })
                
                # RULE 3: Detect Compromise Following a Failure (Account Takeover)
                if status == 'SUCCESS' and ip_failure_counts.get(ip_addr, 0) > 0:
                    incident_alerts.append({
                        "timestamp": timestamp,
                        "rule_triggered": "SIG-003 (Suspicious Account Takeover Verification)",
                        "severity": "CRITICAL",
                        "source_ip": ip_addr,
                        "details": f"User [{username}] logged in successfully after this specific source IP logged previous failures."
                    })

        # Render Live Terminal Dashboard Results
        print(f"Analysis Complete. Detected {len(incident_alerts)} Security Event Anomalies:\n")
        for alert in incident_alerts:
            print(f"[{alert['severity']} ALERT] {alert['rule_triggered']}")
            print(f"  • Occurred At: {alert['timestamp']}")
            print(f"  • Source Actor: {alert['source_ip']}")
            print(f"  • Vector Context: {alert['details']}\n")
            
        # Export structured JSON for Audit Retention 
        with open(output_report_path, 'w') as out_file:
            json.dump(incident_alerts, out_file, indent=4)
        print(f"💾 Permanent audit report compiled and exported to: '{output_report_path}'")
        print("=" * 65)

    except Exception as e:
        print(f"❌ Execution failure: {str(e)}")

if __name__ == "__main__":
    advanced_siem_engine("expanded_auth.log")
