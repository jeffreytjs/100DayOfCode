# Day 59 - Problem 65

# Challenge
# Write a Python program to find all five characters long word in a string.

# Example
# Input: my_string = 'The quick brown fox jumps over the lazy dog.'
# Output: ['quick', 'brown', 'jumps']


import re


def regex_five_char(my_string):
    return re.findall('\w{5}', my_string)  # noqa


def n_char_words(my_string, n):
    # list comprehension
    return [word for word in my_string.split(' ') if (len(word) == n)]


my_string = 'The quick brown fox jumps over the lazy dog.'
print(regex_five_char(my_string))
# n = 5
# print(n_char_words(my_string, n))
