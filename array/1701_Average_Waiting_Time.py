class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        finish_time = 0
        pre_finish_time = 0
        waiting = []
        for customer in customers:
            arrival_time = customer[0]
            
            finish_time = (pre_finish_time + customer[1]) if pre_finish_time > arrival_time else arrival_time + customer[1]
            print(arrival_time, finish_time)
            waiting.append(finish_time - arrival_time)
            pre_finish_time = finish_time
        return float(sum(waiting))/float(len(waiting))
            
