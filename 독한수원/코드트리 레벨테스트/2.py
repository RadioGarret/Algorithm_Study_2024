a, b, c= map(int, input().split())
sums = 0
for i in range(a,b+1):
    if i % c == 0:
        sums += i

print(sums)