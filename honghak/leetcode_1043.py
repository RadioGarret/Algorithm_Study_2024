from typing import List
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


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3))