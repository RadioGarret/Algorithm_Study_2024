'''
[백준 - 삼성 SW 역량 테스트 기출 문제]
경사로
골드3

길이 지나갈 수 있으려면?
1. 길에 속한 모든 칸의 높이가 모두 같아야 한다
2. 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다
   낮은 칸과 높은 칸의 높이 차이는 항상 1
   경사로의 낮은 칸 길이는 L, L개의 연속된 칸이 연속되어 있어야 한다

원래 스택을 사용해서 해결하려다가 블로그에서 코드 봄.
line 별로 처리하는 함수 (세로로 탐색할 때는 함수에 넣을 때 배열 인덱스만 바꿔서)
나는 2차원 배열 자체를 변형해서 넣으려고 했었는데, 이런 방식도 있구나.
구현 자체는 직관적으로 경사로 진입 부분 (높이가 1차이 나는 곳)에서 L 길이만큼 탐색하는 방법을 사용함.
'''

N, L = map(int, (input().split()))
land = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def path(line):
    bri = [False for _ in range(N)]

    for i in range(1, N):
        if abs(line[i]-line[i-1]) > 1: # 높이 차이가 1보다 크면 경사로 만들 수 없음
            return False

        else:
            if (line[i - 1] - line[i]) == 1:  # 오른쪽으로 다리 놓을 때
                for j in range(L):  # 놓을 수 있는지 확인하기 위해 경사로 길이만큼 반복

                    if i + j >= N:  # 경사로가 범위 밖으로 나간다면
                        return False
                    if line[i] != line[i + j]:  # 경사로를 두는 곳의 높이가 다르면
                        return False
                    if bri[i + j] == True:  # 경사로가 이미 있다면
                        return False
                    if bri[i + j] == False:  # 경사로를 두는데 문제가 없다면
                        bri[i + j] = True # 경사로를 놓는다

            elif (line[i - 1] - line[i]) == -1:  # 왼쪽으로 다리 놓을 떄
                for j in range(L):
                    if i - 1 - j < 0:
                        return False
                    if line[i - 1] != line[i - 1 - j]:
                        return False
                    if bri[i - 1 - j] == True:
                        return False
                    if bri[i - j - 1] == False:
                        bri[i - j - 1] = True
    return True  # 경사로를 놓는데에 아무런 문제가 없다면

# 모든 경우의 수(2N)을 돌며 길이 있는지를 판단.

# 가로
for i in range(N):
    if path(land[i]):
        ans += 1

# 세로
for j in range(N):
    if path([land[i][j] for i in range(N)]):
        ans += 1

print(ans)