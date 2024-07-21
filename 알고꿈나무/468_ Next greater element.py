class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        greatmapping = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                #If the stack exists and top of the stack is smaller than the element from nums2,
                greatmapping[stack.pop()] = num
# we pop the element and map it to our hashmap
            stack.append(num)

        return [greatmapping.get(number, -1) for number in nums1]

            