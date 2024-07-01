number = int(input())
n = list(map(int, input().split()))
goal = int(input())

count = 0 
for i in range(number):
    if goal == n[i]:
        count+=1
        
print(count)
