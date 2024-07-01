'''####################################################
24.07.01
백준 16236 아기 상어 (골드 3)
https://www.acmicpc.net/problem/16236
풀이 전략 : 
'''####################################################

N = int(input())
Map = [[0] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# shark info(global)
level = 2
level_cnt = 0
x = 0
y = 0
list_food = []
sum_dist = 0

for j in range(N):
    letter = list(map(int, input().split()))
    for i in range(N):
        Map[j][i] = letter[i]
        if letter[i] == 9:
            x = i
            y = j
            Map[j][i] = 0 ########## 이것때문에 틀렸음

while 1:
    # BFS
    Check = [[0] * N for _ in range(N)]
    Q = [(y, x, 0)]
    Check[y][x] = 1
    max_cnt = 0
    list_food = [] ###### 이렇게 했어야지..
    while Q:
        cur_y, cur_x, cur_cnt = Q[0]
        del Q[0]
        for k in range(4):
            ny = cur_y + dy[k]
            nx = cur_x + dx[k]
            max_cnt = cur_cnt + 1
            if 0 <= nx < N and 0 <= ny < N and Map[ny][nx] <= level and Check[ny][nx] == 0:
                Check[ny][nx] = 1
                Q.append((ny, nx, max_cnt))
                if 0 < Map[ny][nx] < level:
                    list_food.append((max_cnt, ny, nx))
    
    list_food = sorted(list_food, key=lambda x: (x[0], x[1], x[2])) ######### 와.. 이거 이렇게 담아야 하는구나.. 
    
    
    # shark moving, eating
    if len(list_food): # end condition
        dist, y, x = list_food[0]
        Map[y][x] = 0 ########### 먹었으면, 0으로 해야지.. 문제에서 단서를 놓쳤다..
        sum_dist += dist
        # del list_food[0] ####### 이게 아니라.. 그냥 list_food 초기화해야지..
        level_cnt += 1

        # shark upgrade
        if level_cnt == level:
            level += 1
            level_cnt = 0
    else:
        break
    
print(sum_dist)
