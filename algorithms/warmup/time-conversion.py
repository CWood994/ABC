#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    hours = ( int( s[:2] ) + (12 if s[8:] == "PM" else 0 ) ) % 24
    if hours == 12:
        hours = 0
    elif hours == 0:
        hours = 12
    
    hours = "0" + str(hours) if hours < 10 else str(hours)
    return hours + s[2:8]

s = input().strip()
result = timeConversion(s)
print(result)
