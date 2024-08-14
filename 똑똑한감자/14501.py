# 퇴사_14501
# 실버3

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)] # dp: i번째까지 날까지 일했을 때 얻을 수 있는 최대 수익, 날짜 1-index 사용하기 위해 range(N+1)

schedule.reverse()
schedule.insert(0, [])
print(schedule)

for i in range(1, N+1):
    if i < schedule[i][0]: # 일을 그만둔 후 상담을 해야 하는 일정이기 때문에 dp를 이전 인덱스 dp로 대체
        dp[i] = dp[i-1]
    else:
        dp[i] = max(dp[i-1], schedule[i][1] + dp[i-schedule[i][0]])

print(dp[N])

'''
Ti: 3 5 1 1 2 4 2
Pi: 10 20 10 20 15 40 200

이때 schedule.reverse()
Ti: 2 4 2 1 1 5 3 
Pi: 200 40 15 20 10 20 10

schedule.insert(0, [])
Ti: 0 2 4 2 1 1 5 3
Pi: 0 200 40 15 20 10 20 10

for i in range(1, N+1):
  if i < schedule[i][0]:
  ex> 1 < schedule[1][0] => 1 < 2, 즉 기간이 idx 보다 길다면 dp[i] = dp[i-1]
'''