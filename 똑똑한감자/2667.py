# 단지번호 붙이기
from collections import deque

N = int(input())
map = [list(map(int, ' '.join(input().split()))) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
complex = 2
arr = []

def bfs(x, y, complex):
    cnt = 1
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if map[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                map[nx][ny] = complex
                cnt += 1
    return cnt

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            arr.append(bfs(i, j, complex))
            complex += 1

arr.sort()
print(len(arr))
for i in range(len(arr)):
    print(arr[i])