# Example integration test
def test_workflow():
    idea_agent = Idea ForgeAgent()
    ideas = idea_agent.generate_ideas("Create a viral video")
    
    narrative_agent = AutoNarrateAgent()
    narration = narrative_agent.generate_narration(ideas[0])
    
    assert isinstance(narration, str)
