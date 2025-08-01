from model_handler import ModelHandler

class IdeaForgeAgent:
    def __init__(self):
        self.model = ModelHandler("semirsuite_latest")

    def generate_ideas(self, topic: str):
        prompt = f"Generate 5 creative video ideas about: {topic}"
        return self.model.generate(prompt)