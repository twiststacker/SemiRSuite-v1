from model_handler import ModelHandler

class AutoNarrateAgent:
    def __init__(self):
        self.model = ModelHandler("deepseek_r1_32b")

    def generate_narration(self, script: str):
        prompt = f"Generate a voiceover and subtitles for: {script}"
        return self.model.generate(prompt)