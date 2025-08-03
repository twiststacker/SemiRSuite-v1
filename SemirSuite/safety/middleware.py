class SafetyMiddleware:
    def __init__(self):
        self.ban_list = self._load_ban_list()

    def _load_ban_list(self) -> set:
        with open("safety/ban_list.txt", "r") as f:
            return {line.strip() for line in f}

    def validate_output(self, output: str) -> bool:
        for word in self.ban_list:
            if word.lower() in output.lower():
                return False
        return True