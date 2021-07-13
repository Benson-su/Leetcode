class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1,len(rating)):
            left_small = right_large = 0
            left_large = right_small = 0
            for j in range(0,i):
                if rating[j] < rating[i]:
                    left_small += 1
                else:
                    left_large += 1
            for k in range(i+1,len(rating)):
                if rating[k] > rating[i]:
                    right_large += 1
                else:
                    right_small += 1
            
            ans += left_small * right_large
            ans += left_large * right_small
        
        return ans
