class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ret = 0
        sub_num1_arr = {}
        for num in nums:
            mutual_sub = num - int(str(num)[::-1])
            sub_num1_arr[mutual_sub] = sub_num1_arr.get(mutual_sub, 0) + 1
        
        for item in sub_num1_arr.values():
            ret += (item*(item-1) / 2)
        
        return ret % (10 ** 9 + 7)
                
            
