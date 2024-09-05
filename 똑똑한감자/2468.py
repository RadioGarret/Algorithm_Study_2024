"""
[백준] 안전영역

안전영역: 물에 잠기지 않는 지점들이 상하좌우로 인접해 있으며 그 크기가 최대인 영역의 '개수'
개수가 아니라 영역의 크기인줄 알고 헤맸음.
"""
from collections import deque
import copy

N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]

# 서-남-동-북
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

highest = max(max(row) for row in land)

cnt_arr = []

def bfs(x, y, land, visited):
    queue = deque()
    queue.append((x,y))
    # queue = deque([(x,y)])와 동일
    # deque의 생성자에게 전달되는 인자가 반복 가능(iterable)해야 하기 때문에 deque((x,y))는 불가. 리스트로 한번 감싸줘야 함.
    visited[x][y] = 1

    while queue:
        v = queue.popleft()

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue

            if not visited[nx][ny] and land[nx][ny] != 0:  # 방문하지 않고, 잠기지 않은 곳이라면
                queue.append((nx, ny))
                visited[nx][ny] = 1

# 물의 높이를 0부터 highest까지 검사
for h in range(0, highest + 1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]

    # land를 복사하여 tmp_land를 생성
    tmp_land = copy.deepcopy(land)

    for i in range(N):
        for j in range(N):
            if tmp_land[i][j] <= h:  # 물의 높이(h)가 땅의 높이(tmp_land[i][j])보다 크거나 같다면
                tmp_land[i][j] = 0  # 0으로 물에 잠김을 표시

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and tmp_land[i][j] != 0:
                bfs(i, j, tmp_land, visited)
                cnt += 1 # bfs가 종료될 때, 즉 잠기지 않은 영역 탐색이 끝났을 때 cnt를 증가

    cnt_arr.append(cnt)

print(max(cnt_arr))