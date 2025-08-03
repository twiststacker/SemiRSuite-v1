import toml
from typing import Dict, Any
from prometheus_client import Counter

# Prometheus metrics
TASK_COUNTER = Counter("semirsuite_tasks_total", "Total tasks processed", ["agent", "task_type"])

# Temporary agent stubs for testing
class PromptPortAgent:
    def parse(self, request):
        class ParsedTask:
            type = "IDEA_GENERATION"
            topic = "futuristic UI"
            prompt = request
        return ParsedTask()

class IdeaForgeAgent:
    def generate(self, prompt, trends):
        return [f"Idea based on '{prompt}' and trends: {trends}"]

class ClipSlicerAgent:
    def slice(self, idea):
        return f"Sliced clip from idea: {idea}"

class AutoNarrateAgent:
    def narrate(self, clip):
        return f"Narrated version of: {clip}"

class TrendSyncAgent:
    def analyze(self, topic):
        return f"Trending data for: {topic}"

class Orchestrator:
    def __init__(self, registry_path: str = "semirsuite/configs/agent_registry.toml"):
        self.registry = toml.load(registry_path)
        self.agents = self._load_agents()

    def _load_agents(self) -> Dict[str, Any]:
        agent_map = {
            "PromptPort": PromptPortAgent,
            "IdeaForge": IdeaForgeAgent,
            "ClipSlicer": ClipSlicerAgent,
            "AutoNarrate": AutoNarrateAgent,
            "TrendSync": TrendSyncAgent
        }
        agents = {}
        for name, config in self.registry.items():
            if config["status"] == "active" and name in agent_map:
                agents[name] = agent_map[name]()
        return agents

    def _safe_execute(self, agent_name: str, method: str, *args, **kwargs):
        agent = self.agents[agent_name]
        if hasattr(agent, "validate_input"):
            agent.validate_input(*args, **kwargs)
        if hasattr(agent, "run_safety_checks"):
            agent.run_safety_checks(*args, **kwargs)
        return getattr(agent, method)(*args, **kwargs)

    def process_request(self, request: str) -> Dict[str, Any]:
        try:
            parsed_task = self._safe_execute("PromptPort", "parse", request)
            TASK_COUNTER.labels(agent="PromptPort", task_type=parsed_task.type).inc()

            if parsed_task.type == "IDEA_GENERATION":
                trend_data = self._safe_execute("TrendSync", "analyze", parsed_task.topic)
                ideas = self._safe_execute("IdeaForge", "generate", prompt=parsed_task.prompt, trends=trend_data)
                clip = self._safe_execute("ClipSlicer", "slice", ideas[0])
                result = self._safe_execute("AutoNarrate", "narrate", clip)
                return {"status": "success", "result": result}

            elif parsed_task.type == "TREND_ANALYSIS":
                trend_data = self._safe_execute("TrendSync", "analyze", parsed_task.topic)
                return {"status": "success", "trend": trend_data}

            else:
                return {"status": "error", "message": f"Unsupported task type: {parsed_task.type}"}

        except Exception as e:
            return {"status": "error", "message": str(e)}

def orchestrate(request: str) -> Dict[str, Any]:
    orchestrator = Orchestrator("semirsuite/configs/agent_registry.toml")
    return orchestrator.process_request(request)