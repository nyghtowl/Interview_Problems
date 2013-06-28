#!/usr/bin/env python
"""
Given an NxN matrix, rotate the matrix by 90 degrees and return rotated matrix.
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
"""


def rotate(matrix):
    # Short without zip.
    return [[j[i] for j in matrix][::-1] for i in range(len(matrix))]


def rotate_with_zip(matrix):
    # Python trick answer, returns an array with tuples. 
    return zip(*matrix[::-1])


def rotate_explain(matrix):
    # A expanded version to explain each step.
    n = len(matrix)
    new_matrix = []

    for i in range(n):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row[::-1]) # Reverse new_row before appending.
    
    return new_matrix


def rotate_in_place(matrix):
    # Rotate the matrix in place, without creating another matrix.
    # Ideal for situations processing a large matrix with limited space.
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

    print rotate(matrix)
    print rotate_with_zip(matrix)
    print rotate_explain(matrix)
    print rotate_in_place(matrix)

    # Test odd matrix.
    print rotate(odd_matrix)
    print rotate_with_zip(odd_matrix)
    print rotate_explain(odd_matrix)
    print rotate_in_place(odd_matrix)

