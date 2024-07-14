import sys
sys.stdin = open("honghak/boj_10999_input.txt")

import sys
input = sys.stdin.readline

l = []
lazy = [0] * 3000000
tree = [0] * 3000000

def init(node, start, end): 
    if start == end :
        tree[node] = l[start]
        return tree[node]
    else :
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]
    
  
def update_lazy(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end-start+1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0
        
    
def sub_sum(node, start, end, left, right):
    update_lazy(node, start, end)
    if left > end  or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    return sub_sum(node*2, start, (start+end)//2, left, right) + sub_sum(node*2+1, (start+end)//2+1, end, left, right)

def update_range(node, start, end, idx_start, idx_end, diff):
    update_lazy(node, start, end)
    
    if idx_start > end or idx_end < start:
        return
    
    if idx_start <= start and end <= idx_end:
        tree[node] += (end-start+1) * diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    
    update_range(node*2, start, (start+end)//2, idx_start, idx_end, diff)
    update_range(node*2+1, (start+end)//2+1, end, idx_start, idx_end, diff)
    tree[node] = tree[node*2] + tree[node*2+1]
        


N, M, K = map(int, input().split())

for _ in range(N):
    l.append(int(input()))
    
init(1, 0, N-1)
    
for _ in range(M+K):
    commands = list(map(int, input().split()))
    left, right = commands[1]-1, commands[2]-1
    if commands[0] == 1:
        update_range(1, 0, N-1, left, right, commands[3])
    
    elif commands[0] == 2:
        print(sub_sum(1, 0, N-1, left, right))