#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    my_map = {}
    
    for sock in ar:
        try:
            my_map[sock] += 1
        except:
            my_map[sock] = 1
            
    count = 0
    for sock in my_map:
        count += my_map[sock]//2
        
    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
