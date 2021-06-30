class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_dict = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.time_dict:
            if timestamp >= self.time_dict[message]:
                self.time_dict[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.time_dict[message] = timestamp + 10
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
