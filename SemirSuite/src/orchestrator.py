from agents.trend_sync_agent import TrendSyncAgent
from agents.trend_analyzer_agent import TrendAnalyzerAgent

agent_map = {
    "PromptPort": PromptPortAgent,
    "IdeaForge": IdeaForgeAgent,
    "ClipSlicer": ClipSlicerAgent,
    "AutoNarrate": AutoNarrateAgent,
    "TrendSync": TrendSyncAgent,
    "TrendAnalyzer": TrendAnalyzerAgent
}