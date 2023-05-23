#!/usr/bin/python3
"""
UTF-8
"""


def validUTF8(data):
    i = 0
    while i < len(data):
        num = data[i]
        if num < 128:
            i += 1
        elif 128 <= num <= 191:
            return False
        else:
            if num < 224:
                expected_bytes = 2
            elif num < 240:
                expected_bytes = 3
            elif num < 248:
                expected_bytes = 4
            else:
                return False

            for j in range(1, expected_bytes):
                i += 1
                if i >= len(data) or not (128 <= data[i] <= 191):
                    return False
        i += 1

    return True
