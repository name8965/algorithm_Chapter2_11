# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None

        serialize = []
        q = deque([root])

        while q:
            root = q.popleft()

            if root:
                serialize.append(root.val)
                q.append(root.left)
                q.append(root.right)
            else:
                serialize.append(None)

        return str(serialize)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.strip("[]").split(",")
        n = len(data)
        for i in range(n):
            data[i] = data[i].replace(" ", "")
            if data[i] == "None":
                data[i] = None
            else:
                data[i] = int(data[i])

        root = TreeNode(data.pop(0))
        pointer = root
        q = deque([root])

        while q and data:
            root = q.popleft()

            if data:
                val = data.pop(0)
                if val is not None:
                    root.left = TreeNode(val)
                    q.append(root.left)
            if data:
                val = data.pop(0)
                if val is not None:
                    root.right = TreeNode(val)
                    q.append(root.right)

        return pointer


    """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """



def make_list_by_Tree(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value == None:
            return

        parent = TreeNode(value)
        parent.left = make_list_by_Tree(lst, 2 * idx + 1)
        parent.right = make_list_by_Tree(lst, 2 * idx + 2)

    return parent

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

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
s = Codec()
d = Codec()
e = s.deserialize("[1,2,3,None,None,4,5,6,7]")
a = s.serialize(make_list_by_Tree([1,2,3,None,None,4,5,6,7],0))
b = make_list_by_Tree([1,2,3,None,None,4,5,6,7],0)
c = d.deserialize(s.serialize(make_list_by_Tree([1,2,3,None,None,4,5,6,7],0)))
print(d.deserialize(s.serialize(make_list_by_Tree([1,2,3,None,None,4,5],0))))
print("test")