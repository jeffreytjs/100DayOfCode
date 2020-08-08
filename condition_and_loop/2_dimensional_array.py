# Day 8 - Problem 11

# Challenge
# Write a Python program which takes two digits m (row) and n (column) as input
# and generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Examples
# Input
# Input number of rows: 3
# Input number of columns: 4
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]


def make_2d_array(m, n):
    """
    Constructs a 2d-array where the element value in the i-th row and
    j-th column of the array is i*j.

    :params
    * m : int, no. of rows
    * n : int, no. of columns
    """
    result = []
    for i in range(m):
        inner = []
        for j in range(n):
            inner.append(i * j)
        result.append(inner)
    return(result)


row = 3
col = 4
make_2d_array(row, col)
