import sys
input = sys.stdin.readline

def slice(x,y,n):
    tmp = colored_paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if colored_paper[i][j] != tmp:
                slice(x, y, n//2)
                slice(x+n//2, y, n//2)
                slice(x, y+n//2, n//2)
                slice(x+n//2, y+n//2, n//2)
                return
    
    if tmp == 0:
        cnt[0] += 1
    else:
        cnt[1] += 1

        
n = int(input())
colored_paper = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0]

slice(0, 0, n)
print(cnt[0])
print(cnt[1])
