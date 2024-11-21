"""
CP1404
Sliver service test
estimated: 10mins
actual:
"""

from prac_09.sliver_service_taxi import SliverServiceTaxi

def main():

    taxi_test = SliverServiceTaxi("Fancy Taxi", 100, 5)
    taxi_test.drive(100)
    print(taxi_test)

if __name__ == '__main__':
    main()



