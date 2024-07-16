from collections import deque
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_h = 0
for r in range(N):
    for c in range(N):
        if max_h < board[r][c]:
            max_h = board[r][c]
#print(f'max_h:{max_h}')
island = 0 # 아무데도 잠기지 않으면 1이 최소
island_lst = []
visited = [[0]*N for _ in range(N)]
def find_island(depth, sr, sc, island):
    #print(f'{sr},{sc},{depth}에서 find_island 실행됨')
    queue = deque()
    queue.append((sr,sc))
    while queue:
        #print(f'queue:{queue}')
        cr, cc = queue.popleft()
        visited[cr][cc] = 1
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        for d in range(4):
            nr, nc = cr + directions[d][0], cc + directions[d][1]
            if 0<=nr<N and 0<=nc<N:
                if board[nr][nc] > depth and (nr,nc) not in queue and not visited[nr][nc]:
                    queue.append((nr,nc))
    return island + 1

# 물에 잠긴 높이 = depth
# depth 이하이면 물에 잠기고 그보다 크면 물 위에 떠 있음
# find_island
# 물 위에 떠 있는 걸 발견하면 주변 탐색해서 방문 처리하기
# 빠져나올 때 island += 1
# 전체 다 돌아서 전부 다 방문 처리되었을 때 island 를 리스트에 저장
# depth 0부터 max_h 까지 위 작업을 반복하기
# island 리스트에서 최댓값 답으로 출력하기

depth = 0
for depth in range(max_h):
    #print(f'depth:{depth}')
    for r in range(N):
        for c in range(N):
            if board[r][c] > depth and not visited[r][c]:
                island = find_island(depth,r,c,island)
    island_lst.append(island)
    visited = [[0]*N for _ in range(N)] # 방문 표시 배열 초기화
    island = 0 # 섬 개수 초기화

#print(f'island_lst:{island_lst}')
if max(island_lst) == 0:
    print(1)
else:
    print(max(island_lst))