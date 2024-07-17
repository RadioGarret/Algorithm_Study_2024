import sys
input = sys.stdin.readline

while 1:
    n = int(input())
    if n == -1:
        break
    yaksoo = []
    for i in range(1,  int(n ** 0.5) + 1):
        if n % i == 0:
            yaksoo.append(i)
            if i * i != n:
                yaksoo.append(n // i)
    yaksoo.sort()
    if sum(yaksoo[:-1]) == n:
        print(f"{n} = ",end='')
        print(' + '.join(map(str, yaksoo[:-1])))
    else:
        print(f"{n} is NOT perfect.")