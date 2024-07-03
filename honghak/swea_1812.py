import sys
sys.stdin = open("honghak/swea_1812_input.txt", "r")

import heapq


def cut_tile(m, n, x): 
    if m == x:
        return [(x, n-x)]
    elif n == x:
        return [(m-x, x)]
    else:
        return [(m-x, x), (x, n-x), (m-x, n-x)]
    

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    tile_list = [-pow(2, int(x)) for x in input().split()]
    heapq.heapify(tile_list)
    
    m_tile = [(M, M)]    
    count = 1
    while tile_list:
        x = -heapq.heappop(tile_list)
        updated = False
        
        for i in m_tile:
            if x <= min(i[0], i[1]):
                m_tile.remove(i)
                m_tile += cut_tile(i[0], i[1], x)
                updated = True
                break
            
        if not updated:
            m_tile += cut_tile(M, M, x)
            count += 1        
    
    print(f"#{test_case} {count}")    
    