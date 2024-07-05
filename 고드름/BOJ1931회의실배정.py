def solve(N, meetings):
    # 회의를 끝나는 시간 기준으로 정렬
    # 끝나는 시간이 같으면 시작 시간 기준으로 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))

    # 마지막으로 선택된 회의의 끝나는 시간
    last_end_time = 0
    count = 0

    for start, end in meetings:
        # 현재 회의가 마지막으로 선택된 회의와 겹치지 않으면 선택
        if start >= last_end_time:
            last_end_time = end
            count += 1

    return count

N = int(input().strip())
meetings = []
for _ in range(N):
    start, end = map(int, input().strip().split())
    meetings.append((start, end))

print(solve(N, meetings))