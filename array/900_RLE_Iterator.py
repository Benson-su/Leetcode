class RLEIterator(object):

    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self.encoding_arr = encoding
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while len(self.encoding_arr) > 0:
            if self.encoding_arr[0] == 0:
                self.encoding_arr = self.encoding_arr[2:]
            elif self.encoding_arr[0] >= n:
                self.encoding_arr[0] -= n
                return self.encoding_arr[1]
            else:
                n -= self.encoding_arr[0]
                self.encoding_arr = self.encoding_arr[2:]
        if n > 0:
            return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
