# Day 22 - Problem 25

# Challenge
# Write a Python class to convert an integer to a roman numeral.

# Examples
"""
Sample input
1
4000
Sample output
I
MMMM
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

    def convert_int_to_roman(self, input):
        """
        Reference from https://leetcode.com/problems/integer-to-roman/
        """
        int_val = [1000, 500, 100, 50, 10, 5, 1]
        symbols = ["M", "D", "C", "L", "X", "V", "I"]
        result = ''
        i = 0
        while (input > 0):
            for j in range(input // int_val[i]):
                result += symbols[i]
                input -= int_val[i]
            i += 1
        return result


conversion = Conversion()
print(conversion.convert_int_to_roman(1))
print(conversion.convert_int_to_roman(4000))
