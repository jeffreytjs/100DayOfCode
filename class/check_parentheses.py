# Day 19 - Problem 22

# Challenge
# Write a Python program to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].

# Example
"""
These brackets must be close in the correct order,
Input1: ()
Output1: Valid
Input2: ({[)]
Output2: invalid
Input3: "{{{
Output3: Invalid
"""


class Validity:
    """
    Checks if a string of parentheses are properly matched.
    """
    def check_valid(self, query):
        if len(query) % 2 == 1:
            print("Invalid")
        else:
            pairs = {"(": ")", "{": "}", "[": "]"}
            stack = []
            for bracket in query:
                if bracket in pairs:
                    stack.append(bracket)
                else:
                    if bracket == pairs[stack[-1]]:
                        stack.pop()
                        continue
                    elif (stack) == 0 or bracket != pairs[stack[-1]]:
                        return "Invalid"
            return "Valid"


check = Validity()
print(check.check_valid("({[)])"))  # Invalid
print(check.check_valid("({[]})"))  # Valid
