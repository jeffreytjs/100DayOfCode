# Day 13 - Problem 16

# Challenge
# Count the number of even and odd numbers from a series of numbers

# Example
# Input
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4
# Number of odd numbers : 5


def count_odd_even(n):
    odd_count = 0
    even_count = 0
    for i in n:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print('Number of even numbers : ' + str(even_count))
    print('Number of odd numbers : ' + str(odd_count))


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd_even(numbers)
