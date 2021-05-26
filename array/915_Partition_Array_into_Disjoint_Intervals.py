class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_length = 1
        max_left = nums[0]
        max_cur = nums[0]
        for i in range(1, len(nums)):
            max_cur = max(max_cur, nums[i])
            if  max_left > nums[i]:
                min_length = i + 1
                max_left = max_cur

        return min_length
