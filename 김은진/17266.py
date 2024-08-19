N = int(input())
M = int(input())
x = [*map(int, input().split())]
s, e = 0, N
ans = 0
while s <= e:
    mid = (s + e) // 2
    prev = 0
    for v in x:
        if v - mid > prev:
            break
        prev = v + mid
    if prev >= N:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
print(ans)
