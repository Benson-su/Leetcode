class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        arr_len = len(img1)
        zero_img = [0]
        vector_img1 = [(x1, y1) for x1 in range(arr_len) for y1 in range(arr_len) if img1[x1][y1]]
        vector_img2 = [(x1, y1) for x1 in range(arr_len) for y1 in range(arr_len) if img2[x1][y1]]
        
        distances = collections.Counter((x1 - x2 , y1 - y2) for (x1, y1) in vector_img1 for (x2, y2) in vector_img2)
        return max(distances.values() or zero_img)
