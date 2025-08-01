from models.handler import ModelHandler

class AutoNarrateAgent:
    def __init__(self):
        self.model = ModelHandler("deepseek_r1_32b")

    def narrate(self, script):
        return self.model.infer(script)