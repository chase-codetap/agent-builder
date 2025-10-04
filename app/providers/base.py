# Provider base class/interface
class BaseProvider:
    def run(self, prompt, model, **kwargs):
        raise NotImplementedError
