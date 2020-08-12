# Day 38 - Problem 44

# Challenge
# Write a Python program to read a random line from a file.
# Hint: Use test.txt

import random


def read_random(filepath):
    text = open(filepath).read().splitlines()
    line = random.choice(text)
    return(line)


print(read_random('test.txt'))
