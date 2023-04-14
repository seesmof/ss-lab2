import random
import string


def generate_password(length, complexity):
    """Generate a random password with given length and complexity"""
    # define character sets based on complexity
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # select character sets based on complexity
    if complexity == "weak":
        char_set = letters
    elif complexity == "medium":
        char_set = letters + digits
    elif complexity == "strong":
        char_set = letters + digits + symbols
    else:
        raise ValueError("Invalid complexity level")

    # generate password using selected character set
    password = "".join(random.choice(char_set) for i in range(length))
    return password


# prompt user for password length and complexity
length = int(input("Enter password length: "))
complexity = input("Enter password complexity (weak/medium/strong): ")

# generate password and print it to the console
password = generate_password(length, complexity)
print("Your password is: {}".format(password))
