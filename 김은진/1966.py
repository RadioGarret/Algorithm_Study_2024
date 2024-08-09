from collections import deque  
import sys
input = sys.stdin.readline

t = int(input())  
for _ in range(t):
    n, m = map(int, input().split())   
    numbers = list(map(int, input().split()))  
    
    queue = deque()
    for i in range(n):
        queue.append((numbers[i], i))  

    num = 1  
    numbers.sort(reverse=True)  

    while queue:
        x = queue.popleft()
        
        if x[0] == numbers[num-1]:  
            if x[1] == m: 
                print(num)
                break
            num += 1  
        else:
            queue.append(x) 
            
            
