'''
백준 11724. 연결 요소의 개수
'''
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        # print(queue)
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        # print('after', queue)


N, M = map(int,(input().split()))
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# print('graph: ', graph)

count = 0
visited = [False] * (N+1)
for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i, visited)
        count+=1

print(count)