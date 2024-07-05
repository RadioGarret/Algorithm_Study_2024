def running_sum(nums):
    # Initialize the running sum array with the same length as nums
    running_sum_array = [0] * len(nums)
    
    # Set the first element of the running sum array to the first element of nums
    running_sum_array[0] = nums[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # CalculatING the running sum at each position
        running_sum_array[i] = running_sum_array[i - 1] + nums[i]
    
    return running_sum_array