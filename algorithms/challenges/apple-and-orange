#!/bin/python3

import sys

def calculate(house_s, house_t, apple_tree, orange_tree, apples, oranges):
    hits=[0, 0] #apple, orange
    for apple in apples:
        landing_spot = apple + apple_tree
        if landing_spot >= house_s and landing_spot <= house_t:
            hits[0] += 1
            
    for orange in oranges:
        landing_spot = orange + orange_tree
        if landing_spot >= house_s and landing_spot <= house_t:
            hits[1] += 1
            
    return hits

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

hits = calculate(s,t,a,b,apple,orange)

print(str(hits[0]))
print(str(hits[1]))
