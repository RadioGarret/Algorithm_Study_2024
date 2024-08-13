'''
[백준 - 삼성 SW 역량 테스트 기출 문제]
톱니바퀴
골드4
'''

# 입력: 1번~4번 톱니바퀴 상태 입력 받기 (문자열)
gears = [input() for _ in range(4)]

# 입력: k
k = int(input())

# 입력: (gear_num, dir)
cmd = []
for i in range(k):
    gear_num, dir = map(int, input().split())
    cmd.append((gear_num, dir))

# 1차원 배열 회전
def rotate(gear, dir):
    if dir == 1: # 시계 방향 회전
        gear = gear[-1] + gear[:-1]

    elif dir == -1: # 반시계 방향 회전
        gear = gear[1:] + gear[0]

    return gear

# 인접 톱니바퀴 회전 여부 검사
def should_rotate(gear_left, gear_right):
    if gear_left[2] != gear_right[6]: # 극이 다른 경우 회전
        return True
    else:
        return False

# 점수 계산
def scoring(gears):
    sum = 0
    mul = 1
    for g in gears:
        tmp = int(g[0])*mul
        sum += tmp
        mul *= 2
    return sum

for c in cmd:

    gear_num = c[0]-1
    rotate_dir = c[1]
    target_gear = gears[gear_num]

    cur = gear_num+1
    movement = []
    cur_dir = rotate_dir

    while cur != 4:
        if not should_rotate(gears[cur-1], gears[cur]):
            break
        if should_rotate(gears[cur-1], gears[cur]):
            cur_dir = -cur_dir
            movement.append([cur, 1, cur_dir])
        cur += 1

    cur = gear_num-1
    cur_dir = rotate_dir

    while cur != -1:
        if not should_rotate(gears[cur], gears[cur+1]):
            break
        if should_rotate(gears[cur], gears[cur+1]):
            cur_dir = -cur_dir
            movement.append([cur, 1, cur_dir])
        cur -= 1

    new_gear = rotate(gears[gear_num], rotate_dir)
    gears[gear_num] = new_gear # 회전한걸로 교체

    for m in movement:
        if m[1] == 1:
            gears[m[0]] = rotate(gears[m[0]], m[2])

print(scoring(gears))