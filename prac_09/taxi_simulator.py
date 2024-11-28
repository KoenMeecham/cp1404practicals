"""
CP1404
Taxi sim
estimated: 25mins
actual: 29mins
"""

from prac_09.taxi import Taxi
from prac_09.sliver_service_taxi import SliverServiceTaxi

MENU = "(Q)uit, (C)hoose taxi, (D)rive"

def main():
    """
    Taxi simulator
    Each time, until they quit:
    - The user should be able to choose from a list of available taxis,
    - They can choose how far they want to drive,
    - At the end of each trip, show them the trip cost and add it to their bill.
    """
    taxis = [Taxi("Prius", 100), SliverServiceTaxi("Limo", 100, 2), SliverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            display_taxis(taxis)
            current_taxi = taxi_selection(taxis)
        elif choice == "D":
            taxi_drive(current_taxi)
        else:
            print("Invalid choice")
        print(f"Bill: {bill}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: {bill}")
    print("Taxis are now")
    print(taxis)

def display_taxis(taxis):
    """Display the taxis."""
    for i, taxi in enumerate(taxis, 1):
        print(f'{i} - {taxi}')

def taxi_selection(taxis):
    """Select the taxi."""
    taxi_choice = int(input("Choose your taxi: "))
    taxi_choice = taxis[taxi_choice]
    return taxi_choice

def taxi_drive(current_taxi):
    """Drive the taxi."""
    current_taxi.start_fare()
    distance_to_drive = float(input("Enter distance to drive: "))
    current_taxi.drive(distance_to_drive)
    cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
    bill =+ cost
    return current_taxi, bill



if __name__ == '__main__':
    main()