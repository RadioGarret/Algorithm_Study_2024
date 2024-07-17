import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

arr = [[int(x) for x in input().strip()] for _ in range(N)]
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
costs = [[0 for _ in range(M)] for _ in range(N)]

def bfs(i, j):
    queue = deque()
    queue.append([1, i, j])
    
    while queue:
        cost, i, j = queue.popleft()
        
        for move in moves:
            di, dj = i + move[0], j + move[1]
            if 0 <= di < N and 0 <= dj < M and arr[di][dj] == 1 and costs[di][dj] == 0:
                costs[di][dj] = cost+1
                queue.append([cost+1, di, dj])
            
costs[0][0] = 1
bfs(0, 0)

print(costs[N-1][M-1])