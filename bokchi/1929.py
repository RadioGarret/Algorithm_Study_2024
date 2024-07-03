# 소수 구하기 실버 3
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

is_prime = [True] * 1000001
is_prime[0] = is_prime[1] = False
for i in range(2, 1000001):
    if not is_prime[i]:
        continue
    for j in range(i * i, 1000001, i):
        is_prime[j] = False

for i in range(n, m + 1):
    if is_prime[i]: print(i)