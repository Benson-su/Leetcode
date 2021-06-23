class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = [0]
        summation = 0
        for card in cardPoints:
            summation += card
            prefix_sum.append(summation)
        
        ans = 0
        for i in range(k+1):
            leftSum = prefix_sum[i]
            rightSum = prefix_sum[-1] - prefix_sum[len(cardPoints)-k+i]
            ans = max(ans,leftSum+rightSum)
                  
        return ans

