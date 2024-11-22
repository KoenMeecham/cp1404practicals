"""
CP1404
Band class
estimated: 15mins
actual: 20mins
"""

class Band:
    """Band class"""
    def __init__(self, name=""):
        """Construct band class instances"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """String representation of band class"""
        return f'{self.name}, {self.musicians}'

    def __repr__(self):
        """List representation of band class"""
        return str(vars(self))

    def add_musician(self, musician):
        """Add musician to band"""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing what each musician in the band is playing."""
        if not self.musicians:
            return f"{self.name} has no musicians!"
        return "\n".join(musician.play() for musician in self.musicians)






