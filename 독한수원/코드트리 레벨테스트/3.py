n, k = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))
    
count = 0

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
for x in range(r1, r2+1):
    for y in range(c1, c2+1):
        if maps[x][y] <= k:
            count +=1
            
print(count)