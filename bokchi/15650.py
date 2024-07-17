import sys
input = sys.stdin.readline

def recur(cur, cnt):
    if cnt == m:
        print(*selected)
        return
    if cur == n + 1:
        return
    selected.append(cur)
    recur(cur + 1, cnt + 1)
    selected.pop()
    recur(cur + 1, cnt)

n, m = map(int, input().split())

selected = []
recur(1, 0)