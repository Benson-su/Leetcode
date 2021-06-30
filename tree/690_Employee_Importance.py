"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def dfs(self, id, employee_dict):
        importance = employee_dict[id].importance
        for subordinate in employee_dict[id].subordinates:
            importance += self.dfs(subordinate, employee_dict)
        return importance

    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        employee_dict = {employee.id : employee for employee in employees}
        return self.dfs(id, employee_dict)
            
                
