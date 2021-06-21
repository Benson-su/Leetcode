class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]
        
        for i in range(len(matrix)):
            if matrix[i][0] == 1:
                dp[i][0] = 1

        for i in range(len(matrix[0])):
            if matrix[0][i] == 1:
                dp[0][i] = 1
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result += dp[i][j]
        
        return result
