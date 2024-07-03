class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        
        seen = set()
        
        def dfs(total):
            if total == target:
                return True
            
            if total in seen or total < 0 or total > x + y:
                return False
            
            
            seen.add(total)
            
            return dfs(total - x) or dfs(total + x) or dfs(total - y) or dfs(total + y)
        
        return dfs(0)
    
    
    
if __name__ == "__main__":
    sol = Solution()
    rst = sol.canMeasureWater(x = 1, y = 2, target = 3)
    print(rst)