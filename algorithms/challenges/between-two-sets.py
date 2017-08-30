#!/bin/python3

import sys
from functools import reduce

def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd(args):
    return reduce(_gcd, args)

def _lcm(a, b):
    return a * b // _gcd(a, b)

def lcm(args):
    return reduce(_lcm, args)

def getTotalX(a, b):
    # Complete this function
    
    return sum(1 for x in range(lcm(a),gcd(b)+1,lcm(a)) if gcd(b)%x==0)
    

if __name__ == "__main__":
    n, m = map(int,input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
