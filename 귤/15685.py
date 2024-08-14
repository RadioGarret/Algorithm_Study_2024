import sys
input = sys.stdin.readline

N = int(input())

board = [[False] * 101 for _ in range(101)]

directs = [(1, 0), (0, -1), (-1, 0), (0, 1)] #dx, dy

for _ in range(N):
    x, y, d, g = map(int, input().split())
    
    v = [(x, y)]
    pivot = (x + directs[d][0], y + directs[d][1])
    v.append(pivot)
    
    board[y][x] = True
    board[pivot[1]][pivot[0]] = True

    def draw_curve(vertices, pivot, count):
        if count == 0:
            return
        else:
            new_vertices = []
            for idx, coord in enumerate(vertices):
                px, py = pivot
                x, y = coord
                nx, ny = -y + py + px, x - px + py
                if idx == 0:
                    new_pivot = nx, ny
                new_vertices.append((nx, ny))
                board[ny][nx] = True
            vertices.extend(new_vertices)
            draw_curve(vertices, new_pivot, count - 1)
    
    draw_curve(v, pivot, g)

answer = 0       
for i in range(100):
    for j in range(100):
        if board[i][j] == True and board[i+1][j] == True and board[i][j+1] == True and board[i+1][j+1] == True:
            answer += 1
            
print(answer)
