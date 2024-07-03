
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        len_citations = len(citations)
        left, right = 0, len_citations -1
        
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] == len_citations - mid:
                return citations[mid]
            
            if citations[mid] > len_citations - mid:
                right = mid -1
                
            if citations[mid] < len_citations - mid:
                left = mid + 1
        
        return len_citations - left
        
            
            
if __name__ == "__main__" :
    sol = Solution()
    rst = sol.hIndex(citations = [0, 1, 3, 5, 6])
    print(rst)
    