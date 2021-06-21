class ProductOfNumbers(object):

    def __init__(self):
        self.product_dp = []
        
    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        print(num)
        if num == 0:
            self.product_dp = []
        elif len(self.product_dp) > 0:
            self.product_dp.append(self.product_dp[-1] * num)
        else:
            self.product_dp.append(num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k > len(self.product_dp):
            return 0
        if (1+k) > len(self.product_dp):
            return self.product_dp[-1]
        return self.product_dp[-1] / self.product_dp[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
