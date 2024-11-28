"""
CP1402
guitar test
expected: 30mins
actual:41mins
"""
from prac_06.guitar import Guitar
def run_tests():
    """Tests for Guitar"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Amazing Guitar", 2020, 20000)

    print(f"{guitar.name} get_age() - Expected {95}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {4}. Got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")

if __name__ == "__main__":
    run_tests()