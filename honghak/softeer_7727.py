"""
4 2
20 26 185 80
100 20 25 80
20 20 88 99
15 32 44 50
1 2
2 3
"""

import sys
sys.stdin = open("honghak/softeer_7727_input.txt", "r")


from itertools import product, permutations, combinations
from collections import deque


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up right down left

N, M = map(int, input().split())

fruit_map = [[int(x) for x in input().split()] for _ in range(N)]

position_dict = {}
for i in range(M):
    i, j = map(int, input().split())
    position_dict[i] = (i-1, j-1)
    

direction_product = list(product(range(4), range(4), range(4)))

trajectories = [[] for _ in range(M+1)]

for k, v in position_dict.items():
    for steps in direction_product:
        x, y = v
        trajectory = []
        for step in steps:
            dx, dy = directions[step]
            if 0 <= x + dx <= N-1 and 0 <= y + dy <= N-1:
                trajectory.append([x + dx, y + dy])
                x = x + dx
                y = y + dy
            else:
                continue
        
        if len(trajectory) == 3:
            trajectories[k].append(trajectory)
            


print()
print()