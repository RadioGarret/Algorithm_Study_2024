import sys
from collections import Counter
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
switch = [list(map(int, input().rstrip().split()))[1:] for _ in range(n)]
lamps = Counter(item for row in switch for item in row)

for s in switch:
    flag = False
    for item in s:
        if lamps[item] - 1 == 0:
            flag = True
            break
    if not flag:
        print(1)
        exit()

print(0)
