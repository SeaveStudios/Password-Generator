import random
import string

def generate_password(length: int) -> str:
    # Get all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Shuffle the characters to get a more random password
    characters = ''.join(random.sample(characters, len(characters)))
    # Select a subset of the characters to use as the password
    password = ''.join(random.sample(characters, length))
    return password

# Generate a password with 16 characters
password = generate_password(16)
print(password)
