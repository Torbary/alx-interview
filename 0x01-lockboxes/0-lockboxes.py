#!/usr/bin/env python3
"""interview question"""


def canUnlockAll(boxes):
    """"""
    n = len(boxes)
    visited = [False] * n
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited[current_box] = True

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                stack.append(key)

    return all(visited)
