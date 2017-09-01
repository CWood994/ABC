#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

map = {}

for i in a:
    try:
        map[i] += 1
    except:
        map[i] = 1
        
my_max = 0
for key in map:
    count = map[key]
    try:
        count1 = map[key-1]
    except:
        count1 = 0
    try: 
        count2 = map[key+1]
    except:
        count2 = 0
    count += max(count1, count2)
    my_max = count if count > my_max else my_max
    
print(my_max)
    