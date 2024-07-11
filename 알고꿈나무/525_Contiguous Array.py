class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        hash_map = {0: -1}
        max_length = 0 
        current_sum =0 
    
        for i,num in enumerate(nums):

            current_sum +=1 if num==1 else -1
        
            if current_sum in hash_map:
                max_length = max(max_length, i- hash_map[current_sum])
            else:
                hash_map[current_sum] = i
        return max_length