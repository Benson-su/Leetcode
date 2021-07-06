class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        tmp_repeat = {}
        sum_cost = 0
        max_value = 0
        total_cost = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                if s[i] not in tmp_repeat:
                    tmp_repeat[s[i]] = cost[i]
                    max_value = max(cost[i], cost[i-1])
                    sum_cost = cost[i] + cost[i - 1]
                else:
                    tmp_repeat[s[i]].append(cost[i])
                    max_value = max(max_value, cost[i])
                    sum_cost += cost[i]
            else:
                total_cost = sum_cost - max_value
                sum_cost = 0
                max_value = 0
                
        
