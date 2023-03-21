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
    n = len(boxes)
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < n:
                keys.append(box)
    return len(keys) == n
