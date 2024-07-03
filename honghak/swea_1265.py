import sys
sys.stdin = open("honghak/swea_1265_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N, P = map(int, input().split())
    
    div = N // P
    mod = N % P
    
    answer = pow(div, P-mod) * pow(div+1, mod)
     
    print(f"#{test_case} {answer}")    
    