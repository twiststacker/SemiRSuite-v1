from models.handler import ModelHandler
from agents.main_agent import AgentBaseClass

class IdeaForgeAgent(AgentBaseClass):
    def __init__(self):
        super().__init__()
        self.model = ModelHandler("semirsuite:latest")

    def generate_ideas(self, prompt: str) -> list:
        return self.model.infer(prompt)