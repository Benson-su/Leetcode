class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        dp = [[0 for j in range(n)] for i in range(m)]
        max_len = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
        return max_len

