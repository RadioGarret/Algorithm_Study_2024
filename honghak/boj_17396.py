import sys
sys.stdin = open("honghak/boj_17396_input.txt", "r")

import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
visible = list(map(int, input().split()))
visible[-1] = 0

graph_dict = {node : {} for node in range(N)}

for _ in range(M):
    a, b, w = map(int, input().split())
    if visible[a] == 0 and visible[b] == 0:
        graph_dict[a][b] = w
        graph_dict[b][a] = w

INF = int(1e+15)
queue = []
heapq.heappush(queue, [0, 0]) # start, dist
distances = [INF for _ in range(N)]
distances[0] = 0

while queue:
    current, dist = heapq.heappop(queue)
    
    if distances[current] < dist:
        continue
    
    for next_node, next_dist in graph_dict[current].items():
        new_dist = dist + next_dist
        if distances[next_node] > new_dist:
            distances[next_node] = new_dist
            heapq.heappush(queue, [next_node, new_dist])
            
            
min_dist = distances[N-1] if distances[N-1] != INF else -1
print(min_dist)
    

