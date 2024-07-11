import sys
sys.stdin = open("honghak/boj_9252_input.txt", "r")

import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

n = len(word1)
m = len(word2)

dp = [["" for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + word1[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))
print(dp[-1][-1])


# def dfs(n_s, m_s):
    
#     if n_s >= n or m_s >= m:
#         return 0
    
#     if dp[n_s][m_s] != -1:
#         return dp[n_s][m_s]
    
    
#     for i in range(n_s, n):
#         for j in range(m_s, m):
#             if word1[i] == word2[j]:
#                 dp[i][j] = max(dp[i][j], 1)
#                 max_lcs = max(dp[i][j], dp[i][j]+dfs(i+1, j+1))
    
#     return max_lcs


# print(dfs(0, 0))