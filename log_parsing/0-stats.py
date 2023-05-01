#!/usr/bin/python3
"""
    Log Parsing
"""


import sys


current = {}
fileSize = 0
i = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

for line in sys.stdin:
    lineSplitted = line.split(" ")
    if len(lineSplitted) < 9:
        continue
    try:
        code = int(lineSplitted[7])
    except ValueError:
        continue
    if code not in status_codes:
        continue
    if code not in current:
        current[code] = 1
    else:
        current[code] += 1
    fileSize += int(lineSplitted[8])
    i += 1
    if i % 10 == 0:
        print("File size: {}".format(fileSize))
        for code in sorted(current.keys()):
            print("{}: {}".format(code, current[code]))

print("File size: {}".format(fileSize))
for code in sorted(current.keys()):
    print("{}: {}".format(code, current[code]))
