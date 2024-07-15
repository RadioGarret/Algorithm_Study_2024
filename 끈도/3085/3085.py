'''####################################################
24.07.15
백준 3085 tkxkdrpdla (실버 2)
https://www.acmicpc.net/problem/3085
풀이 전략 :  브루트포스
#######################################################
-
'''

import copy
N = int(input())
gMap = [[0] * N for _ in range(N)]
dy = [0, 0, -1, 1] # 동 서 / 북 남
dx = [1, -1, 0, 0]
max_cnt = 0 # 정답

for j in range(N):
    list_temp = list(input())
    for i in range(N):
        gMap[j][i] = list_temp[i]

def CheckMap(tMap):
    global max_cnt
    # horizontal check
    for j in range(N):
        cnt = 1
        for i in range(N-1):
            if tMap[j][i] == tMap[j][i+1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1

    # vertical check
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if tMap[j][i] == tMap[j+1][i]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1

# 위치바꾸기
for j in range(N):
    for i in range(N):
        # change
        for k in range(4):
            ny, nx = j + dy[k], i + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                tMap = copy.deepcopy(gMap)
                tMap[ny][nx], tMap[j][i] = tMap[j][i], tMap[ny][nx]
                CheckMap(tMap)

print(max_cnt)
