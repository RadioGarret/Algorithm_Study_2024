import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    queue = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                            queue.append((nx, ny))
                            visited[nx][ny] = 1
                cnt += 1  

    print(cnt)
