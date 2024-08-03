def best(x, y, x2, y2):
    count = 0
    for i in range(x, x2+1):
        for j in range(y, y2+1):
            if maps[i][j] >=1:
                count += 1

    return count

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
max_val = -1
for i in range(n-2):
    for j in range(n-2):
        max_val = max(max_val, best(i,j, i+2, j+2))

print(max_val)