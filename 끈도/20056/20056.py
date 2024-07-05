'''####################################################
24.07.05
백준 20056 마법사 상어와 파이어볼 (골드 4)
https://www.acmicpc.net/problem/20056
풀이 전략 :  구현
'''####################################################

# 1번 행은 N번 행과 연결되어있고, 1번 열은 N번 열과 연결되어있다. 
# map 밖으로 나갔다면, 안으로 갖고 들어오는 함수를 만들어야겠다. 

import copy
import math

N, M, K = map(int, input().split())
gMap = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    y, x, mass, speed, dir = map(int, input().split())
    y -= 1
    x -= 1
    gMap[y][x].append((mass, speed, dir))

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def Boundary(y, x):
    flag = 1 ########### 와... 그냥 한번만 하면 될줄알았지? speed가 개빡세서 여러번 boundary 확인해야할수도 있었다...
    while flag:
        if not 0 <= y:
            y = y + N
        if not y < N:
            y = y - N
        if not 0 <= x:
            x = x + N
        if not x < N:
            x = x - N
        if not 0 <= y < N or not 0 <= x < N:
            continue
        flag = 0

    return y, x

def Move(tMap): 
    for j in range(N):
        for i in range(N):
            if len(gMap[j][i]) != 0: # fireball 존재
                for mass, speed, dir in gMap[j][i]:
                    nx = i + dx[dir] * speed
                    ny = j + dy[dir] * speed
                    ny, nx = Boundary(ny, nx) ########### 와... 그냥 한번만 하면 될줄알았지? speed가 개빡세서 여러번 boundary 확인해야할수도 있었다...
                    tMap[ny][nx].append((mass, speed, dir))
    return tMap

def Update(tMap):
    for j in range(N):
        for i in range(N):
            fireballs = len(tMap[j][i])
            if fireballs > 1:
                # 질량을 우선 나누기, 질량 0이면 없애버리기
                mass, speed = 0, 0
                list_dir = []
                for m, s, d in tMap[j][i]:
                    mass += m
                    speed += s
                    list_dir.append(d%2)
                nmass = mass//5
                if nmass == 0:
                    tMap[j][i] = []
                    continue
                # 질량이 0이 아니라면, 속력과 방향을 결정하여 append하기
                nspeed = speed//fireballs
                tMap[j][i] = []

                flag = 0
                for k in range(len(list_dir)-1): ##########와... 여기 k를 i로 했더니 i가 바뀌어버린다....
                    if list_dir[k] != list_dir[k+1]:
                        flag = 1

                if flag == 0:
                    for ndir in range(0, 7, 2):
                        tMap[j][i].append((nmass, nspeed, ndir))
                else:
                    for ndir in range(1, 8, 2):
                        tMap[j][i].append((nmass, nspeed, ndir))

cnt = 0
while cnt < K:
    tMap = [[[] for _ in range(N)] for _ in range(N)]
    Move(tMap)
    Update(tMap)
    gMap = tMap
    cnt += 1

result_mass = 0
for j in range(N):
    for i in range(N):
        if len(gMap[j][i]):
            for mass, _, _ in gMap[j][i]:
                result_mass += mass

print(result_mass)
