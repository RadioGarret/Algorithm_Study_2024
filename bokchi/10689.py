import sys
input = sys.stdin.readline


for tc in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    cnt = len(set(ls)) # 카테고리의 총 개수
    visited = set()
    for i in range(n):
        visited.add(ls[i])
        if len(visited) == cnt:
            print(f'Case {tc+1}: {i + 1}')
            break