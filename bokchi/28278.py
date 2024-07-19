import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        stack.append(oper[1])
    elif oper[0] == 2:
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif oper[0] == 3:
        print(len(stack))
    elif oper[0] == 4:
        print(0 if stack else 1)
    else:
        print(-1 if not stack else stack[-1])