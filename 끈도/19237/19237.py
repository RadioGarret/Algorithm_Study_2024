'''####################################################
24.07.02
백준 19237 어른 상어 (골드 2)
https://www.acmicpc.net/problem/19237
풀이 전략 :  
'''####################################################
import copy
# 방향 숫자 전부 -1할거다. (북 : 0, 남 : 1, 서 : 2, 동 : 3)
# 이동 조건 : 주변에 냄새가 남아있으면, 내 냄새가 남아있는곳으로 가야한다. 

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M, K = map(int, input().split())
# gMap = [상어 번호, 상어방향, 냄새] 
# gDir = [행 : 몇번째 상어, 열 : ]
gMap = [ [[0, 0, 0] for _ in range(N)] for _ in range(N) ]
gDir = [ [[] for _ in range(4) ] for _ in range(M + 1)] # M rows, 4 cols, 4 directions 

# map generation
for j in range(N):
    line = list(map(int, input().split()))
    for i in range(N):
        gMap[j][i][0] = line[i]

# shark dir
line = list(map(int, input().split()))
for m in range(1, M + 1):#################### 상어 번호 1부터 시작
    # searc
    for j in range(N):
        for i in range(N):
            if gMap[j][i][0] == m:
                gMap[j][i][1] = line[m-1] - 1 #################### 상어 번호 1부터 시작
                gMap[j][i][2] = K # 냄새 초기화

# shark direction info generation
for m in range(1, M + 1): ####################
    for i in range(4): # north, south, west, east
        gDir[m][i] = list(map(int, input().split()))
        for k in range(4):
            gDir[m][i][k] -= 1 # index를 0으로 맞추기 위함.

gmax_shark_num = M # 이게 1이면 종료

def OtherDir(dir):
    result = 0
    if dir == 0:
        result = 1
    elif dir == 1:
        result = 0
    elif dir == 2:
        result = 3
    elif dir == 3:
        result = 2
    return result

def OneSharkMove(shark_num, sy, sx, Map):# gMap = [상어 번호, 상어방향, 냄새]
    global gMap
    # 3. SharkMove 할때는 이동하기 전의 자리에는 상어번호와 k의 냄새를 남긴다. 
    # 그리고 상어가 이동한 자리는 냄새가 k+1이다. 
    # 상어 이동후에는 Map 업데이트 해줄때, 이동한 방향으로 상어 방향을 바꿔줘야함. 
    # 상어가 이동하고난 자리는 상어번호를 음수로 바꾼다. 냄새는 양수. : 상어 위치 검색할 때 양수로 검색하기 위해. 
    sdir = Map[sy][sx][1] # 현재 바라보는 방향
    odir = OtherDir(sdir)
    flag = 0
    for k in range(4): # 돌아가지 않는 길에서, 가야하는 길 방향 구하기
        ndir = gDir[shark_num][sdir][k]
        # if ndir == odir: #### 씨발... 원래 이렇게 했었는데.. 지나갔던길을 다시 가는게 무조건 반대로 돌아가는것밖에 없다고 생각했네
        #     continue

        nsy, nsx = sy + dy[ndir], sx + dx[ndir]

        if 0 <= nsy < N and 0 <= nsx < N:
            if Map[nsy][nsx][0] == -shark_num and Map[nsy][nsx][2] != 0: # 일단 다시 돌아가지는 말아봐봐...
                continue 
            
            ############## 애초에 아래처럼 짜면 안된다... 문제 말대로 그대로 짜자... 편의상 이렇게 짜지 말고..
            ############# 원래는 Map을 모든 상어가 지나간다음에 바꿔야했다. 그리고, 겹치게 될 경우에만 없애면 되잖아. 
            if gMap[nsy][nsx][0] == 0 and 0 < Map[nsy][nsx][0] < shark_num: # 원래는 비어있었는데, 쎈상어가 이동했어. 그러면 상어 삭제
                Map[sy][sx][0] = -Map[sy][sx][0] # 상어번호 음수###################### 근데 중요한건, 쎈상어가 되돌아온것이라면, 가면 안됨.
                flag = 1 # 사실 리턴 해버리기때문에 이거 상관 없다. 그러나 시각의 용이성을 위해..
                return

            # 갈 수 있는 곳인지 체크 : 안에있고, 내가 지나온 길이거나, 다른 상어 흔적이 남아있지 않아야함.
            if Map[nsy][nsx][0] == -shark_num or Map[nsy][nsx][0] == 0:
                Map[nsy][nsx][0] = shark_num
                Map[nsy][nsx][1] = ndir
                Map[nsy][nsx][2] = K + 1 # 냄새
                Map[sy][sx][0] = -shark_num # 지나온 곳은 상어번호 음수
                flag = 1
                return
        
    if flag == 0: ########## 왔던 방향으로 돌아가기기.  이걸 이렇게 코딩했어야 했어
        for k in range(4):
            ndir = gDir[shark_num][sdir][k]
            nsy, nsx = sy + dy[ndir], sx + dx[ndir]
            if 0 <= nsy < N and 0 <= nsx < N and Map[nsy][nsx][0] == -shark_num and Map[nsy][nsx][2] != 0:
                Map[nsy][nsx][0] = shark_num
                Map[nsy][nsx][1] = ndir
                Map[nsy][nsx][2] = K + 1 # 냄새
                Map[sy][sx][0] = -shark_num # 지나온 곳은 상어번호 음수
                return

