####################################################
# 2024.08.09
# 백준 2785 체인 (실버1)
# 풀이방법 : 그리디
# link : https://www.acmicpc.net/problem/2785
####################################################

# N = int(input())
# l_input = list(map(int, input().split()))
# l_input.sort()
# flag = 1
# cnt = 0
#
# while flag:
#     N -= 1
#     cnt += l_input[0] # 첫 수
#     del l_input[0]
#     if cnt == N-1:
#         flag = 0
#     elif cnt < N-1:
#         flag = 1
#     elif cnt > N-1:
#         cnt = N
#         flag = 0
# print(cnt)
