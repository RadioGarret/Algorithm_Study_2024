import sys
from collections import deque
input = sys.stdin.readline

q = deque()
for _ in range(int(input())):
    oper = input().split()
    if oper[0] == 'push':
        q.append(int(oper[1]))
    elif oper[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif oper[0] == 'size':
        print(len(q))
    elif oper[0] == 'empty':
        print(1 if not q else 0)
    elif oper[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    else:
        if not q:
            print(-1)
        else:
            print(q[-1])

