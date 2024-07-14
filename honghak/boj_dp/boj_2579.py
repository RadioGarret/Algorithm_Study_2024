import sys
sys.stdin = open("honghak/boj_dp/boj_2579_input.txt")

import sys
input = sys.stdin.readline

N = int(input())

stairs = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        dp[i] = stairs[i]
        continue
    if i == 1:
        dp[i] = stairs[0] + stairs[1]
        continue
    if i == 2:
        dp[i] = max()

    dp[i] = max(dp[i-1], dp[i-2]) + stairs[i]
    
print(dp[N-1])
