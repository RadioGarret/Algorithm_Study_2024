class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # fixed window size, so we keep current window size as 0
        curr = 0
        for i in range(k):
            curr += nums[i]
            
        ans = curr #initializing answer to curr which is the sum of first k elements
        for i in range(k, len(nums)):  # sliding window calculation
            curr += nums[i] - nums[i - k]  # we add and remove one element at a time to make sure k stays same
            ans = max(ans, curr)  # ans updated to be the maximum of ans and curr
            
        return ans/k  # maximum sum divided by k to get the average
        
