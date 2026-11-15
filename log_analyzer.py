
# Read authentication logs
with open("auth.log", "r") as file:
    logs = file.readlines()

# Identify failed login attempts
failed_logins = []

for log in logs:
    if "Failed login" in log:
        failed_logins.append(log.strip())

# Count failed attempts by IP
ip_counts = {}

for log in failed_logins:
    ip = log.split("from ")[1]

    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1

# Generate security report
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

print("\nSecurity report saved successfully!")
