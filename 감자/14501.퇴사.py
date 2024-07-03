days = int(input())
t_and_p = []

for i in range(days):
    t_and_p.append(list(map(int,input().split())))

profits=0

n = 0 # day of work
while n < days:
    if n + t_and_p[n][0] > days:
        break
    print(t_and_p[n][1])
    profits += t_and_p[n][1]
    n += t_and_p[n][0]

print(profits)
                           