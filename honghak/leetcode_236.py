# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        depth_dict = {}
        parent_dict = {}
        queue = deque()
        queue.append([0, root, -1])
        
        while queue:
            depth, current, parent = queue.popleft()
            
            parent_dict[current.val] = parent
            depth_dict[current.val] = depth
            
            if current.left:
                queue.append([depth+1, current.left, current.val])
            if current.right:
                queue.append([depth+1, current.right, current.val])
            
        
        lca_rst = self.lca(p.val, q.val, depth_dict, parent_dict)
        return TreeNode(lca_rst)
        
    
    def lca(self, p_val, q_val, depth_dict, parent_dict):
        
        while depth_dict[p_val] != depth_dict[q_val]:
            if depth_dict[p_val] > depth_dict[q_val]:
                p_val = parent_dict[p_val]
            else:
                q_val = parent_dict[q_val]
                
        while p_val != q_val:
            p_val = parent_dict[p_val]
            q_val = parent_dict[q_val]
            
        return p_val
    
    
if __name__ == "__main__":
    root = [3,5,1,6,2,0,8,None,None,7,4]
    p = 5
    q = 1
    
    
    tree2 = TreeNode(2)
    tree2.left = TreeNode(7)
    tree2.right = TreeNode(4)
    
    tree5 = TreeNode(5)
    tree5.left = TreeNode(6)
    tree5.right = tree2
    
    tree1 = TreeNode(1)
    tree1.left = TreeNode(0)
    tree1.right = TreeNode(8)
    
    tree3 = TreeNode(3)
    tree3.left = tree5
    tree3.right = tree1
    
    root = tree3
    
    sol = Solution()
    print(sol.lowestCommonAncestor(root, TreeNode(5), TreeNode(1)))