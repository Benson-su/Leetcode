class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ret_num = 0
        cur_max = 0
        for index, value in enumerate(arr):
            cur_max = max(value, cur_max)
            if cur_max <= index:
                ret_num += 1
                continue

        return ret_num
