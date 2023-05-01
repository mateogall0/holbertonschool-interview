#!/usr/bin/python3
"""
    Log Parsing
"""


import sys


current = {}
fileSize = 0
for i, line in enumerate(sys.stdin):
    lineSplitted = line.split(" ")
    if lineSplitted[7] not in current:
        current[lineSplitted[7]] = 1
    else:
        current[lineSplitted[7]] += 1
    fileSize += int(lineSplitted[8])
    if i != 0 and i % 10 == 0:
        print('File size: {}'.format(fileSize))
        for k in sorted(current.keys()):
            print('{}: {}'.format(k, current[k]))
        current = {}
