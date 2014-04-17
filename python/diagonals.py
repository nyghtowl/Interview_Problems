'''
Matrix diagonals

Input: Matrix / List of Lists 
Output: Print diagonals

Input Example:

[[1, 2, 8],
 [-4, 5, 2],
 [0, -4, -6],
 [-3, 3, 9]]

Output Example:
8
2 2
1 5 -6
-4 -4 9
0 3
-3


NumPy solution initially from: http://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
'''


# List of lists solution

def diag(size):
    return [(i, i) for i in range(size)]

def is_in_matrix(matrix, pair):
    return 0 <= pair[0] < matrix[0] and 0 <= pair[1] < matrix[1]

def transpose(ray, amount):
    return [(x-amount, y) for (x,y) in ray]

def diagonals(h, w):
    for offset in reversed(range(-w, h-1)):
        diagonal = [p for p in transpose(diag(6), offset) if is_in_matrix([h, w], p)]
        if diagonal:
            print diagonal


# NumPy Solution
import numpy as np

matrix = np.array(
         [[-2,  5,  3,  2],
          [ 9, -6,  5,  1],
          [ 3,  2,  7,  3],
          [-1,  8, -4,  8]])

diags = [matrix[::-1,:].diagonal(i) for i in range(-3,4)]
diags.extend(matrix.diagonal(i) for i in range(3,-4,-1))
print [n.tolist() for n in diags]

import numpy as np

# Alter dimensions as needed
x,y = 3,4

# create a default array of specified dimensions
a = np.arange(x*y).reshape(x,y)
print a
print

# a.diagonal returns the top-left-to-lower-right diagonal "i"
# according to this diagram:
#
#  0  1  2  3  4 ...
# -1  0  1  2  3
# -2 -1  0  1  2
# -3 -2 -1  0  1
#  :
#
# You wanted lower-left-to-upper-right and upper-left-to-lower-right diagonals.
#
# The syntax a[slice,slice] returns a new array with elements from the sliced ranges,
# where "slice" is Python's [start[:stop[:step]] format.

# "::-1" returns the rows in reverse. ":" returns the columns as is,
# effectively vertically mirroring the original array so the wanted diagonals are
# lower-right-to-uppper-left.
#
# Then a list comprehension is used to collect all the diagonals.  The range
# is -x+1 to y (exclusive of y), so for a matrix like the example above
# (x,y) = (4,5) = -3 to 4.
diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]

# Now back to the original array to get the upper-left-to-lower-right diagonals,
# starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

# Another list comp to convert back to Python lists from numpy arrays,
# so it prints what you requested.
print [n.tolist() for n in diags]