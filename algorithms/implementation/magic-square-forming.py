#!/bin/python3

import sys

class Magic(object):

    pre = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    def solve(self, s):
        costs = []
        for solution in self.pre:
            cost = 0
            for sol_row, s_row in zip(solution, s):
                for i, j in zip(sol_row, s_row):
                    if not i == j:
                        cost += abs(i-j)
            costs.append(cost)
        return min(costs)

s = []
for s_i in range(3):
   s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
   s.append(s_t)
   m = Magic()
print(m.solve(s))
