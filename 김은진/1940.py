import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
num = sorted(list(map(int, input().split())))

cnt = 0
start, end = 0, len(num)-1

while start < end:
    sum = num[start] + num[end]

    if m > sum:
        start += 1
    elif m < sum:
        end -= 1
    else:
        cnt += 1
        start += 1
        end -= 1

print(cnt)

