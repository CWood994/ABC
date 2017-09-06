#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    due = (sum(ar) - ar[k]) / 2
    if due == b:
        return "Bon Appetit"
    else:
        return int(ar[k]/2)

n, k = map(int,input().strip().split(' '))
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
