from models.handler import ModelHandler
from agents.main_agent import AgentBaseClass

class ClipSlicerAgent(AgentBaseClass):
    def __init__(self):
        super().__init__()
        self.model = ModelHandler("DeepSeek-R1:32B")

    def trim_clip(self, video_path: str, start_time: float, end_time: float) -> str:
        return "Trimmed clip saved successfully."