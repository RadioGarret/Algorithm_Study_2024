import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        emptydict = {}
        for i in range(len(nums)):
            num = nums[i]
            addition = target - num 
            if addition in dict:
                return [i, dict[addition]]
            dict[num] = i 

        return [-1, -1]







class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [1, 0]
        self.assertEqual(self.solution.twoSum(nums, target), expected)

    def test_case_2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [2, 1]
        self.assertEqual(self.solution.twoSum(nums, target), expected)

    def test_case_3(self):
        nums = [3, 3]
        target = 6
        expected = [1, 0]
        self.assertEqual(self.solution.twoSum(nums, target), expected)