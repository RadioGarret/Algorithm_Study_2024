import sys
sys.stdin = open("honghak/boj_2042_input.txt", "r")

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1: # change num:
        pass
    else: # cal sub sum
        pass 
        