import sys
sys.stdin = open("honghak/boj_14003_input.txt", "r")

import sys
input = sys.stdin.readline

N=int(input())
arr = list(map(int,input().split()))

dp = [arr[0]]
dp_list = [(0,arr[0])]

def binarySearch(e):
    left = 0
    right = len(dp) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if dp[mid] == e:
            return mid
        elif dp[mid] < e:
            left = mid + 1
        else:
            right = mid - 1
            
    return left


for i in range(1,N):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
        dp_list.append((len(dp)-1, arr[i]))

    else:
        idx = binarySearch(arr[i])
        dp[idx] = arr[i]
        dp_list.append((idx, arr[i]))


print(len(dp))

count = len(dp) - 1
res = []
for i in range(len(dp_list)-1, -1, -1):
    idx, value = dp_list[i]
    if idx == count:
        res.append(value)
        count-=1

print(*res[::-1])