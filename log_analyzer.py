
logs = [
    "Failed login for user admin from 192.168.1.10",
    "Successful login for user deepa from 192.168.1.15",
    "Failed login for user root from 192.168.1.20",
    "Failed login for user admin from 192.168.1.10",
    "Successful login for user admin from 192.168.1.10",
    "Failed login for user test from 192.168.1.25"
]

failed_logins = []

for log in logs:
    if "Failed login" in log:
        failed_logins.append(log)

ip_counts = {}

for log in failed_logins:
    ip = log.split("from ")[1]

    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1

report = f"""
========== SECURITY ANALYSIS REPORT ==========

Total Log Entries: {len(logs)}
Total Failed Logins: {len(failed_logins)}

Failed Login Attempts by IP:
"""

for ip, count in ip_counts.items():
    report += f"\n{ip} : {count} failed attempts"

report += "\n\nSuspicious IP Addresses:\n"

for ip, count in ip_counts.items():
    if count >= 2:
        report += f"{ip} : {count} failed attempts\n"

report += "\n========== END OF REPORT =========="

print(report)

with open("security_report.txt", "w") as file:
    file.write(report)

print("\nReport saved successfully!")
