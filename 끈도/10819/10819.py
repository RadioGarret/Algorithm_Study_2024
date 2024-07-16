'''####################################################
24.07.16
백준 10819 차이를 최대로 (실버 2)
https://www.acmicpc.net/problem/10819
풀이 전략 :  브루트포스
#######################################################
- 1. 재귀로 풀어보기 
- 2. permutation으로 풀어보기
'''
N = int(input())
li = list(map(int, input().split()))
answer = 0
visited = [0] * N


def rec(lt):
    global answer
    if len(lt) == N:
        total = 0
        for i in range(N-1):
            total += abs(lt[i] - lt[i + 1])
        answer = max(answer, total)
    for i in range(N):
        if visited[i] == 0:
            lt.append(li[i])
            visited[i] = 1
            rec(lt)
            visited[i] = 0
            lt.pop()

rec([])
print(answer)
