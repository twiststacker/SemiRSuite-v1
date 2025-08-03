import os

class SafetyProtocolManager:
    def validate(self, text: str) -> bool:
        return "unsafe" not in text.lower()

        # Locate the ban list relative to this file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ban_list_path = os.path.join(base_dir, "safety_protocols", "ban_list.txt")

        try:
            with open(ban_list_path, "r") as f:
                self.banned_words = [line.strip().lower() for line in f if line.strip()]
        except FileNotFoundError:
            self.banned_words = []
            print("⚠️ Warning: ban_list.txt not found. No safety filtering applied.")

    def validate(self, text: str) -> bool:
        lowered = text.lower()
        return not any(banned in lowered for banned in self.banned_words)