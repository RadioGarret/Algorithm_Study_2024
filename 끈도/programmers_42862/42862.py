'''####################################################
24.07.04
프로그래머스 42862 체육복
https://school.programmers.co.kr/learn/courses/30/lessons/42862
풀이 전략 : 그리디
'''####################################################


def solution(n, lost, reserve):  # 8시 50분까지 20분
    # 기본은 n-lost
    answer = n - len(lost)
    set_lost = set(lost)
    set_reserve = set(reserve)
    
    set_common = set_lost & set_reserve
    answer += len(set_common)
    
    set_lost -= set_common
    set_reserve -= set_common
    
    # 왼쪽을 확인했다가, 오른쪽을 확인
    for num in set_reserve:  # 이부분을 
        if num - 1 in set_lost:
            set_lost.remove(num - 1)
            answer += 1
        elif num + 1 in set_lost:
            set_lost.remove(num + 1)
            answer += 1
    
            
    return answer
