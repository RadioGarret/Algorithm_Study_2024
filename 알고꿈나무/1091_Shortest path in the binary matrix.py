class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        #first checks if the starting cell is blocked(equal to 1). If it is, there is no possible path so the method returns -1
        def valid(row, col):
            return 0 <= row < n and 0 <= col <n and grid[row][col] == 0
        # helper function to check if a given cell is within the matrix bound
        n = len(grid)
        seen = {(0,0)}
        queue = deque([(0,0,1)])
        directions = [(0,1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1),(0,-1),(-1,0)]
                #initialization of visited nodes, directions and queue
        while queue:
            row, col , steps = queue.popleft()
            if (row,col) == (n-1,n-1):
                return steps 
        #BFS LOOP
            for dx, dy in directions:
                next_row, next_col = row+dy, col + dx
                if valid(next_row, next_col) and (next_row,next_col) not in seen:
                    seen.add((next_row,next_col))
                    queue.append((next_row,next_col,steps +1))

            
        return -1
