"""
CP1404
myguitars
expected: 20mins
actual: 22mins
"""

import csv
from prac_07.guitar import Guitar


def main():
    """Program for displaying guitars"""
    guitars = load_guitars()
    add_guitars(guitars)
    display_guitars(guitars)
    save_guitars(guitars)


def load_guitars():
    """Load guitars"""
    guitars = []
    with open ("guitars.csv", "r") as in_file:
        csv_reader = csv.reader(in_file)
        for row in csv_reader:
            guitar = Guitar(row[0], int(row[1]), float(row[2]))
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    """Display guitars sorted by year"""
    guitars.sort()
    for guitar in guitars:
        print(guitar)

def add_guitars(guitars):
    """Add guitars to the list from user input."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        name = input("Name: ")
    return guitars

def save_guitars(guitars):
    """Save the guitars to the csv"""
    print("Saving guitars")
    with open ("guitars.csv", "w", newline='') as out_file:
        csv_writer = csv.writer(out_file)
        for guitar in guitars:
            csv_writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == "__main__":
    main()