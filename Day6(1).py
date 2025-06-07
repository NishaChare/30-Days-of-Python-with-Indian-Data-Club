#  Using list comprehension with join()

import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

print("Secure password:", generate_password())  # e.g., "x7gA2fZq"