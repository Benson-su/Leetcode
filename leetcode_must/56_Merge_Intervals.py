class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()  # Sort by increasing order of the starting time
        ans = []
        n, i = len(intervals), 0
        while i < n:
            start, end = intervals[i]
            i += 1
            while i < n and end >= intervals[i][0]:
                end = max(end, intervals[i][1])
                i += 1
            ans.append([start, end])
        return ans
