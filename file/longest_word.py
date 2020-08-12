# Day 37 - Problem 43

# Challenge
# Write a python program to find the longest words in a file
# Hint: Use test.txt file within the same folder


def get_longest_words(filepath):
    """
    Keeping in mind that multiple words can have the same length,
    1) Find the length of the longest word using max
    2) Find all words with length equal to the longest word
    """
    with open(filepath, 'r') as infile:
        all_words = infile.read().split()
    first_longest_word = max(all_words, key=len)
    len_of_longest_word = len(first_longest_word)
    return [word for word in all_words if len(word) == len_of_longest_word]


print(get_longest_words('test.txt'))
