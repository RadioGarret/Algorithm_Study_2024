import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
sortList = sorted(list(set(x)))

# -10 -9 2 4 4
for target in x:
    left = 0
    right = len(sortList) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > sortList[mid]:
            left = mid + 1
        elif target < sortList[mid]:
            right = mid - 1
        else: # target == sortList[mid]
            print(mid, end=' ')
            break