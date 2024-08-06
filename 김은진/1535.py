import sys 
input = sys.stdin.readline

n = int(input())
people = [0] + list(map(int, sys.stdin.readline().split()))
happiness = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[0] * 101 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        if people[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - people[i]] + happiness[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])



