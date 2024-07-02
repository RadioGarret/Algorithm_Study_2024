"""
Input: nums = [1,2,2,1], k = 1
Output: 4

Input: nums = [1,3], k = 3
Output: 0

Input: nums = [3,2,1,5,4], k = 2
Output: 3

"""

from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        rst = 0
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                a, b = nums[i], nums[j]
                if abs(a-b) == k:
                    rst += 1
        return rst
            
            
if __name__ == "__main__" :
    sol = Solution()
    rst = sol.countKDifference(nums = [1,2,2,1], k = 1)
    print(rst)
    