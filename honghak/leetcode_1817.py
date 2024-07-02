"""
Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
Output: [0,2,0,0,0]
"""

from typing import List
from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        uam_list = [0 for _ in range(k)]
        
        id_dict = defaultdict(dict)
        
        for log in logs:
            _id, _time = log[0], log[1]
            id_dict[_id][_time] = 0 
            
        for time_dict in id_dict.values():
            uam_list[len(time_dict.keys()) - 1] += 1
            
        return uam_list
            
            
if __name__ == "__main__" :
    sol = Solution()
    rst = sol.findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4)
    