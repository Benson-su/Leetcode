class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        j = 0
        for i in range(len(nums)):
            while j < len(groups):
                if i + len(groups[j]) <= len(nums):
                    if groups[j] == nums[i:len(groups[j]) + i]:
                        
                        i = i + len(groups[j])
                        j += 1
                    else:
                        i = i + 1
                else:
                    return False
            return True
