class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(s='', left=0, n=0):
            if n == 0:
                self.res.append(s+')'*left)
                return
            if left > 0:
                helper(s+')', left-1, n)
            helper(s+'(', left+1, n-1)
        self.res = []
        helper('', 0, n)
        return self.res
