class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ret = 0
        set_A = set(arr)
        max_len = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                first = arr[i]
                second = arr[j]
                target = first + second
                tmp_len = 2
                while target in set_A:
                    first = second
                    second = target
                    target = first + second
                    tmp_len += 1
                    max_len = max(max_len, tmp_len)
        return max_len if len(arr) > 2 else 0
