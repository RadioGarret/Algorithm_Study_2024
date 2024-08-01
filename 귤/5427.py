import sys
input = sys.stdin.readline

from collections import deque

EMPTY = "."
WALL = "#"
SANGGEUN = "@"
FIRE = "*"

moving = [(-1, 0), (1, 0), (0, -1), (0, 1)]

T = int(input())

for _ in range(T):
    W, H = map(int, input().split())
    
    board = []
    fires = []
    player = [0, 0]
    for h in range(H):
        row = list(input().strip())
        for w in range(W):
            if row[w] == FIRE:
                fires.append((h, w))
            elif row[w] == SANGGEUN:
                player = (h, w)
        board.append(row)
    
    # fire stamp
    visited = [[False] * W for _ in range(H)]
    for fire in fires:
        visited[fire[0]][fire[1]] = True
        board[fire[0]][fire[1]] = 0
    
    q = deque(fires)
    while q:
        ch, cw = q.popleft()
        for dh, dw in moving:
            nh, nw = ch + dh, cw + dw
            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                continue
            if visited[nh][nw]:
                continue
            if board[nh][nw] == WALL:
                continue
            
            # 처리
            board[nh][nw] = board[ch][cw] + 1
            # visited
            visited[nh][nw] = True
            # queue
            q.append((nh, nw))
        
            
    # player
    visited = [[False] * W for _ in range(H)]
    visited[player[0]][player[1]] = True
    q = deque([(player[0], player[1], 0)])
    
    exit = False
    while q:
        if exit:
            break
        ch, cw, time = q.popleft()
        for dh, dw in moving:
            nh, nw = ch + dh, cw + dw
            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                exit = True
                print(time + 1)
                break
            elif visited[nh][nw]:
                continue
            elif board[nh][nw] == WALL:
                continue
            elif board[nh][nw] != EMPTY and board[nh][nw] <= time + 1:
                continue
            
            visited[nh][nw] = True
            q.append((nh, nw, time + 1))
    
    if not exit:
        print("IMPOSSIBLE")
                       