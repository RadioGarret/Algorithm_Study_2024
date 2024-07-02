import sys
from math import gcd
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ls = list(map(int, input().split()))
    n = len(ls)
    ans = -1
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            ans = max(ans, gcd(ls[i], ls[j]))
    print(ans)