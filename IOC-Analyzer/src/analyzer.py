import re

with open("data/iocs.txt") as f:
iocs = [line.strip() for line in f]

ip_pattern = r"^\d+.\d+.\d+.\d+$"
hash_pattern = r"^[a-fA-F0-9]{32}$"
email_pattern = r"^[^@]+@[^@]+.[^@]+$"

print("IOC Classification")
print("=" * 40)

for ioc in iocs:

if re.match(ip_pattern, ioc):
    print(ioc, "-> IP Address")

elif re.match(hash_pattern, ioc):
    print(ioc, "-> MD5 Hash")

elif re.match(email_pattern, ioc):
    print(ioc, "-> Email Address")

elif "." in ioc:
    print(ioc, "-> Domain")

else:
    print(ioc, "-> Unknown")

