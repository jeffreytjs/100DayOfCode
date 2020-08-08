# Day 1 - Problem 1

# Challenge
# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.


def longest_non_repeat(input):
    max_length = 1
    tokenise = list(input)
    for i in range(len(tokenise)):
        subseq = []
        while (i < len(input)) and (tokenise[i] not in subseq):
            subseq.append(tokenise[i])
            i += 1
        if len(subseq) > max_length:
            max_length = len(subseq)
    print(max_length)
    return max_length


longest_non_repeat("abcabcbb")  # Output = 3
longest_non_repeat("bbbbb")  # Output = 1
longest_non_repeat("pwwkew")  # Output = 3
longest_non_repeat("abcdgbacbegsh")  # Output = 7
