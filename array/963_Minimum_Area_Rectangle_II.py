class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p1,p2,p3):
            l1 = (p1[0]-p3[0])**2 + (p1[1]-p3[1])**2
            l2 = (p2[0]-p3[0])**2 + (p2[1]-p3[1])**2
            return (l1**0.5) * (l2**0.5)
        
        n = len(points)
        D = {}
        min_area = float("inf")
        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                middle = ((x1+x2)/2.0, (y1+y2)/2.0)
                l = (x2-x1)**2 + (y2-y1)**2
                if (middle, l) in D:
                    for p in D[(middle,l)]:
                        min_area = min(area(points[i], points[j], p), min_area)
                    D[(middle, l)].append(points[i])
                else:
                    D[(middle, l)] = [points[i]]
        if min_area == float("inf"):
            return 0
        return min_area
