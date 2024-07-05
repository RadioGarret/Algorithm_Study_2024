import sys
input = sys.stdin.readline

def fact(x):
    if x <= 1:
        return 1
    return fact(x - 1) * x
print(fact(int(input())))
