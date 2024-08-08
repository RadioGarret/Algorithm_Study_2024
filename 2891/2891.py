N,S,R = map(int, input().split())
#팀 수는 필요 없어서 덮어썼다
S = list(map(int, input().split())) # 카약이 손상된 팀 번호
R = list(map(int, input().split())) # 카약이 남는 팀 번호

result = 0 # 출발하지 못하는 팀 수

for i in S:
    if i-1 in R:
        R.remove(i-1)
    elif i+1 in R:
            R.remove(i+1)
    else:
        result+=1
        
print(result)
