'''
[백준] 촌수계산 (실버 2)

부모자식 사이에는 1촌, 형제자매 사이에는 2촌을 더한다.
DFS로 탐색할 때는 부모자식 관계를 따져서 깊이 탐색을 실행하기 때문에 DFS 함수를 호출할 때 cnt를 1씩 늘려주는 방식을 사용하여 푼다.

1. v = 7, cnt = 0, visited = [[False]*8]

[예시1 실행 과정]
1. v = 7, cnt = 0, visited[전부] = False
dfs(7,0)
    visited[7] = True
    if 7 == 3:
        패스
    for i in graph[7]: # graph[7] = 2
        if not visited[2]:
            dfs(2, 1) # 7과 2는 부모자식 관계라 cnt+1 해서 dfs 호출

2. v = 2, cnt = 1, visited[7] = True
dfs(2, 1):
    visited[2] = True
    if 2 == 3:
        패스
    for i in graph[2]: # graph[2] = [1,7,8,9]
        if not visited[1]:
            dfs(1, 2)

3. v = 1, cnt = 2, visited 7, 2 True
dfs(1, 2):
    visited[1] = True
    if 1 == 3:
        패스
    for i in graph[1]: # graph[1] = [2,3]
        if not visited[3]: # visited[2] = True라서 패스, visited[3] = False
            dfs(3, 3)

4. v = 3, cnt = 3, visited 7, 2, 1 True
dfs(3, 3):
    visited[3] = True
    if 3 == 3:
        flag = True
        print(3) # 결과 출력
        return
'''

# 1은 3의 부모, 1은 2의 부모, 2는 7의 부모
'''
(예시 1)
1
- 3, 2
     ㄴ 7

-> 3과 7은 3촌 관계(7-2 1촌 + 2-3 2촌) 
'''

def dfs(v, cnt):
    global flag
    visited[v] = True

    if v == b:
        flag = True
        print(cnt)
        return # 목적 달성했으니 재귀 종료

    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt+1) # v와 i는 부모자식 관계라 cnt+1 하여 dfs 호출

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

flag = False
cnt = 0
dfs(a, cnt)

if not flag:
    print(-1)