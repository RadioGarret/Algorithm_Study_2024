# 백준 14502

import sys
input = sys.stdin.readline

import itertools
from collections import deque

import copy

N, M = map(int, input().split())

board = []
empty = []
virus = []
for n in range(N):
    line = list(map(int, input().split()))
    for m in range(M):
        if line[m] == 0:
            empty.append((n, m))
        elif line[m] == 2:
            virus.append((n, m))
    board.append(line)

max_count = 0
eC3 = itertools.combinations(empty, 3)

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for new_walls in eC3:
    new_board = copy.deepcopy(board)
    for idx in new_walls:
        new_board[idx[0]][idx[1]] = 1
    visited = [[False] * M for _ in range(N)]
    
    for n, m in virus:
        visited[n][m] = True
    q = deque(virus)
    while q:
        cn, cm = q.popleft()
        for dn, dm in move:
            nn, nm = cn + dn, cm + dm
            if nn < 0 or nn >= N or nm < 0 or nm >= M:
                continue
            if visited[nn][nm]:
                continue
            if new_board[nn][nm] == 1:
                continue
            visited[nn][nm] = True
            q.append((nn, nm))
    
    count = sum([row.count(0) for row in visited])
    wall_count = sum([row.count(1) for row in new_board])
    count -= wall_count
    if max_count < count:
        max_count = count
        
print(max_count)
