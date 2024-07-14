import sys
sys.stdin = open("honghak/boj_dp/boj_9095_input.txt", "r")

import sys
input = sys.stdin.readline

T = int(input())

dp = [0 for _ in range(12)]

for i in range(12):
    if i == 0 : continue
    if i == 1 or i == 2: 
        dp[i] = i
        continue
    if i == 3:
        dp[i] = 4
        continue
    
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    
for _ in range(T):
    n = int(input())
    print(dp[n])