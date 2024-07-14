from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(2)] # turn -> start -> end
        
        def dfs(start, end, is_alice):
            if start > end:
                return 0
            
            if dp[is_alice][start][end] != -1:
                return dp[is_alice][start][end]
            
            if is_alice: # alice turn
                dp[is_alice][start][end] = max(dfs(start+1, end, 0) + piles[start], dfs(start, end-1, 0) + piles[end])
                
            else:
                dp[is_alice][start][end] = min(-piles[start] + dfs(start+1, end, 1),-piles[end] +  dfs(start, end-1, 1))
                
            return dp[is_alice][start][end]
        
        
        res = dfs(0, n-1, 1)
        return res >= 0
    
    
sol = Solution()
print(sol.stoneGame(piles=[5, 3, 4, 5]))