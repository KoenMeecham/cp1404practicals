"""
CP1404
Sliver service test
estimated: 10mins
actual: 13mins
"""

from prac_09.taxi import Taxi

class SliverServiceTaxi(Taxi):
    """Sliver service taxi class"""
    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Construct sliver service taxi class instances"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """String representation of sliver service taxi class"""
        return f'{super().__str__()}, flagfall of ${self.flag_fall:.2f}'

    def get_fare(self):
        """Calculate fare"""
        return self.flag_fall + super().get_fare()