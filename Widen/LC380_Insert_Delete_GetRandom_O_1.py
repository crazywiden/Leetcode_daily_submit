"""
380. Insert Delete GetRandom O(1)
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""




# my solution
# Runtime: 420 ms, faster than 10.43% of Python3 online submissions for Insert Delete GetRandom O(1).
# Memory Usage: 17.3 MB, less than 12.50% of Python3 online submissions for Insert Delete GetRandom O(1).
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data:
            self.data.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            self.data.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.sample(self.data, 1)[0]
        


# maintain index of data
# Runtime: 104 ms, faster than 93.84% of Python3 online submissions for Insert Delete GetRandom O(1).
# Memory Usage: 17.1 MB, less than 12.50% of Python3 online submissions for Insert Delete GetRandom O(1).
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.data_index = dict()
        self.len = -1
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data_index or self.data_index[val] < 0:
            self.len += 1
            self.data_index[val] = self.len
            self.data.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data_index or self.data_index[val] < 0:
            return False
        self.data_index[self.data[self.len]] = self.data_index[val]
        self.data[self.data_index[val]], self.data[self.len] = self.data[self.len], self.data[self.data_index[val]]
        self.data_index[val] = -1
        self.data.pop()
        self.len -= 1
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, self.len)
        return self.data[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()










