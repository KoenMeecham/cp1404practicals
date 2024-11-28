"""Quick picks program"""
import random

NUMBERS_PER_LINE = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    number_of_quick_picks = int(input("How many quick picks?: "))
    #Check the input of quick picks
    while number_of_quick_picks < 0:
        print("Please enter some quick picks")
        number_of_quick_picks = input("How many quick picks?: ")

    for i in range(number_of_quick_picks):
        #Create line of quick picks
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            #Generate each random number, if a new number is the same as an old number
            #Generate a new random number
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))
main()