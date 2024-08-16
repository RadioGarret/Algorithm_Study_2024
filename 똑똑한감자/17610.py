N = int(input())  # 중간 지점의 수
V = tuple(map(int, input().split()))  # 중간 지점에서의 속력 제한

cur_speed = 0  # 현재 속력
total = 0  # 이동하는 동안의 속력의 합

# 뒤에서부터 각 중간 지점의 속력을 확인하면서 속력을 조절하고 속력의 합을 계산
for v in V[::-1]:
    if cur_speed < v:  # 현재 속력이 이전 지점의 속력보다 작을 경우
        cur_speed += 1  # 현재 속력을 1 더 높임
    else:  # 현재 속력이 이전 지점의 속력보다 크거나 같을 경우
        cur_speed = v  # 현재 속력을 이전 지점의 속력으로 설정

    total += cur_speed  # 이동하는 동안의 속력의 합에 현재 속력을 더함

print(total)  # 최대 연습의 성과 출력
