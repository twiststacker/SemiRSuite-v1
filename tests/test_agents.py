from agents.IdeaForge.ideaforge_agent import IdeaForgeAgent
from agents.AutoNarrate.autonarrate_agent import AutoNarrateAgent

def test_idea_generation():
    agent = IdeaForgeAgent()
    ideas = agent.generate_ideas("AI in education")
    assert isinstance(ideas, str)

def test_narration_generation():
    agent = AutoNarrateAgent()
    narration = agent.generate_narration("AI is transforming classrooms.")
    assert isinstance(narration, str)