class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        def dfs(city, connect_dict, visited):
            if visited[city] == 1:
                return
            visited[city] = 1
            for sub_city in connect_dict[city]:
                dfs(sub_city, connect_dict, visited)
        
        visited = [0] * len(isConnected)
        connect_dict = collections.defaultdict(list)
        for city_num, item in enumerate(isConnected):
            for connect_city, bool_city in enumerate(item):
                if bool_city == 1:
                    connect_dict[city_num].append(connect_city)
        ret = 0
        for city in connect_dict.keys():
            if visited[city] == 0:
                ret += 1
                dfs(city, connect_dict, visited)
        return ret
            
                    
