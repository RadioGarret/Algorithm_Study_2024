n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited_dfs = [ 0 for _ in range(n+1)]
visited_bfs = [ 0 for _ in range(n+1)]
for _ in range(m):
    e1, e2 = map(int, input().split())
    graph[e1][e2] = 1
    graph[e2][e1] = 1

def dfs(v, visited):
    visited[v] = 1
    print(v, end= ' ')
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i, visited)

from collections import deque
queue = deque()
def bfs(v, visited):
    visited[v] = 1
    queue.append(v)
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, n+1):
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1

dfs(v, visited_dfs)
print()
bfs(v, visited_bfs)
