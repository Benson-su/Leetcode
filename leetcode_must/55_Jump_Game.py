class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_distance = nums[0]
        for i in range(len(nums)):
            if max_distance < i:
                return False
            max_distance = max(max_distance, i + nums[i])
        return True
            
