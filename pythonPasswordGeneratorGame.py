# Create a password generator that will generate a password of a certain length and complexity
# The password should contain at least one uppercase letter, one lowercase letter, tree number and tree special character


import random
import string


def password_generator(length):
    """
    This function will generate a password of a certain length and complexity
    The password should contain at least one uppercase letter, one lowercase letter, tree number and tree special character
    """
    # Create a list of all the characters that can be used in the password
    password_list = []
    for i in range(0, length):
        password_list.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
    # Shuffle the list of characters
    random.shuffle(password_list)
    # Join the list of characters into a string
    password = "".join(password_list)
    # Return the password
    return password


def main():
    """
    This function will call the password_generator function and print the password
    """
    # Get the length of the password from the user
    length = int(input("How long do you want your password to be? "))
    # Call the password_generator function and print the password
    print(password_generator(length))


if __name__ == "__main__":
    main()  