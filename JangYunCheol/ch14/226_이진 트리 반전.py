# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from makeTree import TreeNode,make_tree_by
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def swapTree(node:Optional[TreeNode]):
            if not node:
                return
            if node.left:
                node.left = swapTree(node.left)
            if node.right:
                node.right = swapTree(node.right)
            node.left,node.right=node.right,node.left

            return node


        return swapTree(root)



s = Solution()
makelist = [2,1,3]
makelist2 = [4,2,7,1,3,6,9]
makelist3 = []

print(s.invertTree(make_tree_by(makelist,0)))
print(make_tree_by(makelist,0))