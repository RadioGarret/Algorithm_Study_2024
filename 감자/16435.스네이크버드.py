# silver 5
fruits, length = map(int, input().split())
height = list(map(int, input().split()))

height.sort()

for i in range(fruits):
    if length >= height[i]:
        length +=1

print(length)