
'''####################################################
24.07.23
백준 1459 걷기 (실버 3)
https://www.acmicpc.net/problem/1459
풀이 전략 : 그리디

2024.07.22 / 백준 2012 / 등수매기기 (실버3) / 그리디

#######################################################
- 너무쉬움 -> 아님.. 구조화 잘 해야함.
- 근데, 엣지케이스 생각 못했음. 습관좀 들이자 ...... 제발..
- 대각선 두번에 직선 가능하다는 것을 생각 못함. 제발..
'''

X, Y, W, S = map(int, input().split())
answer = 0
nx, ny = 0, 0
gDist = 0


def getDist():
    global gDist, nx, ny, X, Y
    gDist = abs(nx - X) + abs(ny - Y)

getDist()

while gDist:
    if 2 * W < S:
        answer = gDist * W
        gDist = 0
    else:
        if nx == X or ny == Y: #직선만 남음
            if gDist >= 2:
                if 2 * W > 2 * S: # 대각선 두번으로 직선 길이 2 이동
                    answer += gDist//2 * 2 * S
                    if gDist%2 == 0:
                        gDist = 0
                    else:
                        gDist = 1
                else:
                    answer += gDist * W
                    gDist = 0
            else: # 남은거리 1
                answer += W
                gDist = 0
        else: # 대각으로 최대한 가
            if X <= Y:
                answer += X * S
                ny += X
                nx += X
            else:
                answer += Y * S
                ny += Y
                nx += Y
            getDist()

print(answer)
