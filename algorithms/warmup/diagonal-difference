#!/bin/python3

import sys

def diagonal_diff(n, a):
    tl_br_sum = 0
    tr_bl_sum = 0
    
    for i in range(n):
        tl_br_sum += a[i][i]
        tr_bl_sum += a[i][n-1-i]
    
    return abs(tl_br_sum - tr_bl_sum)

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
result = diagonal_diff(n, a)
print(result)
