#!/usr/bin/python3
"""module for 5-island_perimeter"""


def island_perimeter(grid):
    """
    Computes the perimeter of the island described in the given grid

    Args:
        grid (List[List[int]]): The rectangular grid of 0's and
        1's representing the island.

    Returns:
        int: The perimeter of the island

    Raises:
        ValueError: if the grid is empty
    """

    if not grid:
        raise ValueError("Grid must not be empty")

    perimeter = 0
    height = len(grid)
    width = len(grid[0])

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                """if this is a land cell"""
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
