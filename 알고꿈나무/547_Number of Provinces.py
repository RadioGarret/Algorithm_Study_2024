class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:  # checking for visited nodes
                    seen.add(neighbor)
                    dfs(neighbor) 

        n = len(isConnected)
        graph = defaultdict(list)  #Building graph
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)  #Adding undirected edges
        seen = set()
        answer = 0
        for i in range(n):
            if i not in seen:
                answer+=1
                seen.add(i)
                dfs(i)

        return answer