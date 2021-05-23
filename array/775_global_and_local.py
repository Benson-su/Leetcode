class Solution(object):
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_value = 0
        for index, value in enumerate(nums[:-2]):
            max_value = max(max_value, value)
            if max_value > nums[index + 2]:
                return False
        return True
