import sys
sys.stdin = open("honghak/boj_9252_input.txt", "r")
import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

n = len(word1)
m = len(word2)

dp = [[0 for _ in range(m+10)] for _ in range(n+10)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 #word1[i-1]
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]


count1 = n
count2 = m
res = []

while count1 and count2:
    # if dp[count1][count2] == dp[count1-1][count2-1] + 1 and \
    if word1[count1-1] == word2[count2-1]:
        # dp[count1][count2] != dp[count1-1][count2] and \
        # dp[count1][count2] != dp[count1][count2-1]:
            count1 = max(count1-1, 0)
            count2 = max(count2-1, 0)
            res.append(word1[count1])

    if dp[count1][count2] == dp[count1-1][count2]:
        count1 = max(count1 -1, 0)
        continue
    if dp[count1][count2] == dp[count1][count2-1]:
        count2 = max(count2-1, 0)
        continue

answer = ""
for i in range(len(res)-1, -1, -1):
    answer += res[i]

# res = []
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if dp[i][j] == dp[i-1][j-1] + 1:
#             res.append(word1[i-1])

print(dp[n][m])
print(answer)


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