from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def bfs1(x, y):
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    
    q = deque()
    q.append((x,y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n-1][m-1]

cnt = [[0] * m for _ in range(n)]

def bfs2(x, y):
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    
    q = deque()
    q.append((x,y))
    cnt[0][0] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < m and cnt[nx][ny] == 0 and graph[nx][ny] == 1:
                q.append((nx, ny))
                cnt[nx][ny] = cnt[x][y] + 1
                
    return cnt[n-1][m-1]

print(bfs1(0, 0))
print(bfs2(0, 0))
