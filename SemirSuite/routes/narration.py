from fastapi import APIRouter
from agents.NarrationWeaver.narrationweaver_agent import NarrationWeaverAgent

router = APIRouter(prefix="/api/v1", tags=["Narration"])

@router.post("/generate-script")
def generate_script(topic: str, tone: str = "neutral"):
    agent = NarrationWeaverAgent()
    script = agent.generate_script(topic, tone)
    return {"script": script}