import sys
input = sys.stdin.readline

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
ls.sort(key=lambda x:(x[1], x[0]))

ans = 1
end = ls[0][1]
for i in range(1, n):
    if ls[i][0] >= end:
        ans += 1
        end = ls[i][1]
print(ans)