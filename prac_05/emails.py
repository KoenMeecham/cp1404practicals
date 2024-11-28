"""Emails Question"""
"""
Expected = 20 mins 
Actual = 25 mins
"""

def main():
    #Create dictionary of emails_to_name
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = determine_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def determine_name_from_email(email):
    #Take the email and ge the name for it
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()