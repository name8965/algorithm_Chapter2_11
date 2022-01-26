class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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



def serialize( root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    from collections import deque
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

def deserialize( data):
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
    from collections import deque

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
