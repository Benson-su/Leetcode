class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        dp = [0] * len(prices)
        for i in xrange(0, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return dp[-1]
  
