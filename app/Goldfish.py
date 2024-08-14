from .Fish import Fish

class Goldfish(Fish):
    def __init__(self, name):
        super().__init__(name)

    def glub(self):
        print(f"Goldfish glub: {self.name}")
        super().glub()