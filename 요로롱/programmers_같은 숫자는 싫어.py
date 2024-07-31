def solution(arr):
    answer = []
    exp=[]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(0,len(arr)):
        if [arr[i]] != exp[-1:]:
           # print(arr[i],exp[-1:])
            exp.append(arr[i])
        
    return exp
