"""
CP1404
myguitars
expected: 20mins
actual:
"""

import csv
from prac_07.guitar import Guitar


def main():
    """Program for displaying guitars"""
    guitars = load_guitars()
    display_guitars(guitars)


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


def save_guitars(guitars):
    """Save the guitars to the csv"""
    print("Saving guitars")
    with open ("guitars.csv", "w") as outfile:
        csv_writer = csv.writer(outfile)
        for row in guitars:
            csv_writer.writerow(row)

if __name__ == "__main__":
    main()