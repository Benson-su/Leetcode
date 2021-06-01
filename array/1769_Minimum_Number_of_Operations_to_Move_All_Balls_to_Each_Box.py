class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        ret = [0] * len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    if i==j:
                        continue
                    ret[i] += abs(i - j)
                else:
                    continue
        return ret
