class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val =0 
        total =0 

        for num in nums:
            total+= num
            min_val = min(min_val, total)
        #  change the minimum step-by-step total to 1
        return -min_val + 1