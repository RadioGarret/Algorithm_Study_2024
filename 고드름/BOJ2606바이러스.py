from collections import deque

N = int(input()) # 총 컴퓨터 수
M = int(input()) # 연결된 연결선 수
links = [] # 인접 리스트 저장할 공간
for i in range(M):
    links.append(list(map(int, input().split())))
# 총 컴퓨터 수가 100 이라서 재귀가 시간초과 날 것 같으니까 bfs 로 풀어보기
# 1 에서 갈 수 있는 곳 다 가보기
# visited 변경할 때마다 cnt + 1
cnt = 0
queue = deque()
visited = [0] * (N + 1)
# 시작 지점 큐에 넣기
for link in links:
    front, rear = link[0], link[1]
    if front == 1 :
        queue.append(rear)
    elif rear == 1 :
        queue.append(front)
# 시작 지점 방문 처리
visited[1] = 1
# 큐가 비어 있을 때까지 bfs 돌기
while queue:
    now = queue.popleft()
    visited[now] = 1
    cnt += 1
    for link in links:
        front, rear = link[0], link[1]
        if front == now and not visited[rear] and rear not in queue: # 처음에 and rear not in queue 조건 손으로 명시 안 해서 queue 에 중복으로 들어갔었음
            queue.append(rear)
        elif rear == now and not visited[front] and front not in queue: # 처음에 and front not in queue 조건 손으로 명시 안 해서 queue 에 중복으로 들어갔었음
            queue.append(front)
print(cnt)