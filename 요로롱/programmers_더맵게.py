import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        try:
            least = heapq.heappop(scoville)
            # 최소인 값이 K보다 클 경우 나머지 값들 모두 K보다 크다는 성질을 이용
            if least >= K:
                return answer
            less = heapq.heappop(scoville)
            new = least + (less * 2)
            heapq.heappush(scoville, new)
            answer += 1
        except IndexError:
            return -1
