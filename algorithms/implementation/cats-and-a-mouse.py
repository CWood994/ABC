#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    result = "Cat A" if abs(z-x) < abs(z-y) else "Mouse C" if abs(z-x) == abs(z-y) else "Cat B"
    print(result)
    

