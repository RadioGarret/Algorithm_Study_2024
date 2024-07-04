class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # initialize the left , max number of consecutive 1s and the number of zeros 
        left, max_number, zero_count = 0, 0, 0

        for right in range(len(nums)): # start sliding the windows with the right pointer
            if nums[right] == 0 : # if the element that the right pointer is pointing at is 1, increment the zero count
                zero_count +=1 

            while zero_count >k:  #while the zero count is more than k

                if nums[left] == 0:       
                    zero_count -= 1    

                left += 1
                 
            max_number = max(max_number,right-left+1)


        return max_number         
             
