class ProgrammingLanguage:
    def __init__(self, typing="", reflection="", date=0):
        self.typing = typing
        self.reflection = reflection
        self.date = date

    def is_dynamic(self):
        return self.typing == "dynamic"
