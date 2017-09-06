#!/bin/python3

import sys


n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

leaders = [[1, scores[0]]]
rank = 1
for score in scores[1:]:
    if score != leaders[-1][1]:
        rank += 1
    leaders.append([rank, score])
      
position = len(leaders)
rank = leaders[-1][0] if leaders[-1][1] == 0 else leaders[-1][0] + 1

for a_score in alice:
    while position > 0 and a_score >= leaders[position - 1][1]:
        position -= 1
        rank = leaders[position][0]
    print(rank)