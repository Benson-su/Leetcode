class MyCalendar(object):

    def __init__(self):
        
        self.time_list = []
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.time_list:
            self.time_list.append([start, end])
            return True
        for time in self.time_list:
            if start >= time[1] or end <=time[0]:
                continue
            else:
                return False
        self.time_list.append([start, end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
