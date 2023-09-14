#!/usr/bin/python3
"""Rotate 2D Matirx
"""


def rotate_2d_matrix(matrix):
    """rotate 2D Matrix
    """
    left = 0
    right = len(matrix) - 1
    while left < right:
        matrix[left], matrix[right] = matrix[right], matrix[left]
        left = left + 1
        right = right - 1
    # transpose
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
