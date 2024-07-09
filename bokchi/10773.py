"""
10773 제로
"""
import sys
input = sys.stdin.readline


k = int(input())
stack = []

for _ in range(k):
    x = int(input())
    if x:
        stack.append(x)
    else:
        stack.pop()
print(sum(stack))