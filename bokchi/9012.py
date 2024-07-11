import sys
input = sys.stdin.readline

def check_vps(x):
    stack = []
    for i in x:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            if stack[-1] != '(':
                return False
            stack.pop()
    return not stack

for _ in range(int(input())):
    s = input().strip()
    print('YES'if check_vps(s) else 'NO')
