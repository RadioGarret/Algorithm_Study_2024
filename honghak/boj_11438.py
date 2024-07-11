import sys
sys.stdin = open("honghak/boj_11437_input.txt", "r")

import sys
input = sys.stdin.readline

from collections import deque
from math import log2

N = int(input())

tree_dict = {node : [] for node in range(N+1)}
parent_dict = {node : -1 for node in range(N+1)}
depth_dict = {node : 0 for node in range(N+1)}
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    # parent, child = min(a, b), max(a, b)
    tree_dict[a].append(b)
    tree_dict[b].append(a)
    
queue = deque()
queue.append([1, tree_dict[1], 1]) # parent, childs, depth
depth_dict[1] = 1

while queue:
    parent, childs, depth = queue.popleft()
    visited[parent] = 1
    
    for child in childs:
        if not visited[child]:        
            parent_dict[child] = parent #[child, parent] + parent_dict[parent]
            depth_dict[child] = depth+1
            queue.append([child, tree_dict[child], depth+1])
            
            
logN = int(log2(N) + 1)
dp = [[0 for _ in range(logN)] for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = parent_dict[i]
    
for j in range(1, logN):
    for i in range(1, N + 1):
        dp[i][j] = dp[dp[i][j - 1]][j - 1]

K = int(sys.stdin.readline())
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    if depth_dict[a] > depth_dict[b]:
        a, b = b, a
    diff = depth_dict[b] - depth_dict[a]
    for i in range(logN):
        if diff & 1 << i:
            b = dp[b][i]
            
    if a == b:
        print(a)
        continue
    
    for i in range(logN - 1, -1, -1):
        if dp[a][i] != dp[b][i]:
            a = dp[a][i]
            b = dp[b][i]
    print(dp[b][0])