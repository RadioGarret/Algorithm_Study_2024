'''
[백준 - 삼성 SW 역량 테스트 기출 문제]
로봇 청소기
골드5

계속해서 현재 위치 주변 4칸을 탐색하면서 움직임.
출력: 작동을 멈출 때까지 청소한 칸의 개수
'''
def clean(r, c, d):
    global board, clean_cnt, dir
    # 현재 위치 청소
    if board[r][c] == 0:
        board[r][c] = 2 # 청소 표시: 칸에 2를 넣어서 표현
        clean_cnt += 1 # 청소한 칸의 개수 증가

    # 4 방향 검사 for _ in range(4)
    for _ in range(4):
        d = (d + 3) % 4 # 반시계 방향으로 90도 회전
        nr, nc = r + dir[d][0], c + dir[d][1]
        if board[nr][nc] == 0: # 청소되지 않은 빈 칸이 있는 경우
            clean(nr, nc, d) # 그 방향으로 이동하여 청소
            return # 여기서 return을 하는구나

    # 4 방향 모두 청소가 되어 있거나 벽인 경우 후진
    nd = (d + 2) % 4
    nr, nc = r + dir[nd][0], c + dir[nd][1]
    if board[nr][nc] != 1: # 후진할 위치가 벽이 아니면
        clean(nr, nc, d) # 후진하여 청소 계속. 이때 nd를 넘겨주는 것이 아니라 d를 넘겨야 함.
        return # 후진할 위치가 벽이면 작동 멈춤 (함수 종료)

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # (r, c)는 r번째 줄에 c번째 칸
board = list(list(map(int, input().split())) for _ in range(N))

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]] # d가 0인 경우 북쪽, 1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽

clean_cnt = 0

clean(r, c, d)
print(clean_cnt)
