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


'''
# DFS 시간초과 -> DP 문제 ...

# idx 번째 물건을 선택할 지 아닐 지 결정 하는 함수
def dfs(idx, sum_w, sum_v, chosen):
    global max_v
    if sum_w > K:
        return
    if idx == N: # N-1 일때로 하면 물건이 1개일 때 답이 안 나옴
        if max_v < sum_v:
            max_v = sum_v
        return
    chosen[idx] = 1
    dfs(idx+1, sum_w + products[idx][0], sum_v + products[idx][1], chosen)
    chosen[idx] = 0
    dfs(idx+1, sum_w, sum_v, chosen)


N, K = list(map(int, input().split()))
products = []
for i in range(N):
    products.append(list(map(int, input().split())))
max_v = 0
sorted_products = sorted(products,reverse=True)
min_w = sorted_products[0][0]
if K < min_w:
    print(0)
elif K == min_w:
    print(sorted_products[0][1])
else:
    dfs(0,0,0,[0]*N)
    print(max_v)
'''