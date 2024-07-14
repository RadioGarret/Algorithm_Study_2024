import sys
sys.stdin = open("honghak/boj_2748_input.txt", "r")

import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N+1)]

for i in range(N+1):
    if i == 0:
        dp[i] = 0
        continue
    if i == 1 or i == 2:
        dp[i] = 1
        continue
    
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[N])