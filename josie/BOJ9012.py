import sys
input = sys.stdin.readline

T = int(input())

def solution():
    ps = []
    for i in input():
        if i == "(":
            ps.append(i)
        elif i == ")":
            if ps: # ps matched!
                ps.pop()                
            else: # there's no left ps
                return "NO"
    if ps: # left ps left
        return "NO"
    else:
        return "YES"

for _ in range(T):
    print(solution())
