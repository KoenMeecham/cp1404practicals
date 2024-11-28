"""Hex decimal converter"""
"""
Expected = 15 mins
Actual = 14 mins
"""
COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7",
                "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
                "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    #Dictonary method mean wrong key will get none
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()