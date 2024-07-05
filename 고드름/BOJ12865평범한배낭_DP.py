def knapsack(N, K, items):
    # DP 테이블 초기화
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    # DP 테이블 채우기
    for i in range(1, N + 1):
        weight, value = items[i - 1]
        for w in range(K + 1):
            if w < weight:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    return dp[N][K]


# 입력 받기
N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(knapsack(N, K, items))
