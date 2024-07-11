import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)


N, M = map(int ,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
cnt = 0

visited = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)
