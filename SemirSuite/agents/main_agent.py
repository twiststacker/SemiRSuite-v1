class AgentBaseClass:
    def __init__(self):
        self.safety_protocol = None

    def set_safety_protocol(self, safety_protocol):
        self.safety_protocol = safety_protocol

    def validate_output(self, output: str) -> bool:
        if self.safety_protocol:
            return self.safety_protocol.validate(output)
        return True