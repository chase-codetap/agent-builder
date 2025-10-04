# Base agent class/interface
class BaseAgent:
    def run(self, request):
        raise NotImplementedError

    def build_prompt(self, request):
        raise NotImplementedError
