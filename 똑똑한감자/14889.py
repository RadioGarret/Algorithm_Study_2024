'''
[백준 - 삼성 SW 역량 테스트 기출 문제]
14889. 스타트와 링크
실버1
'''

import itertools

N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]

# N/2명이 한 팀이 되도록 나눠야 함.
# N명 중 N/2명씩 짝을 지을 때 조합 또는 순열을 사용해야 할듯. 팀은 팀원의 순서가 나열되는 것이 의미가 없기 때문에 조합을 사용함.
comb = list(itertools.combinations(members, N//2))

arr = []
for c in comb:
    team_a = 0 # A팀 스탯 합계
    team_b = 0 # B팀 스탯 합계
    extra = [x for x in members if x not in c] # B팀 멤버 (members - c)

    for i in c:
        for j in c:
            team_a += stats[i][j]
    for i in extra:
        for j in extra:
            team_b += stats[i][j]
    arr.append(abs(team_a-team_b))

print(min(arr))