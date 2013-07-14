#!/usr/bin/env python
'''
Turn Matrix

Input: 3x3 matrix of integers

Output: Rotate the matrix by 90 degrees and return rotated matrix

Example:

1 2 3
4 5 6 
7 8 9

Switch to:

7 4 1
8 5 2
9 6 3

'''


#Set data structure as a list of coordinates
def flip_matrix(mat):
    mid = int(len(matrix/6))
    for i, coord in enumerate(matrix):
        if i == 0:
            pass
        # if x is 1 then it just flips x & y
        elif mid == coord[0]:
            coord[0], coord[1] = coord[1], coord[0]
        # if x is less than 1 then x becomes y and y becomes 2
        elif mid > coord[1]:
            coord[0] = coord[1]
            coord[1] = mid + 1
        # if x is greater than 1 then x becomes y and y becomes 1
        elif mid < coord[0]:
            coord[0] = coord[1]
            coord[1] = mid - 1


#Improved approach is new[x,y] = old [y,2-x]

"""
Input: Given an NxN matrix

Output: Rotate the matrix by 90 degrees and return rotated matrix.

Example:
    input: 
           [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
    output:
           [[13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]]

Note: claudiay contributed additional example and test
"""

# Short without zip
def rotate(matrix):
    return [[j[i] for j in matrix][::-1] for i in range(len(matrix))]

# Python trick answer, returns an array with tuples
def rotate_with_zip(matrix):
    return zip(*matrix[::-1])

# A expanded version to explain each step
def rotate_explain(matrix):
    n = len(matrix)
    new_matrix = []

    for i in range(n):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row[::-1]) # Reverse new_row before appending.
    
    return new_matrix

# Rotate the matrix in place, without creating another matrix
# Ideal for situations processing a large matrix with limited space
def rotate_in_place(matrix):
    n = len(matrix)
    for i in range(n/2):
        for j in range(n/2 + n%2):
            swap = matrix[i][j]
            for k in range(4):
                swap, matrix[j][n-i-1] = matrix[j][n-i-1], swap
                i, j = j, n - i - 1
    
    return matrix


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    
    odd_matrix = [[0, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9],
                  [10, 11, 12, 13, 14],
                  [15, 16, 17, 18, 19],
                  [20, 21, 22, 23, 24]]

    #Test section
    print rotate(matrix)
    print rotate_with_zip(matrix)
    print rotate_explain(matrix)
    print rotate_in_place(matrix)


    print rotate(odd_matrix)
    print rotate_with_zip(odd_matrix)
    print rotate_explain(odd_matrix)
    print rotate_in_place(odd_matrix)

