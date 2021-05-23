class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * len(nums)
        prev = -1
        for index, value in enumerate(nums):
            if value < left:
                dp[index] = dp[index - 1]
            elif value > right:
                dp[index] = 0
                prev = index
            else:
                dp[index] = index - prev
        return sum(dp)
