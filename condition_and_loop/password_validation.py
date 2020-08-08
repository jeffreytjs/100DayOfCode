# Day 18 - Problem 21

# Challenge
# Write a Python program to check the validity of a password (input from users).

# Example
"""
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

Input
W3r@100a
Output
Valid password
"""

import re


def check_password():
    """
    Takes in user input and match password to validation via regex.
    """
    pw = input("Please type in your password: ")
    pw_length = len(pw)
    if (pw_length < 6):
        return "Password should be at least 6 characters."
    elif (pw_length > 16):
        return "Password should be at most 16 characters."
    else:
        has_lowercase = re.findall(r'[a-z]', pw)
        has_uppercase = re.findall(r'[A-Z]', pw)
        has_number = re.findall(r'[0-9]', pw)
        has_special = re.findall(r'[$#@]', pw)
        # Length will be 0 if no matching character is found
        if (len(has_lowercase) == 0) or (len(has_uppercase) == 0) or (len(has_number) == 0) or (len(has_special) == 0):
            return "Password should contain at least 1 number [0-9], 1 lowercase alphabet [a-z], 1 uppercase alphabet [A-Z] and one special character [$@#]" # noqa
        else:
            return "Valid password"


check_password()
