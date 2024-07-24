'''####################################################
24.07.22
백준 2012 등수매기기 (실버 3)
https://www.acmicpc.net/problem/2012
풀이 전략 :  그리디
#######################################################
- 브루트포스로 풀면 메모리 초과됨.
'''
# from itertools import permutations
#
# N = int(input())
# list_input = []
# for i in range(N):
#     list_input.append(int(input()))
#
# list_permu = list(permutations(list_input, N))
# answer = 9999999
# for list_temp in list_permu:
#     total = 0
#     for i in range(len(list_temp)):
#         total += abs(list_temp[i] - (i+1))
#     answer = min(answer, total)
#
# print(answer)


# 위의 풀이는 50만! 이므로, 시간초과남. 10!이 360만이고 11!이 4천만인데, 2초는 2억이내임.
# 2트


N = int(input())
list_input = []
for i in range(N):
    list_input.append(int(input()))

list_input.sort()
answer = 0

for i in range(1, N+1):
    answer += abs(i - list_input[i-1])

print(answer)
