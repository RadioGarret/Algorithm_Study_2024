'''####################################################
24.07.17
백준 1182 부분수열의 합 (실버 2)
https://www.acmicpc.net/problem/1182
풀이 전략 :  브루트포스
#######################################################
- combinations로 풀었음.
'''

from itertools import combinations
N, S = map(int, input().split())
li = list(map(int, input().split()))
answer = 0

for cnt in range(1, N+1):
    # cnt 는 원소의 갯수
    lc = list(combinations(li, cnt))
    total = 0
    for lt in lc:
        total = 0
        for num in lt:
            total += num
        if total == S:
            answer += 1
print(answer)
