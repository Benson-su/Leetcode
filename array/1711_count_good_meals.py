class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        ret = 0
        for item in deliciousness:
            for i in range(22):
                ret += d[2**i - item]
            d[item] += 1
        return ret % (10**9+7)
