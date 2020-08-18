# Day 61 - Problem 68

# Challenge
# Write a Python program to find urls in a string.

# Example
# Input: '<p>Contents :</p><a href="https://www.w3schools.com/html/">Python Examples</a><a href="http://github.com">Even More Examples</a>'  # noqa
# Output: Urls:  ['https://w3resource.com/html/', 'http://github.com']


import re


def find_urls(text):
    pattern = '(http|ftp|https)(:\/\/)([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'  # noqa
    url_parts = re.findall(pattern, text)
    url_full = [''.join(url) for url in url_parts]
    return 'Urls: ' + str(url_full)


text = '<p>Contents :</p><a href="https://www.w3schools.com/html/">Python Examples</a><a href="http://github.com">Even More Examples</a>'  # noqa
print(find_urls(text))
