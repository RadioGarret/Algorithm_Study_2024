'''####################################################
24.07.10
백준 1965 상자넣기 (실버 2)
https://www.acmicpc.net/problem/1965
풀이 전략 :  DP top down.
#######################################################
'''

N = int(input())
L = list(map(int, input().split()))
dp = [1] * N  # 모든 상자는 일단 자기 자신 하나씩
max_dp = 0 # 정답 담을 변수

for now in range(1, N): # 앞의 숫자부터 하나씩 dp 업데이트
    for i in range(now): # 맨 처음부터 지금 숫자까지 살펴보기
        if L[i] < L[now]: # 지금 상자에 담길 수 있는가?
            if dp[now] <= dp[i]:
                dp[now] = dp[i] + 1

for i in range(N): # 최대 dp값 찾기
    if max_dp < dp[i]:
        max_dp = dp[i]
print(max_dp)
