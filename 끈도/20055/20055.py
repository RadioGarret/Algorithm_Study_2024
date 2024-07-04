'''####################################################
24.07.03
백준 20055 컨베이어 벨트 위의 로봇 (골드 5)
https://www.acmicpc.net/problem/20055
풀이 전략 :  구현
'''####################################################

# 내구도 감소 요인 
# 로봇이 이동하면 내구도 -1 / 로봇 이동 조건은 2가지 RobotMove()
# 로봇을 올려놓으면 내구도 -1  RobotIn()
# 로봇이 끝자리 가면 무조건 아웃 RobotOut()
N, K = map(int, input().split()) # K는 내구도 0인 칸의 갯수가 K개면 종료
durab = [0] * 2 * N # Rotate하면 내구도 맨 앞에껄 없애버리고 맨뒤로 append
durab = list(map(int, input().split()))

belt = [0] * N # robot의 위치를 표현

def RobotOut():
    belt[-1] = 0

def RobotIn():
    global belt, durab
    if durab[0] != 0:
        belt[0] = 1
        durab[0] -= 1

def RobotMove():
    global belt, durab
    for i in range(N-2, 0, -1): # 끝에서 두번째부터 1번 인덱스까지
        if belt[i] == 1 and belt[i+1] == 0 and durab[i+1] != 0:
            belt[i+1] = 1
            belt[i] = 0
            durab[i+1] -= 1
    RobotOut() ###### 이걸 안해줬다..

def Rotate():
    global belt, durab
    durab.insert(0, durab[-1]) # 내구도 로테이션
    del durab[-1]
    del belt[-1] # 벨트 로테이션 및 자동으로 RobotOut()
    belt.insert(0, 0)
    RobotOut()  ####### 이걸 안해줬다...

step = 0
while 1:
    Rotate()
    RobotMove()
    RobotIn()
    step += 1
    if durab.count(0) >= K:
        break

print(step)
