import sys
sys.stdin = open("honghak/boj_1504_input.txt", "r")

input = sys.stdin.readline
from collections import defaultdict
import heapq

INF = int(1e+9)
N, E = map(int, input().split())

graph_dict = defaultdict(dict)

def dijkstra(start):
    distances = {node : INF for node in range(1, N+1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    
    while queue:
        dist, current = heapq.heappop(queue)
        
        if distances[current] < dist:
            continue
        
        for next_node, next_dist in graph_dict[current].items():
            if distances[next_node] > dist + next_dist:
                distances[next_node] = dist + next_dist
                heapq.heappush(queue, [dist+next_dist, next_node])
                
    return distances

for _ in range(E):
    i, j, w = map(int, input().split())
    graph_dict[i][j] = w
    graph_dict[j][i] = w
    
v1, v2 = map(int, input().split())

distances_dict = {}
# for i in range(1, N+1):
distances_dict[1] = dijkstra(1)
distances_dict[v1] = dijkstra(v1)
distances_dict[v2] = dijkstra(v2)

    
case1 = distances_dict[1][v1] + distances_dict[v1][v2] + distances_dict[v2][N]
case2 = distances_dict[1][v2] + distances_dict[v2][v1] + distances_dict[v1][N]

rst = min(case1, case2)
if rst >= INF :
    rst = -1

print(rst)
