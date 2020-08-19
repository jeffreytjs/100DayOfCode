# Day 63 - Problem 70

# Challenge
# Write a Python program to remove the parenthesis area in a string.

# Example
# Input: my_list = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# Output:
# example
# w3resource
# github
# stackoverflow


import re


def remove_parenthesis(text):
    """
    Remove anything within the parenthesis and remove whitespaces
    """
    return re.sub(r'\([^)]*\)', '', text).strip()


my_list = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for text in my_list:
    print(remove_parenthesis(text))
