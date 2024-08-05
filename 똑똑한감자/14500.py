'''
[백준 - 삼성 SW 역량 테스트 기출 문제]
테트로미노
골드4

요구사항: 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

테트로미노: 정사각형 '4개'를 이어 붙인 폴리오미노
폴리오미노: 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형

DFS 탐색은 'ㅗ' 모양을 탐색할 수 없다.
'ㅗ' 처리는 exceptional 함수에서 따로 처리한다.
'''
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 방향 남-서-북-동
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_val = 0
def dfs(x, y, tmp, cnt):
    global max_val
    if cnt == 4:
        max_val = max(tmp, max_val)
        return # return을 적어주지 않으면 무한 반복

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N or visited[ny][nx]:
            continue
        visited[ny][nx] = True # 방문처리
        dfs(nx, ny, tmp + board[ny][nx], cnt+1)
        visited[ny][nx] = False # 방문처리 제거 (다른 테트로미노 방식으로 해당 칸을 접근할 수 있도록 하기 위함)

# ㅗ 모양 탐색
def exceptional(x, y):
    global max_val
    tmp = board[y][x]
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        arr.append(board[ny][nx])

    if len(arr) == 4:
        arr.sort(reverse=True) # 내림차순으로 정렬하여 가장 작은 값이 맨뒤에 위치
        arr.pop() # 가장 작은 값 제거
        max_val = max(max_val, sum(arr) + board[y][x])
    elif len(arr) == 3:
        max_val = max(max_val, sum(arr) + board[y][x])
    return # length가 2 이하라면 ㅗ 모양이 아님

for i in range(N):
    for j in range(M):
        visited[i][j] = True # 현재 지점 방문처리
        dfs(j, i, board[i][j], 1)
        exceptional(j, i)
        visited[i][j] = False

print(max_val)