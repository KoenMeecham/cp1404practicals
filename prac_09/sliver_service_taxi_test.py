"""
CP1404
Sliver service test
estimated: 10mins
actual: 13mins
"""

from prac_09.sliver_service_taxi import SliverServiceTaxi

def main():
    """Sliver service test"""
    taxi_test = SliverServiceTaxi("Fancy Taxi", 100, 5)
    taxi_test.drive(100)
    print(taxi_test)
    #Should be $6.15
    #Should be $619.5
    print(taxi_test.get_fare())

if __name__ == '__main__':
    main()



