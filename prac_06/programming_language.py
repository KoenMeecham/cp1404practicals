"""
CP1402 prac 6
programming language
expected: 10mins
actual: 15mins
"""

class ProgrammingLanguage:
    """Represent a car object"""
    def __init__(self, name, typing, reflection, year):
        """Construct a programming language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a programming language"""
        return f"{self.name}, {self.typing} typing, reflection: {self.reflection}, first appeared in {self.year}"

    def is_dynamic(self):
        """Determine if this is a dynamic programming language"""
        return self.typing == "Dynamic"