def SmellDiscount_MaxSharkNum():
    global gmax_shark_num, gMap
    temp_max = -1
    for j in range(N):
        for i in range(N):
            if gMap[j][i][2] != 0: # 냄새가 있다면
                gMap[j][i][2] -= 1
                if gMap[j][i][2] == 0: # 냄새가 사라졌다면
                    gMap[j][i][0], gMap[j][i][1], gMap[j][i][2] = 0, 0, 0
            temp_max = max(temp_max, gMap[j][i][0])
        # 맵 탐색하며 최대값 알아내기
        # gmax_shark_num = max(gmax_shark_num, gMap[j][i][0]) ######## 하.. 씨발 이렇게 하면 안되잖아.. 점점 줄어들어야하는데..
    gmax_shark_num = temp_max
    

def SharkMove(): # 모든 상어가 이동한 다음에 map을 갱신해야함.
    global gMap 
    temp_Map = copy.deepcopy(gMap)############
    for shark_num in range(1, M+1): 
        sx, sy = 0, 0 # 상어 위치 초기화
        shark_present = 0 ###################
        # shark search
        for j in range(N):
            for i in range(N):
                if temp_Map[j][i][0] == shark_num:
                    sy = j
                    sx = i
                    shark_present = 1 #############
        if shark_present:
            OneSharkMove(shark_num, sy, sx, temp_Map)
    gMap = copy.deepcopy(temp_Map)

# max_shark_num == 1이면 종료
  
#while문 돌리면서 1000초가 넘으면 -1 출력
cnt = 1
while(cnt != 1001):

    SharkMove()
    SmellDiscount_MaxSharkNum()
    if gmax_shark_num == 1:
        break
    cnt += 1

if gmax_shark_num == 1:
    print(cnt)
else:
    print(-1)


# 상어 : 지금 보고 있는 방향
# 1. Map([상어번호, 방향, 냄새]), 우선순위 Table(M) 입력받기 , max_shark_num = M 
# 2. # 1. 숫자가 낮은 상어부터 움직이는데, 숫자가 높은 상어는 숫자가 낮은 상어 위치로 이동했을 때, 사라진다. 
#  Onesharkmove 
# 3. SharkMove 할때는 이동하기 전의 자리에는 -상어번호와 k의 냄새를 남긴다
# 상어 이동후에는 Map 업데이트 해줄때, 이동한 방향으로 상어 방향을 바꿔줘야함. 
# 4. 상어가 이동(SharkMove) 하고나서 전체적으로 냄새를 하나씩 깎는다(냄새가 0이면 상어표시도 없애야한다.)
# 5. 종료조건 체크함수 : max_shark_num==1일때



# 결국 내가 고려하지 못한것은, 상어 두마리가 겹쳤을 때, 한마리를 없애주는건데, 
# 기존에 비어있던 자리로 두마리가 가는 경우에 상어 한마리를 없애주는거지
# 쎈 상어가 지가 갔던 길 되돌아가는자리로 다시 가면, 그 자리는 원래는 비어있던 자리가 아닌데, 
# 내가 짠 병신같은 코드는, 그냥 쎈 상어 있는곳으로 가면 약한상어 없애버리는 코드이고, 
# 모든 상어가 다 돈 다음에 맵을 업데이트 하는게 아니라, 상어 한마리 한마리 이동할 때 마다 업데이트 해버려서
# 결국, 약한상어가, 기존에 쎈상어가 지나갔던 길로 가버리는 경우가 발생한다. 

# 그리고 두번째로, 지나갔던 길로 다시 되돌아가는것을 'back'한다고 생각만 했는데, 
# 그게 아니라, 어쨋든 지나갔던 길로 다시 돌아가게되는 순간이 오는데(예를들어 한바퀴 돌아서 다시 온다는경우)
# 무조건 다시 되돌아가는것을 '뒷걸음질' 만으로 생각하면 위의 상황이 고려가 안된다. 
