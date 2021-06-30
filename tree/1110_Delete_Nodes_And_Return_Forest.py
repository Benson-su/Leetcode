# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        ds = set(to_delete)
        res = []
        def dfs(root):
            if root is None: return
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root.val not in ds:return root
            if root.left: res.append(root.left)
            if root.right: res.append(root.right)
            return None
        root = dfs(root)
        if root: res.append(root)
        return res
