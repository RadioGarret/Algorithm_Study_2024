"""
상자넣기
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
# def recur(cur, prev): # 현재 cur번을 선택해야 하고, 마지막에 prev번을 선택했을때 만들 수 있는 최대값
#     if cur == n + 1:
#         return 0
#     ret = 0
#     # cur번째 숫자를 선택하지 않는 경우
#     ret = max(ret, recur(cur + 1, prev))
#     # 이전에 선택한 숫자가 없거나, 이전에 선택한 숫자보다 cur번째 숫자가 클 때, cur번째 숫자를 선택 하는경우
#     if prev == 0 or arr[prev] < arr[cur]:
#         ret = max(ret,recur(cur + 1, cur) + 1)
#     return ret

def recur(cur, prev):
    if cur == n + 1:
        return 0
    if memo[cur][prev] != -1:
        return memo[cur][prev]
    ret = 0
    ret = max(ret, recur(cur + 1, prev))
    if prev == 0 or arr[prev] < arr[cur]:
        ret = max(ret, recur(cur + 1, cur) + 1)
    memo[cur][prev] = ret
    return memo[cur][prev]

n = int(input())
arr = [0] + list(map(int, input().split()))
memo = [[-1] * (n + 1) for _ in range(n + 1)]
print(recur(1, 0))