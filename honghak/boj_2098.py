import sys
sys.stdin = open("honghak/boj_2098_input.txt", "r")

import sys
input = sys.stdin.readline

N = int(input())

graph = [[int(x) for x in input().split()] for _ in range(N)]
INF = int(1e+15)

dp = {}

def dfs(current, visited):
    if visited == (1 << N) -1:
        if graph[current][0]:
            return graph[current][0]
        else:
            return INF
        
    if (current, visited) in dp:
        return dp[(current, visited)]
    
    min_cost = INF
    for next_node in range(1, N):
        if graph[current][next_node] == 0 or visited & (1 << next_node):
            continue
        
        cost = dfs(next_node, visited | (1 << next_node)) + graph[current][next_node]
        min_cost = min(cost, min_cost)
        
    dp[(current, visited)] = min_cost
    return min_cost
    
        
print(dfs(0, 1 << 0))