import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, docs):
    cnt = 0
    while docs:
        doc = docs.popleft() # (0, 1)(1,8)(4,5)
        if docs and doc[1] < max(docs, key=lambda x: x[1])[1]:
            docs.append(doc)
        else:
            cnt += 1
            if doc[0] == M:
                return cnt 
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split()) # 4 2
    docs = deque()
    prio = list(map(int, input().split()))
    for i in range(N):
        docs.append((i, prio[i]))
    print(solution(N, M, docs))
