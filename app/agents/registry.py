# Agent registry, loading blueprints + custom agents

class AgentRegistry:
    def __init__(self):
        self.agents = {}

    def load_blueprints(self):
        pass  # Load built-in agent blueprints

    def register_agent(self, agent_id, agent_config):
        self.agents[agent_id] = agent_config

    def get_agent(self, agent_id):
        return self.agents.get(agent_id)
