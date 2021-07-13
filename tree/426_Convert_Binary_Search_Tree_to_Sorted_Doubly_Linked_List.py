"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:return root
        res = []
        def inorder(node):
            if node is None:return
            inorder(node.left)
            res.append(node)
            inorder(node.right)
        inorder(root)
        for i in range(len(res)-1):
            res[i].right = res[i+1]
            res[i+1].left = res[i]
        res[-1].right = res[0]
        res[0].left = res[-1]
        return res[0]
