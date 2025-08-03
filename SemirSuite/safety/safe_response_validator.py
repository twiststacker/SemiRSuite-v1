from safety.logger import log_safety_event

class SafeResponseValidator:
    def __init__(self, ban_list_path: str = "safety/ban_list.txt"):
        self.ban_list = self._load_ban_list(ban_list_path)

    def _load_ban_list(self, path: str) -> set:
        try:
            with open(path, "r") as f:
                return {line.strip().lower() for line in f if line.strip()}
        except FileNotFoundError:
            return set()

    def validate(self, output: str) -> dict:
        violations = [word for word in self.ban_list if word in output.lower()]
        if violations:
            severity = self._assess_severity(violations)
            log_safety_event(output, violations, severity)
            return {
                "is_safe": False,
                "violations": violations,
                "severity": severity
            }
        return {"is_safe": True, "violations": [], "severity": "none"}

    def _assess_severity(self, violations: list) -> str:
        if len(violations) >= 3:
            return "critical"
        elif len(violations) == 2:
            return "moderate"
        else:
            return "low"