#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    keyboards.sort(reverse = True)
    drives.sort()
     
    max = -1
    d = 0
    for k in range(len(keyboards)):
        spent = keyboards[k] + drives[d]
        if spent > max and spent <= s:
            max = spent
        while  d < len(drives)-1 and spent <= s:
            d += 1
            spent = keyboards[k] + drives[d]
            if spent > max and spent <= s:
                max = spent
        
    return max
        

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
