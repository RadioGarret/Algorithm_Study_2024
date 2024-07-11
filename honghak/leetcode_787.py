from typing import List
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph_dict = {node: {} for node in range(n)}
        for flight in flights:
            i, j, w = flight[0], flight[1], flight[2]
            graph_dict[i][j] = w


        INF = int(1e+12)
        def dijkstra(start):
            queue = deque()
            queue.append([0, start, 0])

            distances = [INF for _ in range(n+1)]
            distances[start] = 0

            while queue:
                dist, current, count = queue.popleft()

                # if distances[current] < dist: continue

                for next_node, next_dist in graph_dict[current].items():
                    new_dist = next_dist + dist
                    if distances[next_node] > new_dist and count <= k:
                        distances[next_node] = new_dist
                        queue.append([new_dist, next_node, count + 1])

            return distances

        distances = dijkstra(src)
        # max_dist = max(distances)
        if distances[dst] >= INF:
            return -1
        else:
            return distances[dst]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findCheapestPrice(n = 4, \
                                flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], \
                                    src = 0, dst = 3, k = 1))