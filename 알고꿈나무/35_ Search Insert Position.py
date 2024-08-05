class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
# Utilizing binary search!!
        while left <= right:
            mid = (left + right) // 2
            # If the mid element is already a target
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
                # place it right next to the mid element
            else:
                left = mid + 1
        
        return left