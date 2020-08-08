# Day 2 - Problem 3

# Challenge
# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array
# and deleting a random element.
# Given these two arrays, find which element is missing in the second array.

# Examples
# Here is an example input, the first array is shuffled and
# the number 5 is removed to construct the second array.
# Input:
# finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
# Output:
# 5 is the missing number


def missing_element_1(input):
    """
    Only handles the case when one element has been removed
    """
    first, second = input
    for i in first:
        if i not in second:
            return str(i) + " is the missing number"


def missing_element_2(input):
    """
    Extension to return > 1 missing elements
    """
    first, second = input
    missingNo = []
    for i in first:
        if (i not in missingNo) and (i not in second):
            missingNo.append(str(i))
    # Different phrasing for different number of missing number
    if len(missingNo) == 2:
        return ((' and '.join(missingNo)) + " are the missing numbers")
    else:
        return ((', '.join(missingNo)) + " are the missing numbers")


a = [[1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]]
b = [[1, 2, 3, 4, 5, 6, 7], [3, 7, 1, 4, 6]]
print(missing_element_1(a))  # Output: 5 is the missing number
print(missing_element_2(b))  # Output: 2 and 5 are the missing numbers
