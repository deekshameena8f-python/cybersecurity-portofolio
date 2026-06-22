# src/parser.py

def parse_logs(file_path):
    logs = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split()

            date = parts[0]
            time = parts[1]
            level = parts[2]
            message = " ".join(parts[3:])

            logs.append({
                "date": date,
                "time": time,
                "level": level,
                "message": message
            })

    return logs
