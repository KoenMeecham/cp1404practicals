minimum_length = 4


def version_1():
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        password = input(f"Enter password of at least {minimum_length} characters: ")

    print('*' * len(password))


version_1()