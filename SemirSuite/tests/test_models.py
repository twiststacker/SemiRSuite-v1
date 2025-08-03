import pytest
from models.handler import ModelHandler
from agents.IdeaForge.ideaforge_agent import IdeaForgeAgent

@pytest.fixture
def model_handler():
    return ModelHandler("semirsuite_latest")

@pytest.fixture
def ideaforge_agent():
    return IdeaForgeAgent()

def test_model_loading(model_handler):
    assert model_handler.model is not None, "Model failed to load."

def test_agent_integration(ideaforge_agent):
    prompt = "Create a video tutorial on AI."
    ideas = ideaforge_agent.generate_ideas(prompt)
    assert ideas is not None, "Agent returned None."
    assert isinstance(ideas, list), "Agent output is not a list."
    assert all(isinstance(idea, str) for idea in ideas), "Agent output contains non-string items."

def test_agent_empty_prompt(ideaforge_agent):
    ideas = ideaforge_agent.generate_ideas("")
    assert ideas is not None, "Agent returned None for empty prompt."
    assert isinstance(ideas, list), "Agent output is not a list for empty prompt."

def test_agent_special_characters(ideaforge_agent):
    prompt = "@#$%^&*()_+"
    ideas = ideaforge_agent.generate_ideas(prompt)
    assert ideas is not None, "Agent failed on special characters."
    assert isinstance(ideas, list), "Agent output is not a list for special characters."