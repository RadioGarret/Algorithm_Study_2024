# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pass

    def get_depth(self, root, p, q):
        queue = deque()
        queue.append(root)

        depth = 0
        while queue:
            parent = queue.popleft()
            if parent.val == p.val:
                depth1 = depth

            elif parent.val == q.val:
                depth2 = depth

            else:
                if parent.left is not None:
                    queue.append(parent.left)
                if parent.right is not None:
                    queue.append(parent.right)

                depth += 1
            


    def lca():
        pass
