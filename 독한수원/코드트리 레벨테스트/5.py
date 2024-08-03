from collections import deque
dx, dy = [1,-1,0,0],[0,0,1,-1]


max_val = -1
def bfs(x,y):
    count = 0

    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    count = 0
    while q:
        a, b = q.popleft()
        count += 1
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]  and maps[nx][ny] == 1:
                visited[nx][ny] == 1
                q.append((nx,ny))

    
    
    return count

n = int(input())

maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

visited = [ [False for _ in range(n)] for _ in range(n)  ] 

for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == 1:
            max_val = max(max_val, bfs(i,j))
print(max_val)