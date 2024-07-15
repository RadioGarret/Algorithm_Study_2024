import sys
input = sys.stdin.readline

def get_max():
    mx = 1
    # 모든 행에서 연속한 최대값 찾기
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]: # 현재 위치가 이전 위치랑 같으면 길이 늘리기
                cnt += 1
            else:                              # 다르면 길이 1
                cnt = 1
            mx = max(mx, cnt)
    # 모든 열에서 연속한 최대값 찾기
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if board[i][j] == board[i - 1][j]:
                cnt += 1
            else:
                cnt = 1
            mx = max(mx, cnt)
    return mx

n = int(input())

board = [list(input().strip()) for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(n):
        if i + 1 < n and board[i][j] != board[i + 1][j]:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            ans = max(ans, get_max())
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
        if j + 1 < n and board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            ans = max(ans, get_max())
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
print(ans)