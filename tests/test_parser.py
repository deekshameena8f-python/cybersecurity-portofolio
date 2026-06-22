# test_parser.py

from src.parser import parse_logs

logs = parse_logs("logs/sample.log")

for log in logs:
    print(log)
