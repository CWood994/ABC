#!/bin/python3

import sys

def percents(n, arr):
    # pos, neg, zero
    counts = [0,0,0]

    for el in arr:
        if el > 0:
            counts[0] += 1
        elif el < 0:
            counts[1] += 1
        else:
            counts[2] += 1
    
    result = ""
    for el in counts:
        result += str(el / n) + "\n"
        
    return result
    
    
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

result = percents(n, arr)
print(result)
