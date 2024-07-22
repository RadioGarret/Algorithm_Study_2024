import sys
input = sys.stdin.readline

n = int(input())
ls = sorted([int(input()) for _ in range(n)])
ans = 0
for i in range(1, n + 1):
    ans += abs(ls[i - 1] - i)
print(ans)
