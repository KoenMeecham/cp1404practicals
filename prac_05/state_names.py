"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
"""
Expected = 10 mins
Actual = 8 mins
"""
# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD":"Queensland", "NSW": "New South Wales", "NT" : "Northern Territory", "WA" : "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name:}")
state = input("Enter short state: ").upper()
#while state != "":
    #if state in CODE_TO_NAME:
        #print(state, "is", CODE_TO_NAME[state])
    #else:
        #print("Invalid short state")
    #state = input("Enter short state: ").upper()
while state != "":
    try:
        print(state, "is", CODE_TO_NAME[state])
    except KeyError:
        print("Invalid short state")
    state = input("Enter short state: ").upper()