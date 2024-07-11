'''####################################################
24.07.11
백준 9095 1, 2, 3 더하기 (실버 3)
https://www.acmicpc.net/problem/9095
풀이 전략 :  DP
#######################################################
- DP는 앞으로, 잘 안풀릴때는 피보나치를 항상 생각하자
'''

T = int(input())
dp = {1:1, 2:2, 3:4, 4:7}

def getDP(N):
    if N in dp:
        return dp[N]
    dp[N] = getDP(N-1) + getDP(N-2) + getDP(N-3)
    return dp[N]

for _ in range(T):
    num = int(input())
    print(getDP(num))
