"""
CP1404
unreliable car
estimated: 10mins
actual:
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test the car"""
    car_01 = UnreliableCar("Car 1", 100, 2)
    car_02 = UnreliableCar("Car 2", 100, 99)

    car_01.drive(100)
    car_02.drive(100)

    print(car_01)
    print(car_02)

if __name__ == "__main__":
    main()