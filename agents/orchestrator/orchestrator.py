class AgentOrchestrator:
    def __init__(self):
        self.agents = []

    def register_agent(self, agent):
        self.agents.append(agent)

    def run_all(self):
        for agent in self.agents:
            agent.run()