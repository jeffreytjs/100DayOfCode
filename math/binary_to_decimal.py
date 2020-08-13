# Day 49 - Problem 55

# Challenge
# Write a Python program to convert a binary number to decimal number.

# Example
# Input = 10010
# Output = 18


def bin2dec(input):
    """
    Convert input into a list and reverse it so we can
    work through each position
    """
    result = 0
    binary = list(str(input))[::-1]
    expo = 0
    for i in binary:
        if i == '1':
            result += 2 ** expo
        expo += 1
    return result


input = 10010
print(bin2dec(input))  # 18
