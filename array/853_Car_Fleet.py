class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = [(pos, spe) for pos, spe in zip(position, speed)]
        sorted_cars = sorted(cars, reverse=True)
        times = [float((target - pos)) / spe for pos, spe in sorted_cars]
        stack = []
        for time in times:
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        return len(stack)




