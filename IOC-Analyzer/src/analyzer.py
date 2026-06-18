import re

with open("data/iocs.txt") as f:
iocs = [line.strip() for line in f]

ip_pattern = r"^\d+.\d+.\d+.\d+$"
hash_pattern = r"^[a-fA-F0-9]{32}$"
email_pattern = r"^[^@]+@[^@]+.[^@]+$"

report_lines = []

report_lines.append("IOC ANALYSIS REPORT")
report_lines.append("=" * 50)
report_lines.append("")

for ioc in iocs:

```
if re.match(hash_pattern, ioc):
    ioc_type = "MD5 Hash"
    risk = "HIGH"

elif re.match(ip_pattern, ioc):
    ioc_type = "IP Address"
    risk = "MEDIUM"

elif re.match(email_pattern, ioc):
    ioc_type = "Email Address"
    risk = "MEDIUM"

elif "." in ioc:
    ioc_type = "Domain"
    risk = "HIGH"

else:
    ioc_type = "Unknown"
    risk = "LOW"

line = f"{ioc} | {ioc_type} | {risk}"
report_lines.append(line)
```

with open("reports/report.txt", "w") as report:

```
for line in report_lines:
    report.write(line + "\n")
```

print("Report generated successfully.")




