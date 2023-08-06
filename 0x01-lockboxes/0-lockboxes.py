#!/usr/bin/env python3


from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    n = len(boxes)
    visited = set()
    queue = [0]

    while queue:
        box = queue.pop(0)
        visited.add(box)

        for key in boxes[box]:
            if key not in visited:
                queue.append(key)

    return len(visited) == n
