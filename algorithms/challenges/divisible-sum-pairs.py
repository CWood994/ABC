#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    buckets = [0] * k
    
    for val in ar:
        buckets[val % k] += 1
       
    sum = (buckets[0] * (buckets[0] - 1)) / 2
    
    for i in range(k//2):
        if (i+1) != k-(i+1):
            sum += buckets[i+1] * buckets[k-(i+1)]
        
    if k % 2 == 0:
        sum += (buckets[k//2] * (buckets[k//2] - 1)) / 2
      
    return int(sum)
    
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
