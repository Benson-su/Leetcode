import sys
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0
        left = []
        right = []
        nums.sort()
        for i in range(4):
            left.append(nums[i])
            right.append(nums[-(4-i)])
        min_diff = sys.maxint
        for i in range(len(left)):
            min_diff = min(min_diff, right[i] - left[i])
        return min_diff
