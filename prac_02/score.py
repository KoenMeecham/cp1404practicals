"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """Enter score and run score calculation function"""
    score = float(input("Enter score: "))
    print(get_score(score))

def get_score(score):
    """Calculate score"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent score")
    elif score >= 50:
        print("Pass score")
    else:
        print("Fail score")

main()