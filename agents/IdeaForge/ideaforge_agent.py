# agents/IdeaForge/ideaforge_agent.py

from models.model_handler import ModelHandler


class IdeaForgeAgent:
    """
    Agent responsible for generating creative ideas based on user prompts.
    Designed to produce structured, engaging output for SemiRSuite.
    """

    def __init__(self):
        self.model = ModelHandler("semirsuite_latest")

    def generate_ideas(self, prompt: str) -> list[str]:
        """
        Generates a formatted viral video idea based on the given prompt.

        Args:
            prompt (str): The creative prompt to inspire idea generation.

        Returns:
            list[str]: A list containing one formatted idea string.
        """
        raw_idea = self.model.infer(prompt)

        formatted = f"""
🎥 **Viral Video Concept**
📝 Prompt: _{prompt}_

💡 Idea: {raw_idea}

🔥 Why It Could Go Viral:
- Emotionally engaging or surprising
- Easy to remix or share
- Aligned with current trends

🏷️ Suggested Tags: #ViralIdea #Shorts #CreativeAI
"""
        return [formatted.strip()]