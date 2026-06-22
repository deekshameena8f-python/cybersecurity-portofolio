
from src.parser import parse_logs
from src.detector import detect_alerts

logs = parse_logs("logs/sample.log")

alerts = detect_alerts(logs)

for alert in alerts:
    print(alert)
