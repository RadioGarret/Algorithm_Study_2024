"""
4 4 1
1 2 10
2 4 10
1 3 1
3 4 100
"""

import sys
sys.stdin = open("/Users/hong/Documents/git/Algorithm_Study_2024/honghak/boj_1162_input.txt", "r")

import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())

graph_dict = {node : {} for node in range(1, N+1)}

for _ in range(M):
    i, j, w = map(int, input().split())
    graph_dict[i][j] = w

queue = deque()
queue.append([0, 1, K])

INF = int(1e+12)
distances = [INF for _ in range(N+1)]
distances[1] = 0

while queue:
    dist, current, remain_k = queue.popleft()

    # if distances[current] < dist:
    #     continue

    for next_node, next_dist in graph_dict[current].items():
        new_dist = dist + next_dist
        if distances[next_node] > new_dist:
            distances[next_node] = new_dist
            queue.append([new_dist, next_node, remain_k])

        if remain_k > 0:
            if distances[next_node] > dist:
                distances[next_node] = dist
                queue.append([dist, next_node, remain_k - 1])

print(distances[N])
