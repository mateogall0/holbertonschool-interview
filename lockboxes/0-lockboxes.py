#!/usr/bin/python3
"""Module"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes
    in front of you. Each box is numbered
    sequentially from 0 to n - 1 and each
    box may contain keys to the other
    boxes.
    """
    """keys = list(boxes[0])
    change = True
    while(change):
        change = False
        for i in range(1, len(boxes)):
            if i not in keys:
                continue
            for j in boxes[i]:
                if j not in keys:
                    change = True
                    keys.append(j)
    if len(keys) >= len(boxes):
        return True
    return False"""
    n = len(boxes)
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < n:
                keys.append(box)
    return len(keys) == n
