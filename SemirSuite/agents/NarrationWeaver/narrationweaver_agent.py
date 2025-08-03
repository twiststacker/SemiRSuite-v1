from models.handler import ModelHandler
from agents.main_agent import AgentBaseClass

class NarrationWeaverAgent(AgentBaseClass):
    def __init__(self):
        super().__init__()
        self.model = ModelHandler("NarrationGPT")

    def generate_script(self, topic: str, tone: str = "neutral") -> str:
        prompt = f"Write a {tone} voiceover script about: {topic}"
        return self.model.infer(prompt)