# Day 36 - Problem 42

# Challenge
# Write a Python program to read first n lines of a file.
# Hint: Use test.txt file


def get_first_n_lines(filepath, n):
    with open(filepath, 'r') as infile:
        text = [next(infile) for x in range(n)]
    print(text)


get_first_n_lines('test.txt', 3)
