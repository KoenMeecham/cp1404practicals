"""
CP1404
Taxi test
estimated: 8mins
actual: 6mins
"""

from prac_09.taxi import Taxi

def main():
    """Test taxi"""
    taxi_test = Taxi("Prius 1", 100)
    taxi_test.drive(40)
    print(taxi_test, taxi_test.get_fare())
    taxi_test.start_fare()
    taxi_test.drive(100)
    print(taxi_test, taxi_test.get_fare())


main()