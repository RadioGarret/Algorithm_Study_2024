# 미로탐색
from collections import deque

n, m = map(int, input().split())
# 한 행의 입력이 공백 없이 입력됨.
# '구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줌.
board = [list(map(int, ' '.join(input().split()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 상하좌우 - x를 행, y를 열로 봤을 때 기준
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft() # 이게 분리가 돼? ㅇㅇ 튜플 언패킹이라고 한대

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx > (n-1) or ny < 0 or ny > (m-1):
            continue

        if board[nx][ny] == 1: # 길이 있음 (또한 이전에 방문 안했다는 뜻이기도 함. 방문했으면 무조건 2이상이니까)
            queue.append((nx, ny))
            board[nx][ny] = board[x][y] + 1 # 이전 배열에 값을 더해주는 이유는 nx, ny 배열에 도달하는 데 이동한 칸을 표현하기 위함

print(board[n-1][m-1])