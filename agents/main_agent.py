# This file marks 'agents' as a Python package.

import logging
from models.model_handler import ModelHandler
from agents.safety import SafetyProtocolManager


class AgentBaseClass:
    def __init__(self):
        self.safety_protocol = SafetyProtocolManager()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def run_safety_check(self, text: str) -> bool:
        is_safe = self.safety_protocol.validate(text)
        if not is_safe:
            self.logger.warning("Unsafe output detected.")
        return is_safe


if __name__ == "__main__":
    handler = ModelHandler("semirsuite_latest", env="prod")
    info = handler.get_model_info()
    print("🔍 Loaded Model Info:")
    print(info)

    agent = AgentBaseClass()  # ✅ Instantiate the agent

    test_cases = [
        "This is safe",
        "Execute the protocol",
        "System commands must be restricted",
        "This is malicious behavior",
        "All systems operational",
        "No harmful intent detected"
    ]

    print("🔍 Running safety checks...\n")
    for text in test_cases:
        result = agent.run_safety_check(text)
        print(f"Input: '{text}' → Safety check passed: {result}")