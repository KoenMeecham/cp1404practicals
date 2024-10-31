"""
CP1402 prac 6
programming language
expected: 10mins
actual:
"""

class ProgrammingLanguage:
    """Represent a car object"""
    def __init__(self, typing="", reflection="", date=0):
        """Construct a programming language instance"""
        self.typing = typing
        self.reflection = reflection
        self.date = date

    def is_dynamic(self):
        """Determine if this is a dynamic programming language"""
        return self.typing == "dynamic"
