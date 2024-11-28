"""
CP1404
unreliable car
estimated: 10mins
actual: 9mins
"""

from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    """Unreliable car class"""

    def __init__(self, name, fuel, reliability):
        """Construct unreliable car instances"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car randomly"""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven


