"""
CP1402
guitar
expected: 30mins
actual: 41mins
"""
CURRENT_YEAR = 2024
VINTAGE_AGE = 50
class Guitar:
    """Represents a guitar object"""
    def __init__(self, name="", year=0, cost=0):
        """Construct a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar"""
        return f'{self.name} ({self.year}) :  ${self.cost}'

    def get_age(self):
        """Return the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return true if the guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE

