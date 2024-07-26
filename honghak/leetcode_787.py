from typing import List
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # graph_dict = {node : [] for node in range(n)}

        # for flight in flights:
        #     graph_dict[flight[0]].append([flight[1], flight[2]])
        
        INF = int(1e+15)
        graph = [[INF for _ in range(n)] for _ in range(n)]

        for flight in flights:
            graph[flight[0]][flight[1]] = min(graph[flight[0]][flight[1]], flight[2])
                
        queue = deque()
        queue.append([0, k, src])
        
        distances = [INF for _ in range(n)]
        distances[src] = 0
        
        while queue:
            cost, remain_k, current = queue.popleft()
            
            for next_node in range(n):
                if remain_k >= 0 and graph[current][next_node] != INF:
                    new_cost = cost + graph[current][next_node]
                    if distances[next_node] > new_cost:
                        distances[next_node] = new_cost
                        queue.append([new_cost, remain_k-1, next_node])
                    
        return distances[dst] if distances[dst] != INF else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))