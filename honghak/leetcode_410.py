class Solution:
    def canPartition(self, nums, maxSum, k):
        count, currentSum = 1, 0
        for num in nums:
            if currentSum + num > maxSum:
                count += 1
                currentSum = num
                if count > k:
                    return False
            else:
                currentSum += num
        return True

    def splitArray(self, nums, k):
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if self.canPartition(nums, mid, k):
                right = mid - 1
            else:
                left = mid + 1
        return left
        