#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    store = [0 for i in range(m)]
    count = 0
    
    for n_i in range(n):
        store[1:] = [x + s[n_i] for x in store[:-1]]
        store[0] = s[n_i]
        
        if n_i>=m-1 and store[m-1] == d:
            count += 1
    
    return count
        

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
