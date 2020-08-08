# Day 21 - Problem 24

# Challenge
# Write a Python class to convert a roman numeral to an integer.

# Example
"""
Sample input
'MMMCMLXXXVI'
'MMMM'
'C'

Sample output
3986
4000
100
"""


class Conversion:
    """
    Class to handle the conversion of numbers across different numeral system.
    """
    def convert_roman_to_int(self, input):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(input)):
            if (i > 0) and (roman_values[input[i]] > roman_values[input[i - 1]]):
                result += roman_values[input[i]] - 2 * roman_values[input[i - 1]]
            else:
                result += roman_values[input[i]]
        return result


conversion = Conversion()
print(conversion.convert_roman_to_int('MMMCMLXXXVI'))
print(conversion.convert_roman_to_int('MMMM'))
print(conversion.convert_roman_to_int('C'))
