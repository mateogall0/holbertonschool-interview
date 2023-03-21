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
    keys = list(boxes[0])
    change = True
    while(change):
        change = False
        for i in range(1, len(boxes[1:])):
            if (i not in keys):
                continue
            for j in boxes[i]:
                if j not in keys:
                    change = True
                    keys.append(j)
    if len(keys) >= len(boxes) - 1:
        return True
    return False
