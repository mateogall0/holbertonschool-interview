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
    for i in range(len(boxes)):
        if len(boxes[i]) == 0:
            break
    else:
        return True
    while(i < len(boxes)):
        if len(boxes[i]) != 0:
            return False
        i += 1
    return True
