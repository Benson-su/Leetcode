class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        age_counter = collections.Counter(ages)
        ages = sorted(age_counter.keys())
        ret = 0
        for A in ages:
            for B in range(int(0.5 * A) + 7 + 1, A + 1):
                subtract = A==B
                ret += age_counter[A] * (age_counter[B] - subtract)
        return ret
