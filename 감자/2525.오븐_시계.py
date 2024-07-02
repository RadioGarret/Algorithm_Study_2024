hour, min = map(int, input().split())
time = int(input())

if min+time >= 60:
    plus_h = int((min+time)/60)
    hour += plus_h
    min = min+time - plus_h*60
else:
    min +=time
    
if hour >=24:
    hour -=24

print(int(hour),int(min)) 