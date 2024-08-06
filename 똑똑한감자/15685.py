'''
[백준 - 삼성 SW 역량 테스트 기출 문제]
드래곤 커브
골드3
'''

N = int(input())
# x, y, d(시작 방향), g(세대)
# 0 <= x, y <= 100
curves = [list(map(int, input().split())) for _ in range(N)]

# 동, 북, 서, 남
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

checked = [[0] * 101 for _ in range(101)]

for c in curves:
    x, y, d, g = c[0], c[1], c[2], c[3]
    checked[y][x] = 1  # 방문 표시
    # 초기 방향으로 한 칸 이동
    x += dx[d]
    y += dy[d]
    checked[y][x] = 1  # 이동한 좌표 방문 표시

    # 드래곤 커브의 방향 리스트를 저장
    directions = [d]

    for _ in range(g):
        # 현재 드래곤 커브의 방향들을 역순으로 탐색하여 시계방향 회전 후 추가
        for i in range(len(directions)-1, -1, -1):
            nd = (directions[i] + 1) % 4
            x += dx[nd]
            y += dy[nd]
            checked[y][x] = 1  # 이동한 좌표 방문 표시
            directions.append(nd)

answer = 0
for i in range(100):
    for j in range(100):
        # 1x1 정사각형의 네 꼭지점이 모두 드래곤 커브의 일부인지 확인
        if checked[i][j] and checked[i + 1][j] and checked[i][j + 1] and checked[i + 1][j + 1]:
            answer += 1

print(answer)