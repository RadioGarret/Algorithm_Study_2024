from collections import deque


def bfs(sr, sc, depth, board, visited):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([(sr, sc)])
    visited[sr][sc] = True

    while queue:
        cr, cc = queue.popleft()
        for d in directions:
            nr, nc = cr + d[0], cc + d[1]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] > depth:
                visited[nr][nc] = True
                queue.append((nr, nc))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 가능한 최대 높이를 구합니다.
max_height = max(max(row) for row in board)

max_safe_areas = 0

for depth in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for r in range(N):
        for c in range(N):
            if board[r][c] > depth and not visited[r][c]:
                bfs(r, c, depth, board, visited)
                cnt += 1

    max_safe_areas = max(max_safe_areas, cnt)

print(max_safe_areas)
