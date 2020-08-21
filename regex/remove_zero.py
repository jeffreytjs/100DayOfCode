# Day 65 - Problem 72

# Challenge
# Write a Python program to remove leading zeros from an IP address.

# Example
# Input: address = "00216.08.094.196"
# Output: 216.8.94.196


import re


def remove_lead_zero(text):
    # handle leading zeroes without '.'
    text = re.sub('^[0]*', '', text)
    # handle all zeroes behind '.'
    text = re.sub('\.[0]*', '.', text)  # noqa
    return text


address = "00216.08.094.19600"
print(remove_lead_zero(address))
