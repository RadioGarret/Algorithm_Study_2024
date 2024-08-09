####################################################
# 2024.08.09
# 백준 2195 문자열복사 (골드5)
# 풀이방법 : 그리디
# link : https://www/.acmicpc.net/problem/2195
####################################################

S = input()
P = input()
start = 0
cnt = 0
flag = 1
length = len(P)

while flag:
    for i in range(1, length):
        if P[start:] in S: # 종료조건
            flag = 0
            cnt += 1
            break
        else:
            if P[start : -i] in S:
                start = length - i
                cnt += 1
                break

print(cnt)
