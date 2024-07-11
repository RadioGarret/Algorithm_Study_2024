# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        node_p = self.in_order_search(p)
        node_q = self.in_order_search(q)
        

    def in_order_search(self, parent:TreeNode = None):
        nodes = [parent.value]
        return nodes.extends(self.in_order_search(parent.left) + self.in_order_search(parent.right))
    