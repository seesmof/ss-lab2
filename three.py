import secrets
import string

# Define the character set for the password
char_set = string.ascii_letters + string.digits + string.punctuation

# Generate a password with 16 characters
password = ''.join(secrets.choice(char_set) for i in range(16))

# Save the password to a file called "password.txt"
with open("password.txt", "w") as f:
    f.write(password)

# Print a message to the console
print("Your password has been saved to password.txt.")
