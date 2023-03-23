#!/usr/bin/python3
'''
Rotate 2D  Matrix
'''

def rotate_2d_matrix(matrix):
    '''
    function that rotates an n x n 2D matrix 
    at 90 degrees clockwise
    args:
        matrix: array

    Returns:
        return none

    '''

    #rotated_matrix = []
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row of the transposed matrix
    for i in range(n):
        #matrix[i] = matrix[i][::-1]
        matrix[i].reverse()