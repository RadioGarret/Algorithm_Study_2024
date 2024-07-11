import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split()) # 수빈, 동생
#5, 17
#5 - 순간이동 - 10 - 걷기 - 9 - 순간이동 - 18 - 걷기 - 17 : 4초

lst = [0] * 100001

def bfs(N, K):
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(lst[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and lst[nx] == 0:
                lst[nx] = lst[x] + 1
                q.append(nx)
        
bfs(N, K)

