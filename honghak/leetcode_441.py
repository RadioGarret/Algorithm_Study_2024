
from typing import List

class Solution:
    def arrangeCoins(self, n: int) -> int:
        total_coin = 0
        stair = 0
        while True:
            total_coin += stair
            if total_coin > n:
                return stair -1
            stair += 1
            
            
            
if __name__ == "__main__" :
    sol = Solution()
    rst = sol.arrangeCoins(n = 8)
    print(rst)
    