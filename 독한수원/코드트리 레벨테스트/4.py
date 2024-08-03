import sys
sys.setrecursionlimit(100000)

def recursion(x,n):
    if len(x) >= n:
        if x.count('1') >= 3 and x.count('2') >=3:
            print(x)
    else:
        x += '1'
        x += '2'
        x += '3'
    # print(x)
n = int(input())
recursion('', n)