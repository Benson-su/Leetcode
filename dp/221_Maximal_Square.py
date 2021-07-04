class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[300] * n for i in range(m)]
        max_ret = 0
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            max_ret = max(max_ret, dp[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            max_ret = max(max_ret, dp[0][j])

        print(max_ret)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    max_ret = max(max_ret, dp[i][j])
        return max_ret**2
