import string
import random
# Define character sets for password generation
letters = string.ascii_letters  # All uppercase and lowercase letters (A-Z, a-z)
digits = string.digits          # All digit characters (0-9)
symbols = string.punctuation    # All punctuation/symbol characters (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
# STEP 1: Ensure at least one character from each required category
# Create a list containing:
#   - 1 random letter
#   - 1 random digit
#   - 1 random symbol
mandatory = [
    random.choice(letters),  # Random letter
    random.choice(digits),   # Random digit
    random.choice(symbols)   # Random symbol
]
# STEP 2: Generate remaining characters
# - Combine all character sets (letters + digits + symbols)
# - Randomly select 5 additional characters from the combined pool
# - The 'k=5' parameter specifies we want 5 characters
others = random.choices(letters + digits + symbols, k=5)
# STEP 3: Combine mandatory and additional characters
# This creates an 8-character list (3 mandatory + 5 others)
password_list = mandatory + others
# STEP 4: Shuffle to randomize character positions
# This ensures mandatory characters aren't clustered at the start
random.shuffle(password_list)
# STEP 5: Convert list to string and print
# Join characters into a single string with no separators
password = ''.join(password_list)

print("Generated Password:", ''.join(password))
