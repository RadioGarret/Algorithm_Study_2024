import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
n_list.sort()

# code1
cnt_dict = {}
for target in targets:
    left = 0
    right = N -1
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        if target < n_list[mid]:
            right = mid - 1
        elif target > n_list[mid]:
            left = mid + 1
        else:
            cnt = cnt_dict[target]
            break
    print(cnt, end = ' ')

# code 2
    
cnt_dict = {}
for n in n_list:
    if n in cnt_dict:
        cnt_dict[n] += 1
    else:
        cnt_dict[n] = 1

for target in targets:
    if target in cnt_dict.keys():
        print(cnt_dict[target], end = ' ')
    else:
        print(0, end = ' ')

# code 3
counter = Counter(n_list)
for target in targets:
    print(counter[target], end = ' ')
