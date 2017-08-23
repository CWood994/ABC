#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

print( str( sum(arr) - max(arr) ) + " " + str( sum(arr) - min(arr) ) )
