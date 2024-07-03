from collections import deque


def bfs(point):
    sr, sc, cnt = point[0], point[1], point[2]
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    while queue:
        now = queue.popleft()
        cr, cc, cnt = now[0], now[1], now[2]
        if (cr,cc) == (N-1,M-1):
            return cnt
        for d in range(4):
            nr, nc = cr + directions[d][0], cc + directions[d][1]
            if 0<=nr<N and 0<=nc<M:
                if maze[nr][nc] == 1 and not visited[nr][nc]:
                    if (nr,nc,cnt+1) not in queue:
                        queue.append((nr,nc,cnt+1))
                        maze[nr][nc] = 0

# 1 이동가능 0 이동불가
# (1,1) 에서 출발해서 (N,M) 으로 이동할 때 지나야 하는 최소의 칸 수 구하기
# (0,0) 에서 출발해서 (N-1,M-1로 가기)
# N 세로(행) M 가로(열)
N,M = list(map(int, input().split()))
maze = []
for i in range(N):
    maze.append(list(map(int, input())))
# bfs 로 탐색
visited = [[0]*M for _ in range(N)]
queue = deque()
# visited 에서 갈 수 없는 곳 표시하기
for r in range(N):
    for c in range(M):
        if maze[r][c] == 0 :
            visited[r][c] = -1
queue.append((0,0,1))
result = bfs((0,0,1))
print(result)