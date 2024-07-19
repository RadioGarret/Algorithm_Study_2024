class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        N = len(stones)
        dp = [[-1 for _ in range(N)] for _ in range(N)] # turn -> stone -> stone
        dp_pick = []
        
        def dfs(start, end, sub_sum):
            if start > end:
                return 0
            
            if dp[start][end] != -1:
                return dp[start][end]
            
            sub_first = sub_sum - stones[start]
            sub_last = sub_sum - stones[end]
            
            if (end-start) % 2 != mod_stones:
                dp[start][end] = max(dfs(start, end-1, sub_last) + sub_last,\
                    dfs(start+1, end, sub_first) + sub_first)
            else:
                dp[start][end] = min(dfs(start, end-1, sub_last) - sub_last,\
                    dfs(start+1, end, sub_first) - sub_first)
                
            return dp[start][end]
        
        sub_sum = sum(stones)
        mod_stones = len(stones) % 2
        diff = dfs(0, N-1, sub_sum)
        return diff
        