class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-1>=0:
                    matrix[i][j]^=matrix[i-1][j]
                if j-1>=0:
                    matrix[i][j]^=matrix[i][j-1]
                if i-1>=0 and j-1>=0:
                    matrix[i][j]^=matrix[i-1][j-1]
                l.append(matrix[i][j])

        l.sort(reverse=True)
        return l[k-1]
