from collections import deque

def bfs():
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        cr, cc, days = queue.popleft()
        for d in range(4):
            nr, nc = cr + directions[d][0], cc + directions[d][1]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0xfffff:
                board[nr][nc] = days + 1
                queue.append((nr, nc, days + 1))

# 입력 받기
M, N = list(map(int, input().split()))  # M 가로 N 세로
box = []
for i in range(N):
    box.append(list(map(int, input().split())))

# 익는데 걸리는 날짜 표시할 리스트
board = [[0] * M for _ in range(N)]

# 익은 토마토 있는 곳 표시 (= bfs 시작점)
queue = deque()

# 토마토 넣기
for r in range(N):
    for c in range(M):
        if box[r][c] == 0:  # 익힐 토마토는 0xfffff 으로 초기화
            board[r][c] = 0xfffff
        elif box[r][c] == -1:  # 토마토 없으면 -1 로 표시
            board[r][c] = -1
        elif box[r][c] == 1:  # 토마토가 익어 있으면 0으로 초기화 (bfs 시작점)
            board[r][c] = 0
            queue.append((r, c, 0))

# 토마토 익히기
bfs()

# 토마토 모두 익힌 후에 0xfffff 이 있을 경우 익힐 수 없으므로 -1 출력
isImpossible = False
for r in range(N):
    for c in range(M):
        if board[r][c] == 0xfffff:
            isImpossible = True

# 토마토 모두 익혔으므로 최댓값을 출력하기
max_v = 0
if isImpossible:
    print(-1)
else:
    for r in range(N):
        for c in range(M):
            if board[r][c] > max_v:
                max_v = board[r][c]
    print(max_v)
