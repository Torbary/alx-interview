#!/usr/bin/python3
"""pascal_triangle implemtation"""


def pascal_triangle(n):
    """pascal_triangle"""
    if (n <= 0):
        return []

    triangle = []

    for i in range(n):
        row_int = [1]
        if i > 0:
            prev_row = triangle[-1]
            for j in range(1, i):
                row_int.append(prev_row[j - 1] + prev_row[j])

        if i > 0:
            row_int.append(1)
        triangle.append(row_int)
    return triangle
