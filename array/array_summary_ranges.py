# Day 5 - Problem 8

# Challenge
# Given a sorted integer array without duplicates,
# return the summary of its ranges.

# Examples
# For example, given [0, 1, 2, 4, 5, 7], return ["0->2", "4->5", "7"].


def summarise(input):
    newList = []
    i = 0
    count = 0
    string = ""
    while i <= len(input):
        if count == 0:
            string += str(input[i])
            count += 1
        elif i == len(input):
            newList.append(string)
        elif(input[i + 1] - input[i] != 1):
            count = 0
            string = string + "->" + str(input[i])
            newList.append(string)
            string = ""
        i += 1
    print(newList)


a = [0, 1, 2, 4, 5, 7]
summarise(a)
