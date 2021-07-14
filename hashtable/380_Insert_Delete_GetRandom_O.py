ass RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.positions = {}
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.positions:
            return False
        else:
            self.nums.append(val)
            self.positions[val] = len(self.nums) - 1
            return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        position = self.positions.get(val)
        if position != None:
            self.nums[position], self.nums[-1] = self.nums[-1], self.nums[position]
            self.positions[self.nums[position]] = position
            self.nums.pop()
            del self.positions[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)
