import sys
sys.stdin = open("honghak/boj_3085_input.txt", "r")

import sys
input = sys.stdin.readline

N = int(input())

arr = [list(input().rstrip()) for _ in range(N)]

def get_max_countinue(sub_arr):
    prev = sub_arr[0]
    count = 1
    max_count = count
    for i in range(1, N):
        if prev == sub_arr[i]:
            count += 1

        if prev != sub_arr[i]:
            max_count = max(max_count, count)
            count = 1
            prev = sub_arr[i]

    max_count = max(max_count, count)
    return max_count

def check_rows():
    max_count = 0
    for i in range(N):
        count = get_max_countinue(arr[i])
        max_count = max(max_count, count)

    return max_count

def check_cols():
    max_count = 0
    for i in range(N):
        cols = []
        for j in range(N):
            cols.append(arr[j][i])

        count = get_max_countinue(cols)
        max_count = max(max_count, count)

    return max_count

def swap_value(i,j, dx, dy):
    tmp = arr[i][j]
    arr[i][j] = arr[dx][dy]
    arr[dx][dy] = tmp

swaps = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
total_max = 0
dp = {}

for i in range(N):
    for j in range(N):
        for swap in swaps:
            dx, dy = i + swap[0], j + swap[1]
            if 0 <= dx < N and 0 <= dy < N:
                if (i, j, dx, dy) not in dp or (dx, dy, i, j) not in dp:
                    swap_value(i, j, dx, dy)
                    total_max = max(total_max, check_rows(), check_cols())
                    swap_value(dx, dy, i, j)
                    dp[(i, j, dx, dy)] = 1
                    dp[(dx, dy, i, j)] = 1

print(total_max)