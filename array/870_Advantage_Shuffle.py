class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(A)
        A = collections.deque(sorted(A))
        
        B = collections.deque(sorted((b, i) for i, b in enumerate(B)))
        print(B)
        for i in range(len(A)):
            a = A.popleft()
            b = B[0]
            if a > b[0]:
                B.popleft()
            else:
                b = B.pop()
            res[b[1]] = a
        return res

