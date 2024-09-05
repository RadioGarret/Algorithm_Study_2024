# 유기농 배추 (실버2)

from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def bfs(i, j, ground):
    q = deque()
    q.append((i, j))
    visited = [[0]*n for _ in range(m)]
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x +dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if ground[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    ground[nx][ny] = 0 # bfs로 방문한 땅을 0으로 초기화 해줌.
                    q.append((nx, ny))
    return ground # bfs 방문하여 땅을 0으로 초기화 해준 ground를 반환

t = int(input())

for t in range(t):
    ans = 0
    m, n, k = map(int, input().split()) # 가로 길이 m, 세로 길이 n

    ground = [[0]*n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        ground[x][y] = 1

    for i in range(m):
        for j in range(n):
            if ground[i][j] == 1:
                ground = bfs(i, j, ground)
                ans += 1

    print(ans)