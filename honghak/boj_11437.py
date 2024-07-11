import sys
sys.stdin = open("honghak/boj_11437_input.txt", "r")
import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

tree_dict = {node : [] for node in range(1, N+1)}
parent_dict = {node : -1 for node in range(1, N+1)}
depth_dict = {node : 0 for node in range(1, N+1)}
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    # parent, child = min(a, b), max(a, b)
    tree_dict[a].append(b)
    tree_dict[b].append(a)
    
queue = deque()
queue.append([1, tree_dict[1], 1]) # parent, childs, depth
depth_dict[1] = 1

while queue:
    parent, childs, depth = queue.popleft()
    visited[parent] = 1
    
    for child in childs:
        if not visited[child]:        
            parent_dict[child] = parent #[child, parent] + parent_dict[parent]
            depth_dict[child] = depth+1
            queue.append([child, tree_dict[child], depth+1])

def lca(a, b):
    while depth_dict[a] != depth_dict[b]:
        if depth_dict[a] > depth_dict[b]:
            a = parent_dict[a]
        else:
            b = parent_dict[b]
            
    while a != b:
        a = parent_dict[a]
        b = parent_dict[b]
        
    return a

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    print(lca(a, b))