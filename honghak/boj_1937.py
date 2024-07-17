import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = {} #[[[-1 for _ in range(N*N)]for _ in range(N)] for _ in range(N)] # N -> N -> depth
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left

def dfs(x, y):
    if (x, y) in dp:
        return dp[(x, y)]
    
    dp[(x, y)] = 1
    
    for move in moves:
        dx, dy = x + move[0], y + move[1]
        if 0 <= dx < N and 0 <= dy < N and arr[dx][dy] > arr[x][y]:
            dp[(x, y)] = max(dp[(x, y)], dfs(dx, dy)+1)
    
    return dp[(x, y)]

max_val = -1
for i in range(N):
    for j in range(N):
        if (i, j) not in dp:
            max_val = max(max_val, dfs(i, j))
        
print(max_val)