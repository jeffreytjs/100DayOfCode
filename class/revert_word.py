# Day 25 - Problem 28

# Challenge
# Write a Python class to reverse a string word by word.
# Example:
# Sample Input: "hello world"
# Sample Output: "world hello"


class Reverse:
    def reverse_order(self, input):
        all_words = input.split(" ")
        all_words.reverse()
        result = ""
        for i in all_words:
            result += i + " "
        return result.strip()


reverse = Reverse()
print(reverse.reverse_order("hello world"))
print(reverse.reverse_order("name is Baby Yoda"))
