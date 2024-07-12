import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))
meetings = deque(meetings)
cnt = 1
time = meetings.popleft()
while meetings:
    new_time = meetings.popleft()
    if new_time[0] < time[1]:
        continue
    else: # >=
       cnt += 1
       time = new_time
       
print(cnt)
