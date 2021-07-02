class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        min_speed, max_speed = 1, max(piles)
        while min_speed < max_speed:
            speed = min_speed + (max_speed - min_speed) / 2
            curH = 0
            for pile in piles:
                curH += pile // speed + (1 if pile % speed else 0)
            if curH > h:
                min_speed = speed + 1
            else:
                max_speed = speed
        return min_speed

