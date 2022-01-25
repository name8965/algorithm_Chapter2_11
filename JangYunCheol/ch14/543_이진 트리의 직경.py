# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def depth(node:Optional[TreeNode]):
            nonlocal count

            left = 0
            right = 0
            if node.left:
                left = depth(node.left)
            if node.right:
                right = depth(node.right)


            count = max(count,(right+left))
            return max(left,right)+1
        count =0

        depth(root)
        return count

def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value == None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent




s = Solution()
t = [TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(5)]
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
f = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = f
# print
lst = [1,2,3,4,5]
root = make_tree_by(lst,0)
print(s.diameterOfBinaryTree(root))