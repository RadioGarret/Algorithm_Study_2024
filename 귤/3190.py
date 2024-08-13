import sys
input = sys.stdin.readline

# 0 아무것도 없음
# -1 사과
# 1 이상의 숫자: 뱀
N = int(input())
board = [[0] * (N + 1) for _ in range(N + 1)]

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = -1

L = int(input())
rotate = dict()
for _ in range(L):
    time, direction = input().split()
    time = int(time)
    rotate[time] = direction

clock = 1
head = [1, 1]
tail = [1, 1]
heading_idx = 0
heading_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while True:
    # 머리 이동
    head = [head[0] + heading_list[heading_idx][0], head[1] + heading_list[heading_idx][1]]
    # 벽이면 종료
    if head[0] <= 0 or head[0] > N or head[1] <= 0 or head[1] > N:
        break
    # 자기 자신이면 종료
    if board[head[0]][head[1]] > 0:
        break
    
    # head 표시
    is_apple = board[head[0]][head[1]]
    board[head[0]][head[1]] = clock
    
    # 사과가 아니면 tail 이동
    if is_apple != -1:
        board[tail[0]][tail[1]] = 0
        next_tail = [0, 0]
        min_value = float('inf')
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            temp_r = tail[0] + dr
            temp_c = tail[1] + dc
            if temp_r <= 0 or temp_r > N or temp_c <= 0 or temp_c > N:
                continue
            if board[temp_r][temp_c] == -1 or board[temp_r][temp_c] == 0:
                continue
            if board[temp_r][temp_c] < min_value:
                next_tail = [temp_r, temp_c]
                min_value = board[temp_r][temp_c]
        tail = next_tail
    
    # heading 변경
    if clock in rotate.keys():
        command = rotate[clock]
        rotate.pop(clock)
        if command == "L":
            heading_idx = heading_idx - 1
            if heading_idx < 0:
                heading_idx = 3
        elif command == "D":
            heading_idx = heading_idx + 1
            if heading_idx > 3:
                heading_idx = 0
        else:
            print("Wrong rotation command")
    
    clock += 1

print(clock)