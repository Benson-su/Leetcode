class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        dp = {}
        for i, a in enumerate(arr):
            dp[a] = 1
            for j in range(i):
                if a % arr[j] == 0 and a / arr[j] in dp:
                    dp[a] += dp[arr[j]] * dp[a / arr[j]]
        return sum(dp.values()) % (10**9 + 7)
