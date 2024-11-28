menu_title = "(H)ell0/n(G)oodbye/n(Q)uit"
name = input("What is your name? ")
print(menu_title)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("hello", name)
    elif choice == "G":
        print("goodbye", name)
    else:
        print("invalid input")
    print(menu_title)
    choice = input(">>> ").upper()
print("Done")