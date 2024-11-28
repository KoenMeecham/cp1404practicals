minimum_length = 4

def main():
    """Get and print password"""
    password = get_password(minimum_length)
    print_asterisks(password)

def get_password():
    """Get password, check for minimum length"""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password

def print_asterisks(password):
    """Print the asterisks"""
    print('*' * len(password))


main()