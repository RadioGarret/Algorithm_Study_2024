'''
[백준] 14888. 연산자 끼워넣기
'''

'''
문제 이해: N개의 수열이 주어지고 N-1개의 연산자를 끼워 넣는다. 이때 수의 순서는 바꿀 수 없다.
연산자는 덧셈, 뺄셈, 곱셈, 나눗셈(몫만 취함)으로 이루어져 있다.
식의 계산은 앞에서부터 진행한다. 연산 결과는 무조건 정수 

풀이: 연산자 배치를 어떻게 구현할지 모르겠다.
스택이나 큐를 사용해야 하나?
'''

N = int(input())

numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_val = -1e9 # e가 지수를 의미 -1 * 10의 9승 (10의 9승은 10억)
min_val = 1e9

def dfs(idx, num):

    global max_val, min_val

    if idx == N-1:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return

    if operators[0] > 0:
        operators[0] -= 1
        dfs(idx+1, num + numbers[idx+1])
        operators[0] += 1
    if operators[1] > 0:
        operators[1] -= 1
        dfs(idx+1, num - numbers[idx+1])
        operators[1] += 1

    if operators[2] > 0:
        operators[2] -= 1
        dfs(idx+1, num * numbers[idx+1])
        operators[2] += 1

    if operators[3] > 0:
        operators[3] -= 1
        dfs(idx+1, int(num/numbers[idx+1]))
        operators[3] += 1


dfs(0, numbers[0])
print(max_val)
print(min_val)