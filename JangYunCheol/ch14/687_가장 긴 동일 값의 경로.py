# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        count =0
        def detph(node: Optional[TreeNode]):
            nonlocal count
            if not node:
                return 0

            left = detph(node.left)
            right = detph(node.right)
            if node.left and node.val == node.left.val:
                left +=1
            else:
                left =0
            if node.right and node.val == node.right.val:
                right +=1
            else:
                right=0
            count = max(count,left+right)

            return max(left,right)


        detph(root)
        return count




s = Solution()


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
maketree = make_tree_by([5,4,5,1,1,5],0)
makelist = [1,4,5,4,4,5]
print(s.longestUnivaluePath(make_tree_by(makelist,0)))