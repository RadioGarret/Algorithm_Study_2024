####################################################
# 2024.08.10 / 백준 1697 / 숨바꼭질 (실버1) / BFS, DFS
# link : https://www.acmicpc.net/problem/1697
####################################################

N, K = map(int, input().split())
Value = [0] * 10000000
answer_cnt = 9999999999999


def BFS():
    Q = [N]
    while Q:
        now = Q[0]
        del Q[0]
        if now == K:
            return Value[now]
        for i in (now-1, now+1, now*2):
            if i >= 0 and i <= 200000 and Value[i] == 0:
                Q.append(i)
                Value[i] = Value[now] + 1

if N == K:
    print(0)
else:
    print(BFS())
