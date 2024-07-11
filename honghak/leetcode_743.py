"""
You are given a network of n nodes, labeled from 1 to n. 
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. 
Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.
"""

from typing import List
from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph_dict = {node: {} for node in range(1, n+1)}
        for time in times:
            i, j, w = time[0], time[1], time[2]
            graph_dict[i][j] = w


        INF = int(1e+12)
        def dijkstra(start):
            queue = deque()
            queue.append([0, start])

            distances = [INF for _ in range(n+1)]
            distances[start] = 0

            while queue:
                dist, current = queue.popleft()

                if distances[current] < dist: continue

                for next_node, next_dist in graph_dict[current].items():
                    new_dist = next_dist + dist
                    if distances[next_node] > new_dist:
                        distances[next_node] = new_dist
                        queue.append([new_dist, next_node])

            return distances[1:]

        distances = dijkstra(k)
        max_dist = max(distances)
        if max_dist >= INF:
            return -1
        else:
            return max_dist


if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))