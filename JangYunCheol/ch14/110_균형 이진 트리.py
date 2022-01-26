# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from makeTree import TreeNode,deserialize

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(node):
            if not node:
                return 0
            return 1 + max(getDepth(node.left),getDepth(node.right))

        if not root:
            return True

        return abs(getDepth(root.left) - getDepth(root.right)) <= 1and self.isBalanced(root.left) and self.isBalanced(root.right)


s = Solution()
print(s.isBalanced(deserialize("[3,9,20,None,None,15,7]")))



