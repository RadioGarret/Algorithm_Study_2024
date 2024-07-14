import sys
sys.stdin = open("honghak/boj_2934_input.txt")

import sys
input = sys.stdin.readline

MAX = 100000
l = []
lazy = [0] * (MAX*4)
tree = [0] * (MAX*4)

def update_lazy(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end-start+1)*lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0
        
def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    
    mid = (start + end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]
    
def get_value(node, start, end, idx):
    update_lazy(node, start, end)
    if idx > end or idx < start:
        return 0
    
    if start == end and start == idx:
        result = tree[node]
        tree[node] = 0
        return result
    
    mid = (start+end) // 2
    return max(get_value(node*2, start, mid, idx), get_value(node*2+1, mid+1, end, idx))
    
def update_range(node, start, end, idx_start, idx_end, diff):
    update_lazy(node, start, end)
    
    if idx_start > end or idx_end < start:
        return 0
    
    if idx_start <= start and end <= idx_end:
        tree[node] += (end-start+1) * diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    
    mid = (start+end) // 2
    update_range(node*2, start, mid, idx_start, idx_end, diff)
    update_range(node*2+1, mid+1, end, idx_start, idx_end, diff)
    tree[node] = tree[node*2] + tree[node*2+1]
        


K = int(input())
for _ in range(K):
    L, R = map(int, input().split())
    print(get_value(1, 0, MAX-1, L) + get_value(1, 0, MAX-1, R))
    update_range(1, 0, MAX-1, L+1, R-1, 1)
