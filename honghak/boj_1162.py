import sys
sys.stdin = open("honghak/boj_1162_input.txt", "r")

import sys
input = sys.stdin.readline
import heapq

INF = sys.maxsize
N, M, K = map(int, input().split())

graph = [[] for _ in range(N+1)]
distances = [[INF for _ in range(K+1)] for _ in range(N+1)]

for _ in range(M):
    i, j, w = map(int, input().split())
    graph[i].append((w,j))
    graph[j].append((w,i))
    
def dijkstra(start):
    queue = []
    count = 0
    distances[start][count] = 0
    heapq.heappush(queue, [0, start, count])

    while queue:
        dist, current, count = heapq.heappop(queue)

        if distances[current][count] < dist:
            continue

        for next_dist, next_node in graph[current]:
            new_dist = dist + next_dist
            if distances[next_node][count] > new_dist:
                distances[next_node][count] = new_dist
                heapq.heappush(queue, [new_dist, next_node, count])

            if count < K and distances[next_node][count+1] > dist:
                distances[next_node][count+1] = dist
                heapq.heappush(queue, [dist, next_node, count + 1])
                
dijkstra(1)
print(min(distances[N]))
