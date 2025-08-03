from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from agents.IdeaForge.ideaforge_agent import IdeaForgeAgent

router = APIRouter(prefix="/api/v1", tags=["Agents"])

@router.post("/generate-ideas")
def generate_ideas(prompt: str, db: Session = Depends(get_db)):
    agent = IdeaForgeAgent()
    ideas = agent.generate_ideas(prompt)
    return {"ideas": ideas}