import sys
sys.stdin = open("honghak/boj_dp/boj_1463_input.txt")

import sys
input = sys.stdin.readline

N = int(input())

dp = [99999 for _ in range(N+1)]
   
    
for i in range(N+1):
    if i == 0 or i == 1:
        dp[i] = 0
        continue
    
    if i == 2 or i == 3:
        dp[i] = 1
        continue
    
    dp[i] = min(dp[i], dp[i-1] + 1)
    
    if i % 3 == 0:
        prev = i // 3
        dp[i] = min(dp[i], dp[prev] + 1)
        
    if i % 2 == 0:
        prev = i // 2
        dp[i] = min(dp[i], dp[prev] + 1)
    
    
print(dp[N])