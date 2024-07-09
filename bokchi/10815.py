"""
10815 숫자 카드
"""

import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in b:
    print(int(i in a), end=' ')