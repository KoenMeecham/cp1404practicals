"""Menu string"""
MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result 
(S)how stars 
(Q)uit"""

def main(grade=None):
    """Enter score and check that it is valid"""
    validate_grade()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            validate_grade()
        elif choice == "P":
            get_result(grade)
        elif choice == "S":
            show_stars(grade)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Bye")

def validate_grade():
    """Check if grade is valid"""
    grade = float(input("Enter grade: "))
    if grade < 0 or grade > 100:
        print("Invalid score. Must be between 0 and 100.")
    else:
        print("Grade is valid")
        return grade

def get_result(grade):
    """Calculate grade score"""
    if grade >= 90:
        print("Excellent score")
    elif grade >= 50:
        print("Pass score")
    else:
        print("Fail score")
    return grade

def show_stars(grade):
    """Print stars"""
    print("* " * int(grade))
main()