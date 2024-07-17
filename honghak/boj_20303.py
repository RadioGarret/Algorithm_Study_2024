import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
weights = list(map(int, input().split()))
graph_dict = {node: [] for node in range(N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    graph_dict[a].append(b)
    graph_dict[b].append(a)
    
def get_friends(start):
    friends = [1, weights[start]]
    queue = deque()
    queue.append(start)
    while queue:
        current = queue.popleft()
        visited[current] = 1
        for next_node in graph_dict[current]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                friends[0] += 1
                friends[1] += weights[next_node]
                queue.append(next_node)
    
    return friends

visited = [0 for _ in range(N)]
relationships = []
for i in range(N):
    if visited[i] == 1:
        continue
    visited[i] = 1
    relationships.append(get_friends(i))

len_relations = len(relationships)

dp = [[0 for _ in range(K)] for _ in range(len_relations+1)]

for i in range(1, len_relations+1):
    for j in range(1, K):
        num, weight = relationships[i-1][0], relationships[i-1][1]
        if j < num:
            dp[i][j] = dp[i-1][j] 
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-num] + weight)

print(dp[len_relations][K-1])
