N = int(input())
boxes = list(map(int, input().split()))
# dp = 해당 인덱스의 박스가 넣을 수 있는 박스의 개수
dp = [1] * N # 자기 자신은 무조건 넣을 수 있으므로 최소 1을 갖는다
max_dp = 0 # 답

# dp 채우기
for now in range(1, N): # 인덱스 1부터 시작하기 (0번째는 무조건 1개만 가질 수 있음)
    for i in range(now):
        if boxes[i] < boxes[now]: # 지금 상자에 담길 수 있는가?
            if dp[now] <= dp[i]:
                dp[now] = dp[i] + 1

# dp 배열의 최댓값 구하기
for i in range(N):
    if max_dp < dp[i]:
        max_dp = dp[i]
print(max_dp)
