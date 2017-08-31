#!/bin/python3

import sys

def solve(grades):
    # Complete this function
     for i in range(len(grades)):
            if grades[i] > 37:
                f_digit = int(grades[i] / 10)
                l_digit = grades[i] % 10
                if l_digit > 2 and l_digit < 5:
                    grades[i]= (f_digit * 10) + 5
                elif l_digit > 7:
                    grades[i]= ( ( f_digit + 1 ) * 10)
                    
     return grades
                    

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


