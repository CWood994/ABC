#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    max = min = s[0]
    max_c = 0
    min_c = 0
    for score in s:
        if score < max:
            max = score
            max_c += 1
        elif score > min:
            min = score
            min_c += 1
    return [min_c, max_c]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
