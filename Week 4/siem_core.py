import re
from collections import defaultdict

def parse_and_analyze_logs(log_file_path, failure_threshold=5):
    print("=" * 60)
    print(f"🚀 INITIALIZING SIEM CORE LOG PARSING ENGINE")
    print("=" * 60)
    
    # Track failed logins per IP address
    failed_attempts = defaultdict(int)
    total_lines = 0
    
    # Regular expression pattern to extract log metadata named capture groups
    log_pattern = r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - IP: (?P<ip>[\d\.]+) - STATUS: (?P<status>\w+) - USER: (?P<user>\w+)"
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                total_lines += 1
                match = re.search(log_pattern, line)
                if match:
                    data = match.groupdict()
                    if data['status'] == 'FAILED':
                        failed_attempts[data['ip']] += 1
                        
        print(f"Successfully processed {total_lines} lines of log telemetry.\n")
        print("🚨 --- MONITORING ACTIVE SECURITY ALERTS ---")
        
        alerts_triggered = False
        for ip, count in failed_attempts.items():
            if count >= failure_threshold:
                print(f"[ALERT] [HIGH PRIORITY] - Potential Brute-Force Attack Detected!")
                print(f"  • Source IP: {ip}")
                print(f"  • Failed Logins: {count} attempts recorded.")
                print(f"  • Status: Flagged for Containment via local firewall policies.\n")
                alerts_triggered = True
                
        if not alerts_triggered:
            print("🟢 Security Status: Nominal. No alert thresholds breached.")
            
    except FileNotFoundError:
        print(f"❌ Error: The file target '{log_file_path}' was not found.")
        
if __name__ == "__main__":
    # Execute analysis on the log file
    parse_and_analyze_logs("auth.log")
