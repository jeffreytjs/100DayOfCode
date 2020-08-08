# Day 1 - Problem 2

# Challenge
# Given a collection of intervals which are already sorted by start number,
# merge all overlapping intervals.

# Examples
# Given [[1, 3], [2, 6], [5, 10], [11, 16], [15, 18], [19, 22]],
# return [[1, 10], [11, 18], [19, 22]]


def merge_overlap(input):
    merged = [input[0]]
    for current in input:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    print(merged)


a = [[1, 3], [2, 6], [5, 10], [11, 16], [15, 18], [19, 22]]
merge_overlap(a)  # Output: [[1, 10], [11, 18], [19, 22]]
