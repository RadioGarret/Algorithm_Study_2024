N, K = list(map(int, input().split()))
products = [list(map(int, input().split())) for _ in range(N)]

# dp[i] 는 최대 i 무게에서 얻을 수 있는 최대 가치를 의미
dp = [0] * (K+1)

# 물건을 배낭에 넣기
for weight, value in products:
    for i in range(K, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)

answer = dp[K]
print(answer)