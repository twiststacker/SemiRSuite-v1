import os
from semirsuite.configs.config_loader import load_config

class SafeResponseValidator:
    def __init__(self):
        config = load_config()
        ban_list_path = config["safety"]["ban_list_path"]
        self.ban_list = self._load_ban_list(ban_list_path)

    def _load_ban_list(self, path: str) -> set:
        full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", path)
        if not os.path.exists(full_path):
            return set()
        with open(full_path, "r", encoding="utf-8") as f:
            return set(line.strip().lower() for line in f if line.strip())

    def validate(self, output: str) -> bool:
        output_lower = output.lower()
        for word in self.ban_list:
            if word in output_lower:
                print(f"[Safety] Blocked output due to banned word: '{word}'")
                return False
        return True

# Singleton instance
validator = SafeResponseValidator()

def validate_response(output: str) -> bool:
    return validator.validate(output)