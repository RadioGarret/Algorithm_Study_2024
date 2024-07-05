import sys
input = sys.stdin.readline

n = int(input())
graph = []
answer = []
visited = [[0]*n for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().strip())))
    
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1 and visited[x][y] == 0:
        cnt += 1
        visited[x][y] = 1
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True    


for i in range(n):
    for j in range(n):
        if dfs(i, j):
            answer.append(cnt)
            cnt = 0
            
print(len(answer))            
answer.sort()
for i in range(len(answer)):
    print(answer[i])
