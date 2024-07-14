import sys
sys.stdin = open("honghak/boj_1069_input.txt", "r")

import math
X, Y, D, T = map(int, input().split())

dist = math.sqrt(X**2 + Y**2)

if dist >= D:
    ans = min(T * (dist // D) + dist % D, T * (dist // D + 1), dist)
else:
    ans = min(T + (D - dist), 2 * T, dist)
print(ans)
