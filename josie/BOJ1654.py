import sys
input = sys.stdin.readline

K, N= map(int, input().split())
cables = [int(input()) for _ in range(K)]

min_len, max_len = 1, max(cables)
while min_len <= max_len:
    mid_len = (min_len+max_len) // 2
    cnt = 0
    for cable in cables:
        cnt += cable // mid_len

    if cnt >= N:
        min_len = mid_len + 1
    else:
        max_len = mid_len - 1
print(max_len)
