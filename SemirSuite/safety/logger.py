import datetime

def log_safety_event(output: str, violations: list, severity: str):
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}] Severity: {severity} | Violations: {violations} | Output: {output}\n"
    with open("safety/safety_log.txt", "a") as f:
        f.write(log_entry)