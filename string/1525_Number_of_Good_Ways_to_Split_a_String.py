import collections
class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        left = set()
        right = set(s)
        deq = collections.deque(s)
        for _ in range(len(s)-1):
            popped = deq.popleft()
            left.add(popped)
            if popped not in deq:
                right.remove(popped)
            if len(left) == len(right):
                count += 1
        return count
