"""
CP1402
guitars
expected: 30mins
actual: 41mins
"""

from prac_06.guitar import Guitar

def main():
    """Guitars program, calls guitar"""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Amazing guitar", 2020, 20000))
    #Call is_vintage function
    if guitars != "":
        print("My guitars!")
        for i, guitar in enumerate(guitars):
            vintage_string = " vintage" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars!, go get some")

main()