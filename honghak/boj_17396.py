import sys
sys.stdin = open("honghak/boj_17396_input.txt", "r")

import sys
input = sys.stdin.readline
import heapq


N, M = map(int, input().split())
sight = list(map(int, input().split()))
sight[-1] = 0

INF = int(1e+9)
graph_dict = {node : {} for node in range(N)}

for _ in range(M):
    i, j, w = map(int, input().split())
    if sight[j] == 1 or sight[i] == 1:
        continue
    graph_dict[i][j] = w
    graph_dict[j][i] = w


def dijkstra(start):
    distances = [INF for _ in range(N)]
    distances[start] = 0
    queue = [[0, start]]
    
    while queue:
        dist, current = heapq.heappop(queue)
        
        if distances[current] < dist:
            continue
            
        for next_node, next_dist in graph_dict[current].items():
            # if sight[next_node] == 1:
                # continue
            
            new_dist = dist + next_dist
            if distances[next_node] > new_dist:
                distances[next_node] = new_dist
                heapq.heappush(queue, [new_dist, next_node])
    
    return distances


distances = dijkstra(0)

if distances[N-1] == INF:
    print(-1)
else:
    print(distances[N-1])