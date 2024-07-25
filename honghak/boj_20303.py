import sys
sys.stdin = open("honghak/boj_20303_input.txt", "r")


import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
weights = list(map(int, input().split()))


parents = [i for i in range(N)]
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
        
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
        
        
for _ in range(K):
    a, b = map(int, input().split())
    union(a-1, b-1)
    
    
groups = {}
for i in range(N):
    if i != parents[i]:
        parent_i = find(i)
        if parent_i not in groups:
            groups[parent_i] = [1, weights[i]]
        else:
            groups[parent_i] = [groups[parent_i][0] + 1, groups[parent_i][1] + weights[i]]
        
dp = [0 for _ in range(K)]
for key, value in groups.items():
    k, weight = value[0], value[1]
    
    if k >= K-1:
        continue
    
    for j in range(K-1, 0, -1):
        if j + k <= K-1 and dp[j] != 0:
            dp[j+k] = max(dp[j+k], dp[j] + weight)
    dp[k] = max(dp[k], weight)
    
print(max(dp))