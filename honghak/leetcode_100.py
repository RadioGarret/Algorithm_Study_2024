from typing import Optional
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p, q))
        
        while queue:
            local_p, local_q = queue.popleft()
            if local_p is None and local_q is None: # both None
                continue
            
            if local_p is not None and local_q is None: # local_q None
                return False
            
            if local_p is None and local_q is not None: # local_p None
                return False
                
            if local_p.val != local_q.val:
                return False
            
            queue.append((local_p.left, local_q.left))
            queue.append((local_p.right, local_q.right))
        
        return True