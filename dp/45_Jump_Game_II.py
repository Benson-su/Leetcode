class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_num = len(nums)
        dp = [sys.maxint] * length_num
        dp[0] = 0
        for i in range(length_num):
            for j in range(i+1, i + nums[i]+1):
                if j < length_num:
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]
