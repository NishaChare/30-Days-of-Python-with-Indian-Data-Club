# Import the regular expression module
import re

# Define a regex pattern to validate email addresses
# This pattern checks for:
# - Alphanumeric characters, dots, underscores, percent signs, plus or minus signs before @
# - A domain name with at least one dot
# - A top-level domain with at least 2 characters
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Function to validate an email using the regex pattern
def validate_gmail(email):
    # re.match() checks if the email matches the pattern from the start
    if re.match(pattern, email):
        return "valid gmail address"
    else:
        return "invalid gmail address"

# List of sample email addresses to test
emails = ["nisha@gmail.com", "chare@gmail", "123.com@gmail", "abcd@gmail.com"]

# Loop through each email and validate it
for e in emails:
    print(f"{e}: {validate_gmail(e)}")
