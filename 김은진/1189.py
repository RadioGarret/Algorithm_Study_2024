from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(y, x, cnt):
    global answer
    
    if cnt == k and y == 0 and x == (c - 1):
        answer += 1
        
    else:
        graph[y][x] = "T"
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx = x + dx
            ny = y + dy
        
            if 0 <= ny < r and 0 <= nx < c:
                if graph[ny][nx] == ".":
                    graph[ny][nx] = "T"
                    dfs(ny, nx, cnt + 1)
                    graph[ny][nx] = "."


r, c, k = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(r)]
answer = 0

dfs(r - 1, 0, 1)
print(answer)
