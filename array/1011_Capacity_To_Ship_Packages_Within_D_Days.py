class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        left, right = max(weights), sum(weights)
 
        def can_delivery(weights, ability, days):
            if ability < max(weights):
                return False
            total_time, temp = 1, 0
            for i in weights:
                temp += i
                if temp > ability:
                    total_time += 1
                    temp = i
            return total_time <= days
 
        while left <= right:
            mid = left + (right - left) // 2
            if can_delivery(weights, mid, days):
                right = mid - 1
            elif can_delivery(weights, mid, days) == False:
                left = mid + 1
        return left
