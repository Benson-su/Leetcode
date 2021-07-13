# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    level_queue = collections.deque()
    ret = []
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.level_queue.clear()
        self.ret = []
        self.level_queue.append(root)
        level = 0
        if root is None:
            return []
        def level_order(level):
            tmp_level = []
            for i in range(len(self.level_queue)):
                item = self.level_queue.popleft()
                if item.left:
                    self.level_queue.append(item.left)
                if item.right:
                    self.level_queue.append(item.right)
                
                tmp_level.append(item.val)
            if level % 2 == 0:
                self.ret.append(tmp_level)
            else:
                tmp_level.reverse()
                self.ret.append(tmp_level)

        while self.level_queue:
            level_order(level)
            level += 1
        return self.ret
        
            
            
            
