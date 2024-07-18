class Solution:
    def knightDialer(self, n: int) -> int:
        can_move = {
            0 : [4, 6],
            1 : [6, 8],
            2 : [7, 9],
            3 : [4, 8],
            4 : [0, 3, 9],
            6 : [0, 1, 7],
            7 : [2, 6],
            8 : [1, 3],
            9 : [2, 4]
        }
        
        dp = [[-1 for _ in range(10)] for _ in range(n+1)]
        
        def dfs(current, k):
            if k == 1:
                dp[k][current] = 1
                return dp[k][current]
            
            if dp[k][current] != -1:
                return dp[k][current]
            
            total = 0
            if current in can_move:
                for move in can_move[current]:
                    total += dfs(move, k-1)
            
            dp[k][current] = total
            return total
            
        for i in range(10):
            dfs(i, n)
            
        return sum(dp[n]) % (10**9 + 7)