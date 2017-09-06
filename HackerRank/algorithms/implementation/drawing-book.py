#!/bin/python3

import sys

def solve(n, p):
    # Complete this function
    back = (n-(p-1))//2 if n%2==0 else (n-p)//2
    return min((p//2), back )

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
