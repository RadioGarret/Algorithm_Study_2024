from typing import List
<<<<<<< HEAD
from collections import deque

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        len_arr = len(arr)

        init_arr_idx = []
        for _ in range(len_arr // k):
            init_arr_idx.append(k)
        init_arr_idx.append(len_arr % k)

        visited = set()
        visited.add(init_arr_idx)

        queue = deque()
        queue.append(init_arr_idx)

        while queue:
            arr_idxs = queue.popleft()
            

        

        print()

        pass


=======

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0 for _ in range(n)]
        
        for i in range(n):
            current_max = 0
            # 고려할 부분 배열의 최대 길이는 k
            for j in range(1, k + 1):
                if i - j + 1 >= 0:
                    current_max = max(current_max, arr[i - j + 1])
                    if i - j >= 0:
                        dp[i] = max(dp[i], dp[i - j] + current_max * j)
                    else:
                        dp[i] = max(dp[i], current_max * j)
        
        return dp[-1]
    
    
>>>>>>> f0ea61c7b4c8d408ec5b2400fbe8e40aa8f34623
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3))