# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from makeTree import TreeNode,make_list_by_Tree
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1,root2):
            if not root1:
                return root2
            if not root2:
                return root1

            root3 = TreeNode(root1.val+root2.val)
            root3.left = merge(root1.left,root2.left)
            root3.right = merge(root1.right,root2.right)

            return root3
        return merge(root1,root2)


def make_Tree_by_list(root):
    if not root:
        return []
    from collections import deque
    q = deque([root])
    lst = []

    while q:
        node = q.popleft()
        lst.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return lst


s = Solution()
print(s.mergeTrees(make_list_by_Tree([1,3,2,5],0),make_list_by_Tree([2,1,3,None,4,None,7],0)))
print("test")
