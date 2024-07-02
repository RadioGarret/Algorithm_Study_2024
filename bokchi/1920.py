import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

# 이분탐색 풀이 (624ms)
# for i in target:
#     s = 0
#     e = n - 1
#     flag = False
#     while s <= e:
#         mid = (s + e) // 2
#         if arr[mid] == i:
#             flag = True
#             break
#         if arr[mid] < i:
#             s = mid + 1
#         else:
#             e = mid - 1
#     print(int(flag))

# map풀이 (216ms)
cnt = defaultdict(int)
for i in arr:
    cnt[i] = 1
for i in target:
    print(cnt[i])
