import sys
input = sys.stdin.readline

import itertools

N, M = map(int, input().split())

board = []
home = []
chicken = []
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            home.append((r, c))
        elif row[c] == 2:
            chicken.append((r, c))
    board.append(row)
    
# 집 ~ 각 치킨 집까지의 거리, matrix[집][치킨]
matrix = []
for h in home:
    l = []
    hr, hc = h
    for c in chicken:
        cr, cc = c
        dist = abs(hr - cr) + abs(hc - cc)
        l.append(dist)
    matrix.append(l)

# 살릴 치킨 집 경우의 수 (index)
cand_list = itertools.combinations(list(range(len(chicken))), M)

min_chicken_dist_list = []
for cand in cand_list:
    dist = 0
    for dist_list in matrix:
        dist += min([d for idx, d in enumerate(dist_list) if idx in cand])
    min_chicken_dist_list.append(dist)

print(min(min_chicken_dist_list))