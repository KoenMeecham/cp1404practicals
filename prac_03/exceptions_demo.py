"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

is_finished = False

while not is_finished:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        is_finished = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")

#1. When a user inputs a value that is not a integer i.e a string or float

#2.When the user inputs zero as the denominator

#3. Creat a loop that loops until the user inputs a value that is not zero